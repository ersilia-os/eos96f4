import os
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors
from rdkit.Chem.EnumerateStereoisomers import (
    StereoEnumerationOptions,
    GetStereoisomerCount,
)

from mc.scscorer.scscore.standalone_model_numpy import SCScorer


def _get_scorer():
    """Initializes and restores the SCScorer model."""
    model = SCScorer()
    model.restore(
        os.path.join(
            "mc",
            "scscorer",
            "models",
            "full_reaxys_model_2048bool",
            "model.ckpt-10654.as_numpy.json.gz",
        ),
        FP_len=2048,
    )
    return model

def featurize(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates molecular features. Returns NaN if a molecule cannot be processed 
    to prevent runtime crashes.
    """
    
    def safe_calc(mol, func, is_smiles=False):
        """
        Helper to safely calculate descriptors. 
        Ensures RingInfo is initialized to avoid RDKit Pre-condition Violations.
        """
        try:
            if is_smiles:
                if pd.isna(mol) or mol is None:
                    return np.nan
                # For functions taking SMILES strings
                return func(mol)
            
            if mol is None:
                return np.nan
            
            # Force ring initialization to prevent 'RingInfo not initialized' error
            Chem.GetSymmSSSR(mol)
            return func(mol)
        except Exception:
            return np.nan

    # Molecule-based descriptors
    data["weight"] = data["mol"].apply(lambda x: safe_calc(x, Descriptors.ExactMolWt))
    data["num_of_atoms"] = data["mol"].apply(lambda x: x.GetNumAtoms() if x else np.nan)
    data["tpsa"] = data["mol"].apply(lambda x: safe_calc(x, Descriptors.TPSA))
    data["num_heteroatoms"] = data["mol"].apply(
        lambda x: safe_calc(x, lambda m: float(Descriptors.NumHeteroatoms(m)))
    )
    
    # Structural descriptors
    data["spiro"] = data["mol"].apply(lambda x: safe_calc(x, rdMolDescriptors.CalcNumSpiroAtoms))
    data["rotb"] = data["mol"].apply(lambda x: safe_calc(x, rdMolDescriptors.CalcNumRotatableBonds))
    data["aliph_cycles"] = data["mol"].apply(
        lambda x: safe_calc(x, rdMolDescriptors.CalcNumAliphaticCarbocycles)
    )
    data["arom_cycles"] = data["mol"].apply(
        lambda x: safe_calc(x, rdMolDescriptors.CalcNumAromaticCarbocycles)
    )
    data["aliph_heterocycles"] = data["mol"].apply(
        lambda x: safe_calc(x, rdMolDescriptors.CalcNumAliphaticHeterocycles)
    )
    data["arom_heterocycles"] = data["mol"].apply(
        lambda x: safe_calc(x, rdMolDescriptors.CalcNumAromaticHeterocycles)
    )
    data["bridge_atoms"] = data["mol"].apply(
        lambda x: safe_calc(x, rdMolDescriptors.CalcNumBridgeheadAtoms)
    )

    # Stereochemistry
    # Note: Using Chem.MolFromSmiles(x) here as in original code, but wrapped safely
    data["atom_stereo_centers"] = data["smiles"].apply(
        lambda x: safe_calc(x, lambda s: rdMolDescriptors.CalcNumAtomStereoCenters(Chem.MolFromSmiles(s)), is_smiles=True)
    )
    
    opts = StereoEnumerationOptions(onlyUnassigned=False, unique=True)
    data["num_of_stereoisomers"] = data["mol"].apply(
        lambda x: safe_calc(x, lambda m: float(GetStereoisomerCount(m, options=opts)))
    )

    # SCScore
    scorer = _get_scorer()
    data["scscore"] = data["smiles"].apply(
        lambda x: safe_calc(x, lambda s: scorer.get_score_from_smi(s)[-1], is_smiles=True)
    )

    return data