# Datasheet — ECOSTRESS manmade all axis 4a5262f7

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade all axis 4a5262f7. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 3 sample(s), 3 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade all | source instruments vary by sample | other | 0.3–15 none | 3 | 561 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=3, missing=0, classes=3, top Construction Concrete (×1) |
| class_label | target | categorical | *Not specified.* | n=3, missing=0, classes=2, top Roofing Material (×2) |
| subclass | target | categorical | *Not specified.* | n=3, missing=0, classes=3, top Construction Concrete (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top manmade.concrete.constructionconcrete.solid.all.0598uuucnc.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top manmade (×3) |
| material_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top manmade (×3) |
| site | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Spectra obtained from the Noncoventional Exploitation FactorsData System of the National Photographic Interpretation Center. (×3) |
| country | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Approximately 30-year-old runway construction concrete with (mostly granite) aggregate showing. Sample was light gray and weathered. Original ASTER Spectral Library name was jhu.becknic.manmade.concrete.construction.solid.0598uuu.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top jhu.becknic (×3) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×3) |
| signal_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Reflectance (percent) (×3) |
| axis_unit | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Wavelength (micrometers) (×3) |
| axis_min | metadata | numeric | *Not specified.* | n=3, missing=0, range 0.3–0.3, mean 0.3 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3, missing=0, range 15–15, mean 15 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3, missing=0, range 561–561, mean 561 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×3) |
| citation | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×3) |
| license | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×3) |
| rights_status | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top manual_review_needed (×3) |
| usage_scope | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top private_use_only (×3) |
| notes | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top none (×3) |

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
- **Content hash:** `6854ff43aa75b61c456cc5b057bb5624f51abc742342c14ccea896fb64d70e24`
- **Processing hash:** `f21a4b8612c9f4b9ea943a0363573dd21c83e31f61d8be5a2cd2adb9c96fcc19` | **metadata hash:** `cc4512104fc15fda4207ec22a30cfc4feb595b5ba83230c14adbadaa98077c3a`
