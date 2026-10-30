# Datasheet — Mendeley agricultural soil fertility NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley agricultural soil fertility NIR. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** NIR spectra datasets of agricultural soil and fertility properties

## Composition

- **Alignment:** sample level; 40 sample(s), 40 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NIR spectra | *Not specified.* | NIR | 999.9–2500 nm | 40 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| N_content_pct | target | numeric | *Not specified.* | n=40, missing=0, range 0.01882–0.521, mean 0.1482 ± 0.1437 |
| P_ppm | target | numeric | *Not specified.* | n=40, missing=0, range 1.68–40.92, mean 14.49 ± 11.46 |
| K_cmol_kg | target | numeric | *Not specified.* | n=40, missing=0, range 0.26–2.58, mean 0.8805 ± 0.5144 |
| pH_KCl | target | numeric | *Not specified.* | n=40, missing=0, range 2.57–11.21, mean 5.784 ± 2.212 |
| Mg_cmol_kg | target | numeric | *Not specified.* | n=40, missing=0, range 0.31–18.07, mean 6.431 ± 4.754 |
| Ca_cmol_kg | target | numeric | *Not specified.* | n=40, missing=0, range 0.39–20.18, mean 7.453 ± 6.408 |
| api_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/h8mht3jsbz/snapshot/1 (×40) |
| files_api_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/h8mht3jsbz/files?folder_id=root&version=1&$start=0&$limit=1000 (×40) |
| doi_dataset | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top 10.17632/h8mht3jsbz.1 (×40) |
| license | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×40) |
| license_id | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top cc-by-4.0 (×40) |
| license_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×40) |
| rights_status | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top explicit_open (×40) |
| usage_scope | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top public_reuse_possible (×40) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top True (×40) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top NIR (×40) |
| axis_unit | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top nm (×40) |
| axis_min | metadata | numeric | *Not specified.* | n=40, missing=0, range 999.9–999.9, mean 999.9 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=40, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=40, missing=0, range 1557–1557, mean 1557 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top NIR spectra of agricultural soil samples with wet-chemistry fertility properties. (×40) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/h8mht3jsbz/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/h8mht3jsbz/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/h8mht3jsbz/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 6 fields, measurements: 0 fields, passport: 19 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `7ae5c48e5a333d3691f4d838c5464093d8950d2f8be1b15e75ccb6d3485c87a9`
- **Processing hash:** `ccc51be1f97e6340e484226485a68e931e316307f093ad4dc9687bbb71631e8f` | **metadata hash:** `f1bb2fc2c14b4dbd306025f586b2fa6992b763390eb7314f98cc46aa8c1b0ffd`
