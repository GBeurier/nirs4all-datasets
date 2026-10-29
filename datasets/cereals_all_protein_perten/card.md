# Datasheet — Perten cereals all protein NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cereals
- **Description:** Perten cereals all protein NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cereals
- **Contributor:** sensAIfood cereal NIR data (wheat, corn, barley) and reference protein and moisture (Perten set)

## Composition

- **Alignment:** sample level; 450 sample(s), 450 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Perten cereals all protein NIR | Perten DA7200/DA72xx/DA7440/DA7250/DA7300 as available by sample | NIR | 950–1650 nm | 450 | 141 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| protein | target | numeric | *Not specified.* | n=450, missing=0, range 6.397–20.29, mean 11.58 ± 2.54 |
| SpectralRep | metadata | numeric | *Not specified.* | n=450, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top sensAIfood Perten Cereals (×450) |
| dataset_title | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top All cereals Perten protein (×450) |
| dataset_slug | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top cereals_all_protein_perten (×450) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top NIR (×450) |
| cereal_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top barley\|corn\|wheat (×450) |
| trait_header | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top protein (×450) |
| trait_header_original | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top Protein (×450) |
| task_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top regression (×450) |
| raw_label | metadata | categorical | *Not specified.* | n=450, missing=0, classes=450, top BarleyWholePerten0001 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=450, missing=0, range 6.397–20.29, mean 11.58 ± 2.54 |
| n_points_original | metadata | numeric | *Not specified.* | n=450, missing=0, range 141–141, mean 141 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top 1D (×450) |
| axis_note | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top source_axis_950_to_1650_nm_step_5 (×450) |
| ID | metadata | categorical | *Not specified.* | n=450, missing=0, classes=450, top BarleyWholePerten0001 (×1) |
| Spectrometer | metadata | categorical | *Not specified.* | n=450, missing=0, classes=6, top Perten_DA7200 (×396) |
| Cereal | metadata | categorical | *Not specified.* | n=450, missing=0, classes=3, top barley (×150) |
| Variety | metadata | categorical | *Not specified.* | n=450, missing=0, classes=4, top Unknown (×300) |
| Country | metadata | categorical | *Not specified.* | n=450, missing=0, classes=13, top US (×98) |
| Year | metadata | numeric | *Not specified.* | n=450, missing=0, range 0–2017, mean 1753 ± 668.5 |
| Moisture | metadata | numeric | *Not specified.* | n=450, missing=0, range 6.37–31.82, mean 13.07 ± 3.481 |
| meta_Spectrometer_Make_Model | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top Perten: mixed cereal subsets (×450) |
| meta_Wavelength_Range_nm | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top 950-1650 (×450) |
| meta_Combined_cereals | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top barley\|corn\|wheat (×450) |
| axis_unit | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top nm (×450) |
| axis_min | metadata | numeric | *Not specified.* | n=450, missing=0, range 950–950, mean 950 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=450, missing=0, range 1650–1650, mean 1650 ± 0 |
| license | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top CC BY 4.0 (×450) |
| license_url | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×450) |
| rights_status | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top explicit_open (×450) |
| usage_scope | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top public_reuse_possible (×450) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top True (×450) |
| doi_dataset | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top 10.5281/zenodo.15838136 (×450) |
| notes | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top Task-specific view of Perten source numeric axis, no interpolation or resampling by standardization. (×450) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/15838136`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/15838136`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `10.5281/zenodo.15838136`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 5 fields, Y: 1 fields, measurements: 1 fields, passport: 32 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Public redistribution is allowed under CC BY 4.0 with attribution, license link, and indication of modifications.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `cecc4ecafb54f369ddf4b55dd554753a79a750d5d023648303dd6e8d57e53092`
- **Processing hash:** `b0660d9a767236cdc1c27ebffab2a6b88c18ff6e87adfc712b4d1c809bd9b7d7` | **metadata hash:** `5e7bdaee2b1a00cacfe7008a99af36afa364b0030159707df5fe59824727fdf6`
