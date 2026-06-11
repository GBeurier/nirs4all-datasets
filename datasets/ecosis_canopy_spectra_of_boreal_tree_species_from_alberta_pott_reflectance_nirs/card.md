# Datasheet — EcoSIS Canopy spectra of boreal tree species from Alberta potted tree experiment (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Canopy spectra of boreal tree species from Alberta potted tree experiment (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Canopy spectra of boreal tree species from Alberta potted tree experiment

## Composition

- **Alignment:** observation level; 2550 sample(s), 2550 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | RooftopDCReflectance.csv | PP System Unispec DC | NIR | 350–1130 nm | 2550 | 781 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Genus | target | categorical | *Not specified.* | n=2550, missing=810, classes=4, top Picea (×580) |
| Species | target | categorical | *Not specified.* | n=2550, missing=810, classes=6, top laricina (×290) |
| Individual | target | numeric | *Not specified.* | n=2550, missing=0, range 1–5, mean 3 ± 1.414 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top 121ea0c1-b3b1-4502-95a1-d13fae6d1323 (×2550) |
| site | metadata | categorical | *Not specified.* | n=2550, missing=2550, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2550, missing=2550, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=2550, missing=2550, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=2550, missing=0, range 53.53–53.53, mean 53.53 ± 0 |
| longitude | metadata | numeric | *Not specified.* | n=2550, missing=0, range -113.5–-113.5, mean -113.5 ± 2.843e-14 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top source-provided coordinates when available (×2550) |
| year | metadata | numeric | *Not specified.* | n=2550, missing=0, range 2016–2016, mean 2016 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=58, top 20150721 (×45) |
| species | metadata | categorical | *Not specified.* | n=2550, missing=810, classes=6, top laricina (×290) |
| genus | metadata | categorical | *Not specified.* | n=2550, missing=810, classes=4, top Picea (×580) |
| family | metadata | categorical | *Not specified.* | n=2550, missing=2550, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top Canopy (×2550) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top canopy (×2550) |
| instrument | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top PP System Unispec DC (×2550) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top Proximal (×2550) |
| signal_type | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top reflectance (×2550) |
| axis_unit | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top nm (×2550) |
| axis_min | metadata | numeric | *Not specified.* | n=2550, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2550, missing=0, range 1130–1130, mean 1130 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2550, missing=0, range 781–781, mean 781 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top 10.21232/aY2V7zCr \| 10.21232/dep7jvyq \| 10.3390/rs9070691 (×2550) |
| citation | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top Ran Wang, Kyle R. Springer and John A. Gamon. 2016. Canopy spectra of boreal tree species from Alberta potted tree experiment. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/aY2V7zCr (×2550) |
| license | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×2550) |
| rights_status | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top explicit_open (×2550) |
| usage_scope | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top public_reuse_possible (×2550) |
| notes | metadata | categorical | *Not specified.* | n=2550, missing=0, classes=1, top EcoSIS package canopy-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment, no interpolation applied by project. (×2550) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/canopy-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Parallel Seasonal Patterns of Photosynthesis, Fluorescence, and Reflectance Indices in Boreal Trees — [10.3390/rs9070691](https://doi.org/10.3390/rs9070691)
- Canopy spectra of boreal tree species from Alberta potted tree experiment — [10.21232/aY2V7zCr](https://doi.org/10.21232/aY2V7zCr)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `688edbd0667fb6180dab23514c02ba4056d3e3f5289b788a717ac4f4b57ff501`
- **Processing hash:** `72a57f9701c463ce927000249300a60d6067a8c0bf070cb0ee3794dd548e6ce8` | **metadata hash:** `e9f4397f54c3957f3c5763cb9da5201af8acbf07b07195f52c3b441e163ad496`
