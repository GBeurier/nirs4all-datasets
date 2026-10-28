# Datasheet — Nirpy Research milk NIR classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research milk NIR classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** observation level; 450 sample(s), 450 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research milk NIR classification | *Not specified.* | NIR | 2–602 index | 450 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| labels | target | categorical | *Not specified.* | n=450, missing=0, classes=9, top 1 (×50) |
| repository_url | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×450) |
| license | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top MIT License (×450) |
| license_url | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×450) |
| rights_status | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top explicit_open (×450) |
| usage_scope | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top public_reuse_possible (×450) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top True (×450) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top NIR (×450) |
| axis_unit | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top index (×450) |
| axis_min | metadata | numeric | *Not specified.* | n=450, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=450, missing=0, range 602–602, mean 602 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=450, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×450) |
| original_sample_id | metadata | categorical | *Not specified.* | n=450, missing=0, classes=50, top 1/02/2018 (×9) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/milk.csv`
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
- **Content hash:** `ab0456a6eccef9ca7cd462df7c07a1bd367621886d7e23d2b33745a3f5851d4a`
- **Processing hash:** `d51b01bd92958d955ddc0da11cf7df85b63a61c484eddd500b0e647dbff9b526` | **metadata hash:** `fab747e17e9c0fcba9f73e07cc30e94ff74771d1bfe406c5e9acdec11d560d73`
