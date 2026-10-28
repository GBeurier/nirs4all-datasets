# Datasheet — ECOSTRESS rock all axis 5a744ba8

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 5a744ba8. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 4 sample(s), 4 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 4 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=4, missing=0, classes=3, top Picrite (×2) |
| subclass | target | categorical | *Not specified.* | n=4, missing=0, classes=2, top Ultramafic (×3) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top rock.igneous.mafic.fine.all.diabase_h1.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top rock (×4) |
| material_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top rock (×4) |
| site | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top from St. Peters, Pennsylvania, via Ward's Scientific (Cat. No. W-127) (×1) |
| country | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top The sample from which the powder was derived was a medium-grained dark gray rock consisting of feldspar and pyroxene.Particle size was 0-75 micrometers. Original ASTER Spectral Library name was jhu.becknic.rock.igneous.mafic.fine.diabas1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top jhu.becknic (×4) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×4) |
| signal_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Reflectance (percent) (×4) |
| axis_unit | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Wavelength (micrometers) (×4) |
| axis_min | metadata | numeric | *Not specified.* | n=4, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=4, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=4, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×4) |
| citation | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×4) |
| license | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×4) |
| rights_status | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top manual_review_needed (×4) |
| usage_scope | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top private_use_only (×4) |
| notes | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top rock.igneous.mafic.fine.all.diabase_h1.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `f1e3c96ea97e47415187bcc576db87f5c8bb59454b2134a1329282615772807d`
- **Processing hash:** `e8d1855f773392a8a816fc9a89c65fa482cca5dc01fe977152f9fcc83a7e002d` | **metadata hash:** `71eb1d6230b9a009261ef5e6b69479ee4423ac41e1a7190bc5831983c4238956`
