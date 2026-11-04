# Datasheet — Harvard Dataverse NIR spectra of Plasmodium falciparum infected Anopheles gambiae

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** harvard
- **Description:** Harvard Dataverse NIR spectra of Plasmodium falciparum infected Anopheles gambiae. Origin database composed from 2 standardized v2.0 leaves: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, harvard
- **Contributor:** Malaria Anopheles gambiae oocyst NIR

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 562 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | malaria_nir | NIR | NIR | 350–2500 none | 562 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| parasite_load | target | numeric | *Not specified.* | n=562, missing=0, range 0–2.359e+05, mean 6241 ± 1.891e+04 |
| ID1 | metadata | categorical | *Not specified.* | n=562, missing=0, classes=90, top infection/S2161 (×18) |
| ID2 | metadata | numeric | *Not specified.* | n=562, missing=0, range 0–9, mean 4.222 ± 2.802 |
| ID | metadata | categorical | *Not specified.* | n=562, missing=0, classes=365, top Minfection/11310 (×2) |
| Oocytes | metadata | numeric | *Not specified.* | n=562, missing=229, range 0–6.096e+04, mean 2386 ± 6742 |
| active_status | metadata | categorical | *Not specified.* | n=562, missing=0, classes=1, top active (×562) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=562, missing=0, classes=2, top bacon_malaria_oocist_333_maia_classification (×333) |
| active_replacement_source_note | metadata | categorical | *Not specified.* | n=562, missing=0, classes=1, top rebuilt_from_existing_standardized_export_with_official_source_documented (×562) |
| infection_stage | metadata | categorical | *Not specified.* | n=562, missing=0, classes=2, top oocyst (×333) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 365, test: 197

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Harvard Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.7910/DVN/YD34OX`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: 274 ID strings for 333 rows; ID1/ID2 may collide after concatenation. Mosquito identity and reacquisitions are not established by the available reconstruction script.
- **Curated views:** M: 1 fields, Y: 1 fields, passport: 13 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `5c4185984d596f73ed1aaa1c00933b838befe06da4fc0db171265a092a7821d3`
- **Processing hash:** `21a1363144ceaf5795dff0c6d97c9a1408bb7171d554687914fb4ceb5fdbfd2e` | **metadata hash:** `508a52d7e9393eed113b96bf8158df27df77f49fee1818a163a001358ad7a52b`
