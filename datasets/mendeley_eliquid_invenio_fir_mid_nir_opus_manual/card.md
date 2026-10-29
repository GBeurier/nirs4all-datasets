# Datasheet — E-liquid Invenio-R FIR/MID/NIR OPUS transmittance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** E-liquid Invenio-R FIR/MID/NIR OPUS transmittance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Mendeley e-liquid Invenio-R FIR/MID/NIR spectra

## Composition

- **Alignment:** sample level; 27 sample(s), 27 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | MIR | 79.08–5997 cm-1 | 27 | 3069 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| instrument_family | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top eliquid_invenio (×27) |
| format_reader | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top nirs4all_formats::readers::bruker_opus (×27) |
| format_name | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top bruker-opus (×27) |
| signal_name | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top transmittance (×27) |
| axis_kind | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top wavenumber (×27) |
| axis_unit | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top cm-1 (×27) |
| axis_order | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top descending (×27) |
| manual_download | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top True (×27) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\eliquid (×27) |
| manual_download_file | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top The FIR MID NIR spectra of e liquids were acquired using a Bruker Invenio-R (Universiti Putra Malaysia) instrument equipped with an attenuated total internal reflection (ATR).zip (×27) |
| official_source_url | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top https://data.mendeley.com/datasets/2cwtxdtstn/1 (×27) |
| standardization_batch | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top v0.8.61 (×27) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/2cwtxdtstn/1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 14 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `95f37348d6405c95407996354c6758b3e403a435fae62659be0ef74e31fc0835`
- **Processing hash:** `8d8534f493af9c3c02506e5d7113e5f665832dafa0c01c04f751694e59cd7d4f` | **metadata hash:** `21e65860f6f913d9be1dccdefbdcae396c77d88b5db4db17cef9167b4197c710`
