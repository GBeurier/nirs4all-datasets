# Datasheet — Rice flag leaf reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Rice flag leaf reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD rice leaf

## Composition

- **Alignment:** sample level; 2700 sample(s), 2700 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 281.8–1114 nm | 2700 | 1024 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| variety | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=11, top CY1000 (×270) |
| manual_download | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=1, top True (×2700) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\rice leaf (×2700) |
| manual_download_file | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=1, top data+for+publish.rar::*_Reflectance_flag leaf.xlsx (×2700) |
| official_source_url | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.p8pq7fq (×2700) |
| standardization_batch | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=1, top v0.8.58 (×2700) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.p8pq7fq`
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
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual RAR download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `f9508e1cc6fcc24a02e0afe940e99bcb69d623530c6b0eb665b247689b02840b`
- **Processing hash:** `8f0876fa8e950fbb476ffced31378a4213ff14966f944247a28a1c76b3d60e74` | **metadata hash:** `b8aa8f0452f51a78bf4fa2ff876e2aacd70385f5b54bd041c57889e04d67d1e9`
