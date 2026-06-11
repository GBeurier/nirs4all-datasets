# Datasheet — Pharmaceutical tablets NIR Shootout Eigenvector

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** pharmaceutical
- **Description:** Pharmaceutical tablets NIR Shootout Eigenvector. v2.0 standardized NIRS package: 2 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, pharmaceutical
- **Contributor:** Eigenvector data sets

## Composition

- **Alignment:** sample level; 655 sample(s), 1310 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

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

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 460, calibration: 155, validation: 40

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2019/06/nir_shootout_2002.mat_.zip`
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
- **Redistribution rights:** license unknown, redistribution not cleared
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `3e8b450fefad8ff2ac0cc60360a52d63ae39a8445c76d1cca1364e7c03f1dde4`
- **Processing hash:** `f0e60cf5c8304195ccae4d340e921953401158ce3b51f90601f66fc474c1ebae` | **metadata hash:** `033b7352e7c105f40e02176f9a0fdafcb0898ea2483c25462ad8d3d36765932f`
