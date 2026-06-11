# Datasheet — ECOSTRESS rock all axis 5431484a

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 5431484a. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 2 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Aplite (×1) |
| class_label | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Igneous (×1) |
| subclass | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Felsic (×1) |
| particle_size | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Solid (×1) |
| measurement | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Directional (10 degree) hemispherical reflectance (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top rock.igneous.felsic.solid.all.aplite_h1.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top rock (×2) |
| material_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top rock (×2) |
| site | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top From Boulder County, Colorado via Ward's Scientific (Cat. No. W-101) (×1) |
| country | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top A fine-grained to medium-grained leucocratic rock composed of quartz, feldspar, micas and opaques. Original ASTER Spectral Library name was jhu.becknic.rock.igneous.felsic.solid.aplite1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top jhu.becknic (×2) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top Directional (10 degree) hemispherical reflectance (×1) |
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
| notes | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top rock.igneous.felsic.solid.all.aplite_h1.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `b43fdcb038534978673d1d655762613be50d1cfd60c0137fb3b81a35e1f87077`
- **Processing hash:** `e0761821581a75726cfc54a0ad5e81f8250c75d28496f1386035c14f5d46e318` | **metadata hash:** `87dd7e95dbb02da5e641d329cf13028b0cd8cadb72c87fe8bb4af9f10cf6c5ce`
