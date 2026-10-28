# Datasheet — Frog spectral reflectance grouped means

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Frog spectral reflectance grouped means. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD frogs

## Composition

- **Alignment:** sample level; 7 sample(s), 7 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

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
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.6t1g1jx4p`
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
- **Content hash:** `26e959f708450eae25f022c410211b932f1e5445040c4e072c6a7a129a1bf920`
- **Processing hash:** `7d9cc6c497cf4c175d4a79d1f275102e2b74c50267fba2426a30cdddcfdf3ebd` | **metadata hash:** `bcc3fa851f26065b9d19c5561ff65d399187d11017814665f5e197356a286827`
