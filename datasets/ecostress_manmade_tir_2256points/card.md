# Datasheet — ECOSTRESS manmade tir axis 85fbc8f6

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade tir axis 85fbc8f6. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 16 sample(s), 16 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade tir | source instruments vary by sample | other | 2–15.39 none | 16 | 2256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=16, missing=0, classes=2, top Brass plate (×15) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=16, missing=0, classes=16, top manmade.reflectancetarget.none.solid.tir.001682.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top manmade (×16) |
| material_type | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Manmade (×16) |
| site | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Labsphere, P.O. Box 70, Shaker Street, North Sutton, NH 03260(603) 927-4266 (×16) |
| country | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=16, missing=0, classes=16, top Measurement made at center. Field Gold.Oct. 29 1997 to Oct. 30 1997. Original ASTER Spectral Library name was jpl.nicolet.manmade.target.none.solid.fg11097j.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top jpl.nicolet (×16) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Hemispherical Reflectance (×16) |
| signal_type | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Reflectence (percent) (×16) |
| axis_unit | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Wavelength (micrometers) (×16) |
| axis_min | metadata | numeric | *Not specified.* | n=16, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=16, missing=0, range 15.39–15.39, mean 15.39 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=16, missing=0, range 2256–2256, mean 2256 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×16) |
| citation | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×16) |
| license | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×16) |
| rights_status | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top manual_review_needed (×16) |
| usage_scope | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top private_use_only (×16) |
| notes | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top none (×16) |

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
- **Content hash:** `f7ee04a0568ed3ba03940162d003b6321d598529d28386f296e0ac9516698943`
- **Processing hash:** `ee5c1faa67913cedd4b6162f85e5702d2b389fa4008660b797880341571eabb8` | **metadata hash:** `11b718918de202dc4c9bbd45617de5bed4eba101862e74e95d784f92675feaf3`
