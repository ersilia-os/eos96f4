import sys
import os
import csv
import pickle

input_file = os.path.abspath(sys.argv[1])
output_file = os.path.abspath(sys.argv[2])

cwd = os.getcwd()

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)
os.chdir(root)

from mc.analyzers import Predictor

checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles_list = [row[0] for row in reader]


def load_file(path: str):
    path = os.path.abspath(path)
    print(f"Loading file from {path}")
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data

print(smiles_list)
def get_predictor() -> Predictor:
    dump = load_file(os.path.join(checkpoints_dir, "model.pkl"))[(0.7, 0.1, 0.2)]
    print(dump.keys())
    ranker = dump["ranker"]
    scaler = dump["scaler"]
    return Predictor(ranker, scaler)


predictor = get_predictor()

# Run predictor per molecule with try/except safety net
mc_list = []
for smi in smiles_list:
    try:
        result = predictor.predict([smi])
        mc_list.append(result[0])
    except Exception:
        mc_list.append("")

with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["molecular_complexity"])
    for mc in mc_list:
        writer.writerow([mc])

os.chdir(cwd)
