# Datasheet — Mendeley intact mango TA Vit C raw NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley intact mango TA Vit C raw NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Enhanced Spectra dataset of NIRS in intact mangos

## Composition

- **Alignment:** sample level; 58 sample(s), 58 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Raw NIR spectra | *Not specified.* | NIR | 999.9–2500 nm | 58 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TA_mg_100gr_FM | target | numeric | *Not specified.* | n=58, missing=0, range 189.7–772.8, mean 495.5 ± 131.1 |
| Vit_C_mg_100gr_FM | target | numeric | *Not specified.* | n=58, missing=0, range 28.93–35.66, mean 32.21 ± 1.306 |
| mango_variety | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top Kent (×58) |
| api_url | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/ph57ynng46/snapshot/1 (×58) |
| files_api_url | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/ph57ynng46/files?folder_id=root&version=1&$start=0&$limit=1000 (×58) |
| article_url | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340920304650 (×58) |
| doi_dataset | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top 10.17632/ph57ynng46.1 (×58) |
| license | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×58) |
| license_id | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top cc-by-4.0 (×58) |
| license_url | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×58) |
| rights_status | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top explicit_open (×58) |
| usage_scope | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top public_reuse_possible (×58) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top True (×58) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top NIR (×58) |
| axis_unit | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top nm (×58) |
| axis_min | metadata | numeric | *Not specified.* | n=58, missing=0, range 999.9–999.9, mean 999.9 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=58, missing=0, range 2500–2500, mean 2500 ± 9.174e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=58, missing=0, range 1557–1557, mean 1557 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=58, missing=0, classes=1, top Raw NIR spectra used, MSC/BLC preprocessed sheets are available in source workbook but not standardized here. (×58) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/ph57ynng46/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/ph57ynng46/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/ph57ynng46/files?folder_id=root&version=1&$start=0&$limit=1000`
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
- **Content hash:** `878bb02a48afd475ef5cd3789b7e6cd3ab4340f40d769d0837e1b790f368d801`
- **Processing hash:** `3800e8c177e9fc33fe215d4ff2b9c7c8992f05fecdfff91928002e50c24fb336` | **metadata hash:** `c480aa4a84599667e8f389d5e6bb598560e8ee20c337b57f78ef4a0e870db939`
