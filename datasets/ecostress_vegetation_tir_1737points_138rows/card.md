# Datasheet — ECOSTRESS vegetation tir axis 8b6bc3b9

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS vegetation tir axis 8b6bc3b9. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 138 sample(s), 138 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | vegetation tir | source instruments vary by sample | other | 2.501–15.39 none | 138 | 1737 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=138, missing=0, classes=62, top Bambusa beecheyana (×6) |
| class_label | target | categorical | *Not specified.* | n=138, missing=0, classes=2, top Tree (×118) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=138, missing=0, classes=138, top vegetation.shrub.agave.attenuata.tir.jpl060.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top vegetation (×138) |
| material_type | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top vegetation (×138) |
| site | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=138, missing=0, classes=119, top 34.12593, - 118.10983, WGS84 (×6) |
| country | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=138, missing=0, classes=3, top 10/3/2016 (×60) |
| species | metadata | categorical | *Not specified.* | n=138, missing=0, classes=2, top Tree (×118) |
| genus | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Samples were collected at the Huntington Garden in San Marino California as part of a JPL Subcontract studying HyTES imagery. Samples were taken to JPL and processed within 48 hours of collection. The same leaves were processed in the Nicolet and then measured using the ASD. (×138) |
| instrument | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top jpl.nicolet (×138) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Hemispherical reflectance (×138) |
| signal_type | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Reflectance (percentage) (×138) |
| axis_unit | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Wavelength (micrometer) (×138) |
| axis_min | metadata | numeric | *Not specified.* | n=138, missing=0, range 2.501–2.501, mean 2.501 ± 4.457e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=138, missing=0, range 15.39–15.39, mean 15.39 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=138, missing=0, range 1737–1737, mean 1737 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×138) |
| citation | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×138) |
| license | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×138) |
| rights_status | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top manual_review_needed (×138) |
| usage_scope | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top private_use_only (×138) |
| notes | metadata | categorical | *Not specified.* | n=138, missing=50, classes=88, top vegetation.tree.acacia.visco.tir.jpl196.jpl.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `3933d0e152011cb91f248d1e12deab8a6f59e362870a974f9198a4e89bffc7d4`
- **Processing hash:** `110e4856b92a3ddd402d770a45002b30aecdabae248a9e91116ac5d71b1ea544` | **metadata hash:** `fb3b99ea8b0f0827f36c40cd499b688a4eb4806912bff76c76569776661bd350`
