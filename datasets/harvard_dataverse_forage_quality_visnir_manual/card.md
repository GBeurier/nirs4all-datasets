# Datasheet — Forage quality Vis-NIR spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** harvard
- **Description:** Forage quality Vis-NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, harvard
- **Contributor:** Data In Brief / Harvard Dataverse forage

## Composition

- **Alignment:** sample level; *Not specified.* sample(s), 1112 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 400–2498 nm | 1112 | 1050 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| FDN | target | numeric | *Not specified.* | n=1112, missing=117, range 0.564–84.73, mean 67.29 ± 6.267 |
| FDA | target | numeric | *Not specified.* | n=1112, missing=116, range 0.59–58.22, mean 36.35 ± 5.291 |
| DIVMS | target | numeric | *Not specified.* | n=1112, missing=117, range 0.613–108.5, mean 62.88 ± 9.027 |
| PC | target | numeric | *Not specified.* | n=1112, missing=643, range 0.634–17.55, mean 7.251 ± 2.846 |
| country | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=2, top Colombia (×1104) |
| location | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=6, top Palmira (×833) |
| harvest_date | metadata | categorical | *Not specified.* | n=1112, missing=1, classes=25, top 1/1/2019 (×228) |
| manual_download | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=1, top True (×1112) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\forage (×1112) |
| manual_download_file | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=1, top dataverse_files.zip::02a. Fulldata.csv (×1112) |
| official_source_url | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=1, top https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/XPNIQY (×1112) |
| standardization_batch | metadata | categorical | *Not specified.* | n=1112, missing=0, classes=1, top v0.8.57 (×1112) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Harvard Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.7910/DVN/XPNIQY`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Non déterminé
- **Curated views:** M: 3 fields, Y: 4 fields, passport: 5 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Manual download after Harvard Dataverse guestbook blockage; blocked inventory recorded CC BY 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `33a68ecccb48217ba2f612ac703c4ef081bca7e4b66a7cc8af3554c3bc4c22ce`
- **Processing hash:** `dd1250165c7e6326f9916981007cba024fe76e255ddf997e3a234ad3ae24f4bd` | **metadata hash:** `8b6154013410ae322845187ede0e7cbf420bda7c39a1b0ce4a821d103fc743db`
