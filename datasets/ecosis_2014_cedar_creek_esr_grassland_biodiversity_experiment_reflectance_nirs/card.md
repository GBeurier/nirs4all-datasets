# Datasheet — EcoSIS 2014 Cedar Creek ESR Grassland Biodiversity Experiment: Leaf-level Contact Data: Trait Predictions (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 2014 Cedar Creek ESR Grassland Biodiversity Experiment: Leaf-level Contact Data: Trait Predictions (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 11 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 2014 Cedar Creek ESR Grassland Biodiversity Experiment: Leaf-level Contact Data: Trait Predictions

## Composition

- **Alignment:** observation level; 831 sample(s), 831 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CedarCreekLeafSpectra2014.csv | ASD Inc. ASD FieldSpec 3 | NIR | 400–2500 nm | 831 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| C | target | numeric | *Not specified.* | n=831, missing=0, range 44.89–52.36, mean 47.62 ± 1.03 |
| C_N | target | numeric | *Not specified.* | n=831, missing=0, range 11.5–138.3, mean 29.27 ± 10.05 |
| Cell | target | numeric | *Not specified.* | n=831, missing=0, range 3.856–33.03, mean 19.06 ± 3.862 |
| Chl_g_m2 | target | numeric | *Not specified.* | n=831, missing=0, range 0.001204–0.4337, mean 0.2243 ± 0.06044 |
| Fiber | target | numeric | *Not specified.* | n=831, missing=0, range 9.486–83.42, mean 32.81 ± 9.053 |
| LMA_g_m2 | target | numeric | *Not specified.* | n=831, missing=24, range 10.05–184.4, mean 63.06 ± 28.3 |
| Lignin | target | numeric | *Not specified.* | n=831, missing=12, range 2.023–48.56, mean 16.09 ± 7.049 |
| N | target | numeric | *Not specified.* | n=831, missing=0, range 0.3391–4.056, mean 1.772 ± 0.4904 |
| NDWI | target | numeric | *Not specified.* | n=831, missing=0, range -0.04767–0.0843, mean 0.04134 ± 0.01469 |
| N_spp | target | numeric | *Not specified.* | n=831, missing=0, range 1–16, mean 4.378 ± 3.604 |
| PRI | target | numeric | *Not specified.* | n=831, missing=0, range -0.1246–0.1056, mean -0.01346 ± 0.02287 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top 550b8e60-1354-4b54-8f6c-1a4db9b1cae3 (×831) |
| site | metadata | numeric | *Not specified.* | n=831, missing=0, range 2–265, mean 56.56 ± 59.95 |
| location | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top source-provided coordinates when available (×831) |
| year | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top Leaf (×831) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top leaf (×831) |
| instrument | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top ASD Inc. ASD FieldSpec 3 (×831) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top Contact (×831) |
| signal_type | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top reflectance (×831) |
| axis_unit | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top nm (×831) |
| axis_min | metadata | numeric | *Not specified.* | n=831, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=831, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=831, missing=0, range 2101–2101, mean 2101 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top 10.21232/dep7jvyq (×831) |
| citation | metadata | categorical | *Not specified.* | n=831, missing=831, classes=0, — |
| license | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top not specified (×831) |
| rights_status | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top manual_review_needed (×831) |
| usage_scope | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top private_use_only (×831) |
| notes | metadata | categorical | *Not specified.* | n=831, missing=0, classes=1, top EcoSIS package 2014-cedar-creek-esr-grassland-biodiversity-experiment--leaf-level-contact-data--trait-predictions, no interpolation applied by project. (×831) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2014-cedar-creek-esr-grassland-biodiversity-experiment--leaf-level-contact-data--trait-predictions`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `2ca32b1a9ef75642923f8af4fd0034abab1cc44f46ff0e72bae91f0e21d8307e`
- **Processing hash:** `21ede1aeebd43ac8988ee74544e5d365729101c0203dbd4e543abb5d00257ffc` | **metadata hash:** `6a33fabd56be65b79f1f214448752d6b0977f1d04b36f4319e5803daa0c113e5`
