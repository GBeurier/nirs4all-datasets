# Datasheet — Malaria Anopheles gambiae oocyst NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** malaria
- **Description:** Malaria Anopheles gambiae oocyst NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, malaria
- **Contributor:** Malaria Anopheles gambiae oocyst NIR

## Composition

- **Alignment:** observation level; 333 sample(s), 333 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | malaria_nir | NIR | NIR | 350–2500 none | 333 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| x | target | numeric | *Not specified.* | n=333, missing=0, range 0–6.096e+04, mean 2386 ± 6742 |
| ID1 | metadata | categorical | *Not specified.* | n=333, missing=0, classes=71, top Minfection/113G3 (×14) |
| ID2 | metadata | numeric | *Not specified.* | n=333, missing=0, range 0–9, mean 4.21 ± 2.809 |
| ID | metadata | categorical | *Not specified.* | n=333, missing=0, classes=274, top Minfection/11310 (×2) |
| Oocytes | metadata | numeric | *Not specified.* | n=333, missing=0, range 0–6.096e+04, mean 2386 ± 6742 |
| active_status | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top active (×333) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top bacon_malaria_oocist_333_maia_classification (×333) |
| active_replacement_source_note | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top rebuilt_from_existing_standardized_export_with_official_source_documented (×333) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 227, test: 106

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Harvard Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.7910/DVN/YD34OX`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `cd0d19fcecd868619c09fceb7822ee43be534dd37a1708886c02f5de9a173d31`
- **Processing hash:** `941780cde2ed375f081d6605d96aba1bb21d9620a389bc0e05ab00ee3401ff2d` | **metadata hash:** `e4d66c82feaed6d2c46a0d0b160bb5dc9ada85cbef3f83f2785cc5dc7df50f44`
