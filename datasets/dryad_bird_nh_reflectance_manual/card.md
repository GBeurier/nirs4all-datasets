# Datasheet — Bird NHReflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Bird NHReflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD bird

## Composition

- **Alignment:** sample level; 42 sample(s), 42 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

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
- **Content hash:** `120851d863763f70b35e8a808064272af9690ae41757bacf92f9c1fe0a740404`
- **Processing hash:** `5598eb694cb8d31426d1f537a8b8e8e2b6af379bd17c120f20c9b58f46901833` | **metadata hash:** `7e461b7c825475dc02f5ab469509755331117bbfa277a37fb0486bf4c50ea949`
