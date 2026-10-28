# Datasheet — ECOSTRESS soil all axis 7258ef46

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis 7258ef46. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.01 none | 2 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Vary dark grayish brown loam (×1) |
| subclass | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Agriudoll (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top soil.mollisol.agriudoll.none.all.87p757.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top soil (×2) |
| material_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top soil (×2) |
| site | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top Jefferson Co., Tn. via USDA Soil Conservation service. (×1) |
| country | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top Parent material is alluvium from mixed material. Very dark grayish brown loam, (fine-loamy, mixed, thermic typic). Physiography: flood plain in hills. Original ASTER Spectral Library name was jhu.becknic.soil.mollisol.agriudoll.coarse.87P757.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top jhu.becknic (×2) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×2) |
| signal_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Reflectance (percent) (×2) |
| axis_unit | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Wavelength (micrometers) (×2) |
| axis_min | metadata | numeric | *Not specified.* | n=2, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×2) |
| citation | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×2) |
| license | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×2) |
| rights_status | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top manual_review_needed (×2) |
| usage_scope | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top private_use_only (×2) |
| notes | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top soil.mollisol.agriudoll.none.all.87p757.jhu.becknic.ancillary.txt (×1) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.

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
- **Content hash:** `72e58286439a00625b53eee33e2b81c4fd511815ba69db3cc6130e8ffaebf1fd`
- **Processing hash:** `921b6939ddc53dd4a82bd73a224c30b6132311070a2a2099f475b26a2dc1f535` | **metadata hash:** `a18f863dc1aee6d41fe79c70f02e18a07c384faeda180d6d29c0bea5f2f991c5`
