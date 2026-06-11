# Datasheet — EcoSIS Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 14 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** observation level; 35 sample(s), 363 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 9–16 (mean 10.37).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_freshspectra.csv | Spectral Evolution PSR-3500+ | NIR | 350–2500 nm | 363 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| foreoptic_type | target | categorical | *Not specified.* | n=35, missing=0, classes=2, top LC (×28) |
| sample_number | target | numeric | *Not specified.* | n=35, missing=0, range 5–76, mean 43.8 ± 20.92 |
| family | target | categorical | *Not specified.* | n=35, missing=0, classes=10, top Fagaceae (×9) |
| genus | target | categorical | *Not specified.* | n=35, missing=1, classes=9, top Quercus (×9) |
| species | target | categorical | *Not specified.* | n=35, missing=7, classes=13, top kelloggii (×5) |
| plant_functional_type | target | categorical | *Not specified.* | n=35, missing=0, classes=3, top Shrub (×23) |
| tree_DBH_cm | target | numeric | *Not specified.* | n=35, missing=25, range 21.4–88.8, mean 49.53 ± 24.8 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=35, missing=27, range 6.75–19.9, mean 13.04 ± 4.135 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=35, missing=25, range 8.5–19.4, mean 12.58 ± 3.243 |
| tree_height_m | target | numeric | *Not specified.* | n=35, missing=25, range 4.5–15.96, mean 9.117 ± 3.319 |
| crown_length_m | target | numeric | *Not specified.* | n=35, missing=25, range 3.875–13.52, mean 8.243 ± 2.68 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=35, missing=0, range 37.36–306.3, mean 130.6 ± 71.97 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=35, missing=0, range 40.16–75.69, mean 55.67 ± 8.039 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=35, missing=0, range 293–835, mean 462.9 ± 107.3 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top 56f8a7af-5e0d-42dd-8368-2c953940855f (×35) |
| site | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Sierra Nevada of California (×35) |
| country | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top source-provided coordinates when available (×35) |
| year | metadata | numeric | *Not specified.* | n=35, missing=0, range 2023–2023, mean 2023 ± 0 |
| date | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Leaf (×35) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top leaf (×35) |
| instrument | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Spectral Evolution PSR-3500+ (×35) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Contact (×35) |
| signal_type | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top reflectance (×35) |
| axis_unit | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top nm (×35) |
| axis_min | metadata | numeric | *Not specified.* | n=35, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=35, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=35, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×35) |
| license | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×35) |
| rights_status | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top explicit_open (×35) |
| usage_scope | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top public_reuse_possible (×35) |
| notes | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top EcoSIS package fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×35) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
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
- **Content hash:** `a4c54e2019ee582f70d7a8c435419cac92901db42abe4a8d062152bb9ab78117`
- **Processing hash:** `68bb2b812c386fd05772b599174f07e26bf1d3f198093801618a9e756144ef9b` | **metadata hash:** `3a62aebf06c99e744700d179cc77dda9d7c5e9107cf3fc35f67ba59ebafed611`
