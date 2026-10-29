# Datasheet — Dryad Hawaii avocado Felix handheld NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad Hawaii avocado Felix handheld NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 1139 sample(s), 1991 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–5 (mean 1.748).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad Hawaii avocado Felix handheld NIR | *Not specified.* | NIR | 729–975 nm | 1991 | 83 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Variety | target | categorical | *Not specified.* | n=1991, missing=0, classes=5, top SW (×1139) |
| Days in Room Temp | target | numeric | *Not specified.* | n=1991, missing=27, range 1–8, mean 4.596 ± 2.733 |
| harvest_date | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=6, top 2023-05-29 00:00:00 (×956) |
| nir_date | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=13, top 2023-06-14 00:00:00 (×239) |
| instrument_context | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=1, top Felix_F750_handheld_2023 (×1991) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\advocado (×1991) |
| manual_download_file | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=1, top Felix_2nd_ave.xlsx (×1991) |
| official_source_url | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.98sf7m0rj (×1991) |
| manual_download | metadata | categorical | *Not specified.* | n=1991, missing=0, classes=1, top True (×1991) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.98sf7m0rj`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Mesures répétées du même identifiant de fruit ; les dates NIR varient au cours du suivi.
- **Curated views:** M: 2 fields, Y: 2 fields, measurements: 0 fields, passport: 7 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Manual download preserved as provenance; public reuse follows source Dryad dataset terms.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `17b560fb77192110b947f7ea3ff4c361077263ca5d103483d872ec3da3e712ec`
- **Processing hash:** `da3b1ac4fb01384c1f19e245d96eb3006e045b7ba1817fcaecb6875961147b4f` | **metadata hash:** `91d2e2e757ac0605c6faba62a2869b837d77d9af879ff751d0e66cb3ed74d3c6`
