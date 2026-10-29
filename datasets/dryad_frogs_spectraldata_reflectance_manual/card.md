# Datasheet — Frog spectral reflectance grouped means

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Frog spectral reflectance grouped means. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD frogs

## Composition

- **Alignment:** sample level; *Not specified.* sample(s), 7 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–1700 nm | 7 | 1401 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | metadata | categorical | *Not specified.* | n=7, missing=0, classes=6, top Model (×2) |
| nir_class | metadata | categorical | *Not specified.* | n=7, missing=0, classes=2, top High (×4) |
| type | metadata | categorical | *Not specified.* | n=7, missing=0, classes=2, top Real (×5) |
| treatment | metadata | categorical | *Not specified.* | n=7, missing=0, classes=7, top HighC. calcarifer (×1) |
| manual_download | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top True (×7) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\frogs (×7) |
| manual_download_file | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top doi_10_5061_dryad_6t1g1jx4p__v20250212.zip::spectraldata.csv (×7) |
| official_source_url | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.6t1g1jx4p (×7) |
| standardization_batch | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top v0.8.57 (×7) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.6t1g1jx4p`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Non déterminé
- **Curated views:** M: 2 fields, Y: 0 fields, passport: 6 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `bf0aba8af415421b975f05c78fe059ee9d851f1f2a6fd82a41c7e0a789bc6f10`
- **Processing hash:** `2d42dea3dea5e80f0b7468556ae3efaf104b74d32d43dfb95e94545f3039bd86` | **metadata hash:** `5ff45c1737607e1d82bc473c758e3e53197f9b94e8fe14b8c287cff8af3bd33d`
