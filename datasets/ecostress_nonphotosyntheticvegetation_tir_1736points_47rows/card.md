# Datasheet — ECOSTRESS nonphotosyntheticvegetation tir axis d3f7b526

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS nonphotosyntheticvegetation tir axis d3f7b526. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 47 sample(s), 47 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | nonphotosyntheticvegetation tir | source instruments vary by sample | other | 2.501–15.34 none | 47 | 1736 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=47, missing=0, classes=22, top Pinus coulteri bark (×3) |
| class_label | target | categorical | *Not specified.* | n=47, missing=0, classes=4, top bark (×18) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=47, missing=0, classes=47, top nonphotosyntheticvegetation.bark.abies.concolor.tir.vh311.ucsb.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top nonphotosyntheticvegetation (×47) |
| material_type | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top non photosynthetic vegetation (×47) |
| site | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=47, missing=0, classes=5, top 37.04403333, -119.30225, WGS84 (×19) |
| country | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=47, missing=0, classes=3, top 5/10/2014 (×19) |
| species | metadata | categorical | *Not specified.* | n=47, missing=0, classes=4, top bark (×18) |
| genus | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=47, missing=47, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=47, missing=0, classes=10, top Samples were collected as part of the HyspIRI Airborne Campaign proposal titled: HyspIRI discrimination of plant species and functional types along a strong environmental temperature gradient. The same materials were processed in the Nicolet and then measured using the ASD. (×25) |
| instrument | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top ucsb.nicolet (×47) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top Hemispherical reflectance (×47) |
| signal_type | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top Reflectance (percentage) (×47) |
| axis_unit | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top Wavelength (micrometers) (×47) |
| axis_min | metadata | numeric | *Not specified.* | n=47, missing=0, range 2.501–2.501, mean 2.501 ± 4.489e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=47, missing=0, range 15.34–15.34, mean 15.34 ± 1.796e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=47, missing=0, range 1736–1736, mean 1736 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×47) |
| citation | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×47) |
| license | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×47) |
| rights_status | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top manual_review_needed (×47) |
| usage_scope | metadata | categorical | *Not specified.* | n=47, missing=0, classes=1, top private_use_only (×47) |
| notes | metadata | categorical | *Not specified.* | n=47, missing=37, classes=10, top nonphotosyntheticvegetation.bark.acer.rubrum.tir.acru-1-81.ucsb.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `30ad7a7d15cd37add7ef6bd732b35fadf0cdf56b7032485a3b232416dfdb4580`
- **Processing hash:** `5cb01e707afe8774905493d1bc2cfea105a0caba59ae2312ef1875f4c1dc57bf` | **metadata hash:** `d2e4f93a6f47003e08b06f3f96caa3b8d1d416798b1012bb864e89a2659d3d89`
