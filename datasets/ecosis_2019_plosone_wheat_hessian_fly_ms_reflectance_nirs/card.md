# Datasheet — EcoSIS 2019 PLOSONE wheat hessian fly ms (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 2019 PLOSONE wheat hessian fly ms (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 2019 PLOSONE wheat hessian fly ms

## Composition

- **Alignment:** observation level; 1 sample(s), 74 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 74–74 (mean 74).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | C_N_data.csv | SVC 1024i | NIR | 350–2500 nm | 74 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| N | target | numeric | *Not specified.* | n=1, missing=0, range 3.825–3.825, mean 3.825 ± 0 |
| C | target | numeric | *Not specified.* | n=1, missing=0, range 38.06–38.06, mean 38.06 ± 0 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 03ed9c21-3120-455c-acb4-53711b2eb381 (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top West Lafayette, IN (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Leaf (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top SVC 1024i (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Contact (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.21232/dep7jvyq \| 10.21232/qpx6-2145 (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top CamposMedina C Cotrozzi L Stuart JJ Couture. 2019 PLOSONE wheat hessian fly ms. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). doi:10.21232/qpx6-2145 (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top not specified (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top manual_review_needed (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top private_use_only (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package 2019-plosone-wheat-hessian-fly-ms, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2019-plosone-wheat-hessian-fly-ms`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- 2019 PLOSONE wheat hessian fly ms — [10.21232/qpx6-2145](https://doi.org/10.21232/qpx6-2145)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `c1da2f2b5f3cf0a89b7f40ce891910c354815fc5273ef8c50bacd0e23254f8ae`
- **Processing hash:** `0992826eaa42a23f1a2d6a3ea6f69b944d96df6c437d0ca7d6a95082df8a11a5` | **metadata hash:** `f1719fc656bb08ef0950f2718203db6396420c3758d038268cab07bbc832d866`
