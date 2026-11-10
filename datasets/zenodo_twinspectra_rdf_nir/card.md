# Datasheet — TwinSpectra soils — ASD FieldSpec + MicroNIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo TwinSpectra soil NIR, ASD FieldSpec and MicroNIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** TwinSpectra Dataset

## Composition

- **Alignment:** sample level; 768 sample(s), 1438 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_fieldspec | ASD FieldSpec 4 Hi-Res | ASD FieldSpec 4 Hi-Res | NIR | 350–2500 nm | 718 | 2151 |
| X_micronir | Viavi microNIR | Viavi microNIR | NIR | 908.1–1676 nm | 720 | 125 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| group | target | categorical | *Not specified.* | n=1438, missing=0, classes=6, top Rubber (×240) |
| file_url | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=2, top https://zenodo.org/api/records/18471662/files/measurements_125.csv/content (×720) |
| article_url | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340926004713 (×1438) |
| doi_dataset | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top 10.5281/zenodo.18471662 (×1438) |
| doi_publication | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top 10.1016/j.dib.2026.112920 (×1438) |
| license | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×1438) |
| license_id | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top cc-by-4.0 (×1438) |
| license_url | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×1438) |
| rights_status | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top explicit_open (×1438) |
| usage_scope | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top public_reuse_possible (×1438) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top True (×1438) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top NIR (×1438) |
| axis_unit | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top nm (×1438) |
| axis_min | metadata | numeric | *Not specified.* | n=1438, missing=0, range 350–908.1, mean 629.4 ± 279.1 |
| axis_max | metadata | numeric | *Not specified.* | n=1438, missing=0, range 1676–2500, mean 2088 ± 412 |
| n_points_original | metadata | numeric | *Not specified.* | n=1438, missing=0, range 125–2151, mean 1137 ± 1013 |
| notes | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=1, top Refuse-derived fuel particle spectra with class labels and predefined subset folds. (×1438) |
| id | metadata | categorical | *Not specified.* | n=1438, missing=0, classes=363, top 575 (×6) |
| sample | metadata | numeric | *Not specified.* | n=1438, missing=0, range 0–777, mean 373.1 ± 214.8 |
| fold | metadata | numeric | *Not specified.* | n=1438, missing=0, range 0–4, mean 1.998 ± 1.414 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/18471662`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/18471662/files/measurements_2151.csv/content`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/18471662/files/measurements_125.csv/content`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 23 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Zenodo record license is CC-BY-4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `6a3812c17d55334525e3bd483fe94a6edb4979f68d29a2a89b8901958e38f321`
- **Processing hash:** `66d2540a3fe0a6fac24376cecf264c78010704b43702fb5a96ba0c7468ff2edf` | **metadata hash:** `047f0a09dae39848669529ed882c5ee3221dfcd544d879fb4d863189032c9203`
