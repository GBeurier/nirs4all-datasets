# Datasheet — GitHub spectral-network Streptanthus leaf reflectance VIS-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** github
- **Description:** GitHub spectral-network Streptanthus leaf reflectance VIS-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, github
- **Contributor:** IntBio-UCD spectral-network data

## Composition

- **Alignment:** sample level; 51 sample(s), 51 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_reflectance_mean | *Not specified.* | NIR | 400–2515 nm | 51 | 2116 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| PopID | target | categorical | *Not specified.* | n=51, missing=0, classes=4, top TM2 (×32) |
| UID | metadata | numeric | *Not specified.* | n=51, missing=0, range 3–259, mean 116.4 ± 92.22 |
| repository_url | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top https://github.com/IntBio-UCD/spectral-network (×51) |
| data_url | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/data/mergeMetaSpectraLong.tsv (×51) |
| license | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top MIT License (×51) |
| license_url | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/LICENSE (×51) |
| rights_status | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top explicit_open (×51) |
| usage_scope | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top public_reuse_possible (×51) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top True (×51) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top VIS-NIR (×51) |
| axis_unit | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top nm (×51) |
| axis_min | metadata | numeric | *Not specified.* | n=51, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=51, missing=0, range 2515–2515, mean 2515 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=51, missing=0, range 2116–2116, mean 2116 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=51, missing=0, classes=1, top Converted from long-table mean leaf reflectance without interpolation or resampling, PopID retained as classification target. (×51) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/IntBio-UCD/spectral-network/tree/main/data`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/data/mergeMetaSpectraLong.tsv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits reuse, modification, publication and distribution with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `d81e2384cf1b51b02519210cd5312938e227883892f92ec2353078092f19c17a`
- **Processing hash:** `f66cfa94b4244b7cf261c5e1a530a6abce80589f2820b3d1257011a40f62172f` | **metadata hash:** `b38e24540f17b9d21027f158448233657a325dfc412eafa153d82b92af272963`
