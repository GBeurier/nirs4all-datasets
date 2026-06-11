# Datasheet — ECOSTRESS rock all axis 1fb6fa59

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 1fb6fa59. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 46 sample(s), 46 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 46 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=46, missing=0, classes=36, top Basalt (×5) |
| class_label | target | categorical | *Not specified.* | n=46, missing=0, classes=3, top Igneous (×30) |
| subclass | target | categorical | *Not specified.* | n=46, missing=0, classes=11, top Mafic (×11) |
| particle_size | target | categorical | *Not specified.* | n=46, missing=0, classes=2, top Solid (×30) |
| measurement | target | categorical | *Not specified.* | n=46, missing=0, classes=2, top Directional (10 degree) hemispherical reflectance (×30) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=46, missing=0, classes=46, top rock.igneous.felsic.solid.all.granite_h1.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top rock (×46) |
| material_type | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top rock (×46) |
| site | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=46, missing=0, classes=46, top From Quincy, Norfolk, Massachusetts via Ward's Scientific (Cat.No. W-4) (×1) |
| country | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=46, missing=46, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=46, missing=0, classes=46, top A gray, medium- to coarse-grained rock composed of quartz, feldspar, and a mafic mineral. Original ASTER Spectral Library name was jhu.becknic.rock.igneous.felsic.solid.granit1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top jhu.becknic (×46) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=46, missing=0, classes=2, top Directional (10 degree) hemispherical reflectance (×30) |
| signal_type | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top Reflectance (percent) (×46) |
| axis_unit | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top Wavelength (micrometers) (×46) |
| axis_min | metadata | numeric | *Not specified.* | n=46, missing=0, range 0.4–0.4, mean 0.4 ± 2.245e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=46, missing=0, range 14.01–14.01, mean 14.01 ± 3.592e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=46, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×46) |
| citation | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×46) |
| license | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×46) |
| rights_status | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top manual_review_needed (×46) |
| usage_scope | metadata | categorical | *Not specified.* | n=46, missing=0, classes=1, top private_use_only (×46) |
| notes | metadata | categorical | *Not specified.* | n=46, missing=0, classes=32, top none (×15) |

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
- **Content hash:** `9dff635484dd026720164029526f6cac60b889a6efb6c0e5e966c16be1cf8595`
- **Processing hash:** `36006d674c6ef0f0f8c334c39688eaf6cadf981e58c07dfed2e4b05ef2b09fa7` | **metadata hash:** `3138fa4b3284c2bb236edbe223352f27ab787eae59ee612e637e835e5e46d27a`
