# Datasheet — ECOSTRESS mineral tir axis 85fbc8f6

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 85fbc8f6. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 402 sample(s), 402 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2–15.39 none | 402 | 2256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=402, missing=0, classes=134, top Quartz SiO_2 (×14) |
| class_label | target | categorical | *Not specified.* | n=402, missing=0, classes=12, top Silicate (×201) |
| subclass | target | categorical | *Not specified.* | n=402, missing=200, classes=7, top Phyllosilicate (×69) |
| particle_size | target | categorical | *Not specified.* | n=402, missing=0, classes=3, top Fine (×150) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=402, missing=0, classes=402, top mineral.arsenate.none.coarse.tir.a-1a.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top mineral (×402) |
| material_type | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Mineral (×402) |
| site | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=402, missing=55, classes=109, top USA, California, Kern County, Boron (×15) |
| country | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=402, missing=0, classes=402, top Particle size was 125-500um.Collected by JPL Original ASTER Spectral Library name was jpl.nicolet.mineral.arsenate.none.coarse.a01a.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top jpl.nicolet (×402) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Hemispherical reflectance (×402) |
| signal_type | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Reflectance (percent) (×402) |
| axis_unit | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Wavelength (micrometers) (×402) |
| axis_min | metadata | numeric | *Not specified.* | n=402, missing=0, range 2–2, mean 2 ± 4.446e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=402, missing=0, range 15.39–15.39, mean 15.39 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=402, missing=0, range 2256–2256, mean 2256 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×402) |
| citation | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×402) |
| license | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×402) |
| rights_status | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top manual_review_needed (×402) |
| usage_scope | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top private_use_only (×402) |
| notes | metadata | categorical | *Not specified.* | n=402, missing=5, classes=397, top mineral.arsenate.none.coarse.tir.a-1a.jpl.nicolet.ancillary.txt (×1) |
| original_sample_id | metadata | categorical | *Not specified.* | n=402, missing=0, classes=150, top A-1A (×3) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Observation identity is used as the canonical join key because source sample_id has differing per-observation values in ecostress_resource_id, sample_description, notes, material_name, particle_size. The original physical-sample key is preserved as metadata 'original_sample_id'; sample grouping must use that field.

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
- **Content hash:** `3b841ca8339334b96f6014d02f79f53d2cd0815f5f010b73eb2e22e47c273045`
- **Processing hash:** `23f6fa95858b5e31fae6bf38c137d0d7ffee7220a01495295c991fcd10ee41dc` | **metadata hash:** `b32c0b1f485ba41e2d0c4ab4ed02c8f6d5e32083f6d43fc8e4377f886585706a`
