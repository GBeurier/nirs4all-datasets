# Datasheet — EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (reflectance). Origin database composed from 4 standardized v2.0 leaves: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska

## Composition

- **Alignment:** sample level; 511 sample(s), 511 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Seward_2017_Canopy_Spectral_Reflectance.csv | Spectra Vista Corporation HR-1024i | NIR | 350–2500 nm | 511 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Spectra_Group | target | categorical | *Not specified.* | n=511, missing=1, classes=74, top NGEEArctic_Council_Transect01_8deg_Refl (×32) |
| Target_Type | target | categorical | *Not specified.* | n=511, missing=1, classes=3, top Vegetation (×479) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top 786ab19f-ae0b-4d80-ab93-3bc6c8610aae (×511) |
| site | metadata | categorical | *Not specified.* | n=511, missing=1, classes=3, top Seward_Teller (×366) |
| latitude | metadata | numeric | *Not specified.* | n=511, missing=1, range 64.73–65.17, mean 64.81 ± 0.1472 |
| longitude | metadata | numeric | *Not specified.* | n=511, missing=1, range -165.9–-163.7, mean -165.5 ± 0.833 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top source-provided coordinates when available (×511) |
| year | metadata | numeric | *Not specified.* | n=511, missing=0, range 2017–2017, mean 2017 ± 0 |
| date | metadata | categorical | *Not specified.* | n=511, missing=1, classes=5, top 20170730 (×218) |
| plant_part | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top NPV, Canopy, Rock, Soil, Water (×511) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top canopy (×511) |
| instrument | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×511) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Proximal (×511) |
| signal_type | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top reflectance (×511) |
| axis_unit | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top nm (×511) |
| axis_min | metadata | numeric | *Not specified.* | n=511, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=511, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=511, missing=0, range 2151–2151, mean 2151 ± 0 |
| citation | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Shawn P. Serbin Daryl Yang Ran Meng Andrew McMahon Wouter Hantson Daniel Hayes Kim Ely. 2017. NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×511) |
| license | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Creative Commons Attribution (×511) |
| rights_status | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top explicit_open (×511) |
| usage_scope | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top public_reuse_possible (×511) |
| notes | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top EcoSIS package ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska, no interpolation applied by project. (×511) |
| LMA | target | numeric | *Not specified.* | n=511, missing=468, range 33.82–331.9, mean 108 ± 58.44 |
| LWC | target | numeric | *Not specified.* | n=511, missing=468, range 40.2–91.37, mean 57.32 ± 11.01 |
| Narea | target | numeric | *Not specified.* | n=511, missing=470, range 0.75–5.81, mean 2.22 ± 1.145 |
| source_SampleID | metadata | categorical | *Not specified.* | n=511, missing=0, classes=511, top NGEEArctic_Council_Road01_8deg_Refl_000 (×1) |
| source_Site | metadata | categorical | *Not specified.* | n=511, missing=1, classes=3, top Seward_Teller (×366) |
| source_Date | metadata | categorical | *Not specified.* | n=511, missing=1, classes=5, top 20170730 (×218) |
| source_Spectra_Name | metadata | categorical | *Not specified.* | n=511, missing=1, classes=505, top NGEEArctic_Teller_Plot06_Canopy01_8deg_Refl (×4) |
| source_Dominant_Species | metadata | categorical | *Not specified.* | n=511, missing=1, classes=15, top -9999 (×467) |
| source_Measurement_Time_UTC | metadata | categorical | *Not specified.* | n=511, missing=1, classes=502, top 0:48:28 (×4) |
| source_Latitude | metadata | numeric | *Not specified.* | n=511, missing=1, range 64.73–65.17, mean 64.81 ± 0.1472 |
| source_Longitude | metadata | numeric | *Not specified.* | n=511, missing=1, range -165.9–-163.7, mean -165.5 ± 0.833 |
| source_Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Spectra Vista Corporation (×510) |
| source_Instrument_Model | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top HR-1024i (×510) |
| source_Instrument_Serial_Number | metadata | numeric | *Not specified.* | n=511, missing=1, range 2041–2041, mean 2041 ± 0 |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top 8deg (×510) |
| source_Collection_Units | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Radiance (×510) |
| source_Spectra_Units | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Percent_Reflectance_0_100 (×510) |
| source_Spectra_Type | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Canopy (×510) |
| source_Reflectance_Type | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Spectralon_Corrected (×510) |
| source_White_Reference_Standard | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top 99AA04-0715-2212-SRT-99-100 (×510) |
| source_Spectral_Resolution | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top 1nm (×510) |
| source_Interpolation_Method | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Linear (×510) |
| source_Overlap_Handling | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Removed (×510) |
| source_Overlap_Removal | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Post_processing (×510) |
| source_Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=511, missing=1, classes=1, top Radiance (×510) |
| SpectralRep | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 1 (×43) |
| SampleID | metadata | categorical | *Not specified.* | n=511, missing=468, classes=43, top BNL13145 (×1) |
| Site | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Seward_Teller (×43) |
| Date | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 20170730.0 (×43) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=511, missing=468, classes=38, top NGEEArctic_Teller_Plot06_Canopy01_8deg_Refl (×4) |
| Dominant_Species | metadata | categorical | *Not specified.* | n=511, missing=468, classes=14, top SAPU15 (×11) |
| Measurement_Time_UTC | metadata | categorical | *Not specified.* | n=511, missing=468, classes=38, top 0:48:28 (×4) |
| Latitude | metadata | categorical | *Not specified.* | n=511, missing=468, classes=38, top 64.73128 (×4) |
| Longitude | metadata | categorical | *Not specified.* | n=511, missing=468, classes=38, top -165.94782 (×4) |
| Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Spectra Vista Corporation (×43) |
| Instrument_Model | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top HR-1024i (×43) |
| Instrument_Serial_Number | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 2041.0 (×43) |
| Foreoptic | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 8deg (×43) |
| Collection_Units | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Radiance (×43) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Percent_Reflectance_0_100 (×43) |
| Spectra_Type | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Canopy (×43) |
| Reflectance_Type | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Spectralon_Corrected (×43) |
| White_Reference_Standard | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 99AA04-0715-2212-SRT-99-100 (×43) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 1nm (×43) |
| Interpolation_Method | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Linear (×43) |
| Overlap_Handling | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Removed (×43) |
| Overlap_Removal | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Post_processing (×43) |
| Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top Radiance (×43) |
| CNratio | metadata | categorical | *Not specified.* | n=511, missing=470, classes=41, top 23.52 (×1) |
| Cmass | metadata | categorical | *Not specified.* | n=511, missing=470, classes=40, top 469.3 (×2) |
| Nmass | metadata | categorical | *Not specified.* | n=511, missing=470, classes=37, top 22.1 (×2) |
| Carea | metadata | categorical | *Not specified.* | n=511, missing=470, classes=41, top 108.36 (×1) |
| dataset | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top EcoSIS (×43) |
| dimensions | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top 1D (×43) |
| axis_note | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×43) |
| official_data_url | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top https://data.ecosis.org/dataset/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska (×43) |
| official_package_url | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top https://ecosis.org/package/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska (×43) |
| license_url | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top http://www.opendefinition.org/licenses/cc-by (×43) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top True (×43) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=511, missing=468, classes=1, top ecosis_ngee_arctic_2017_canopy_spectral_reflectance_seward_pen_reflectance_nirs (×43) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 8 fields, Y: 4 fields, passport: 50 fields, measurements: 5 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `57753b0d401fcceb61518800c64b55299f6f838abe39178fd73cdb7b6d3871d0`
- **Processing hash:** `31529f8f5805f97d4469032acfe5d414406a0234ca257256432143ea445d446e` | **metadata hash:** `9c4e0b99be58ee8a3d7372c2a5dd965d783f013a0138bf2251bb6564385ae151`
