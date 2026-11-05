# Datasheet — UW-BNL HyspIRI California — ground-target reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra

## Composition

- **Alignment:** sample level; 64 sample(s), 64 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW-BNL_NASA_HyspIRI_Airborne_Campaign_Ground_Cal_Target_Spectra_spectral_measurements.csv | Spectral Evolution PSM-3500 | NIR | 350–2500 nm | 64 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Target_Type | target | categorical | *Not specified.* | n=64, missing=0, classes=8, top Bare ground / field (×23) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top 2874cc96-3343-4124-bd05-89b8082f78f0 (×64) |
| site | metadata | categorical | *Not specified.* | n=64, missing=0, classes=4, top Sierra National Forest (×27) |
| location | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=64, missing=0, range 33.52–37.08, mean 35.54 ± 1.714 |
| longitude | metadata | numeric | *Not specified.* | n=64, missing=0, range -119.3–-115.4, mean -117.8 ± 1.594 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top source-provided coordinates when available (×64) |
| year | metadata | numeric | *Not specified.* | n=64, missing=0, range 2015–2015, mean 2015 ± 0 |
| date | metadata | categorical | *Not specified.* | n=64, missing=0, classes=7, top 6/18/13 (×22) |
| species | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Rock, Soil, NPV, Mineral (×64) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=64, missing=64, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Spectral Evolution PSM-3500 (×64) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Proximal (×64) |
| signal_type | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top reflectance (×64) |
| axis_unit | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top nm (×64) |
| axis_min | metadata | numeric | *Not specified.* | n=64, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=64, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=64, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top 10.21232/CDHbHePS (×64) |
| citation | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Shawn Serbin Sean DuBois Andrew Jablonski Ankur Desai Eric Kruger Philip Townsend. 2015. UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/CDHbHePS (×64) |
| license | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Open Data Commons Attribution License (×64) |
| rights_status | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top explicit_open (×64) |
| usage_scope | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top public_reuse_possible (×64) |
| notes | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top EcoSIS package uw-bnl-nasa-hyspiri-california-airborne-campaign-ground-target-spectra, no interpolation applied by project. (×64) |
| source_Spectra | metadata | categorical | *Not specified.* | n=64, missing=0, classes=64, top Ivanpah_1 (×1) |
| source_Site | metadata | categorical | *Not specified.* | n=64, missing=0, classes=4, top Sierra National Forest (×27) |
| source_Site_Code | metadata | categorical | *Not specified.* | n=64, missing=0, classes=4, top SNF (×27) |
| source_Measurement_Date | metadata | categorical | *Not specified.* | n=64, missing=0, classes=7, top 6/18/13 (×22) |
| source_Measurement_Time | metadata | categorical | *Not specified.* | n=64, missing=12, classes=16, top 16:52:03 (×15) |
| source_Latitude | metadata | numeric | *Not specified.* | n=64, missing=0, range 33.52–37.08, mean 35.54 ± 1.714 |
| source_Longitude | metadata | numeric | *Not specified.* | n=64, missing=0, range -119.3–-115.4, mean -117.8 ± 1.594 |
| source_Reference | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Spectralon (×64) |
| source_Measurement | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Reflectance (×64) |
| source_Spectra_Units | metadata | categorical | *Not specified.* | n=64, missing=0, classes=2, top Ratio (×51) |
| source_Spectral_Resolution | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top 1nm (×64) |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=64, missing=0, classes=3, top Bare_Fiber (×39) |
| source_Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top Spectral Evolution (×64) |
| source_Instrument_Model | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top PSM-3500 (×64) |
| source_Instrument_Serial_Number | metadata | categorical | *Not specified.* | n=64, missing=0, classes=1, top SN1336023[3] (×64) |
| source_Comments | metadata | categorical | *Not specified.* | n=64, missing=22, classes=4, top Collection details: Spectra was collected using a 1.5 meter long fiber connected to the instrument collection port. Data collection was done using the bare (22deg) fiber mounted in a pistol grip assembly. A white reference was collected prior to collection of the concrete and blacktop target spectrum. Target spectrum were collected ~90cm away from the operator at a height of ~1.2 meters above the surface. The sky was 100% cloud free, wind was minimal, slightly hazy. (×22) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-california-airborne-campaign-ground-target-spectra`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 8 fields, Y: 1 fields, measurements: 1 fields, passport: 35 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra — [10.21232/CDHbHePS](https://doi.org/10.21232/CDHbHePS)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `a5583a61de9b63b400434bffa5c065f6e25a58c4c71f7d97e50eb7624e62a8ef`
- **Processing hash:** `ce05b7465200e635d5bd27b5dde9ca4581d5d12132f1e349a1f158f0c4191659` | **metadata hash:** `78b18f8da0d5a339f56c02be266faca65028762693bf70aa290b6f7213632b8b`
