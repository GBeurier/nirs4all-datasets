# Datasheet — ECOSTRESS soil all axis 1fb6fa59

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis 1fb6fa59. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 13 sample(s), 13 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.01 none | 13 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=13, missing=0, classes=13, top Brown to dark brown gravelly loam (×1) |
| class_label | target | categorical | *Not specified.* | n=13, missing=0, classes=6, top Alfisol (×5) |
| subclass | target | categorical | *Not specified.* | n=13, missing=0, classes=11, top Haplustalf (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top soil.alfisol.haploxeralf.none.all.87p313.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top soil (×13) |
| material_type | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top soil (×13) |
| site | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=13, missing=0, classes=10, top Klickitat Co., Wa. via USDA Soil Conservation service. (×3) |
| country | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top Brown to dark brown gravelly loam (medial-skeletal, frigid ultic). Original ASTER Spectral Library name was jhu.becknic.soil.alfisol.haploxeralf.coarse.87P313.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top jhu.becknic (×13) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×13) |
| signal_type | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Reflectance (percent) (×13) |
| axis_unit | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Wavelength (micrometers) (×13) |
| axis_min | metadata | numeric | *Not specified.* | n=13, missing=0, range 0.4–0.4, mean 0.4 ± 5.778e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=13, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=13, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×13) |
| citation | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×13) |
| license | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×13) |
| rights_status | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top manual_review_needed (×13) |
| usage_scope | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top private_use_only (×13) |
| notes | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top soil.alfisol.haploxeralf.none.all.87p313.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `6349ebea437ca60b1d30804ddefbce2707810433c5a52ed85cfff3e19957fecd`
- **Processing hash:** `841cf395b555a3e8f981cb089e64aa06b3a7dd62aeb846744d0c9cb6eeb1e655` | **metadata hash:** `ea525a1dbf557e490b612b75a666eaeba2bf1f961d79f69a3f9193ca6b5539ff`
