# Datasheet — Mendeley chicken meat authenticity handheld NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley chicken meat authenticity handheld NIR. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Data of: Integration of handheld NIR and machine learning for the development of a Measure & Monitor technology for chicken meat authenticity

## Composition

- **Alignment:** sample level; 153 sample(s), 4053 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 10–37 (mean 26.49).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Handheld NIR spectra | handheld NIR | NIR | 908.1–1676 nm | 4053 | 125 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Production_system | target | categorical | *Not specified.* | n=4053, missing=0, classes=8, top MAR (×1025) |
| Scan_type | target | categorical | *Not specified.* | n=4053, missing=0, classes=3, top OM (×1498) |
| Freshness | target | categorical | *Not specified.* | n=4053, missing=0, classes=2, top FR (×2208) |
| api_url | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/cp2hdhkys3/snapshot/6 (×4053) |
| files_api_url | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/cp2hdhkys3/files?folder_id=root&version=6&$start=0&$limit=1000 (×4053) |
| article_url | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top https://doi.org/10.1016/j.foodcont.2019.106857 (×4053) |
| doi_dataset | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top 10.17632/cp2hdhkys3.6 (×4053) |
| license | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×4053) |
| license_id | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top cc-by-4.0 (×4053) |
| license_url | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×4053) |
| rights_status | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top explicit_open (×4053) |
| usage_scope | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top public_reuse_possible (×4053) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top True (×4053) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top NIR (×4053) |
| axis_unit | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top nm (×4053) |
| axis_min | metadata | numeric | *Not specified.* | n=4053, missing=0, range 908.1–908.1, mean 908.1 ± 1.137e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=4053, missing=0, range 1676–1676, mean 1676 ± 2.274e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=4053, missing=0, range 125–125, mean 125 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=4053, missing=0, classes=1, top Handheld NIR chicken meat authenticity data, repeated scans per sample are retained as independent observations. (×4053) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/cp2hdhkys3/6`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/cp2hdhkys3/snapshot/6`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/cp2hdhkys3/files?folder_id=root&version=6&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 0 fields, Y: 3 fields, measurements: 0 fields, passport: 20 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `4fca3073759acfa1544b189d369c40c3001c4f821911b2d3570f622ada47ac10`
- **Processing hash:** `8c5a4aabdc1030fd268fd7298c9b66b46593b786d0a35033d6942f756f3a1302` | **metadata hash:** `ee9348a4476a4fa37bc3d28130103ed67fa46d6662874f1df8b1cde106ad69fd`
