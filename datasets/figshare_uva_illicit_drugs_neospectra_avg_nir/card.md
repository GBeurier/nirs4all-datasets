# Datasheet — UvA Figshare illicit-drugs NeoSpectra averaged NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** UvA Figshare illicit-drugs NeoSpectra averaged NIR. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 429 sample(s), 429 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NeoSpectra averaged NIR | NeoSpectra | NIR | 1299–2604 nm | 429 | 160 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=429, missing=89, classes=81, top cocaine (×95) |
| set | target | categorical | *Not specified.* | n=429, missing=89, classes=7, top K (×88) |
| salt_form | target | categorical | *Not specified.* | n=429, missing=328, classes=4, top HCl (×91) |
| matrix | target | categorical | *Not specified.* | n=429, missing=89, classes=4, top powder (×267) |
| color | target | categorical | *Not specified.* | n=429, missing=90, classes=17, top white (×200) |
| instrument | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top NeoSpectra (×429) |
| instrument_code | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top NeoSpectra (×429) |
| api_url | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×429) |
| download_url | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×429) |
| article_url | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×429) |
| doi_dataset | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×429) |
| doi_publication | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×429) |
| license | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×429) |
| license_id | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top cc-by-4.0 (×429) |
| license_url | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×429) |
| rights_status | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top explicit_open (×429) |
| usage_scope | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top public_reuse_possible (×429) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top True (×429) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top NIR (×429) |
| axis_unit | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top nm (×429) |
| axis_min | metadata | numeric | *Not specified.* | n=429, missing=0, range 1299–1299, mean 1299 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=429, missing=0, range 2604–2604, mean 2604 ± 4.553e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=429, missing=0, range 160–160, mean 160 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top absorbance (×429) |
| decoder | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top pandas.read_excel/openpyxl (×429) |
| notes | metadata | categorical | *Not specified.* | n=429, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×429) |
| nr | metadata | numeric | *Not specified.* | n=429, missing=89, range 0–133, mean 48.05 ± 41.89 |
| other | metadata | categorical | *Not specified.* | n=429, missing=203, classes=116, top cocaine 100wt% (×8) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://uvaauas.figshare.com/articles/dataset/Dataset_of_Near-Infrared_Spectral_Data_of_Illicit-Drugs_and_Forensic_Casework_Samples_Analyzed_by_Five_Portable_Spectrometers_Operating_in_Different_Wavelength_Ranges/21252300`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/21252300`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 4 fields, measurements: 0 fields, passport: 29 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `019e1f8cb6848d6679cb5614e528fb1b01ce15f7e8b5ae3723eebcb311888021`
- **Processing hash:** `5544d2e314ff0618f4a7137f7e779e398fc9b93ddc56ad1c3ace0763ae889bfa` | **metadata hash:** `704bd86af9707b9532e80f0eaac45e8299d47eaaba619143976771ee60588de6`
