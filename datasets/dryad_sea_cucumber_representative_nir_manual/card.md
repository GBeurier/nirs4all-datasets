# Datasheet — Sea cucumber representative NIR spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Sea cucumber representative NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD sea cucumber

## Composition

- **Alignment:** sample level; 61 sample(s), 61 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 800.4–2500 nm | 61 | 3439 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| class | target | categorical | *Not specified.* | n=61, missing=0, classes=3, top YT (×27) |
| class_label | metadata | categorical | *Not specified.* | n=61, missing=0, classes=3, top YT (×27) |
| manual_download | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top True (×61) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\see cucumber (×61) |
| manual_download_file | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top representative+original+spectra.rar (×61) |
| official_source_url | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.n1066 (×61) |
| standardization_batch | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top v0.8.58 (×61) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.n1066`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: Original sample identifier retained under a prefixed/equivalent name
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 1 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual RAR download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `2825ca8e062daf3eb981ddbe6b363d19b0550d2699c5ec96b48df21987e35dc5`
- **Processing hash:** `3609285a66694b0d97c1ba89ff7a7bf465b14c904dddd1cd1b25395b2153bcb4` | **metadata hash:** `6b5c446cd172bdedc8528b5dc2b621dd6ef854eea4759457ffe0513f1d55fe4b`
