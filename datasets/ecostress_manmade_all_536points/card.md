# Datasheet — ECOSTRESS manmade all axis ec3e1c20

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade all axis ec3e1c20. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 22 sample(s), 22 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade all | source instruments vary by sample | other | 0.3–12.5 none | 22 | 536 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=22, missing=0, classes=16, top Copper Metal (×3) |
| class_label | target | categorical | *Not specified.* | n=22, missing=0, classes=3, top Roofing Material (×12) |
| subclass | target | categorical | *Not specified.* | n=22, missing=0, classes=9, top Metal (×7) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=22, missing=0, classes=22, top manmade.generalconstructionmaterial.brick.solid.all.0097uuubrk.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top manmade (×22) |
| material_type | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top manmade (×22) |
| site | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Spectra obtained from the Noncoventional Exploitation FactorsData System of the National Photographic Interpretation Center. (×22) |
| country | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=22, missing=22, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=22, missing=0, classes=22, top Smooth-faced red building construction brick. Original ASTER Spectral Library name was jhu.becknic.manmade.construction.brick.solid.0097uuu.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top jhu.becknic (×22) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×22) |
| signal_type | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Reflectance (percent) (×22) |
| axis_unit | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Wavelength (micrometers) (×22) |
| axis_min | metadata | numeric | *Not specified.* | n=22, missing=0, range 0.3–0.3, mean 0.3 ± 5.682e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=22, missing=0, range 12.5–12.5, mean 12.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=22, missing=0, range 536–536, mean 536 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×22) |
| citation | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×22) |
| license | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×22) |
| rights_status | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top manual_review_needed (×22) |
| usage_scope | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top private_use_only (×22) |
| notes | metadata | categorical | *Not specified.* | n=22, missing=0, classes=1, top none (×22) |

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
- **Content hash:** `c43e9a1ac0d93cb0fd2b44570be892e5cd248e6b69d3bc4814d8902b1fa24a31`
- **Processing hash:** `edf77e4d4dfb8e8e6774323543445b43022a67154ed009e699aa1ad60f593a57` | **metadata hash:** `e1caa6a149385be278c7d7277484fb1449ffd88c4502533422f3453393104c91`
