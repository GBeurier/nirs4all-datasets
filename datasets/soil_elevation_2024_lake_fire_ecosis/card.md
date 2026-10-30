# Datasheet — EcoSIS Lake Fire Endmembers (elevation)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** soil
- **Description:** EcoSIS Lake Fire Endmembers (elevation). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, soil
- **Contributor:** Lake Fire Endmembers

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 106 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | 2024_LakeFireEndmembers | *Not specified.* | NIR | 350–2500 nm | 106 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| elevation | target | numeric | *Not specified.* | n=106, missing=0, range 0–741.4, mean 441.7 ± 175.5 |
| SpectralRep | metadata | numeric | *Not specified.* | n=106, missing=0, range 1–1, mean 1 ± 0 |
| date | metadata | categorical | *Not specified.* | n=106, missing=0, classes=2, top 8/29/2024 (×79) |
| plot_name | metadata | categorical | *Not specified.* | n=106, missing=0, classes=7, top Spectral - 070 (×20) |
| file_name | metadata | categorical | *Not specified.* | n=106, missing=0, classes=106, top G:\My Drive\terraspec\slpit\data\spectral_transects\Spectral - 077\SP_00046.asd (×1) |
| line_num | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top l1 (×106) |
| level_1 | metadata | categorical | *Not specified.* | n=106, missing=0, classes=5, top NPV (×33) |
| species | metadata | categorical | *Not specified.* | n=106, missing=72, classes=5, top UNK- (×30) |
| file_num | metadata | numeric | *Not specified.* | n=106, missing=0, range 37–57, mean 45.1 ± 4.938 |
| longitude | metadata | numeric | *Not specified.* | n=106, missing=0, range -120–-120, mean -120 ± 0.004448 |
| latitude | metadata | numeric | *Not specified.* | n=106, missing=0, range 34.7–34.74, mean 34.71 ± 0.01573 |
| utc_time | metadata | categorical | *Not specified.* | n=106, missing=0, classes=106, top 20:16:25 (×1) |
| dataset | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top EcoSIS (×106) |
| dataset_slug | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top lake-fire-endmembers (×106) |
| task_type | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top regression (×106) |
| trait_header | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top elevation (×106) |
| target_original_name | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top elevation (×106) |
| measurement_hint | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top 2024_LakeFireEndmembers (×106) |
| raw_label | metadata | categorical | *Not specified.* | n=106, missing=0, classes=88, top 0.0 (×4) |
| reference_value | metadata | numeric | *Not specified.* | n=106, missing=0, range 0–741.4, mean 441.7 ± 175.5 |
| class_index | metadata | categorical | *Not specified.* | n=106, missing=106, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=106, missing=106, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=106, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top 1D (×106) |
| axis_note | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×106) |
| official_data_url | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top https://data.ecosis.org/dataset/lake-fire-endmembers (×106) |
| official_package_url | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top https://ecosis.org/package/lake-fire-endmembers (×106) |
| license | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top Creative Commons Attribution (×106) |
| license_url | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×106) |
| rights_status | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top explicit_open (×106) |
| usage_scope | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top public_reuse_possible (×106) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top True (×106) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=106, missing=106, classes=0, — |
| notes | metadata | categorical | *Not specified.* | n=106, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×106) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/lake-fire-endmembers`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=lake-fire-endmembers`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/lake-fire-endmembers`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: The upstream converter selected date: 27 and 79 rows on two dates. The 106 ASD files and times are distinct, with 7 plots; the date is not a sample identifier and the file identifies an acquisition.
- **Curated views:** M: 7 fields, Y: 1 fields, measurements: 1 fields, passport: 32 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Creative Commons Attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `4b0edcc6820027d5304374390b7343e2ef312b537ec0059f1c8181092c448e9b`
- **Processing hash:** `f3512933a607c282ae79086066c1047b65f490da9c2a2428f1445b965712d8ee` | **metadata hash:** `de81871cb5dd7c7ddafae6875fbcc8254e1f97d5aef0bf5fb239d0e67ab4da5e`
