# Datasheet — ECOSTRESS soil tir axis 2895e351

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil tir axis 2895e351. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 11 sample(s), 11 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil tir | source instruments vary by sample | other | 2–14.01 none | 11 | 2223 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=11, missing=0, classes=8, top Red-orange sandy loam (×3) |
| class_label | target | categorical | *Not specified.* | n=11, missing=0, classes=2, top Entisol (×7) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=11, missing=0, classes=11, top soil.aridisol.none.unsorted.tir.fgg009.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top soil (×11) |
| material_type | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top soil (×11) |
| site | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Fowlers Gap, western New South Wales, AustraliaHewson(1998) PhD thesis (×11) |
| country | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=11, missing=0, classes=11, top Parent material consists of aeolian silts/clays and sandstone debris.Physiography: Alluvium along creek on footslopes of sandstone (Nundooka Sandstone) outcropping hills Original ASTER Spectral Library name was jpl.nicolet.soil.aridisol.none.unsorted.fgg009.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top jpl.nicolet (×11) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Directional hemispherical reflectance (×11) |
| signal_type | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Reflectance (percent) (×11) |
| axis_unit | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Wavelength (micrometers) (×11) |
| axis_min | metadata | numeric | *Not specified.* | n=11, missing=0, range 2–2, mean 2 ± 4.658e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=11, missing=0, range 14.01–14.01, mean 14.01 ± 1.863e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=11, missing=0, range 2223–2223, mean 2223 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×11) |
| citation | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×11) |
| license | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×11) |
| rights_status | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top manual_review_needed (×11) |
| usage_scope | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top private_use_only (×11) |
| notes | metadata | categorical | *Not specified.* | n=11, missing=1, classes=10, top soil.aridisol.none.unsorted.tir.fgg009.jpl.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `d0e8db61b114dd2a3661223c45609e488bc2a007efc1c6b8561c07abd6d06c1b`
- **Processing hash:** `325c7573ff7f4523c6b7d6024bb81e0710194fbafbe611f868ba57d600aa7814` | **metadata hash:** `b4dbcadb3229a41a400c6b0e9d185206ce4d0396e9f1aa0eaa9864ab1a33c3bb`
