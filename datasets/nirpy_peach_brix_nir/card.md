# Datasheet — Nirpy Research peach Brix NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research peach Brix NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 50 sample(s), 50 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research peach Brix NIR | *Not specified.* | NIR | 1–600 index | 50 | 600 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Brix | target | numeric | *Not specified.* | n=50, missing=0, range 11.2–20, mean 16.44 ± 2.181 |
| repository_url | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×50) |
| license | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top MIT License (×50) |
| license_url | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×50) |
| rights_status | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top explicit_open (×50) |
| usage_scope | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top public_reuse_possible (×50) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top True (×50) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top NIR (×50) |
| axis_unit | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top index (×50) |
| axis_min | metadata | numeric | *Not specified.* | n=50, missing=0, range 1–1, mean 1 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=50, missing=0, range 600–600, mean 600 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=50, missing=0, range 600–600, mean 600 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=50, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×50) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/peach_spectra_brix.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 16 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `7e6e52b7301bb79ea1ec399c83e8b18e9a2ebf73e9b6d00d62b817d252d12545`
- **Processing hash:** `5ffdf835683d99734d21ed321773f72c1e598eb1491adab50175c6b39205bd82` | **metadata hash:** `f67ee6e689acc9148f56ff0c28982fba49abf8d5ae678bd6de278f8b19eaaced`
