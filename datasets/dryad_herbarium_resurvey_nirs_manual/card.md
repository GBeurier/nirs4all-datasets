# Datasheet — Herbarium resurvey NIRS spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Herbarium resurvey NIRS spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD herbarium

## Composition

- **Alignment:** sample level; 2718 sample(s), 2718 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2718 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=2718, missing=0, classes=1, top True (×2718) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=2718, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\herbarium (×2718) |
| manual_download_file | metadata | categorical | *Not specified.* | n=2718, missing=0, classes=1, top doi_10_5061_dryad_z34tmpgpw__v20241216.zip::Kuehn_et_al._Resurvey_-_JEcol_Open_Data.zip::*dpt (×2718) |
| official_source_url | metadata | categorical | *Not specified.* | n=2718, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.z34tmpgpw (×2718) |
| standardization_batch | metadata | categorical | *Not specified.* | n=2718, missing=0, classes=1, top v0.8.60 (×2718) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.z34tmpgpw`
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
- **Content hash:** `6dec520c520ac572f1d00d30cc42237c8520136ca548d97008ddddd3aea2f413`
- **Processing hash:** `b0c9ae943c16e92e3abc492a3f38237e27a68aed80f01301647d45b6eac595cd` | **metadata hash:** `4ada1c053f865cb1e6b5103a895a193183568b4d91b5424bdb61413ac319930e`
