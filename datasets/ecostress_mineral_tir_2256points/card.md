# Datasheet — ECOSTRESS mineral tir axis 85fbc8f6

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 85fbc8f6. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 150 sample(s), 402 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–3 (mean 2.68).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2–15.39 none | 402 | 2256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=150, missing=0, classes=133, top Quartz SiO_2 (×5) |
| class_label | target | categorical | *Not specified.* | n=150, missing=0, classes=12, top Silicate (×78) |
| subclass | target | categorical | *Not specified.* | n=150, missing=71, classes=7, top Phyllosilicate (×29) |
| particle_size | target | categorical | *Not specified.* | n=150, missing=0, classes=2, top Coarse (×122) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top mineral.arsenate.none.coarse.tir.a-1a.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top mineral (×150) |
| material_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Mineral (×150) |
| site | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=150, missing=24, classes=109, top USA, California, Kern County, Boron (×5) |
| country | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=150, missing=150, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top Particle size was 125-500um.Collected by JPL Original ASTER Spectral Library name was jpl.nicolet.mineral.arsenate.none.coarse.a01a.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top jpl.nicolet (×150) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Hemispherical reflectance (×150) |
| signal_type | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Reflectance (percent) (×150) |
| axis_unit | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Wavelength (micrometers) (×150) |
| axis_min | metadata | numeric | *Not specified.* | n=150, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=150, missing=0, range 15.39–15.39, mean 15.39 ± 3.565e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=150, missing=0, range 2256–2256, mean 2256 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×150) |
| citation | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×150) |
| license | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×150) |
| rights_status | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top manual_review_needed (×150) |
| usage_scope | metadata | categorical | *Not specified.* | n=150, missing=0, classes=1, top private_use_only (×150) |
| notes | metadata | categorical | *Not specified.* | n=150, missing=0, classes=150, top mineral.arsenate.none.coarse.tir.a-1a.jpl.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `bd9c52b2bf68f6123a7e746fcbeabf292ab70e5f09fe3980566327c5b3ef5797`
- **Processing hash:** `a664ab99584084fd6fa73ef8a86988209f64904304b5f358dfa7d8389fb031c6` | **metadata hash:** `187b6465716541672dbc0e68018d4fe6e9bfd54fc231274f77d94923f60e5d4a`
