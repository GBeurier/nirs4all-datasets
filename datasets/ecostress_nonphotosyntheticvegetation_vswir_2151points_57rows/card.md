# Datasheet — ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 54 sample(s), 57 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.056).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | nonphotosyntheticvegetation vswir | source instruments vary by sample | other | 0.35–2.5 none | 57 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=54, missing=0, classes=28, top Pinus coulteri bark (×3) |
| type | target | categorical | *Not specified.* | n=54, missing=0, classes=2, top non photosynthetic vegetation (×51) |
| class_label | target | categorical | *Not specified.* | n=54, missing=0, classes=6, top bark (×18) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=54, missing=0, classes=54, top nonphotosyntheticvegetation.bark.abies.concolor.vswir.vh311.ucsb.asd.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top nonphotosyntheticvegetation (×54) |
| material_type | metadata | categorical | *Not specified.* | n=54, missing=0, classes=2, top non photosynthetic vegetation (×51) |
| site | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=54, missing=0, classes=7, top 37.04403333, -119.30225, WGS84 (×19) |
| country | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=54, missing=0, classes=4, top 5/10/2014 (×19) |
| species | metadata | categorical | *Not specified.* | n=54, missing=0, classes=6, top bark (×18) |
| genus | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=54, missing=54, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=54, missing=0, classes=11, top Samples were collected as part of the HyspIRI Airborne Campaign proposal titled: HyspIRI discrimination of plant species and functional types along a strong environmental temperature gradient. The same materials were processed in the Nicolet and then measured using the ASD. (×25) |
| instrument | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top ucsb.asd (×54) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top Bidirectional reflectance (×54) |
| signal_type | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top Reflectance (percentage) (×54) |
| axis_unit | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top Wavelength (micrometers) (×54) |
| axis_min | metadata | numeric | *Not specified.* | n=54, missing=0, range 0.35–0.35, mean 0.35 ± 1.681e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=54, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=54, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×54) |
| citation | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×54) |
| license | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×54) |
| rights_status | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top manual_review_needed (×54) |
| usage_scope | metadata | categorical | *Not specified.* | n=54, missing=0, classes=1, top private_use_only (×54) |
| notes | metadata | categorical | *Not specified.* | n=54, missing=37, classes=17, top nonphotosyntheticvegetation.bark.acer.rubrum.vswir.acru-1-81.ucsb.asd.ancillary.txt (×1) |

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
- **Content hash:** `fc3c300017dd8d4b842c01c2b5f244652b818a8e030397c606366a50824c1668`
- **Processing hash:** `c9a49f9a51b37a85999973ad6d7bbe57fcf6b91b1058d1788893f44ca2e396a4` | **metadata hash:** `f19909c128554760fe0be7ef1540d8bb99300128099ec16b6db59840c5c07f79`
