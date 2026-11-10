# Datasheet — Streptanthus leaves — Vis-NIR reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** github
- **Description:** GitHub spectral-network Streptanthus leaf reflectance VIS-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, github
- **Contributor:** IntBio-UCD spectral-network data

## Composition

- **Alignment:** sample level; 51 sample(s), 51 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/IntBio-UCD/spectral-network/tree/main/data`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/data/mergeMetaSpectraLong.tsv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/IntBio-UCD/spectral-network/main/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 19 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `f55eb4696e25dfa2f8285907a23b6e9193e1068ec79c188fe8b25636a4276617`
- **Processing hash:** `ac150d3ef23487b56fc2f7c65ea32169c3a10b37388c0673947a5cc7a13331a0` | **metadata hash:** `e9f6ebbf0488b1e288428a8f6282778270dbf8906d8827a353b070f24c77ec7a`
