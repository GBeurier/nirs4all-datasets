# Datasheet — ECOSTRESS meteorites tir axis d3032c60

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS meteorites tir axis d3032c60. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 55 sample(s), 57 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.036).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | meteorites tir | source instruments vary by sample | other | 2.079–25.04 none | 57 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=57, missing=0, classes=57, top ALH 84007 (×1) |
| class_label | target | categorical | *Not specified.* | n=57, missing=0, classes=6, top Ordinary Chondrite (×19) |
| subclass | target | categorical | *Not specified.* | n=57, missing=0, classes=22, top CM2 (×5) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=57, missing=0, classes=57, top meteorites.achondrite.aubrite.fine.tir.alh84007.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top meteorites (×57) |
| material_type | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Meteorites (×57) |
| site | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=57, missing=0, classes=55, top Smithsonian sample without a USNM catalognumber. (×2) |
| country | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top N/A (×57) |
| species | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=57, missing=0, classes=57, top Stony Meteorites. Meteorite found in Antarctica in 1984. Particle size was 0-75 micrometers. Original ASTER Spectral Library name was jhu.becknic.meteorite.achondrite.aubrite.fine.a84007.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top jhu.becknic (×57) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Bidirectional reflectance (×57) |
| signal_type | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Reflectance (percent) (×57) |
| axis_unit | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Wavelength (micrometers) (×57) |
| axis_min | metadata | numeric | *Not specified.* | n=57, missing=0, range 2.079–2.079, mean 2.079 ± 4.48e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=57, missing=0, range 25.04–25.04, mean 25.04 ± 3.584e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=57, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×57) |
| citation | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×57) |
| license | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×57) |
| rights_status | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top manual_review_needed (×57) |
| usage_scope | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top private_use_only (×57) |
| notes | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top none (×57) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 1 fields, Y: 3 fields, measurements: 4 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `ed2b00489957bbd76c3cb207f956beb347a24230b4d12b9f42479773e5c46b7b`
- **Processing hash:** `055aef6243db1b6de813987c78b45fcaf15f662ccebf69ddbcc0a351d3351bcd` | **metadata hash:** `0ea9b93ba6d6d0c35f502308cda4eb373e06a7bf47aca7a78f9fdfb81cabf123`
