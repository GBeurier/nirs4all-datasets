# Datasheet — Gastropod reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Gastropod reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD gastropods

## Composition

- **Alignment:** sample level; 197 sample(s), 197 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 187.6–1709 nm | 197 | 2482 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species_code | metadata | categorical | *Not specified.* | n=197, missing=0, classes=21, top CTRAM (×38) |
| individual_id | metadata | categorical | *Not specified.* | n=197, missing=0, classes=9, top 3 (×56) |
| state | metadata | categorical | *Not specified.* | n=197, missing=0, classes=2, top WET (×99) |
| body_region | metadata | categorical | *Not specified.* | n=197, missing=0, classes=12, top TOP (×48) |
| size_code | metadata | categorical | *Not specified.* | n=197, missing=0, classes=4, top XXX (×159) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.905qfttnv`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.

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
- **Content hash:** `d0b90e9ba67449b0397146489ee5c68034ccb31399cf2740b64392faf269eb04`
- **Processing hash:** `c200b1a0e74e8d76802a7b0010ea956e9a57480422c7ac2ea99ba5b0ceeeb493` | **metadata hash:** `609e4d194a7f166e628d6c10232e8b5829b099481f9ef245ae4d2af20f7583a8`
