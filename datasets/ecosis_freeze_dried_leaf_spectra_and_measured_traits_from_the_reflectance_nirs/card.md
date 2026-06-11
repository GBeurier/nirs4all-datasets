# Datasheet — EcoSIS Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 16 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** observation level; 82 sample(s), 492 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 6–6 (mean 6).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_freezedried_dryspectra.csv | Analytical Spectral Devices FieldSpec 3 | NIR | 350–2500 nm | 492 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_number | target | numeric | *Not specified.* | n=82, missing=0, range 1–82, mean 41.5 ± 23.82 |
| family | target | categorical | *Not specified.* | n=82, missing=2, classes=14, top Pinaceae (×31) |
| genus | target | categorical | *Not specified.* | n=82, missing=4, classes=15, top Pinus (×17) |
| species | target | categorical | *Not specified.* | n=82, missing=13, classes=23, top decurrens (×9) |
| plant_functional_type | target | categorical | *Not specified.* | n=82, missing=0, classes=6, top Tree (×50) |
| part_of_plant | target | categorical | *Not specified.* | n=82, missing=0, classes=2, top Leaf (×81) |
| young_needle_percent | target | numeric | *Not specified.* | n=82, missing=45, range 0–80, mean 25 ± 19.86 |
| old_needle_percent | target | numeric | *Not specified.* | n=82, missing=45, range 20–100, mean 75 ± 19.86 |
| tree_DBH_cm | target | numeric | *Not specified.* | n=82, missing=32, range 21.4–158.5, mean 89.98 ± 38.15 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=82, missing=38, range 6.75–19.9, mean 11.59 ± 3.05 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=82, missing=32, range 7.3–19.4, mean 11.25 ± 2.859 |
| tree_height_m | target | numeric | *Not specified.* | n=82, missing=32, range 4.5–19.97, mean 11.85 ± 3.673 |
| crown_length_m | target | numeric | *Not specified.* | n=82, missing=32, range 3.875–16.5, mean 9.299 ± 2.719 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=82, missing=1, range 37.36–606.8, mean 227.4 ± 142.4 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=82, missing=1, range 40.16–87.92, mean 56.52 ± 9.38 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=82, missing=1, range 95–835, mean 403 ± 115.7 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top 33d4f97e-591c-4e6f-a913-f8f6465fa735 (×82) |
| site | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Sierra Nevada of California (×82) |
| country | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top source-provided coordinates when available (×82) |
| year | metadata | numeric | *Not specified.* | n=82, missing=0, range 2023–2023, mean 2023 ± 0 |
| date | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Leaf (×82) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top leaf (×82) |
| instrument | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Analytical Spectral Devices FieldSpec 3 (×82) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Contact (×82) |
| signal_type | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top reflectance (×82) |
| axis_unit | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top nm (×82) |
| axis_min | metadata | numeric | *Not specified.* | n=82, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=82, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=82, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=82, missing=82, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×82) |
| license | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×82) |
| rights_status | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top explicit_open (×82) |
| usage_scope | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top public_reuse_possible (×82) |
| notes | metadata | categorical | *Not specified.* | n=82, missing=0, classes=1, top EcoSIS package freeze-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×82) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/freeze-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
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
- **Content hash:** `b6bc6d79aeb923dd7e96f5d58789ed557f9bcaef72047bf1d24c56bcb6a5da6e`
- **Processing hash:** `7b4149a1a3b31044194d5c3b1444fce867e0ef5ed3e3b8bfbb77187d7c035e3c` | **metadata hash:** `daeb65c50ec0d8ffa7e12e05046863f183e1110cd7a026e67ad584a30f1dcbfe`
