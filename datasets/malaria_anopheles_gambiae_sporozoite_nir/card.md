# Datasheet — Malaria Anopheles gambiae sporozoite NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** malaria
- **Description:** Malaria Anopheles gambiae sporozoite NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, malaria
- **Contributor:** Malaria Anopheles gambiae sporozoite NIR

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 229 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | malaria_nir | NIR | NIR | 350–2500 none | 229 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| x | target | numeric | *Not specified.* | n=229, missing=0, range 0–2.359e+05, mean 1.185e+04 ± 2.758e+04 |
| ID1 | metadata | categorical | *Not specified.* | n=229, missing=0, classes=33, top infection/S2161 (×18) |
| ID2 | metadata | numeric | *Not specified.* | n=229, missing=0, range 0–9, mean 4.24 ± 2.797 |
| ID | metadata | categorical | *Not specified.* | n=229, missing=0, classes=138, top infection/S2140 (×2) |
| active_status | metadata | categorical | *Not specified.* | n=229, missing=0, classes=1, top active (×229) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=229, missing=0, classes=1, top bacon_malaria_sporozoite_229_maia_classification (×229) |
| active_replacement_source_note | metadata | categorical | *Not specified.* | n=229, missing=0, classes=1, top rebuilt_from_existing_standardized_export_with_official_source_documented (×229) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 91, train: 138

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Harvard Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.7910/DVN/YD34OX`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: 138 ID strings for 229 rows; ID1/ID2 may collide after concatenation. Mosquito identity and reacquisitions are not established by the available reconstruction script.
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 13 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `0a55c2566652e45af7bab9b31444fa0b7d915a0ddc9259decdb3cf77191e62c6`
- **Processing hash:** `63d147a8d7967498f09b16ccd62ea4223a8d5fd9458543248e95e209b5b5085c` | **metadata hash:** `22fe879998ef504a4d6a0bc58be4659061f5bdde3892b208a9a27127e8543343`
