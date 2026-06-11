# Datasheet — EcoSIS Leaf spectra of boreal tree species from Alberta potted tree experiment (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf spectra of boreal tree species from Alberta potted tree experiment (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf spectra of boreal tree species from Alberta potted tree experiment

## Composition

- **Alignment:** observation level; 3235 sample(s), 3235 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | RooftopSCReflectance.csv | PP System Unispec | NIR | 350–1130 nm | 3235 | 781 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Genus | target | categorical | *Not specified.* | n=3235, missing=0, classes=4, top Picea (×1428) |
| Species | target | categorical | *Not specified.* | n=3235, missing=0, classes=6, top banksiana (×735) |
| Individual | target | numeric | *Not specified.* | n=3235, missing=0, range 1–30, mean 14.84 ± 8.485 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top bdfae3cc-844a-47e7-bf17-fb9111ae9467 (×3235) |
| site | metadata | categorical | *Not specified.* | n=3235, missing=3235, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Edmonton, Alberta, Canada (×3235) |
| country | metadata | categorical | *Not specified.* | n=3235, missing=3235, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=3235, missing=0, range 53.53–53.53, mean 53.53 ± 0 |
| longitude | metadata | numeric | *Not specified.* | n=3235, missing=0, range -113.5–-113.5, mean -113.5 ± 0 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top source-provided coordinates when available (×3235) |
| year | metadata | numeric | *Not specified.* | n=3235, missing=0, range 2016–2016, mean 2016 ± 0 |
| date | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=27, top 2016519 (×180) |
| species | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top banksiana (×735) |
| genus | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=4, top Picea (×1428) |
| family | metadata | categorical | *Not specified.* | n=3235, missing=3235, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Leaf (×3235) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top leaf (×3235) |
| instrument | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top PP System Unispec (×3235) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Contact (×3235) |
| signal_type | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top reflectance (×3235) |
| axis_unit | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top nm (×3235) |
| axis_min | metadata | numeric | *Not specified.* | n=3235, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3235, missing=0, range 1130–1130, mean 1130 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3235, missing=0, range 781–781, mean 781 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top 10.21232/HbGMYtyz \| 10.3390/rs9070691 (×3235) |
| citation | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Ran Wang, Kyle R. Springer and John A. Gamon. 2016. Leaf spectra of boreal tree species from Alberta potted tree experiment. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/HbGMYtyz (×3235) |
| license | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×3235) |
| rights_status | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top explicit_open (×3235) |
| usage_scope | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top public_reuse_possible (×3235) |
| notes | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top EcoSIS package leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment, no interpolation applied by project. (×3235) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Leaf spectra of boreal tree species from Alberta potted tree experiment — [10.21232/HbGMYtyz](https://doi.org/10.21232/HbGMYtyz)
- *Not specified.* — [10.3390/rs9070691](https://doi.org/10.3390/rs9070691)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `fc95e5588dd1423627c916c067a9ad4c637dd56008a3f0b462de9eaed5f11b47`
- **Processing hash:** `54d2a55d50de661cc41a72b4ae0b280e5f6da1dd7ec7c01ac8eb7c0309d3f053` | **metadata hash:** `6f5f153e7bc74eec83c6cf1259e9bc98cb2380b8ced83b5d610e50bb5374965e`
