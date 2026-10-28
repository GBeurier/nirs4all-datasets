# Datasheet — Mendeley intact mango raw NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley intact mango raw NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Dataset of NIR spectrum for intact mango fruits

## Composition

- **Alignment:** sample level; 186 sample(s), 186 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

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
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/b9d6s7hr33/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/b9d6s7hr33/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/b9d6s7hr33/files?folder_id=root&version=1&$start=0&$limit=1000`
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
- **Content hash:** `ff19067d4226e4974f500f8e3f3887e51cbe69d091498228ac42e34a0172ad72`
- **Processing hash:** `a2e39ce85e2dba2bb957c82fe3d8adbf73605ce4b6c02f4f675c7b6ef7c8db91` | **metadata hash:** `7a7d0d4a9f8e7bbb68fdee147c41944a2a1a1567ce6dbca2af556d69427b2dc3`
