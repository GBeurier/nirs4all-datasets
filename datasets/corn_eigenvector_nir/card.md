# Datasheet — CORN Eigenvector NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** corn
- **Description:** CORN Eigenvector NIR. v2.0 standardized NIRS package: 3 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, corn
- **Contributor:** Eigenvector CORN

## Composition

- **Alignment:** sample level; 80 sample(s), 240 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/Corn/`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2019/06/corn.mat_.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://www.eigenvector.com/data/Corn/corn.mat`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 4 fields, measurements: 0 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `e48c1df02aaf777303bb563982985087cb1c1b187718acff727fa46ce4dda10e`
- **Processing hash:** `febfb0792a07c2a27a92ca2af929d9fd3320a2b09a3044d4095d187d525484e6` | **metadata hash:** `af4f077e8c781c0edc6ab89cef8bdae430b562e41034d04886e57ed53fd00350`
