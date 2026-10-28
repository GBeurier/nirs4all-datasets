# Datasheet — Nirpy Research milk powder NIR classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research milk powder NIR classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** observation level; 220 sample(s), 220 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research milk powder NIR classification | *Not specified.* | NIR | 2–602 index | 220 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| labels | target | numeric | *Not specified.* | n=220, missing=0, range 1–11, mean 6 ± 3.169 |
| repository_url | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×220) |
| license | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top MIT License (×220) |
| license_url | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×220) |
| rights_status | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top explicit_open (×220) |
| usage_scope | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top public_reuse_possible (×220) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top True (×220) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top NIR (×220) |
| axis_unit | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top index (×220) |
| axis_min | metadata | numeric | *Not specified.* | n=220, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=220, missing=0, range 602–602, mean 602 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=220, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×220) |
| original_sample_id | metadata | categorical | *Not specified.* | n=220, missing=0, classes=20, top 12/01/2018 (×11) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/milk-powder.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Observation identity is used as the canonical join key because source sample_id has differing per-observation values in labels. The original physical-sample key is preserved as metadata 'original_sample_id'; sample grouping must use that field.

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
- **Content hash:** `c2c617cbbdfad60f7687c4c5e5cef4bbaa7470d7ddaef984c43acfb1c5c0f367`
- **Processing hash:** `68b6f5d4c539c3b286f3aae1de71bea8a9a790c702f6587ee8e7bcf029193abc` | **metadata hash:** `9f6d5725ab9cf8ba5573e3ea7c5b8e3dbadccd11b1642092ad9e0fd77ba7a35c`
