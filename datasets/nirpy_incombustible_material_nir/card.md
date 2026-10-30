# Datasheet — Nirpy Research incombustible material NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research incombustible material NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 62 sample(s), 62 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research incombustible material NIR | *Not specified.* | NIR | 868–1771 nm | 62 | 512 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TIC Value | target | numeric | *Not specified.* | n=62, missing=0, range 60.24–97.59, mean 78.36 ± 7.984 |
| repository_url | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×62) |
| license | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top MIT License (×62) |
| license_url | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×62) |
| rights_status | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top explicit_open (×62) |
| usage_scope | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top public_reuse_possible (×62) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top True (×62) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top NIR (×62) |
| axis_unit | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top nm (×62) |
| axis_min | metadata | numeric | *Not specified.* | n=62, missing=0, range 868–868, mean 868 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=62, missing=0, range 1771–1771, mean 1771 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=62, missing=0, range 512–512, mean 512 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=62, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×62) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/Incombustible_Material_NIR.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 16 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `e6d9b10e175a4f4e575238729eb2dc3be0491571fa6d18a6fc34e0597293cd08`
- **Processing hash:** `f0bd54e19f17841f0c61c506e2cd9ea7ff2df051410121809687cea79637a0d0` | **metadata hash:** `686dce704e34568859f055348312f84ac06635eca763ead54f5339c087e23190`
