# Datasheet — EcoSIS Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 16 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** sample level; 82 sample(s), 492 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 6–6 (mean 6).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_freezedried_dryspectra.csv | Analytical Spectral Devices FieldSpec 3 | NIR | 350–2500 nm | 492 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_number | target | numeric | *Not specified.* | n=492, missing=0, range 1–82, mean 41.5 ± 23.69 |
| family | target | categorical | *Not specified.* | n=492, missing=12, classes=14, top Pinaceae (×186) |
| genus | target | categorical | *Not specified.* | n=492, missing=24, classes=15, top Pinus (×102) |
| species | target | categorical | *Not specified.* | n=492, missing=78, classes=23, top decurrens (×54) |
| plant_functional_type | target | categorical | *Not specified.* | n=492, missing=0, classes=6, top Tree (×300) |
| part_of_plant | target | categorical | *Not specified.* | n=492, missing=0, classes=2, top Leaf (×486) |
| young_needle_percent | target | numeric | *Not specified.* | n=492, missing=270, range 0–80, mean 25 ± 19.63 |
| old_needle_percent | target | numeric | *Not specified.* | n=492, missing=270, range 20–100, mean 75 ± 19.63 |
| tree_DBH_cm | target | numeric | *Not specified.* | n=492, missing=192, range 21.4–158.5, mean 89.98 ± 37.83 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=492, missing=228, range 6.75–19.9, mean 11.59 ± 3.021 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=492, missing=192, range 7.3–19.4, mean 11.25 ± 2.835 |
| tree_height_m | target | numeric | *Not specified.* | n=492, missing=192, range 4.5–19.97, mean 11.85 ± 3.642 |
| crown_length_m | target | numeric | *Not specified.* | n=492, missing=192, range 3.875–16.5, mean 9.299 ± 2.696 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=492, missing=6, range 37.36–606.8, mean 227.4 ± 141.6 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=492, missing=6, range 40.16–87.92, mean 56.52 ± 9.332 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=492, missing=6, range 95–835, mean 403 ± 115.1 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top 33d4f97e-591c-4e6f-a913-f8f6465fa735 (×492) |
| site | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Sierra Nevada of California (×492) |
| country | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top source-provided coordinates when available (×492) |
| year | metadata | numeric | *Not specified.* | n=492, missing=0, range 2023–2023, mean 2023 ± 0 |
| date | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Leaf (×492) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top leaf (×492) |
| instrument | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Analytical Spectral Devices FieldSpec 3 (×492) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Contact (×492) |
| signal_type | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top reflectance (×492) |
| axis_unit | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top nm (×492) |
| axis_min | metadata | numeric | *Not specified.* | n=492, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=492, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=492, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=492, missing=492, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Freeze Dried Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×492) |
| license | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×492) |
| rights_status | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top explicit_open (×492) |
| usage_scope | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top public_reuse_possible (×492) |
| notes | metadata | categorical | *Not specified.* | n=492, missing=0, classes=1, top EcoSIS package freeze-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×492) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/freeze-dried-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
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
- **Content hash:** `964c9f3e9f079a9628a864b3e3daf2d329b7ff9dbb8a63de41a9c8e92b1e61fd`
- **Processing hash:** `b0ec43d92c6eeef8c3eaf534d822b966ca954e82ce8b8cb8bc1a9b7286b82864` | **metadata hash:** `762a3c8ca62ffa7538e8248ef2d461a7f1801b1d2f6c08800430a585c922b555`
