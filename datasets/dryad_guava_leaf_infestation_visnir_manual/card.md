# Datasheet — Guava leaf infestation reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Guava leaf infestation reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD guava leaf

## Composition

- **Alignment:** sample level; 15 sample(s), 15 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 325–1075 nm | 15 | 751 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| infestation_status | target | numeric | *Not specified.* | n=15, missing=15, range —, mean *Not specified.* ± *Not specified.* |
| manual_download | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top True (×15) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\guava leaf (×15) |
| manual_download_file | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top doi_10_5061_dryad_tx95x6bbn__v20260304.zip::Dataset-Spectral.zip::Dataset/Data-global.csv (×15) |
| official_source_url | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.tx95x6bbn (×15) |
| standardization_batch | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top v0.8.58 (×15) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.tx95x6bbn`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Original sample identifier retained under a prefixed/equivalent name
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 8 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `94b77af45aa8391a4a9983a328d9bb830ccf07b803a0c5373738efeb400bbbcb`
- **Processing hash:** `7510048caadad9117bac0681ca8877115e3d19379a20398296d15dfa014e1b31` | **metadata hash:** `efca2b99dab0c862df300629b9940c05a80d565686eff24af6e75c1beefdb355`
