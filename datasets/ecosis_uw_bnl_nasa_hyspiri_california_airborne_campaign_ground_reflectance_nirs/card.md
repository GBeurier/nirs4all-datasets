# Datasheet — EcoSIS UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** UW-BNL NASA HyspIRI California Airborne Campaign Ground Target Spectra

## Composition

- **Alignment:** observation level; 64 sample(s), 64 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

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

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-california-airborne-campaign-ground-target-spectra`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `cb659ee33b73d0dc1fc7997f0410c095a13757d656f13564c2f023b51ce631cd`
- **Processing hash:** `7c1191e7543f0e7c73ed1c1251dc2ac43be7a298c888c9daf23c92cf270fbed8` | **metadata hash:** `4fee2ee35e8461c447abd7b67dfc3e199ae3aa2ed04ab5b42249761feeb3d4a7`
