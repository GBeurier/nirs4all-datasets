# Datasheet — UCPH wheat kernel NIT

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH wheat kernel NIT. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** Wheat Kernels

## Composition

- **Alignment:** sample level; 523 sample(s), 523 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | single wheat kernel NIT | *Not specified.* | NIR | 850–1048 nm | 523 | 100 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Y_reference | target | numeric | *Not specified.* | n=523, missing=0, range 6.77–16.95, mean 9.958 ± 1.604 |
| original_split | metadata | categorical | *Not specified.* | n=523, missing=0, classes=2, top calibration (×415) |
| license | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top NOASSERTION (×523) |
| rights_status | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top manual_review_needed (×523) |
| usage_scope | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top internal_benchmark_only_until_license_review (×523) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top False (×523) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top NIT (×523) |
| axis_unit | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top nm (×523) |
| axis_min | metadata | numeric | *Not specified.* | n=523, missing=0, range 850–850, mean 850 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=523, missing=0, range 1048–1048, mean 1048 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=523, missing=0, range 100–100, mean 100 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=523, missing=0, classes=1, top Public UCPH/ERDA dataset, local readme does not state explicit redistribution license or semantic name of Y variable. (×523) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/dLQ6VHNshw/Wheat%20kernels%20.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/datasets/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `96ba674d4e7f875b385ee7857d82f8d3a46a36a43ed64c06abbaf884134b10a8`
- **Processing hash:** `0ef103028c5852a07a6f61098538c9491058a99a286e6c3e44c5cb40d3912015` | **metadata hash:** `f54c3de7077983649e88d44cf093e723202c02f27d9849c52c575b10e9c4d810`
