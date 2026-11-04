# Datasheet — Bird NNReflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Bird NNReflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD bird

## Composition

- **Alignment:** sample level; 45 sample(s), 45 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300.2–1.998e+04 nm | 45 | 11311 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top True (×45) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\bird (×45) |
| manual_download_file | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top Final.BirdData.xlsx::NNReflectance (×45) |
| official_source_url | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.fxpnvx13b (×45) |
| standardization_batch | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top v0.8.57 (×45) |
| source_sample_id | metadata | categorical | *Not specified.* | n=45, missing=0, classes=45, top 23556 (×1) |
| source_sheet | metadata | categorical | *Not specified.* | n=45, missing=0, classes=1, top NNReflectance (×45) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.fxpnvx13b`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Original sample identifier retained under a prefixed/equivalent name
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 7 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `0104fd678f41da5e9f30a1807642a2c16bbd15ae325d1fe3c620c1e8040fa0ce`
- **Processing hash:** `03d18c5c7acf82a8bd8ba04b41356fa50486791dfdfdfa9213779fe5fc2e06d8` | **metadata hash:** `c83d37205cb8c104fe54e8eae4d486ec167de98bb33a90d93bd756529128bafa`
