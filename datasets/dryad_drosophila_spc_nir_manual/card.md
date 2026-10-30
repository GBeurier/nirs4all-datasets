# Datasheet — Drosophila SPC NIR spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Drosophila SPC NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD drosophila

## Composition

- **Alignment:** sample level; 266 sample(s), 266 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 266 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_group_code | target | categorical | *Not specified.* | n=266, missing=0, classes=5, top Tri (×112) |
| format_reader | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top nirs4all_formats::readers::galactic_spc (×266) |
| format_name | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top galactic-spc (×266) |
| signal_type | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top absorbance (×266) |
| manual_download | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top True (×266) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\drosophila (×266) |
| manual_download_file | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top NIRS.zip::*.spc (×266) |
| official_source_url | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.324ch00 (×266) |
| standardization_batch | metadata | categorical | *Not specified.* | n=266, missing=0, classes=1, top v0.8.59 (×266) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.324ch00`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Original sample identifier retained under a prefixed/equivalent name
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 11 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual ZIP download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `b3e5775e758704c5f863586befd4f514e34b682f26fefcd1bfa2bf8fe6829261`
- **Processing hash:** `e099144c0da1e24e9893326d0effa6a5769fa33971c3dd29ad609ac74d371286` | **metadata hash:** `0f5cbe5c6c26cbb420c28aa9d74b68d3438d87cc8e04abdf72a7cdfda7f1e0db`
