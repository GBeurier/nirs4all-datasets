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
| infestation_status | target | categorical | *Not specified.* | n=15, missing=0, classes=3, top infested_l1 (×5) |
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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 7 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `cfbbeb064d831a8f614ea1319055614b85b683ac42a1c5c2eb196201565b8eb6`
- **Processing hash:** `68002d3e2ccd971b94a1cd8a5f7ee9b9590e56f76aaa2fd73e4e4a738999b023` | **metadata hash:** `417349046d5458fa4dc9185b1deabbbb8685d88c20e74c763ed9d4e654291282`
