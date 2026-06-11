# Datasheet — ECOSTRESS rock all axis 4cb30554

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 4cb30554. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 29 sample(s), 29 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 29 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=29, missing=0, classes=20, top Basalt (×6) |
| subclass | target | categorical | *Not specified.* | n=29, missing=0, classes=4, top Mafic (×12) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=29, missing=0, classes=29, top rock.igneous.felsic.fine.all.granite_h1.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top rock (×29) |
| material_type | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top rock (×29) |
| site | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=29, missing=0, classes=29, top From Quincy, Norfolk, Massachusetts via Ward's Scientific (Cat.No. W-4) (×1) |
| country | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=29, missing=29, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=29, missing=0, classes=29, top Sample from which powder was derived is a gray, medium- to coarse-grained rock composed of quartz, feldspar, and a mafic mineral.Particle size was 0-75 micrometers. Original ASTER Spectral Library name was jhu.becknic.rock.igneous.felsic.fine.granit1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top jhu.becknic (×29) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×29) |
| signal_type | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top Reflectance (percent) (×29) |
| axis_unit | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top Wavelength (micrometers) (×29) |
| axis_min | metadata | numeric | *Not specified.* | n=29, missing=0, range 0.4–0.4, mean 0.4 ± 1.13e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=29, missing=0, range 14.01–14.01, mean 14.01 ± 5.423e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=29, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×29) |
| citation | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×29) |
| license | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×29) |
| rights_status | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top manual_review_needed (×29) |
| usage_scope | metadata | categorical | *Not specified.* | n=29, missing=0, classes=1, top private_use_only (×29) |
| notes | metadata | categorical | *Not specified.* | n=29, missing=0, classes=29, top rock.igneous.felsic.fine.all.granite_h1.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `bb8e1d62f4e8c635e2677408722a47c7c70a14863c15946284143e6219fcffab`
- **Processing hash:** `77751eacb3f649275d69f6258bec3fa51807b534ce461a1168edaf9d3e0cf850` | **metadata hash:** `006dee8affe5f8463c447d2f4d555982029b3b747e9ed95f00a8e8c25fd72aa3`
