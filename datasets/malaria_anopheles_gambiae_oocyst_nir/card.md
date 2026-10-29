# Datasheet — Malaria Anopheles gambiae oocyst NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** malaria
- **Description:** Malaria Anopheles gambiae oocyst NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, malaria
- **Contributor:** Malaria Anopheles gambiae oocyst NIR

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 333 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | malaria_nir | NIR | NIR | 350–2500 none | 333 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| x | target | numeric | *Not specified.* | n=333, missing=0, range 0–6.096e+04, mean 2386 ± 6742 |
| ID1 | metadata | categorical | *Not specified.* | n=333, missing=0, classes=71, top Minfection/114 (×14) |
| ID2 | metadata | numeric | *Not specified.* | n=333, missing=0, range 0–9, mean 4.21 ± 2.809 |
| ID | metadata | categorical | *Not specified.* | n=333, missing=0, classes=274, top Minfection/11310 (×2) |
| Oocytes | metadata | numeric | *Not specified.* | n=333, missing=0, range 0–6.096e+04, mean 2386 ± 6742 |
| active_status | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top active (×333) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top bacon_malaria_oocist_333_maia_classification (×333) |
| active_replacement_source_note | metadata | categorical | *Not specified.* | n=333, missing=0, classes=1, top rebuilt_from_existing_standardized_export_with_official_source_documented (×333) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 106, train: 227

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Harvard Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.7910/DVN/YD34OX`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: 274 chaînes ID pour 333 lignes ; ID1/ID2 peuvent entrer en collision après concaténation. Identité des moustiques et réacquisitions non établies par le script de reconstruction disponible.
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 13 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `dd31b0f333961869d43c5ee2f5dfc96e655295666c38ffba0e64547953b24768`
- **Processing hash:** `83a61ffa4daa70f3102b7a03930c2470033ddb90d5e204e95eb0220f27e409e2` | **metadata hash:** `413de6253900daca33207f6a3efa97a85e1891b8248d33cdcb6f3b251e62cf0d`
