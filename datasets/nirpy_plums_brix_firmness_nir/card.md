# Datasheet — Nirpy Research plums Brix and firmness NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research plums Brix and firmness NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 40 sample(s), 40 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research plums Brix and firmness NIR | *Not specified.* | NIR | 0–599 index | 40 | 600 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Brix | target | numeric | *Not specified.* | n=40, missing=0, range 19.65–23.5, mean 21.86 ± 0.9559 |
| Firmness | target | numeric | *Not specified.* | n=40, missing=0, range 2.85–4.85, mean 3.924 ± 0.4442 |
| repository_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×40) |
| license | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top MIT License (×40) |
| license_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×40) |
| rights_status | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top explicit_open (×40) |
| usage_scope | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top public_reuse_possible (×40) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top True (×40) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top NIR (×40) |
| axis_unit | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top index (×40) |
| axis_min | metadata | numeric | *Not specified.* | n=40, missing=0, range 0–0, mean 0 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=40, missing=0, range 599–599, mean 599 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=40, missing=0, range 600–600, mean 600 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×40) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/NIRplums_brix_firmness.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
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
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0da665b8365616fdfcdaa72a60dbbe671ebfc45ccadb74c865c2f89cbf276910`
- **Processing hash:** `a96f0c8f96d8bd09af8fe36334d47c566b00627b02f920637e6169fd8f2b9200` | **metadata hash:** `8a0a4c4b855f7ef0e505455ebeb99ea99e988c460c3a7102788efb55f2df12e2`
