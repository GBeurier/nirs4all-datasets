# Datasheet — Nirpy Research coffee classification NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research coffee classification NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 70 sample(s), 70 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research coffee classification NIR | *Not specified.* | NIR | 1–601 index | 70 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Coffee Type | target | categorical | *Not specified.* | n=70, missing=0, classes=7, top Tauro (×10) |
| repository_url | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×70) |
| license | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top MIT License (×70) |
| license_url | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×70) |
| rights_status | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top explicit_open (×70) |
| usage_scope | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top public_reuse_possible (×70) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top True (×70) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top NIR (×70) |
| axis_unit | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top index (×70) |
| axis_min | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=70, missing=0, range 601–601, mean 601 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=70, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×70) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/coffee_classification.csv`
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
- **Content hash:** `f834f90c9c662814e196afe1276fdf71ebba9f59e01bd3f9ac7df63f72c2574a`
- **Processing hash:** `77f3b4a5f048333835190346010d396db905fde43d9b66132965195399a8a51d` | **metadata hash:** `f3f78cdbd7c45cd8b1de57024d9b4d83a1de3f33da0c82bd13128a9a973fbc75`
