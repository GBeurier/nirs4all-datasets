# Datasheet — Pharmaceutical tablets — NIR Shootout (Eigenvector)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** pharmaceutical
- **Description:** Pharmaceutical tablets NIR Shootout Eigenvector. v2.0 standardized NIRS package: 2 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, pharmaceutical
- **Contributor:** Eigenvector data sets

## Composition

- **Alignment:** sample level; 655 sample(s), 1310 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | spectrometer_1 | unknown, source suffix _1 | NIR | 600–1898 nm | 655 | 650 |
| X2 | spectrometer_2 | unknown, source suffix _2 | NIR | 600–1898 nm | 655 | 650 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| weight | target | numeric | *Not specified.* | n=655, missing=0, range 363.9–391, mean 378.9 ± 4.748 |
| hardness | target | numeric | *Not specified.* | n=655, missing=0, range 13.8–23.5, mean 19.38 ± 1.265 |
| assay | target | numeric | *Not specified.* | n=655, missing=0, range 151.6–239.1, mean 189.9 ± 17.14 |
| source_split | metadata | categorical | *Not specified.* | n=655, missing=0, classes=3, top test (×460) |
| source_split_index | metadata | numeric | *Not specified.* | n=655, missing=0, range 1–460, mean 181.6 ± 136.7 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): calibration: 155, test: 460, validation: 40

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2019/06/nir_shootout_2002.mat_.zip`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 3 fields, measurements: 0 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** license unknown, redistribution not cleared
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `05a1df76bc03bee4e043088315c09b5710c4c0b29f3ae090a776a53ed50682ab`
- **Processing hash:** `e2e606d825bcf1b6b09a349603a506ce1e5d807122e1ac3083c01a7fcaf4f101` | **metadata hash:** `f47cc29e4a07b8cf50f6ceb25c71ff45deb128f159cd66b4d54db5866ecf3608`
