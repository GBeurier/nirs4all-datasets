# Datasheet — EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (LMA)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** canopy
- **Description:** EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (LMA). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, canopy
- **Contributor:** NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska

## Composition

- **Alignment:** sample level; 43 sample(s), 43 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Seward_2017_Canopy_Spectral_Reflectance | *Not specified.* | NIR | 350–2500 nm | 43 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=43, missing=0, range 33.82–331.9, mean 108 ± 58.44 |
| SpectralRep | metadata | numeric | *Not specified.* | n=43, missing=0, range 1–1, mean 1 ± 0 |
| SampleID | metadata | categorical | *Not specified.* | n=43, missing=0, classes=43, top BNL13145 (×1) |
| Site | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Seward_Teller (×43) |
| Date | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top 20170730.0 (×43) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=43, missing=0, classes=38, top NGEEArctic_Teller_Plot06_Canopy01_8deg_Refl (×4) |
| Spectra_Group | metadata | categorical | *Not specified.* | n=43, missing=0, classes=38, top Plot06_Canopy01 (×4) |
| Target_Type | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Vegetation (×43) |
| Dominant_Species | metadata | categorical | *Not specified.* | n=43, missing=0, classes=14, top SAPU15 (×11) |
| Measurement_Time_UTC | metadata | categorical | *Not specified.* | n=43, missing=0, classes=38, top 0:48:28 (×4) |
| Latitude | metadata | numeric | *Not specified.* | n=43, missing=0, range 64.73–64.73, mean 64.73 ± 0.002043 |
| Longitude | metadata | numeric | *Not specified.* | n=43, missing=0, range -165.9–-165.9, mean -165.9 ± 0.003006 |
| Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Spectra Vista Corporation (×43) |
| Instrument_Model | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top HR-1024i (×43) |
| Instrument_Serial_Number | metadata | numeric | *Not specified.* | n=43, missing=0, range 2041–2041, mean 2041 ± 0 |
| Foreoptic | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top 8deg (×43) |
| Collection_Units | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Radiance (×43) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Percent_Reflectance_0_100 (×43) |
| Spectra_Type | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Canopy (×43) |
| Reflectance_Type | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Spectralon_Corrected (×43) |
| White_Reference_Standard | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top 99AA04-0715-2212-SRT-99-100 (×43) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top 1nm (×43) |
| Interpolation_Method | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Linear (×43) |
| Overlap_Handling | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Removed (×43) |
| Overlap_Removal | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Post_processing (×43) |
| Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Radiance (×43) |
| CNratio | metadata | numeric | *Not specified.* | n=43, missing=2, range 16.17–35.88, mean 24.55 ± 5.536 |
| Cmass | metadata | numeric | *Not specified.* | n=43, missing=2, range 333.1–538.5, mean 473.3 ± 45.48 |
| Nmass | metadata | numeric | *Not specified.* | n=43, missing=2, range 13.1–31.6, mean 20.12 ± 4.501 |
| Carea | metadata | numeric | *Not specified.* | n=43, missing=2, range 14.04–171.2, mean 53.8 ± 31.35 |
| Narea | metadata | numeric | *Not specified.* | n=43, missing=2, range 0.75–5.81, mean 2.22 ± 1.145 |
| LWC | metadata | numeric | *Not specified.* | n=43, missing=0, range 40.2–91.37, mean 57.32 ± 11.01 |
| dataset | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top EcoSIS (×43) |
| dataset_slug | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska (×43) |
| task_type | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top regression (×43) |
| trait_header | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top LMA (×43) |
| target_original_name | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top LMA (×43) |
| measurement_hint | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Seward_2017_Canopy_Spectral_Reflectance (×43) |
| raw_label | metadata | categorical | *Not specified.* | n=43, missing=0, classes=43, top 201.22 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=43, missing=0, range 33.82–331.9, mean 108 ± 58.44 |
| class_index | metadata | categorical | *Not specified.* | n=43, missing=43, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=43, missing=43, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=43, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top 1D (×43) |
| axis_note | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×43) |
| official_data_url | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top https://data.ecosis.org/dataset/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska (×43) |
| official_package_url | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top https://ecosis.org/package/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska (×43) |
| license | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Creative Commons Attribution (×43) |
| license_url | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×43) |
| rights_status | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top explicit_open (×43) |
| usage_scope | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top public_reuse_possible (×43) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top True (×43) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top ecosis_ngee_arctic_2017_canopy_spectral_reflectance_seward_pen_reflectance_nirs (×43) |
| notes | metadata | categorical | *Not specified.* | n=43, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×43) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 4 fields, Y: 1 fields, measurements: 9 fields, passport: 47 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `15b3bb756cd9340c5f83c3065c9b01e87a980f5a53b482f943219025ebba6c37`
- **Processing hash:** `a99b23c49a6a1b8768d130d3282dfc92b3d44373236abaee2b2dd14d4abd395f` | **metadata hash:** `d36304b981d339329394bc2f44f1ce6a3f676b65893fb1d07e49ba40576f3eaa`
