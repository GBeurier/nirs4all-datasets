# Datasheet — Bird NNReflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Bird NNReflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD bird

## Composition

- **Alignment:** sample level; 45 sample(s), 45 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

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

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.fxpnvx13b`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `09fa5efbe59386307c098f5c62c1c449c1b830fc89019c3f9e84acfe92eb4203`
- **Processing hash:** `645a5c9c4a188e1e250bec6fd3e7fb90589b6ea9c0e51da4f641ade8c8c664de` | **metadata hash:** `ac4857294f9e51f28617416f0ca12e4201512ca129941ef43b63f5728e8f6f08`
