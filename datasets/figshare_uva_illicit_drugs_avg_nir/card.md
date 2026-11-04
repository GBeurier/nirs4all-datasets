# Datasheet — Figshare UvA illicit drugs NIR, five instruments, sample-averaged

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** Figshare UvA illicit drugs NIR, five instruments, sample-averaged. Origin database composed from 5 standardized v2.0 leaves: 5 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 599 sample(s), 2003 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_asd | ASD FieldSpec averaged NIR | ASD FieldSpec | NIR | 350–2500 nm | 390 | 2151 |
| X_micronir | Viavi MicroNIR averaged NIR | Viavi MicroNIR | NIR | 908.1–1676 nm | 424 | 125 |
| X_neospectra | NeoSpectra averaged NIR | NeoSpectra | NIR | 1299–2604 nm | 429 | 160 |
| X_nirone | NIRONE averaged NIR | NIRONE | NIR | 1550–1950 nm | 341 | 201 |
| X_scio | Consumer Physics SCiO averaged NIR | Consumer Physics SCiO | NIR | 740–1070 nm | 419 | 331 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=2003, missing=181, classes=86, top cocaine (×542) |
| set | target | categorical | *Not specified.* | n=2003, missing=181, classes=7, top PAM (×419) |
| salt_form | target | categorical | *Not specified.* | n=2003, missing=1467, classes=4, top HCl (×425) |
| matrix | target | categorical | *Not specified.* | n=2003, missing=181, classes=4, top powder (×1462) |
| color | target | categorical | *Not specified.* | n=2003, missing=185, classes=17, top white (×1131) |
| instrument | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=5, top NeoSpectra (×429) |
| instrument_code | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=5, top NeoSpectra (×429) |
| source_set_from_file | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=5, top PAM (×599) |
| api_url | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×2003) |
| download_url | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×2003) |
| article_url | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×2003) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×2003) |
| doi_publication | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×2003) |
| license | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×2003) |
| license_id | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top cc-by-4.0 (×2003) |
| license_url | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×2003) |
| rights_status | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top explicit_open (×2003) |
| usage_scope | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top public_reuse_possible (×2003) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top True (×2003) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top NIR (×2003) |
| axis_unit | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top nm (×2003) |
| axis_min | metadata | numeric | *Not specified.* | n=2003, missing=0, range 350–1550, mean 957.4 ± 408.8 |
| axis_max | metadata | numeric | *Not specified.* | n=2003, missing=0, range 1070–2604, mean 1955 ± 573.2 |
| n_points_original | metadata | numeric | *Not specified.* | n=2003, missing=0, range 125–2151, mean 583 ± 774.5 |
| signal_type | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=2, top absorbance (×1584) |
| decoder | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top pandas.read_excel/openpyxl (×2003) |
| notes | metadata | categorical | *Not specified.* | n=2003, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×2003) |
| nr | metadata | numeric | *Not specified.* | n=2003, missing=181, range 0–200, mean 54.87 ± 46.26 |
| other | metadata | categorical | *Not specified.* | n=2003, missing=909, classes=128, top levamisole (×47) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://uvaauas.figshare.com/articles/dataset/Dataset_of_Near-Infrared_Spectral_Data_of_Illicit-Drugs_and_Forensic_Casework_Samples_Analyzed_by_Five_Portable_Spectrometers_Operating_in_Different_Wavelength_Ranges/21252300`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/21252300`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 2 fields, Y: 4 fields, passport: 27 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Figshare API reports CC BY 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `15e76fa807ea7e49d21a7cee87a6a0801f372b962dd79c813986b1cd942d2198`
- **Processing hash:** `13b8a2a1d5923b9000698d1eb71d13cbcd91d4b00d2f9cfc4a8e20d2af2f654a` | **metadata hash:** `20c93ae0d254a6997242e5fa01761cf06fde1cd93e069c09b5b5b6ccb514a01a`
