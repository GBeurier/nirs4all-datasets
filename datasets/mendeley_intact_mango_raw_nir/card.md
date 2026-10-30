# Datasheet — Mendeley intact mango raw NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley intact mango raw NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Dataset of NIR spectrum for intact mango fruits

## Composition

- **Alignment:** sample level; 186 sample(s), 186 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Raw NIR spectra | *Not specified.* | NIR | 999.9–2500 nm | 186 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Mango_Cultivar | target | categorical | *Not specified.* | n=186, missing=0, classes=4, top Kent (×85) |
| Vit_C_mg_100g | target | numeric | *Not specified.* | n=186, missing=0, range 18.33–77.86, mean 42.78 ± 13.69 |
| TA_mg_100g | target | numeric | *Not specified.* | n=186, missing=0, range 111.7–993.8, mean 489.5 ± 167.4 |
| SSC_oBrix | target | numeric | *Not specified.* | n=186, missing=0, range 7.91–25.51, mean 15.76 ± 3.905 |
| api_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/b9d6s7hr33/snapshot/1 (×186) |
| files_api_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/b9d6s7hr33/files?folder_id=root&version=1&$start=0&$limit=1000 (×186) |
| article_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340919311448 (×186) |
| doi_dataset | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top 10.17632/b9d6s7hr33.1 (×186) |
| license | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×186) |
| license_id | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top cc-by-4.0 (×186) |
| license_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×186) |
| rights_status | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top explicit_open (×186) |
| usage_scope | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top public_reuse_possible (×186) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top True (×186) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top NIR (×186) |
| axis_unit | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top nm (×186) |
| axis_min | metadata | numeric | *Not specified.* | n=186, missing=0, range 999.9–999.9, mean 999.9 ± 1.14e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=186, missing=0, range 2500–2500, mean 2500 ± 4.56e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=186, missing=0, range 1557–1557, mean 1557 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Raw NIR spectra of intact mango fruits, source label duplicates Mango Cultivars and is kept as metadata. (×186) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/b9d6s7hr33/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/b9d6s7hr33/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/b9d6s7hr33/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 4 fields, measurements: 0 fields, passport: 21 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `e8ff65acc7fefe0c0ba872b287a8c346351decc92f326ad1211d4a98ea03326c`
- **Processing hash:** `e4ac728d111dba1e6b38176928f7071239c7a941ebbfacc78303e12036c34c15` | **metadata hash:** `63588cd9da7bca9cd54a0be12488604bf6c6904371dd0ecf71af3756cf352229`
