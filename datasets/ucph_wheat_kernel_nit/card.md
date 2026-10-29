# Datasheet — UCPH wheat kernel NIT

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH wheat kernel NIT. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** Wheat Kernels

## Composition

- **Alignment:** sample level; 523 sample(s), 523 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/dLQ6VHNshw/Wheat%20kernels%20.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/datasets/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 16 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `6990e7ed677575f6187c527cca1b4cddcc8542a08b4c5c7ebf082401c190c6bd`
- **Processing hash:** `be565fd45fd50f37fc8f0dc04f4310271a96679918ad4897ba7363d47536d907` | **metadata hash:** `8032e2109ddcd072200d160c9d38afdd1205932252cfe7047b78295613bc339a`
