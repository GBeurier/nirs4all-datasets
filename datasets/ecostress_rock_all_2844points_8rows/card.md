# Datasheet — ECOSTRESS rock all axis 2228baf8

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 2228baf8. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 8 sample(s), 8 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 8 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=8, missing=0, classes=8, top Nepheline Syenite (×1) |
| class_label | target | categorical | *Not specified.* | n=8, missing=0, classes=2, top Sedimentary (×5) |
| subclass | target | categorical | *Not specified.* | n=8, missing=0, classes=5, top Mafic (×2) |
| particle_size | target | categorical | *Not specified.* | n=8, missing=0, classes=2, top Coarse (×5) |
| measurement | target | categorical | *Not specified.* | n=8, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×5) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=8, missing=0, classes=8, top rock.igneous.intermediate.solid.all.syenite_h2.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top rock (×8) |
| material_type | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top rock (×8) |
| site | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=8, missing=0, classes=8, top Blue Mountain, Methuen Twp., Ontario, via Ward's Scientific (Cat.No. W-17) (×1) |
| country | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=8, missing=8, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=8, missing=0, classes=8, top A medium-grained leucocratic rock showing some foliation, consisting of plagioclase, nepheline and biotite. Original ASTER Spectral Library name was jhu.becknic.rock.igneous.intermediate.solid.syenit2.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top jhu.becknic (×8) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=8, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×5) |
| signal_type | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top Reflectance (percent) (×8) |
| axis_unit | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top Wavelength (micrometers) (×8) |
| axis_min | metadata | numeric | *Not specified.* | n=8, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=8, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=8, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×8) |
| citation | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×8) |
| license | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×8) |
| rights_status | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top manual_review_needed (×8) |
| usage_scope | metadata | categorical | *Not specified.* | n=8, missing=0, classes=1, top private_use_only (×8) |
| notes | metadata | categorical | *Not specified.* | n=8, missing=0, classes=4, top none (×5) |

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
- **Content hash:** `0b30ebc61e824d11760fda8dbd560a1c130fa021bc07fec5add7f776ca9c9474`
- **Processing hash:** `fcdc6aa6d6ceda660d732a266f08f7aa44a54a9477c9372664f38607bd2968c0` | **metadata hash:** `a1ffdaf86bc3e48ffa58c6f8d613ca9ba4a41d9750640ca6ef58303a9b9e7d14`
