# Datasheet — EcoSIS 3D LMA Canopy Level Spectra (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 3D LMA Canopy Level Spectra (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 3D LMA Canopy Level Spectra

## Composition

- **Alignment:** observation level; 1 sample(s), 59 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 59–59 (mean 59).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | chlus_et_al_3D_LMA_NEON_refl_brdf.csv | NEON AOP | NIR | 405–2445 nm | 59 | 351 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| easting | target | numeric | *Not specified.* | n=1, missing=0, range 3.07e+05–3.07e+05, mean 3.07e+05 ± 0 |
| northing | target | numeric | *Not specified.* | n=1, missing=0, range 5.117e+06–5.117e+06, mean 5.117e+06 ± 0 |
| lma_g_m2 | target | numeric | *Not specified.* | n=1, missing=0, range 52.12–52.12, mean 52.12 ± 0 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 0290ec63-4a5b-4168-aa43-4e6664db57f7 (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top NEON Domain 5 Great Lakes (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2016–2016, mean 2016 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Canopy (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top canopy (×1) |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top NEON AOP (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Proximal (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 405–405, mean 405 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 2445–2445, mean 2445 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 351–351, mean 351 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.1016/j.rse.2020.112043 \| 10.21232/dep7jvyq (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Chlus et al.. 2020. 3D LMA Canopy Level Spectra. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top not specified (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top manual_review_needed (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top private_use_only (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package 3d-lma-canopy-level-spectra, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/3d-lma-canopy-level-spectra`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Mapping three-dimensional variation in leaf mass per area with imaging spectroscopy and lidar in a temperate broadleaf forest — [10.1016/j.rse.2020.112043](https://doi.org/10.1016/j.rse.2020.112043)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `cd0a8ea48bab6e0b286181f19bbbf5483b65dd792a8cd8dbc1d2b8c2f057d237`
- **Processing hash:** `f458de515b1324b11086c9559c0bccb1713012163bb995c0ad11a6c44b3c02ea` | **metadata hash:** `8033bc2259f1fa570c76052ef8d1ae3bad11b927f88bf65dc4cc508981f02003`
