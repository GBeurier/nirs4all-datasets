# Datasheet — EcoSIS Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023 (reflectance). Origin database composed from 3 standardized v2.0 leaves: 1 spectral source(s), 16 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023

## Composition

- **Alignment:** sample level; 35 sample(s), 363 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 9–16 (mean 10.37).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CA2023_freshspectra.csv | Spectral Evolution PSR-3500+ | NIR | 350–2500 nm | 363 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| foreoptic_type | target | categorical | *Not specified.* | n=363, missing=0, classes=2, top LC (×294) |
| sample_number | target | numeric | *Not specified.* | n=363, missing=0, range 5–76, mean 43.53 ± 21.2 |
| family | target | categorical | *Not specified.* | n=363, missing=0, classes=10, top Fagaceae (×89) |
| genus | target | categorical | *Not specified.* | n=363, missing=10, classes=9, top Quercus (×89) |
| species | target | categorical | *Not specified.* | n=363, missing=80, classes=13, top kelloggii (×50) |
| plant_functional_type | target | categorical | *Not specified.* | n=363, missing=0, classes=3, top Shrub (×243) |
| tree_DBH_cm | target | numeric | *Not specified.* | n=363, missing=263, range 21.4–88.8, mean 49.53 ± 23.65 |
| NS_crown_width_m | target | numeric | *Not specified.* | n=363, missing=283, range 6.75–19.9, mean 13.04 ± 3.892 |
| WE_crown_width_m | target | numeric | *Not specified.* | n=363, missing=263, range 8.5–19.4, mean 12.58 ± 3.092 |
| tree_height_m | target | numeric | *Not specified.* | n=363, missing=263, range 4.5–15.96, mean 9.117 ± 3.164 |
| crown_length_m | target | numeric | *Not specified.* | n=363, missing=263, range 3.875–13.52, mean 8.243 ± 2.555 |
| LMA_value_g/m2 | target | numeric | *Not specified.* | n=363, missing=0, range 37.36–306.3, mean 132.6 ± 71.95 |
| leaf_water_content_percent | target | numeric | *Not specified.* | n=363, missing=0, range 40.16–75.69, mean 55.78 ± 7.858 |
| chlorophyll__mg/m2 | target | numeric | *Not specified.* | n=363, missing=0, range 293–835, mean 459.1 ± 106.3 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top 56f8a7af-5e0d-42dd-8368-2c953940855f (×363) |
| location | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Sierra Nevada of California (×363) |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top source-provided coordinates when available (×363) |
| year | metadata | numeric | *Not specified.* | n=363, missing=0, range 2023–2023, mean 2023 ± 0 |
| plant_part | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Leaf (×363) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top leaf (×363) |
| instrument | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Spectral Evolution PSR-3500+ (×363) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Contact (×363) |
| signal_type | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top reflectance (×363) |
| axis_unit | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top nm (×363) |
| axis_min | metadata | numeric | *Not specified.* | n=363, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=363, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=363, missing=0, range 2151–2151, mean 2151 ± 0 |
| citation | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Cecilia Vanden Heuvel, Natalie Queally, Ting Zheng, Laura Berman, Zach Breuer, Joel Cryer, Callan Lapinskas, Annabelle Majerus, Elliott Marsh and Philip Townsend. 2023. Fresh Leaf Spectra and Measured Traits from the Sierra Nevada (CA) in July 2023. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×363) |
| license | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×363) |
| rights_status | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top explicit_open (×363) |
| usage_scope | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top public_reuse_possible (×363) |
| notes | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top EcoSIS package fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023, no interpolation applied by project. (×363) |
| source_sample_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=35, top CA2023_076 (×16) |
| source_replicate_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=34, top LC_00004 (×28) |
| source_individualspectra_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=363, top CA2023_005_LC_00002 (×1) |
| source_sampling_date | metadata | categorical | *Not specified.* | n=363, missing=0, classes=8, top 7/7/2023 (×100) |
| source_plot_name | metadata | categorical | *Not specified.* | n=363, missing=0, classes=29, top SL_023 (×30) |
| source_latitude_of_plot | metadata | numeric | *Not specified.* | n=363, missing=0, range 37.03–37.94, mean 37.46 ± 0.3405 |
| source_longitude_of_plot | metadata | numeric | *Not specified.* | n=363, missing=0, range -119.8–-119.2, mean -119.5 ± 0.2578 |
| source_trimble_location_within_plot | metadata | categorical | *Not specified.* | n=363, missing=0, classes=3, top Center (×273) |
| source_common_name | metadata | categorical | *Not specified.* | n=363, missing=0, classes=16, top Manzanita (×70) |
| source_part_of_plant | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Leaf (×363) |
| SpectralRep | metadata | numeric | *Not specified.* | n=363, missing=0, range 1–1, mean 1 ± 0 |
| replicate_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=34, top LC_00004 (×28) |
| individualspectra_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=363, top CA2023_005_LC_00002 (×1) |
| sampling_date | metadata | categorical | *Not specified.* | n=363, missing=0, classes=8, top 7/7/2023 (×100) |
| plot_name | metadata | categorical | *Not specified.* | n=363, missing=0, classes=29, top SL_023 (×30) |
| latitude_of_plot | metadata | numeric | *Not specified.* | n=363, missing=0, range 37.03–37.94, mean 37.46 ± 0.3405 |
| longitude_of_plot | metadata | numeric | *Not specified.* | n=363, missing=0, range -119.8–-119.2, mean -119.5 ± 0.2578 |
| trimble_location_within_plot | metadata | categorical | *Not specified.* | n=363, missing=0, classes=3, top Center (×273) |
| common_name | metadata | categorical | *Not specified.* | n=363, missing=0, classes=16, top Manzanita (×70) |
| part_of_plant | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top Leaf (×363) |
| NS_crown_width_m_ | metadata | numeric | *Not specified.* | n=363, missing=283, range 6.75–19.9, mean 13.04 ± 3.892 |
| chlorophyll _mg/m2 | metadata | numeric | *Not specified.* | n=363, missing=0, range 293–835, mean 459.1 ± 106.3 |
| dataset | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top EcoSIS (×363) |
| dimensions | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top 1D (×363) |
| axis_note | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×363) |
| official_data_url | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top https://data.ecosis.org/dataset/fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023 (×363) |
| official_package_url | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top https://ecosis.org/package/fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023 (×363) |
| license_url | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top http://www.opendefinition.org/licenses/odc-odbl (×363) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top True (×363) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=363, missing=0, classes=1, top ecosis_fresh_leaf_spectra_and_measured_traits_from_the_sierra_reflectance_nirs (×363) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-leaf-spectra-and-measured-traits-from-the-sierra-nevada--ca--in-july-2023`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates. Index fields examined: source_replicate_id. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 6 fields, Y: 13 fields, passport: 38 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `a081680748a4b9e02e1006091e61fac51d01cc14eb154900a2a4404258d473e9`
- **Processing hash:** `ba7d5d9672a35ef8daddf9d641eebc821cae890b9f040add2482ee33c73f907d` | **metadata hash:** `77dc20a0e3cabf033142912a7fc685168dab95e57f11699e7330db25676f8595`
