# Datasheet — Mendeley diesel and biodiesel FTIR OPUS

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley diesel and biodiesel FTIR OPUS. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Experimental raw data of B7 and B10

## Composition

- **Alignment:** sample level; 30 sample(s), 30 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | OPUS transmittance spectra | Bruker Invenio-R ATR | MIR | 79.08–5997 cm-1 | 30 | 3069 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| fuel_blend_class | target | categorical | *Not specified.* | n=30, missing=0, classes=2, top B10 (×20) |
| product_name | target | categorical | *Not specified.* | n=30, missing=0, classes=14, top DIESEL MAX B10 (×6) |
| brand | target | categorical | *Not specified.* | n=30, missing=0, classes=7, top Petronas (×8) |
| lot_number | metadata | categorical | *Not specified.* | n=30, missing=0, classes=30, top DE5_BP1_433 (×1) |
| api_url | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/d7sx7bf2hk/snapshot/1 (×30) |
| files_api_url | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/d7sx7bf2hk/files?folder_id=root&version=1&$start=0&$limit=1000 (×30) |
| doi_dataset | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top 10.17632/d7sx7bf2hk.1 (×30) |
| license | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×30) |
| license_id | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top cc-by-4.0 (×30) |
| license_url | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×30) |
| rights_status | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top explicit_open (×30) |
| usage_scope | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top public_reuse_possible (×30) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top True (×30) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top FTIR (×30) |
| spectral_signal | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top transmittance (×30) |
| axis_unit | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top cm-1 (×30) |
| axis_min | metadata | numeric | *Not specified.* | n=30, missing=0, range 79.08–79.08, mean 79.08 ± 2.891e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=30, missing=0, range 5997–5997, mean 5997 ± 1.85e-12 |
| n_points_original | metadata | numeric | *Not specified.* | n=30, missing=0, range 3069–3069, mean 3069 ± 0 |
| decoder | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top nirs4all-formats (×30) |
| decoder_signal | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top transmittance (×30) |
| notes | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Bruker OPUS binary decoded with nirs4all-formats 0.2.10, sample metadata transcribed from official Mendeley record description. (×30) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/d7sx7bf2hk/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/d7sx7bf2hk/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/d7sx7bf2hk/files?folder_id=root&version=1&$start=0&$limit=1000`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Official Mendeley Data public API reports CC BY 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0a0b90cdbdafb918e4206233e46842ee81352e8dbea2636b848a050831b561db`
- **Processing hash:** `ce309778f347fe613c5c9ccfc31447694ce13afe1a116d33e4bd5a3097b35718` | **metadata hash:** `4bbc2b82a98bed5ead663504f4f8be9471ef2aa168a76529ba97a741567d351e`
