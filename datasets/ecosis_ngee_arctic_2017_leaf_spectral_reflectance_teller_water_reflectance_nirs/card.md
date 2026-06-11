# Datasheet — EcoSIS NGEE Arctic 2017 Leaf Spectral Reflectance Teller Watershed Seward Peninsula Alaska (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Arctic 2017 Leaf Spectral Reflectance Teller Watershed Seward Peninsula Alaska (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Arctic 2017 Leaf Spectral Reflectance Teller Watershed Seward Peninsula Alaska

## Composition

- **Alignment:** observation level; 163 sample(s), 163 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Seward_2017_Leaf_Spectral_Reflectance.csv | Spectra Vista Corporation HR-1024i | NIR | 350–2500 nm | 163 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=163, missing=0, classes=16, top SAPU15 (×78) |
| CNratio | target | numeric | *Not specified.* | n=163, missing=43, range 15.19–38.15, mean 23.39 ± 5.06 |
| Cmass | target | numeric | *Not specified.* | n=163, missing=43, range 306.6–538.5, mean 479.1 ± 36.29 |
| Nmass | target | numeric | *Not specified.* | n=163, missing=43, range 9.4–31.6, mean 21.34 ± 4.362 |
| Carea | target | numeric | *Not specified.* | n=163, missing=43, range -9999–171.2, mean -119.5 ± 1292 |
| Narea | target | numeric | *Not specified.* | n=163, missing=43, range -9999–5.81, mean -164.6 ± 1286 |
| LWC | target | numeric | *Not specified.* | n=163, missing=0, range -9999–100, mean -251 ± 1739 |
| LMA | target | numeric | *Not specified.* | n=163, missing=0, range -9999–331.9, mean -150.2 ± 1567 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top d313ca44-f906-4603-8fe8-2d739c2f14f3 (×163) |
| site | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Seward_Teller (×163) |
| location | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top NGEE-Arctic Teller Watershed (×163) |
| country | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top source-provided coordinates when available (×163) |
| year | metadata | numeric | *Not specified.* | n=163, missing=0, range 2017–2017, mean 2017 ± 0 |
| date | metadata | categorical | *Not specified.* | n=163, missing=0, classes=4, top 20170802 (×68) |
| species | metadata | categorical | *Not specified.* | n=163, missing=0, classes=16, top SAPU15 (×78) |
| genus | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Leaf (×163) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top leaf (×163) |
| instrument | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×163) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Contact (×163) |
| signal_type | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top reflectance (×163) |
| axis_unit | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top nm (×163) |
| axis_min | metadata | numeric | *Not specified.* | n=163, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=163, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=163, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=163, missing=163, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Shawn P. Serbin Daryl Yang Ran Meng Andrew McMahon Wouter Hantson Daniel Hayes Kim Ely. 2017. NGEE Arctic 2017 Leaf Spectral Reflectance Teller Watershed Seward Peninsula Alaska. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×163) |
| license | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top Creative Commons Attribution (×163) |
| rights_status | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top explicit_open (×163) |
| usage_scope | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top public_reuse_possible (×163) |
| notes | metadata | categorical | *Not specified.* | n=163, missing=0, classes=1, top EcoSIS package ngee-arctic-2017-leaf-spectral-reflectance-teller-watershed-seward-peninsula-alaska, no interpolation applied by project. (×163) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-2017-leaf-spectral-reflectance-teller-watershed-seward-peninsula-alaska`
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
- **Content hash:** `053c533eae850c3dbada9f243beb9bf519cbbb2004272e6ce8053d024b69c593`
- **Processing hash:** `f4543459006fa3823a8b2a10d82239df52af328029786bea034ecb26182ee196` | **metadata hash:** `06e5e4a57f8a9f14544dd337aa692a77f788d3128010f556f72c382810c2efcc`
