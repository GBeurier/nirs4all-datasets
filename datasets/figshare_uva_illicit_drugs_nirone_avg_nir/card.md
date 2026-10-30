# Datasheet — UvA Figshare illicit-drugs NIRONE averaged NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** UvA Figshare illicit-drugs NIRONE averaged NIR. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 341 sample(s), 341 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NIRONE averaged NIR | NIRONE | NIR | 1550–1950 nm | 341 | 201 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=341, missing=0, classes=84, top MDMA (×87) |
| set | target | categorical | *Not specified.* | n=341, missing=0, classes=6, top PAM (×104) |
| salt_form | target | categorical | *Not specified.* | n=341, missing=271, classes=4, top HCl (×41) |
| matrix | target | categorical | *Not specified.* | n=341, missing=0, classes=4, top powder (×269) |
| color | target | categorical | *Not specified.* | n=341, missing=1, classes=17, top white (×202) |
| instrument | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top NIRONE (×341) |
| instrument_code | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top NIRONE (×341) |
| api_url | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×341) |
| download_url | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×341) |
| article_url | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×341) |
| doi_dataset | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×341) |
| doi_publication | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×341) |
| license | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×341) |
| license_id | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top cc-by-4.0 (×341) |
| license_url | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×341) |
| rights_status | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top explicit_open (×341) |
| usage_scope | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top public_reuse_possible (×341) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top True (×341) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top NIR (×341) |
| axis_unit | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top nm (×341) |
| axis_min | metadata | numeric | *Not specified.* | n=341, missing=0, range 1550–1550, mean 1550 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=341, missing=0, range 1950–1950, mean 1950 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=341, missing=0, range 201–201, mean 201 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top absorbance (×341) |
| decoder | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top pandas.read_excel/openpyxl (×341) |
| notes | metadata | categorical | *Not specified.* | n=341, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×341) |
| nr | metadata | numeric | *Not specified.* | n=341, missing=0, range 0–133, mean 49.72 ± 42.11 |
| other | metadata | categorical | *Not specified.* | n=341, missing=170, classes=51, top levamisole (×11) |

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
- **Content hash:** `7e80831faaa27069232f9081c6d340ede6ad4c6dabdf634b6075e24de96c3e53`
- **Processing hash:** `de69eb39c6f38b24f5780a8d6d8358570e0846a72b199cef74b5680fae299c32` | **metadata hash:** `c896e632c11edf044dfed9864e53eaaa012d966a5355b07f172c4781387af414`
