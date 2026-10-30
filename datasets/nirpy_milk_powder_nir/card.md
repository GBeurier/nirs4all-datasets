# Datasheet — Nirpy Research milk powder NIR classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research milk powder NIR classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 220 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research milk powder NIR classification | *Not specified.* | NIR | 2–602 index | 220 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| labels | target | numeric | *Not specified.* | n=220, missing=0, range 1–11, mean 6 ± 3.169 |
| repository_url | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×220) |
| license | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top MIT License (×220) |
| license_url | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×220) |
| rights_status | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top explicit_open (×220) |
| usage_scope | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top public_reuse_possible (×220) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top True (×220) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top NIR (×220) |
| axis_unit | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top index (×220) |
| axis_min | metadata | numeric | *Not specified.* | n=220, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=220, missing=0, range 602–602, mean 602 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=220, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=220, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×220) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/milk-powder.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant de type date/indice de colonne, identité physique non établie ; le comptage littéral est rejeté. Chaque libellé est réutilisé dans 11 classes Y différentes ; les anciennes valeurs 9/11 ne décrivaient pas des répétitions du même lait.
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 16 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `ec66012d1b4dacf237599fbce8b1ece0a7c6275eb889e984afdb86cb99c37902`
- **Processing hash:** `e25193a1635a1ca15badfa6cb5f490e0a3b09751b1616f95649901c242c8bf6d` | **metadata hash:** `018fd216066637d820e0d0a6b4cbc3f59ed5b34cfce79c8a7009d24ad0b93634`
