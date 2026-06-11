# Datasheet — CORN Eigenvector NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** corn
- **Description:** CORN Eigenvector NIR. v2.0 standardized NIRS package: 3 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, corn
- **Contributor:** Eigenvector CORN

## Composition

- **Alignment:** sample level; 80 sample(s), 240 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | m5spec | m5 | NIR | 1100–2498 nm | 80 | 700 |
| X2 | mp5spec | mp5 | NIR | 1100–2498 nm | 80 | 700 |
| X3 | mp6spec | mp6 | NIR | 1100–2498 nm | 80 | 700 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Moisture | target | numeric | *Not specified.* | n=80, missing=0, range 9.377–10.99, mean 10.23 ± 0.3804 |
| Oil | target | numeric | *Not specified.* | n=80, missing=0, range 3.088–3.832, mean 3.498 ± 0.177 |
| Protein | target | numeric | *Not specified.* | n=80, missing=0, range 7.654–9.711, mean 8.668 ± 0.4986 |
| Starch | target | numeric | *Not specified.* | n=80, missing=0, range 62.83–66.47, mean 64.7 ± 0.8207 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/Corn/`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2019/06/corn.mat_.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/Corn/corn.mat`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Eigenvector page says the data are available for download but no explicit redistribution license was detected.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `1209011756a8f2d735f7855ceccebf22b8451644fbf5e2b7d6eb8dff7cb410ba`
- **Processing hash:** `b3772222aa96d7824d939eefb2b8d6053122c2320cda3b689534f622f9141ebf` | **metadata hash:** `b9291350222a0b5c4ce90c8f796f388dd6cf5ccfd0256b7dfffac1d1a734b4de`
