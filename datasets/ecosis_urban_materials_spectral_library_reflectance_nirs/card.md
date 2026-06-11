# Datasheet — EcoSIS Urban Materials Spectral Library reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Urban Materials Spectral Library reflectance. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Urban Materials Spectral Library

## Composition

- **Alignment:** observation level; 60 sample(s), 60 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Filtered Asphalt Brick Spectra.xlsx | Ocean Optics JAZ-EL350 | NIR | 0.45–0.95 none | 60 | 256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material | target | categorical | *Not specified.* | n=60, missing=0, classes=2, top Asphalt (×32) |
| date | metadata | categorical | *Not specified.* | n=60, missing=0, classes=4, top 2017-11-08 00:00:00 (×20) |
| location | metadata | categorical | *Not specified.* | n=60, missing=0, classes=11, top 207 East 6th St., Dayton, OH (×8) |
| latitude | metadata | numeric | *Not specified.* | n=60, missing=0, range 39.68–40.01, mean 39.8 ± 0.1039 |
| longitude | metadata | numeric | *Not specified.* | n=60, missing=0, range -84.19–-83.01, mean -83.95 ± 0.389 |
| comment | metadata | categorical | *Not specified.* | n=60, missing=11, classes=38, top worn (×3) |
| instrument | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Ocean Optics JAZ-EL350 (×60) |
| signal_type | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top reflectance (×60) |
| axis_unit | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top um (×60) |
| axis_min | metadata | numeric | *Not specified.* | n=60, missing=0, range 0.45–0.45, mean 0.45 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=60, missing=0, range 0.95–0.95, mean 0.95 ± 3.359e-16 |
| n_points_original | metadata | numeric | *Not specified.* | n=60, missing=0, range 256–256, mean 256 ± 0 |
| rights_status | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top manual_review_needed (×60) |
| usage_scope | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top private_use_only (×60) |
| notes | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Source metadata reports Processing Interpolated=no and Processing Resampled=no. No project interpolation or resampling applied. (×60) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/urban-materials-spectral-library`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `http://data.ecosis.org/dataset/6dc358cd-ce2d-4e97-920a-82a3b04c8bc2/resource/5021e0fc-5041-4863-a234-a769f075c1f1/download/filtered-asphalt-brick-spectra.xlsx`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `http://data.ecosis.org/dataset/6dc358cd-ce2d-4e97-920a-82a3b04c8bc2/resource/3298c8e2-6dec-4f1f-93e8-9713e8cffe21/download/filtered-asphalt-brick-metadata.xlsx`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS package license not specified in local CKAN metadata.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `7a7907afa3d915c8c93e7b6cb4e71657425fdb7cb70a9f99241247330a682671`
- **Processing hash:** `c739ca03c965bf32a197442b29994cdd3b772b17b314de0cfac535e3b181d7eb` | **metadata hash:** `7381085925372cec6e546dee1c8ef186992cfcc7fe5af1e09dd64d3c87d8fa6f`
