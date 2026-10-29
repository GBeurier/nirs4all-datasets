# Datasheet — Bird NHReflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Bird NHReflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD bird

## Composition

- **Alignment:** sample level; 42 sample(s), 42 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–1.998e+04 nm | 42 | 10652 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=42, missing=0, classes=1, top True (×42) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=42, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\bird (×42) |
| manual_download_file | metadata | categorical | *Not specified.* | n=42, missing=0, classes=1, top Final.BirdData.xlsx::NHReflectance (×42) |
| official_source_url | metadata | categorical | *Not specified.* | n=42, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.fxpnvx13b (×42) |
| standardization_batch | metadata | categorical | *Not specified.* | n=42, missing=0, classes=1, top v0.8.57 (×42) |

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

- **Conversion warnings:** Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `ad5dfdd39c4da8d63c318e4a09bb266669627d21f4848376f8aafffb9ba92e00`
- **Processing hash:** `0a53687a99b60acbdd062885d76ae3e137c1a86ddb29d8be378e5c8b1aeae00d` | **metadata hash:** `a0ebc19db0a9f9cd091a2116f89480b014b42eb338aa56733a36a979e04757b0`
