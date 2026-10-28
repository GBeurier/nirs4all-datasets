# Datasheet — Scarab first batch reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Scarab first batch reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD scarab

## Composition

- **Alignment:** sample level; 236 sample(s), 236 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–2100 nm | 236 | 901 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top True (×236) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\scarab (×236) |
| manual_download_file | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top doi_10_5061_dryad_rv15dv4f7__v20240603.zip::2_Reflectance_FirstBatch.csv (×236) |
| official_source_url | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.rv15dv4f7 (×236) |
| standardization_batch | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top v0.8.57 (×236) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.rv15dv4f7`
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
- **Content hash:** `ca9d1a0d4fb59e4e744917aa0119d30ef3ee85ed8b6b300825dcb99ac997ccb6`
- **Processing hash:** `9de21e0d19765c6440b2c4f37f94fb3bab98d050f37b6181aebc648ac19db213` | **metadata hash:** `34f7b7ce469a50999ba629497c2e4cbcad4770c8eb783b694ad7cd234755731d`
