# Digitization of molecular complexity

Quantifies how complex a molecule appears to an experienced chemist, learned from expert judgements rather than defined by a formula. The authors framed this as learning to rank, training on pairwise complexity comparisons, and used Shapley analysis to identify which structural characteristics drive the assessments, among them ring fusion, stereocentres and unusual heteroatom arrangements. Because the target is human perception, the score reflects the intuitions of the chemists who supplied the rankings.

This model was incorporated on 2026-01-30.Last packaged on 2026-03-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos96f4`
- **Slug:** `digitization-complexity`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Molecular complexity score where higher values indicate a more complex compound.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| molecular_complexity | float | high | Score representing the predicted molecular complexity |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos96f4](https://hub.docker.com/r/ersiliaos/eos96f4)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos96f4.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos96f4.zip)

### Resource Consumption
- **Model Size (Mb):** `916`
- **Environment Size (Mb):** `1371`
- **Image Size (Mb):** `2985.59`

**Computational Performance (seconds):**
- 10 inputs: `37`
- 100 inputs: `102.47`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/Ananikov-Lab/digitizing_molecular_complexity](https://github.com/Ananikov-Lab/digitizing_molecular_complexity)
- **Publication**: [https://doi.org/10.1039/D4SC07320G](https://doi.org/10.1039/D4SC07320G)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [CC-BY-4.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos96f4
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos96f4
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
