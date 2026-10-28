# Datasheet — Mendeley cucurbitaceae fruits Vis-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley cucurbitaceae fruits Vis-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Dataset of Vis-NIR spectra for intact cucurbitaceae fruits

## Composition

- **Alignment:** sample level; 300 sample(s), 300 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Vis-NIR spectra | *Not specified.* | NIR | 381–1065 nm | 300 | 229 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Water_Content_pct | target | numeric | *Not specified.* | n=300, missing=0, range 88.26–96.8, mean 92.3 ± 2.204 |
| SSC_pct | target | numeric | *Not specified.* | n=300, missing=0, range 2.65–10.8, mean 4.424 ± 1.927 |
| commodity | metadata | categorical | *Not specified.* | n=300, missing=0, classes=6, top Zucchini (×50) |
| original_split | metadata | categorical | *Not specified.* | n=300, missing=0, classes=2, top calibration (×200) |
| api_url | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/k55b8mvs84/snapshot/1 (×300) |
| files_api_url | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/k55b8mvs84/files?folder_id=root&version=1&$start=0&$limit=1000 (×300) |
| article_url | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S235234092100740X (×300) |
| doi_dataset | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top 10.17632/k55b8mvs84.1 (×300) |
| license | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×300) |
| license_id | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top cc-by-4.0 (×300) |
| license_url | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×300) |
| rights_status | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top explicit_open (×300) |
| usage_scope | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top public_reuse_possible (×300) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top True (×300) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top Vis-NIR (×300) |
| axis_unit | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top nm (×300) |
| axis_min | metadata | numeric | *Not specified.* | n=300, missing=0, range 381–381, mean 381 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=300, missing=0, range 1065–1065, mean 1065 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=300, missing=0, range 229–229, mean 229 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=300, missing=0, classes=1, top Raw Vis-NIR spectra for intact cucurbitaceae fruits, source calibration/prediction split preserved as metadata. (×300) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/k55b8mvs84/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/k55b8mvs84/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/k55b8mvs84/files?folder_id=root&version=1&$start=0&$limit=1000`
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
- **Content hash:** `fc35e62fb0874607fcede6bead7954d62d8386c3bc3596c21203a2e6aab662fe`
- **Processing hash:** `7dae3bf17b7c5ba2c7e87304adba605caa087e281bca5ca90eb2fbede67c98bd` | **metadata hash:** `8425ca2967eebef8d8ba89192ebe122b093ea206c1d84eea87ea7fd074beef03`
