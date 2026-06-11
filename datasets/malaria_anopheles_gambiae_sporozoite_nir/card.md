# Datasheet — Malaria Anopheles gambiae sporozoite NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** malaria
- **Description:** Malaria Anopheles gambiae sporozoite NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, malaria
- **Contributor:** Malaria Anopheles gambiae sporozoite NIR

## Composition

- **Alignment:** observation level; 229 sample(s), 229 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

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

- **original** (documented, not applied): train: 138, test: 91

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
- **Content hash:** `77aec0141e9312bb89013d51cbc642b1ab22801a757ba74b2e212655c801906d`
- **Processing hash:** `8cabf18935a997f0297a8a2fe836bbe3de031571c6e96e0483a405b12f921ab2` | **metadata hash:** `449792b4efbe736b4163589b530b1d850a998dc95cfe656b20ef530cee8765fe`
