# Datasheet — Gastropod reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Gastropod reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD gastropods

## Composition

- **Alignment:** sample level; 197 sample(s), 197 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 187.6–1709 nm | 197 | 2422 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species_code | metadata | categorical | *Not specified.* | n=197, missing=0, classes=21, top CTRAM (×38) |
| individual_id | metadata | categorical | *Not specified.* | n=197, missing=0, classes=9, top 3 (×56) |
| state | metadata | categorical | *Not specified.* | n=197, missing=0, classes=2, top WET (×99) |
| body_region | metadata | categorical | *Not specified.* | n=197, missing=0, classes=12, top TOP (×48) |
| size_code | metadata | categorical | *Not specified.* | n=197, missing=0, classes=4, top XXX (×159) |
| manual_download | metadata | categorical | *Not specified.* | n=197, missing=0, classes=1, top True (×197) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=197, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\gastropods (×197) |
| manual_download_file | metadata | categorical | *Not specified.* | n=197, missing=0, classes=1, top doi_10_5061_dryad_905qfttnv__v20221207.zip::Spec_RealDat.zip (×197) |
| official_source_url | metadata | categorical | *Not specified.* | n=197, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.905qfttnv (×197) |
| standardization_batch | metadata | categorical | *Not specified.* | n=197, missing=0, classes=1, top v0.8.58 (×197) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.905qfttnv`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
- **Curated views:** M: 4 fields, Y: 0 fields, measurements: 0 fields, passport: 7 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `0364127082099ae5c64054e40fcc73854e6f39b4d455445167c9d76ed43afac6`
- **Processing hash:** `a05672e073defc529125d257fbd9089b74560abd82159a8de35840e27a52bffb` | **metadata hash:** `08a607ee6511e44c6785aac4d92ff70d90e97d2c611256426f751a445151bb63`
