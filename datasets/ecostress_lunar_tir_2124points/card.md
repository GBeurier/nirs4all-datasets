# Datasheet — ECOSTRESS lunar tir axis 69ac2056

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS lunar tir axis 69ac2056. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 17 sample(s), 17 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | lunar tir | source instruments vary by sample | other | 2.079–14.01 none | 17 | 2124 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top 60051.19 (×1) |
| subclass | target | categorical | *Not specified.* | n=17, missing=0, classes=3, top Highland (×8) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top soil.lunar.highland.fine.tir.60051_19.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top lunar (×17) |
| material_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Soil (×17) |
| site | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=17, missing=0, classes=4, top Apollo 16 landing site via the NASA Lunar Sample Repository at JohnsonSpace Center, Houston, TX. (×8) |
| country | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top This sample is one of a suite of relatively more aluminous and lower iron and titanium soils at the Apollo 16 site, and has the second oldest exposure age of the four soils of that suite (Is/FeO=57). Original ASTER Spectral Library name was jhu.becknic.soil.lunar.highlands.fine.60051.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top jhu.becknic (×17) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×17) |
| signal_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Reflectance (percent) (×17) |
| axis_unit | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Wavelength (micrometers) (×17) |
| axis_min | metadata | numeric | *Not specified.* | n=17, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=17, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=17, missing=0, range 2124–2124, mean 2124 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×17) |
| citation | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×17) |
| license | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×17) |
| rights_status | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top manual_review_needed (×17) |
| usage_scope | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top private_use_only (×17) |
| notes | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top none (×17) |

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
- **Content hash:** `c1063eabbf6df1f3be3ec82175aede97aba663df3f6677052e98ea91690a48f9`
- **Processing hash:** `ad5cf165c1e1c2e783acc33008b2a61312f0e94f6325565455ef7a5b90650e67` | **metadata hash:** `264959881f3d69f71bf1cead240e37736f9d8a7a9a2d536408f94c3443af6ffa`
