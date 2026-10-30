# Datasheet — UCPH soil SOM ergosterol NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH soil SOM ergosterol NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** NIR soil

## Composition

- **Alignment:** sample level; 108 sample(s), 108 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil NIR reflectance | *Not specified.* | NIR | 400–2498 nm | 108 | 1050 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| SOM | target | numeric | *Not specified.* | n=108, missing=0, range 42.91–95.85, mean 85.43 ± 10.82 |
| Ergogdw | target | numeric | *Not specified.* | n=108, missing=0, range 53.72–434.1, mean 207.4 ± 85.49 |
| sample_no | metadata | numeric | *Not specified.* | n=108, missing=0, range 1–108, mean 54.5 ± 31.32 |
| license | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top NOASSERTION (×108) |
| rights_status | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top manual_review_needed (×108) |
| usage_scope | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top internal_benchmark_only_until_license_review (×108) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top False (×108) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top NIR (×108) |
| axis_unit | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top nm (×108) |
| axis_min | metadata | numeric | *Not specified.* | n=108, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=108, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=108, missing=0, range 1050–1050, mean 1050 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=108, missing=0, classes=1, top SOM measured as loss on ignition at 550 C, ergosterol determined through HPLC per UCPH page. (×108) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/cFmELMw2C6/NIR%20Soil.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/soilnir/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Source sample from the MAT file; grouped by the source column retained in M. Exported multiplicity does not prove the number of scans averaged upstream.
- **Curated views:** M: 0 fields, Y: 2 fields, measurements: 0 fields, passport: 15 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `69a9c0ea87e7428189b09c067e21dd01342572539024e045b63849363d784a69`
- **Processing hash:** `4a3faacd6bf50ab9453485b819a1feab177fa2d00f08925b2bf9db67e89d58b3` | **metadata hash:** `5a858f58a57cacc26f066ec388c13fd42dfe5f525704a8241bbbffae6aea6d46`
