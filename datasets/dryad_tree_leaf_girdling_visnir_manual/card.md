# Datasheet — Tree leaf girdling reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Tree leaf girdling reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD tree leaf

## Composition

- **Alignment:** sample level; 2722 sample(s), 2731 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.003).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2731 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| treatment | target | numeric | *Not specified.* | n=2722, missing=2722, range —, mean *Not specified.* ± *Not specified.* |
| leaf_code | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=2722, top CON_001_JAN21_L100000 (×1) |
| camera | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=5, top Cam02 (×700) |
| manual_download | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top True (×2722) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\tree leaf (×2722) |
| manual_download_file | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top doi_10_5061_dryad_d51c5b01n__v20201112.zip::*_spectra.xlsx (×2722) |
| official_source_url | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.d51c5b01n (×2722) |
| standardization_batch | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top v0.8.58 (×2722) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.d51c5b01n`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: 2722 source codes for 2731 rows. Each of the 9 repeated codes has two strictly identical spectral vectors; these are not demonstrated reacquisitions. No rows were removed from the sources.
- **Curated views:** M: 1 fields, Y: 0 fields, measurements: 0 fields, passport: 9 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `86ce3a659f027e8b39fbac661c7d5228c74f2918dfa865353be233aa8dbde378`
- **Processing hash:** `9517aacfbe7ae25e8f803eed0024d8e0c87224c77be3625b2de2f573c594c8b2` | **metadata hash:** `70c8465c71817e1cb57bc17c8e689db73e46b2a201d03d884efd95045952907c`
