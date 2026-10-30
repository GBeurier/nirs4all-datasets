# Datasheet — EcoSIS Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 16 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** sample level; 83 sample(s), 498 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 6–6 (mean 6).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_ovendried_dryspectra.csv | Analytical Spectral Devices FieldSpec 3 | NIR | 350–2500 nm | 498 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_number | target | numeric | *Not specified.* | n=498, missing=0, range 1–83, mean 42 ± 23.98 |
| family | target | categorical | *Not specified.* | n=498, missing=18, classes=14, top Pinaceae (×186) |
| genus | target | categorical | *Not specified.* | n=498, missing=30, classes=15, top Pinus (×102) |
| species | target | categorical | *Not specified.* | n=498, missing=84, classes=23, top decurrens (×54) |
| plant_functional_type | target | categorical | *Not specified.* | n=498, missing=0, classes=7, top Tree (×300) |
| part_of_plant | target | categorical | *Not specified.* | n=498, missing=0, classes=3, top Leaf (×486) |
| young_needle_percent | target | numeric | *Not specified.* | n=498, missing=276, range 0–80, mean 25 ± 19.63 |
| old_needle_percent | target | numeric | *Not specified.* | n=498, missing=276, range 20–100, mean 75 ± 19.63 |
| tree_DBH_cm | target | numeric | *Not specified.* | n=498, missing=198, range 21.4–158.5, mean 89.98 ± 37.83 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=498, missing=234, range 6.75–19.9, mean 11.59 ± 3.021 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=498, missing=198, range 7.3–19.4, mean 11.25 ± 2.835 |
| tree_height_m | target | numeric | *Not specified.* | n=498, missing=198, range 4.5–19.97, mean 11.85 ± 3.642 |
| crown_length_m | target | numeric | *Not specified.* | n=498, missing=198, range 3.875–16.5, mean 9.299 ± 2.696 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=498, missing=12, range 37.36–606.8, mean 227.4 ± 141.6 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=498, missing=12, range 40.16–87.92, mean 56.52 ± 9.332 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=498, missing=12, range 95–835, mean 403 ± 115.1 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top 132d4f67-b37d-4211-b685-5adea4527c75 (×498) |
| site | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Sierra Nevada of California (×498) |
| country | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top source-provided coordinates when available (×498) |
| year | metadata | numeric | *Not specified.* | n=498, missing=0, range 2023–2023, mean 2023 ± 0 |
| date | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Leaf (×498) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top leaf (×498) |
| instrument | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Analytical Spectral Devices FieldSpec 3 (×498) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Contact (×498) |
| signal_type | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top reflectance (×498) |
| axis_unit | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top nm (×498) |
| axis_min | metadata | numeric | *Not specified.* | n=498, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=498, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=498, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=498, missing=498, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Oven Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×498) |
| license | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×498) |
| rights_status | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top explicit_open (×498) |
| usage_scope | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top public_reuse_possible (×498) |
| notes | metadata | categorical | *Not specified.* | n=498, missing=0, classes=1, top EcoSIS package oven-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×498) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/oven-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates. Index fields examined: source_replicate_id. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 7 fields, Y: 15 fields, measurements: 0 fields, passport: 34 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `ebc561c23f07f56ef140f21a40d42e2608e6cc6b530a0b815c9e2767a28b9d3f`
- **Processing hash:** `d24f5c6b3775022b31717fb28720625161216e7c753b9a0880e2528b092ba463` | **metadata hash:** `fe3033dafa7f5fcf5c8a35a45ec5f828a64c1c21c73f2ccc2f1db99d173941ef`
