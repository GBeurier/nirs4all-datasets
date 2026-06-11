# Datasheet — CGL_NIR grain protein Eigenvector

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cgl
- **Description:** CGL_NIR grain protein Eigenvector. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cgl
- **Contributor:** Eigenvector data sets

## Composition

- **Alignment:** sample level; 231 sample(s), 231 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra | unknown | NIR | 1104–2496 nm | 231 | 117 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Casein_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–88.83, mean 29.61 ± 22.49 |
| Glucose_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–91.5, mean 30.5 ± 23.17 |
| Lactate_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–75.71, mean 25.24 ± 19.17 |
| Moisture_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 5.3–24.29, mean 12.7 ± 4.459 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): calibration: 153, test: 78

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2021/04/CGL_nir.mat_.zip`
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
- **Content hash:** `ab6177e4e5ddee7e32d00e53ef3ffb22998658cd6ee64380b535f889fa1cce86`
- **Processing hash:** `262dcacad6e5f8b95b1c5aa2a6561a191bdfc4739004ffd7bc83a0569cf7412e` | **metadata hash:** `a47dfcaa7c6c515b78aa5a9efcb24c8a5e847c491793ad21b67806c32785fbc6`
