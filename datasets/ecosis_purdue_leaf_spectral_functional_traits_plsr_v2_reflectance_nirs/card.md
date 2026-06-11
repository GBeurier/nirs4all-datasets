# Datasheet — EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2

## Composition

- **Alignment:** observation level; 987 sample(s), 987 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | 2018+2019_stress_six_leaf_traits_spec.csv | Spectravista Corporation HR-1024i | NIR | 350–2500 nm | 987 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Data_Collection_Date | target | categorical | *Not specified.* | n=987, missing=0, classes=15, top 20180727 (×98) |
| Genus | target | categorical | *Not specified.* | n=987, missing=0, classes=2, top Juglans (×839) |
| Species | target | categorical | *Not specified.* | n=987, missing=0, classes=2, top nigra (×839) |
| Plant_ID | target | categorical | *Not specified.* | n=987, missing=0, classes=146, top p3 (×50) |
| E18_SoilTypes | target | categorical | *Not specified.* | n=987, missing=0, classes=4, top noTreatment (×815) |
| Foliar_Trait_Code | target | categorical | *Not specified.* | n=987, missing=0, classes=3, top 1 (×449) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 119086c5-0492-4bb6-b508-aabf2dd49614 (×987) |
| site | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top West Lafayette, IN, USA (×987) |
| country | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=987, missing=0, range 40.42–40.43, mean 40.43 ± 0.004691 |
| longitude | metadata | numeric | *Not specified.* | n=987, missing=0, range -87.04–-86.91, mean -86.98 ± 0.06194 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top source-provided coordinates when available (×987) |
| year | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top USDA NIFA (2016-2023) / CAFS (2021-2024) / HTIRC (2018-2021) (×987) |
| date | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top nigra (×839) |
| genus | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top Juglans (×839) |
| family | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Leaf (×987) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top leaf (×987) |
| instrument | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Spectravista Corporation HR-1024i (×987) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Contact (×987) |
| signal_type | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top reflectance (×987) |
| axis_unit | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top nm (×987) |
| axis_min | metadata | numeric | *Not specified.* | n=987, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=987, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=987, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 10.21232/bCRYo6R2 (×987) |
| citation | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Minjee Park Lorenzo Cotrozzi Geoffrey M Williams Matthew D Ginzel Michael V Mickelbart Douglass F Jacobs John J Couture. USDA NIFA (2016-2023) / CAFS (2021-2024) / HTIRC (2018-2021). Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/bCRYo6R2 (×987) |
| license | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Other (Open) (×987) |
| rights_status | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top explicit_open (×987) |
| usage_scope | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top public_reuse_possible (×987) |
| notes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top EcoSIS package purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling-v2, no interpolation applied by project. (×987) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling-v2`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 — [10.21232/bCRYo6R2](https://doi.org/10.21232/bCRYo6R2)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `c3773ba3cc68c04bc61bf98447ce6fdf57a5c90f0099ec70d75de8937a8fa842`
- **Processing hash:** `b2fb9461a642f9bf2e0b3f65998b2d8468037356c764d062c061ea05a9983979` | **metadata hash:** `fcafc76427369b676a39bfb18cd197872e68fe4bf1ff556782d7cf9a32b61503`
