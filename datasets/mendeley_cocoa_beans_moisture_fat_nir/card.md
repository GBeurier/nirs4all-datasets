# Datasheet — Mendeley cocoa beans moisture fat NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley cocoa beans moisture fat NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** NIR spectral data and actual quality measurement of intact cocoa Bean samples

## Composition

- **Alignment:** sample level; 72 sample(s), 72 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NIR absorbance spectra | *Not specified.* | NIR | 999.9–2500 nm | 72 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Moisture_Content_pct | target | numeric | *Not specified.* | n=72, missing=0, range 6.74–12.08, mean 9.036 ± 1.277 |
| Fat_Content_pct | target | numeric | *Not specified.* | n=72, missing=0, range 35.26–45.75, mean 40.32 ± 2.153 |
| api_url | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/7734j4fd98/snapshot/1 (×72) |
| files_api_url | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/7734j4fd98/files?folder_id=root&version=1&$start=0&$limit=1000 (×72) |
| article_url | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340920301451 (×72) |
| doi_dataset | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top 10.17632/7734j4fd98.1 (×72) |
| license | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×72) |
| license_id | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top cc-by-4.0 (×72) |
| license_url | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×72) |
| rights_status | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top explicit_open (×72) |
| usage_scope | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top public_reuse_possible (×72) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top True (×72) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top NIR (×72) |
| axis_unit | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top nm (×72) |
| axis_min | metadata | numeric | *Not specified.* | n=72, missing=0, range 999.9–999.9, mean 999.9 ± 1.145e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=72, missing=0, range 2500–2500, mean 2500 ± 4.579e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=72, missing=0, range 1557–1557, mean 1557 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=72, missing=0, classes=1, top NIR absorbance spectra of intact cocoa bean samples with moisture and fat content targets. (×72) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/7734j4fd98/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7734j4fd98/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7734j4fd98/files?folder_id=root&version=1&$start=0&$limit=1000`
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
- **Content hash:** `c2f03249a56f1f5e17ea5849c4056ba16db4df10290605d00498ccd3ada16cab`
- **Processing hash:** `8e88d31c60f133fd768efa60c2c4000285cf5ce26ca5d6d626e983d43a321b11` | **metadata hash:** `143360cb2acbf15a52c0769c8a9826bf03a883296610904742ebfca35ca46279`
