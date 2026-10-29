# Datasheet — UCPH tablet NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH tablet NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** UCPH Chemometrics tablet dataset

## Composition

- **Alignment:** sample level; 310 sample(s), 310 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | tablet_nir | NIR transmittance | NIR | 7398–1.051e+04 cm-1 | 310 | 404 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| active_w_w | target | numeric | *Not specified.* | n=310, missing=0, range 4.61–9.786, mean 7.428 ± 1.295 |
| tablet_type | target | categorical | *Not specified.* | n=310, missing=0, classes=4, top B (×80) |
| batch | metadata | numeric | *Not specified.* | n=310, missing=0, range 1–31, mean 16 ± 8.959 |
| replicate | metadata | numeric | *Not specified.* | n=310, missing=0, range 1–10, mean 5.5 ± 2.877 |
| scale | metadata | categorical | *Not specified.* | n=310, missing=0, classes=3, top pilot (×120) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): by_batch_grouping_documented_not_applied: 310

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/tablet/`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/datasets/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Le source_sample_id inclut lot et numéro de comprimé ; les dix numéros ne démontrent pas dix réacquisitions du même comprimé.
- **Curated views:** M: 2 fields, Y: 2 fields, passport: 6 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f59aa9a7ab078438d3d73170553aeba2eb63d729e6194508390d1c61834061d2`
- **Processing hash:** `870b4ea7b8f066ca9c8a4becf372cb90ad3da700554f72154420d3b7bc12f845` | **metadata hash:** `302656a3202577d15b7129c9adb272bdd6d0231df90f0f80bbaab8050d6d6dc1`
