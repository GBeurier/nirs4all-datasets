# Datasheet — E-liquid Alpha II MID OPUS transmittance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** E-liquid Alpha II MID OPUS transmittance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Mendeley e-liquid Alpha II MID spectra

## Composition

- **Alignment:** sample level; 26 sample(s), 26 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | MIR | 598.5–3996 cm-1 | 26 | 1653 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| instrument_family | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top eliquid_alpha (×26) |
| format_reader | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top nirs4all_formats::readers::bruker_opus (×26) |
| format_name | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top bruker-opus (×26) |
| signal_name | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top transmittance (×26) |
| axis_kind | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top wavenumber (×26) |
| axis_unit | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top cm-1 (×26) |
| axis_order | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top descending (×26) |
| manual_download | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top True (×26) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\eliquid (×26) |
| manual_download_file | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top The MID spectra of e liquids were acquired using a Bruker Alpha II (Universiti Putra Malaysia) instrument equipped with an attenuated total internal reflection (ATR).zip (×26) |
| official_source_url | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top https://data.mendeley.com/datasets/ddrzk7t5nt/1 (×26) |
| standardization_batch | metadata | categorical | *Not specified.* | n=26, missing=0, classes=1, top v0.8.61 (×26) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/ddrzk7t5nt/1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 14 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Data in Brief article and Mendeley record indicate open CC BY reuse; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `1bc3ac13e3257c41f2ab26172dcd5cf1d2680465d7506df526974815027f32a6`
- **Processing hash:** `3199dcd6ebd69ad6718d1eaaf2bcb27f0b6975c84b47007188de8b2a6a45c1f6` | **metadata hash:** `c616f4ecc6197be17326d57d94566be11723e2620318346427bc342440035282`
