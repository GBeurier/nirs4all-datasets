# Datasheet — Wheat Perten protein NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** wheat
- **Description:** Wheat Perten protein NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, wheat
- **Contributor:** sensAIfood cereal NIR data (wheat, corn, barley) and reference protein and moisture (Perten set)

## Composition

- **Alignment:** sample level; 150 sample(s), 150 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Wheat Perten protein NIR | Perten DA7200/DA72xx/DA7440/DA7250/DA7300 as available by sample | NIR | 950–1650 nm | 150 | 141 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| protein | target | numeric | *Not specified.* | n=150, missing=0, range 8.42–20.29, mean 12.79 ± 2.571 |
| SpectralRep | metadata | numeric | *Not specified.* | n=150, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top sensAIfood Perten Cereals (×150) |
| dataset_title | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Wheat Perten protein (×150) |
| dataset_slug | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top wheat_protein_perten (×150) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top NIR (×150) |
| cereal_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top wheat (×150) |
| trait_header | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top protein (×150) |
| trait_header_original | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Protein (×150) |
| task_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top regression (×150) |
| raw_label | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top WheatWholePerten0001 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=150, missing=0, range 8.42–20.29, mean 12.79 ± 2.571 |
| n_points_original | metadata | numeric | *Not specified.* | n=150, missing=0, range 141–141, mean 141 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 1D (×150) |
| axis_note | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top source_axis_950_to_1650_nm_step_5 (×150) |
| ID | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top WheatWholePerten0001 (×1) |
| Spectrometer | metadata | categorical | *Not specified.* | n=150, missing=0, classes=3, top Perten_DA7200 (×141) |
| Cereal | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top wheat (×150) |
| Variety | metadata | categorical | *Not specified.* | n=150, missing=0, classes=3, top Wheat (×99) |
| Country | metadata | categorical | *Not specified.* | n=150, missing=0, classes=7, top Spain (×57) |
| Year | metadata | numeric | *Not specified.* | n=150, missing=0, range 2002–2014, mean 2007 ± 3.114 |
| Moisture | metadata | numeric | *Not specified.* | n=150, missing=0, range 7.6–19.28, mean 12.42 ± 2.499 |
| meta_Spectrometer_Make_Model | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Perten: DA7200, DA7300 (×150) |
| meta_Wavelength_Range_nm | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 950-1650 (×150) |
| meta_Spectral_Resolution_nm | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top WL accuracy < 0.05 nm, all data provided is 5nm step (×150) |
| meta_Number_of_Scans_per_Spectrum | metadata | numeric | *Not specified.* | n=150, missing=0, range 100–100, mean 100 ± 0 |
| meta_Grain_Type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Wheat (whole) (×150) |
| meta_Variety | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Durum, Wheat, Canadian Hard R (×150) |
| meta_Country | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Spain, Sweden, Australia, Canada, US, UK, Norway (×150) |
| meta_Year | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 2002, 2006, 2007, 2008, 2011, 2014 (×150) |
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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 4 fields, Y: 1 fields, measurements: 1 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `638aa55c77e7860778f590ab3b772967db974085cb9509ebec6d553c7abbc638`
- **Processing hash:** `84906bc87df8d0bb1ed0c1509285d6334b8482761776cd1e0d79e1cc2d608aa3` | **metadata hash:** `49f9d7817555b1a0aa8b5113fcb5ff88b9e00c8bbd5d800f836772ac26dba672`
