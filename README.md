# Digitization of molecular complexity

This model uses a learning-to-rank machine learning framework to quantify molecular complexity in a supervised way. Based on Shapley value analysis, authors were able to identify molecular characteristics that guide experts in assigning molecular complexity, such as molecular weight or number of aromatic cycles. The model was developed using a dataset of ca. 300k data points across diverse structures, and it was applied to study trends in synthetic strategies, among other analyses.

This model was incorporated on 2026-01-30.Last packaged on 2026-02-02.

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
- **Interpretation:** The output score represents the predicted molecular complexity of the input compound, with higher scores indicating greater complexity.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| molecular_complexity | float | high | Score representing the predicted molecular complexity |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos96f4](https://hub.docker.com/r/ersiliaos/eos96f4)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos96f4.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos96f4.zip)

### Resource Consumption
- **Model Size (Mb):** `916`
- **Environment Size (Mb):** `1362`
- **Image Size (Mb):** `2987.53`

**Computational Performance (seconds):**
- 10 inputs: `30.06`
- 100 inputs: `20.38`
- 10000 inputs: `181.46`

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
