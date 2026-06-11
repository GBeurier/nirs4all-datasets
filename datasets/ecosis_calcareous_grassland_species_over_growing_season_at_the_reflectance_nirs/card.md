# Datasheet — EcoSIS Calcareous grassland species over growing season at the leaf level (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Calcareous grassland species over growing season at the leaf level (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Calcareous grassland species over growing season at the leaf level

## Composition

- **Alignment:** observation level; 1100 sample(s), 1100 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ecoSIS_data.csv | Spectra Vista Corporation HR-1024i | NIR | 350–2500 nm | 1100 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| doy | target | numeric | *Not specified.* | n=1100, missing=0, range 119–204, mean 160.5 ± 26.12 |
| species | target | categorical | *Not specified.* | n=1100, missing=0, classes=17, top agrimonia_eupatoria (×65) |
| species_short | target | categorical | *Not specified.* | n=1100, missing=0, classes=17, top ag_eu (×65) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top 32c119ff-8121-4613-9633-0530872a5dae (×1100) |
| site | metadata | categorical | *Not specified.* | n=1100, missing=1100, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top Wrotham Water, Kent, United Kingdom (×1100) |
| country | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top UK (×1100) |
| latitude | metadata | categorical | *Not specified.* | n=1100, missing=1100, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1100, missing=1100, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top source-provided coordinates when available (×1100) |
| year | metadata | numeric | *Not specified.* | n=1100, missing=0, range 2021–2021, mean 2021 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=13, top 29/04/2021 (×85) |
| genus | metadata | categorical | *Not specified.* | n=1100, missing=1100, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1100, missing=1100, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top Leaf (×1100) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top leaf (×1100) |
| instrument | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×1100) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top Proximal (×1100) |
| signal_type | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top reflectance (×1100) |
| axis_unit | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top nm (×1100) |
| axis_min | metadata | numeric | *Not specified.* | n=1100, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1100, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1100, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top 10.21232/dep7jvyq (×1100) |
| citation | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top R Thornley. 2021. Calcareous grassland species over growing season at the leaf level. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1100) |
| license | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top Other (Open) (×1100) |
| rights_status | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top explicit_open (×1100) |
| usage_scope | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top public_reuse_possible (×1100) |
| notes | metadata | categorical | *Not specified.* | n=1100, missing=0, classes=1, top EcoSIS package calcareous-grassland-species-over-growing-season-at-the-leaf-level, no interpolation applied by project. (×1100) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/calcareous-grassland-species-over-growing-season-at-the-leaf-level`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `db30ec92b4c7ccf0f56f4cada94eb5f92a6ec25cbb2316a2764331459230eb68`
- **Processing hash:** `c2ecc8f264dd6a7384f2b2d723bb4bd69d55507f75718d4c972b744f0b3e5758` | **metadata hash:** `f07d23c184b95e5541a08ce0f900b0e18f0c8004482a7ed4b5027064a2cdb108`
