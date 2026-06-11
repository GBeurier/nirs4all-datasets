# Datasheet — EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska

## Composition

- **Alignment:** observation level; 511 sample(s), 511 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

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
| location | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=511, missing=1, range 64.73–65.17, mean 64.81 ± 0.1472 |
| longitude | metadata | numeric | *Not specified.* | n=511, missing=1, range -165.9–-163.7, mean -165.5 ± 0.833 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top source-provided coordinates when available (×511) |
| year | metadata | numeric | *Not specified.* | n=511, missing=0, range 2017–2017, mean 2017 ± 0 |
| date | metadata | categorical | *Not specified.* | n=511, missing=1, classes=5, top 20170730.0 (×218) |
| species | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top NPV, Canopy, Rock, Soil, Water (×511) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top canopy (×511) |
| instrument | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×511) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Proximal (×511) |
| signal_type | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top reflectance (×511) |
| axis_unit | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top nm (×511) |
| axis_min | metadata | numeric | *Not specified.* | n=511, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=511, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=511, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=511, missing=511, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Shawn P. Serbin Daryl Yang Ran Meng Andrew McMahon Wouter Hantson Daniel Hayes Kim Ely. 2017. NGEE Arctic 2017 Canopy Spectral Reflectance Seward Peninsula Alaska. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×511) |
| license | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top Creative Commons Attribution (×511) |
| rights_status | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top explicit_open (×511) |
| usage_scope | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top public_reuse_possible (×511) |
| notes | metadata | categorical | *Not specified.* | n=511, missing=0, classes=1, top EcoSIS package ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska, no interpolation applied by project. (×511) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-2017-canopy-spectral-reflectance-seward-peninsula-alaska`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `60209b7e951fcee9ab323ebcabfdba31680c94ddb5f496ce3b49ec0eb9d984d7`
- **Processing hash:** `37317ba6644819811af1413d8803e17d132c7a5061316f993027e255cbd1d8d6` | **metadata hash:** `fe7d3cf5c79ef0aecc2cec69d3147700f18014e6ac66999ccbb6e2d5280550fa`
