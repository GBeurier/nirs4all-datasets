# Datasheet — EcoSIS 3D LMA Leaf Level Spectra (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 3D LMA Leaf Level Spectra (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 3D LMA Leaf Level Spectra

## Composition

- **Alignment:** observation level; 1485 sample(s), 1485 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | chlus_et_al_3D_LMA_psr_spectra.csv | ASD, Spectral Evolution Fieldspec 3, PSR 3500+ | NIR | 400–2500 nm | 1485 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| lma_g_m2 | target | numeric | *Not specified.* | n=1485, missing=0, range 16.11–138.7, mean 55.5 ± 23.06 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top fccb20b5-7d47-4878-9da6-eba7798197a7 (×1485) |
| site | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top source-provided coordinates when available (×1485) |
| year | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1485, missing=1485, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top Leaf (×1485) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top leaf (×1485) |
| instrument | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top ASD, Spectral Evolution Fieldspec 3, PSR 3500+ (×1485) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top Contact (×1485) |
| signal_type | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top reflectance (×1485) |
| axis_unit | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top nm (×1485) |
| axis_min | metadata | numeric | *Not specified.* | n=1485, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1485, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1485, missing=0, range 2101–2101, mean 2101 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top 10.21232/dep7jvyq (×1485) |
| citation | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top Chlus A Kruger E.L. Townsend P.A.. 3D LMA Leaf Level Spectra. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1485) |
| license | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top not specified (×1485) |
| rights_status | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top manual_review_needed (×1485) |
| usage_scope | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top private_use_only (×1485) |
| notes | metadata | categorical | *Not specified.* | n=1485, missing=0, classes=1, top EcoSIS package 3d-lma-leaf-level-spectra, no interpolation applied by project. (×1485) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/3d-lma-leaf-level-spectra`
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
- **Content hash:** `1d6a62d60e4756d1ee7628b37950a98dd92d4183c3c0af1891cc42f2d9696438`
- **Processing hash:** `3d1247d4196488a68431938e982204d55caf88b05a7d3c1f2ed72cb5535e1891` | **metadata hash:** `df6b0acc1f509ad9005896cde03725026322ad265db399c3b8dad27aad1a5af4`
