# Datasheet — Rice flag leaves — reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Rice flag leaf reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD rice leaf

## Composition

- **Alignment:** sample level; 2700 sample(s), 2700 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
| source_sample_id | metadata | categorical | *Not specified.* | n=2700, missing=0, classes=495, top S1 (×6) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.p8pq7fq`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: The 495 column names are local to the 11 variety files. Merging them produces false groups of 5–6 spectra. 2700 variety × column pairs are distinct; physical independence and technical replicates are not established.
- **Curated views:** M: 1 fields, Y: 0 fields, measurements: 0 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `0947e407789581ba5b4cba0b0f29b225c526b88861fcf3c349c285ad73e4f900`
- **Processing hash:** `a873299ceab94b7db5ce075345ef901359ce4799e79e2442880addae28fb5f23` | **metadata hash:** `22da46d2a7728cf805184661f04ed99082ba5287ba55d61212bd681d8aa5ccaa`
