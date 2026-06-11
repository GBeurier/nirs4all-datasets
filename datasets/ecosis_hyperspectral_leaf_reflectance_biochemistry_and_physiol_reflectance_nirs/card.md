# Datasheet — EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops

## Composition

- **Alignment:** observation level; 1 sample(s), 118 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 118–118 (mean 118).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | canopy_spectra.csv | Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i | NIR | 350–2500 nm | 118 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Treatment | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top watered (×1) |
| Plant_Age | target | numeric | *Not specified.* | n=1, missing=0, range 47–47, mean 47 ± 0 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 8c9139b5-5f24-4925-8d7d-bb4453cfb68d (×1) |
| site | metadata | numeric | *Not specified.* | n=1, missing=0, range 2–2, mean 2 ± 0 |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Brookhaven National Laboratory (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 7/24/19 (×1) |
| species | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top CUPE (×1) |
| genus | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Leaf, Canopy (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top canopy (×1) |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Proximal (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.1093/jxb/erab255 \| 10.21232/UTK8zaW4 \| 10.21232/utk8zaw4 (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Angela C Burnett Shawn P Serbin Kenneth J Davidson Kim S Ely Alistair Rogers. 2020. Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/UTK8zaW4 (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Creative Commons Attribution (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top explicit_open (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top public_reuse_possible (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Detection of the metabolic response to drought stress using hyperspectral reflectance — [10.1093/jxb/erab255](https://doi.org/10.1093/jxb/erab255)
- Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops — [10.21232/UTK8zaW4](https://doi.org/10.21232/UTK8zaW4)
- *Not specified.* — [10.21232/utk8zaw4](https://doi.org/10.21232/utk8zaw4)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `26924860cb0d87cb31943e242ba36113ee994f1fe4985503a173bcbd0b4af051`
- **Processing hash:** `caf833c0e1c38878af900b2f072cb9888357af17a2f08a40e064d180dd2e659f` | **metadata hash:** `741f8190a2fcb42d3343a560231c081b1fb2b50f746968e5277096a3dc6403a2`
