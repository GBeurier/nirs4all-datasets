# Datasheet — EcoSIS Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 16 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** observation level; 83 sample(s), 498 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 6–6 (mean 6).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_ovendried_dryspectra.csv | Analytical Spectral Devices FieldSpec 3 | NIR | 350–2500 nm | 498 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_number | target | numeric | *Not specified.* | n=83, missing=0, range 1–83, mean 42 ± 24.1 |
| family | target | categorical | *Not specified.* | n=83, missing=3, classes=14, top Pinaceae (×31) |
| genus | target | categorical | *Not specified.* | n=83, missing=5, classes=15, top Pinus (×17) |
| species | target | categorical | *Not specified.* | n=83, missing=14, classes=23, top decurrens (×9) |
| plant_functional_type | target | categorical | *Not specified.* | n=83, missing=0, classes=7, top Tree (×50) |
| part_of_plant | target | categorical | *Not specified.* | n=83, missing=0, classes=3, top Leaf (×81) |
| young_needle_percent | target | numeric | *Not specified.* | n=83, missing=46, range 0–80, mean 25 ± 19.86 |
| old_needle_percent | target | numeric | *Not specified.* | n=83, missing=46, range 20–100, mean 75 ± 19.86 |
| tree_DBH_cm | target | numeric | *Not specified.* | n=83, missing=33, range 21.4–158.5, mean 89.98 ± 38.15 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=83, missing=39, range 6.75–19.9, mean 11.59 ± 3.05 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=83, missing=33, range 7.3–19.4, mean 11.25 ± 2.859 |
| tree_height_m | target | numeric | *Not specified.* | n=83, missing=33, range 4.5–19.97, mean 11.85 ± 3.673 |
| crown_length_m | target | numeric | *Not specified.* | n=83, missing=33, range 3.875–16.5, mean 9.299 ± 2.719 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=83, missing=2, range 37.36–606.8, mean 227.4 ± 142.4 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=83, missing=2, range 40.16–87.92, mean 56.52 ± 9.38 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=83, missing=2, range 95–835, mean 403 ± 115.7 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top 132d4f67-b37d-4211-b685-5adea4527c75 (×83) |
| site | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Sierra Nevada of California (×83) |
| country | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top source-provided coordinates when available (×83) |
| year | metadata | numeric | *Not specified.* | n=83, missing=0, range 2023–2023, mean 2023 ± 0 |
| date | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Leaf (×83) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top leaf (×83) |
| instrument | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Analytical Spectral Devices FieldSpec 3 (×83) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Contact (×83) |
| signal_type | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top reflectance (×83) |
| axis_unit | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top nm (×83) |
| axis_min | metadata | numeric | *Not specified.* | n=83, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=83, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=83, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×83) |
| license | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×83) |
| rights_status | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top explicit_open (×83) |
| usage_scope | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top public_reuse_possible (×83) |
| notes | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top EcoSIS package oven-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×83) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/oven-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** ODbL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `a35b9b0fed5ea4f0f7accac22111321fd756abcb4a0f21a36bc0b0533b9efe76`
- **Processing hash:** `248cecc9b0b929eb1133a5479f38ea5392c174f21e4a654559ec4b09229673a2` | **metadata hash:** `ad43ced16482969a2985d07c5e7164558951310299c7502e6b38fb532e1410a5`
