# Datasheet — UCPH bread staling enzyme NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH bread staling enzyme NIR. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** NIR on Bread stailing

## Composition

- **Alignment:** sample level; 324 sample(s), 324 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | bread NIR spectra | *Not specified.* | NIR | 1009–1694 nm | 324 | 142 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| enzyme_treatment | target | categorical | *Not specified.* | n=324, missing=0, classes=3, top Control (×108) |
| storage_day | target | categorical | *Not specified.* | n=324, missing=0, classes=6, top 01 (×54) |
| bread_position | target | categorical | *Not specified.* | n=324, missing=0, classes=3, top TOP (×108) |
| loaf | metadata | numeric | *Not specified.* | n=324, missing=0, range 1–2, mean 1.5 ± 0.5008 |
| replicate_position | metadata | categorical | *Not specified.* | n=324, missing=0, classes=3, top L (×108) |
| license | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top NOASSERTION (×324) |
| rights_status | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top manual_review_needed (×324) |
| usage_scope | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top internal_benchmark_only_until_license_review (×324) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top False (×324) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top NIR (×324) |
| axis_unit | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top nm (×324) |
| axis_min | metadata | numeric | *Not specified.* | n=324, missing=0, range 1009–1009, mean 1009 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=324, missing=0, range 1694–1694, mean 1694 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=324, missing=0, range 142–142, mean 142 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=324, missing=0, classes=1, top NIR bread staling experiment with enzyme treatment, storage day, loaf, position and replicate classes from MATLAB dataset object. (×324) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/fI7cwNMatT/NIR%20on%20Bread%20stailing.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/nir-data-from-storage-experiment-on-staling-of-bread-produced-using-different-enzymes/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: 324 positions exportées ; L/M/R sont trois positions spatiales. Ne pas confondre pain, position et répétition à position fixe.
- **Curated views:** M: 1 fields, Y: 3 fields, passport: 19 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** No explicit redistribution license found on checked UCPH/ERDA source.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `6d7a06fba70664bc016f7cc06e4bf12e4bcab8efd99b78faa410a2c367748f41`
- **Processing hash:** `8f8462dd18f5f78734da943611ea36948da0b789f1f578563ee0197adab34994` | **metadata hash:** `845efacd60df5f2231e0c9d14187aa7cbf6833b8c415885ca43ae49afe907f00`
