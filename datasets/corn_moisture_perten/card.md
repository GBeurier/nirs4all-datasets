# Datasheet — Corn Perten moisture NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** corn
- **Description:** Corn Perten moisture NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, corn
- **Contributor:** sensAIfood cereal NIR data (wheat, corn, barley) and reference protein and moisture (Perten set)

## Composition

- **Alignment:** sample level; 150 sample(s), 150 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Corn Perten moisture NIR | Perten DA7200/DA72xx/DA7440/DA7250/DA7300 as available by sample | NIR | 950–1650 nm | 150 | 141 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| moisture | target | numeric | *Not specified.* | n=150, missing=0, range 7.925–31.82, mean 13.16 ± 3.864 |
| SpectralRep | metadata | numeric | *Not specified.* | n=150, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top sensAIfood Perten Cereals (×150) |
| dataset_title | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Corn Perten moisture (×150) |
| dataset_slug | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top corn_moisture_perten (×150) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top NIR (×150) |
| cereal_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top corn (×150) |
| trait_header | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top moisture (×150) |
| trait_header_original | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Moisture (×150) |
| task_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top regression (×150) |
| raw_label | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top CornWholePerten0001 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=150, missing=0, range 7.925–31.82, mean 13.16 ± 3.864 |
| n_points_original | metadata | numeric | *Not specified.* | n=150, missing=0, range 141–141, mean 141 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 1D (×150) |
| axis_note | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top source_axis_950_to_1650_nm_step_5 (×150) |
| ID | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top CornWholePerten0001 (×1) |
| Spectrometer | metadata | categorical | *Not specified.* | n=150, missing=0, classes=3, top Perten_DA7200 (×131) |
| Cereal | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top corn (×150) |
| Variety | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Unknown (×150) |
| Country | metadata | categorical | *Not specified.* | n=150, missing=0, classes=5, top US (×53) |
| Year | metadata | numeric | *Not specified.* | n=150, missing=0, range 0–2017, mean 1888 ± 478.5 |
| Protein | metadata | numeric | *Not specified.* | n=150, missing=0, range 6.397–13.83, mean 9.491 ± 1.652 |
| meta_Spectrometer_Make_Model | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Perten: DA7200, DA7250 (×150) |
| meta_Wavelength_Range_nm | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 950-1650 (×150) |
| meta_Spectral_Resolution_nm | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top WL accuracy < 0.05 nm, all data provided is 5nm step (×150) |
| meta_Number_of_Scans_per_Spectrum | metadata | numeric | *Not specified.* | n=150, missing=0, range 100–100, mean 100 ± 0 |
| meta_Grain_Type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Corn (whole) (×150) |
| meta_Variety | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Unknown (×150) |
| meta_Country | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Turkey, South Africa, Croatia, US (×150) |
| meta_Year | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 2006, 2007, 2011, 2012, 2017 (×150) |
| meta_Reference_Method_Protein | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Kjeldahl (×150) |
| meta_Reference_Method_Moisture | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Oven (×150) |
| meta_Units_for_Protein | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top % protein (N6_25) (×150) |
| meta_Units_for_Moisture | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top % moisture (×150) |
| meta_Reference_for_moisture | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Dry Basis (×150) |
| meta_Citation | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Perten (for sensAIfood) (×150) |
| meta_Autorship | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top applications.perten@perkinelmer.com (×150) |
| meta_Detector_Type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Diod-Array: 256 pixel thermoelectrically cooled, high-detectivity indium gallium aresenide (InGaAs) (×150) |
| meta_Geometry | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top diffuse reflectance (post-dispersive) (×150) |
| meta_Optical_Reference_Material | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Teflon coated ceramic reference (×150) |
| meta_Software_Used_for_Acquisition | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Perten Software (Results Plus or Process Plus) (×150) |
| meta_Sampling_notes | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top No duplicated in provided data (×150) |
| axis_unit | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top nm (×150) |
| axis_min | metadata | numeric | *Not specified.* | n=150, missing=0, range 950–950, mean 950 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=150, missing=0, range 1650–1650, mean 1650 ± 0 |
| license | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top CC BY 4.0 (×150) |
| license_url | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×150) |
| rights_status | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top explicit_open (×150) |
| usage_scope | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top public_reuse_possible (×150) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top True (×150) |
| doi_dataset | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 10.5281/zenodo.15838136 (×150) |
| notes | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Task-specific view of Perten source numeric axis, no interpolation or resampling by standardization. (×150) |

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
- **Curated views:** M: 3 fields, Y: 1 fields, measurements: 1 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `e5bbb75196009555a5ba4c4536595d235446d0d23ae195545bb57e91a1214ee9`
- **Processing hash:** `437cf8aa8fab4e3bb19991ad443a118cfda226b9b676d91b5711314e12bfb820` | **metadata hash:** `509b10e35cf4ec64af55aff34b88bb0eb32f1afc7b2c309a3e1401ad91a112f3`
