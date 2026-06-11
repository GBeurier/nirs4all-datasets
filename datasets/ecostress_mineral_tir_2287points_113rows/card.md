# Datasheet — ECOSTRESS mineral tir axis 02866850

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 02866850. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 113 sample(s), 113 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 113 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=113, missing=0, classes=93, top Olivine (Fo92) (Fe+2,Mg)2SiO4 (×4) |
| class_label | target | categorical | *Not specified.* | n=113, missing=0, classes=7, top Silicate (×90) |
| subclass | target | categorical | *Not specified.* | n=113, missing=23, classes=7, top Nesosilicate (×23) |
| measurement | target | categorical | *Not specified.* | n=113, missing=0, classes=3, top Transmission (×111) |
| owner | target | categorical | *Not specified.* | n=113, missing=0, classes=2, top JHU (×112) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=113, missing=0, classes=113, top mineral.carbonate.none.fine.tir.aragonite_1.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top mineral (×113) |
| material_type | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top Mineral (×113) |
| site | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=113, missing=0, classes=113, top Sample from Horenec, Bilina, Cechy, Czechoslovakia, viaSmithsonian (sample no. NMNH B10083). (×1) |
| country | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=113, missing=113, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=113, missing=0, classes=113, top The sample was composed of two transparent, colorless pieces: one prismatic, 1.8 cm x 1.8 cm x 2 cm, and weighing about 2 g, the other a 5 mm x 5 mm x 5 mm cleavage fragment weighing 0.65 g. No impurities were detected in hand sample or microscopically. Particle size was less than 2 Micrometers. Original ASTER Spectral Library name was jhu.nicolet.mineral.carbonate.none.powder.aragon1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top jhu.nicolet (×113) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=113, missing=0, classes=3, top Transmission (×111) |
| signal_type | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top Transmittance (percent) (×113) |
| axis_unit | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top Wavelength (micrometers) (×113) |
| axis_min | metadata | numeric | *Not specified.* | n=113, missing=0, range 2.079–2.079, mean 2.079 ± 4.461e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=113, missing=0, range 25.04–25.04, mean 25.04 ± 7.137e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=113, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×113) |
| citation | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×113) |
| license | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×113) |
| rights_status | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top manual_review_needed (×113) |
| usage_scope | metadata | categorical | *Not specified.* | n=113, missing=0, classes=1, top private_use_only (×113) |
| notes | metadata | categorical | *Not specified.* | n=113, missing=6, classes=92, top none (×16) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- The ECOSTRESS spectral library version 1.0 — [10.1016/j.rse.2019.05.015](https://doi.org/10.1016/j.rse.2019.05.015)
- The ASTER Spectral Library Version 2.0 — [10.1016/j.rse.2008.11.007](https://doi.org/10.1016/j.rse.2008.11.007)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Official ECOSTRESS page requests citation and states copyright/all rights reserved; converted matrices are private/internal until redistribution rights are clarified.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `fffc2d0022f01a5d0cf7a9bc044be8c6c4b3bf506a7e8b14c2fd6f1b9453ba40`
- **Processing hash:** `9b40a5f9c547dff1d352d2e9db21ece8cad63ff77d05cc9a5ce2bd471dd595f5` | **metadata hash:** `788908d815d1eb062c8d15b9ae4b1dd2fcaf4b2dca49d57d4ac3915e38403e20`
