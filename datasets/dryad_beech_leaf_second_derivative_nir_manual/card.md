# Datasheet — Beech leaves — NIR, second derivative

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Beech leaf second-derivative NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD beech leaf

## Composition

- **Alignment:** sample level; *Not specified.* sample(s), 449 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 1363–2506 nm | 449 | 247 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=449, missing=0, classes=1, top True (×449) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=449, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\beech leaf (×449) |
| manual_download_file | metadata | categorical | *Not specified.* | n=449, missing=0, classes=1, top doi_10_5061_dryad_m37pvmdgv__v20260421.zip::Second_derivative_ANF.csv (×449) |
| official_source_url | metadata | categorical | *Not specified.* | n=449, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.m37pvmdgv (×449) |
| standardization_batch | metadata | categorical | *Not specified.* | n=449, missing=0, classes=1, top v0.8.58 (×449) |
| source_row_index | metadata | categorical | *Not specified.* | n=449, missing=0, classes=449, top 1 (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.m37pvmdgv`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Undetermined
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `756b126fc5946af5cf3200d17d8b0f144692a1ff55b0da98d6b908f41227c91c`
- **Processing hash:** `cbfb3c24d856406dad476ffb4e67b0ed28cb4a4a44ecafb492d7c425fe439c02` | **metadata hash:** `bd4f0454065c72824f58ab497ee0626970698f4ffd177bcf53cb186dda514fc1`
