# Datasheet — Mendeley homemade soil OM TC NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley homemade soil OM TC NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Dataset of near-infrared spectral data for prediction of organic matter and total carbon in agricultural soil using homemade NIR spectrometer

## Composition

- **Alignment:** sample level; 190 sample(s), 190 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Homemade NIR raw spectra | homemade NIR spectrometer | NIR | 901.1–1701 nm | 190 | 228 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| OM_pct | target | numeric | *Not specified.* | n=190, missing=0, range 0.2992–9.89, mean 2.396 ± 1.611 |
| TC_pct | target | numeric | *Not specified.* | n=190, missing=0, range 0.46–5.44, mean 1.62 ± 0.8429 |
| api_url | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/yt78nwnhbd/snapshot/1 (×190) |
| files_api_url | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/yt78nwnhbd/files?folder_id=root&version=1&$start=0&$limit=1000 (×190) |
| article_url | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top https://doi.org/10.1016/j.dib.2021.107243 (×190) |
| doi_dataset | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top 10.17632/yt78nwnhbd.1 (×190) |
| license | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×190) |
| license_id | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top cc-by-4.0 (×190) |
| license_url | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×190) |
| rights_status | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top explicit_open (×190) |
| usage_scope | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top public_reuse_possible (×190) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top True (×190) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top NIR (×190) |
| axis_unit | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top nm (×190) |
| axis_min | metadata | numeric | *Not specified.* | n=190, missing=0, range 901.1–901.1, mean 901.1 ± 2.28e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=190, missing=0, range 1701–1701, mean 1701 ± 2.28e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=190, missing=0, range 228–228, mean 228 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Raw spectra and chemical OM/TC targets used, preprocessed sheets and model files are not standardized here. (×190) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/yt78nwnhbd/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/yt78nwnhbd/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/yt78nwnhbd/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Mendeley Data record is licensed CC BY 4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `1661043d2ed64ff11a909381319dc853b0493a672cf73d119a52a2ca9bf89b83`
- **Processing hash:** `368cce6eac2b850b1ba3e2717254f3a48277a6d21d57002d62af4398081f4d4b` | **metadata hash:** `bdfe0fe3c6e5eb3ae4eee0b133c330de5157292ba37986245b22a4f96f76b43c`
