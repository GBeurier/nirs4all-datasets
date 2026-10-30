# Datasheet — Scarab first batch reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Scarab first batch reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD scarab

## Composition

- **Alignment:** sample level; 236 sample(s), 236 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–2100 nm | 236 | 901 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top True (×236) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\scarab (×236) |
| manual_download_file | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top doi_10_5061_dryad_rv15dv4f7__v20240603.zip::2_Reflectance_FirstBatch.csv (×236) |
| official_source_url | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.rv15dv4f7 (×236) |
| standardization_batch | metadata | categorical | *Not specified.* | n=236, missing=0, classes=1, top v0.8.57 (×236) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.rv15dv4f7`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 6 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `ab2e24580ff9d9c3bfa561f7f68f0b014d2eef0db3d061c1309cef19df09bcba`
- **Processing hash:** `a6ef30038279245b38575eccd8965cf90bc19ab8c0cd7697aff272578685dfd1` | **metadata hash:** `f91b1048064fe0c39cb46e3761571074483d8ffa156afc35f861948fa63d1f0f`
