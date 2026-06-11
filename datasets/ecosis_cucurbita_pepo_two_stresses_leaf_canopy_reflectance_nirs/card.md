# Datasheet — EcoSIS Leaf and canopy spectroscopy and biochemical data of field-grown Cucurbita pepo under two stresses (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf and canopy spectroscopy and biochemical data of field-grown Cucurbita pepo under two stresses (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf and canopy spectroscopy and biochemical data of field-grown Cucurbita pepo under two stresses

## Composition

- **Alignment:** observation level; 541 sample(s), 541 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra.csv | Spectral Evolution, Spectra Vista Corporation (leaf clip only) PSR+ | NIR | 350–2500 nm | 541 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Treatment | target | categorical | *Not specified.* | n=541, missing=24, classes=3, top sink (×176) |
| Temperature | target | numeric | *Not specified.* | n=541, missing=24, range 19.5–33.3, mean 25.04 ± 2.552 |
| Chlorophyll | target | numeric | *Not specified.* | n=541, missing=173, range 6.79–74.29, mean 59.77 ± 6.08 |
| PhiPSII | target | numeric | *Not specified.* | n=541, missing=173, range 0.392–0.728, mean 0.5466 ± 0.05872 |
| RWC | target | numeric | *Not specified.* | n=541, missing=291, range 67.05–86.53, mean 79.55 ± 3.548 |
| LMA | target | numeric | *Not specified.* | n=541, missing=291, range 28.82–75.45, mean 48.96 ± 11.39 |
| AminoAcids | target | numeric | *Not specified.* | n=541, missing=292, range 1.401–6.412, mean 3.111 ± 0.9596 |
| Glucose | target | numeric | *Not specified.* | n=541, missing=292, range 1.994–24.23, mean 11.95 ± 4.285 |
| Fructose | target | numeric | *Not specified.* | n=541, missing=292, range 0.7051–11.05, mean 3.523 ± 1.855 |
| Sucrose | target | numeric | *Not specified.* | n=541, missing=292, range 2.189–15.27, mean 5.37 ± 2.217 |
| Starch | target | numeric | *Not specified.* | n=541, missing=292, range 9.787–156.2, mean 67.56 ± 35.65 |
| TNC | target | numeric | *Not specified.* | n=541, missing=292, range 17.85–171.8, mean 88.39 ± 38.11 |
| Protein | target | numeric | *Not specified.* | n=541, missing=292, range 3.782–12.82, mean 7.431 ± 1.558 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top a9282ba1-4b8e-4318-88bf-cda8b9dd42a6 (×541) |
| site | metadata | numeric | *Not specified.* | n=541, missing=24, range 1–18, mean 9.267 ± 5.149 |
| location | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Brookhaven National Laboratory (×541) |
| country | metadata | categorical | *Not specified.* | n=541, missing=541, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=541, missing=541, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=541, missing=541, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top source-provided coordinates when available (×541) |
| year | metadata | numeric | *Not specified.* | n=541, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=541, missing=24, classes=10, top 2019-07-19 (×54) |
| species | metadata | categorical | *Not specified.* | n=541, missing=24, classes=1, top CUPE (×517) |
| genus | metadata | categorical | *Not specified.* | n=541, missing=541, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=541, missing=541, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Leaf (×541) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top canopy (×541) |
| instrument | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Spectral Evolution, Spectra Vista Corporation (leaf clip only) PSR+ (×541) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Other, Proximal (×541) |
| signal_type | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top reflectance (×541) |
| axis_unit | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top nm (×541) |
| axis_min | metadata | numeric | *Not specified.* | n=541, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=541, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=541, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top 10.1111/pce.14056 \| 10.21232/RLmYbmE3 \| 10.21232/rlmybme3 (×541) |
| citation | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Angela C Burnett Shawn P Serbin Alistair Rogers. 2020. Leaf and canopy spectroscopy and biochemical data of field-grown Cucurbita pepo under two stresses. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/RLmYbmE3 (×541) |
| license | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top Creative Commons Attribution (×541) |
| rights_status | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top explicit_open (×541) |
| usage_scope | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top public_reuse_possible (×541) |
| notes | metadata | categorical | *Not specified.* | n=541, missing=0, classes=1, top EcoSIS package leaf-and-canopy-spectroscopy-and-biochemical-data-of-field-grown-cucurbita-pepo-under-two-stresses, no interpolation applied by project. (×541) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-and-canopy-spectroscopy-and-biochemical-data-of-field-grown-cucurbita-pepo-under-two-stresses`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Source:sink imbalance detected with leaf- and canopy-level spectroscopy in a field-grown crop — [10.1111/pce.14056](https://doi.org/10.1111/pce.14056)
- Leaf and canopy spectroscopy and biochemical data of field-grown Cucurbita pepo under two stresses — [10.21232/RLmYbmE3](https://doi.org/10.21232/RLmYbmE3)
- *Not specified.* — [10.21232/rlmybme3](https://doi.org/10.21232/rlmybme3)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `b2a30b835fb7330914feffcaef09046297b97b70e0a3227646488b8ec2fba67e`
- **Processing hash:** `0f3958cf8d3638db936b022c6e295d14734d7865b042f76500de7458a4745371` | **metadata hash:** `d4335dccc8237e278e7490c3910a8a88c1d11c231278620c8041b59e7c6cfd22`
