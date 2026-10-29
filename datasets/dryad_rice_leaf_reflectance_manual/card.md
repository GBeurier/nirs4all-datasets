# Datasheet — Rice flag leaf reflectance spectra

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

- **Conversion warnings:** Curation identity contract: Les 495 noms de colonnes sont locaux aux 11 fichiers de variétés. Les fusionner produit de faux groupes de 5–6 spectres. 2700 couples variété × colonne sont distincts ; indépendance physique et répétitions techniques non établies.
- **Curated views:** M: 1 fields, Y: 0 fields, passport: 6 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `94c7ce2afd2d345efa466c91aa607c4a65f1b99b2e9bc2520f237e4a43f13f14`
- **Processing hash:** `6664cf9e1e66e3be976caf7bc1818662b65dd05d55f75107e35401cec97b6483` | **metadata hash:** `c1a6f5df7883905e9951a388534d069c73c35bef4b0d73135cb69959129e293f`
