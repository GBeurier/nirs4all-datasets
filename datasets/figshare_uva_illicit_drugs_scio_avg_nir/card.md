# Datasheet — UvA Figshare illicit-drugs Consumer Physics SCiO averaged NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** UvA Figshare illicit-drugs Consumer Physics SCiO averaged NIR. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 419 sample(s), 419 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Consumer Physics SCiO averaged NIR | Consumer Physics SCiO | NIR | 740–1070 nm | 419 | 331 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=419, missing=91, classes=69, top cocaine (×89) |
| set | target | categorical | *Not specified.* | n=419, missing=91, classes=7, top PAM (×92) |
| salt_form | target | categorical | *Not specified.* | n=419, missing=346, classes=4, top HCl (×54) |
| matrix | target | categorical | *Not specified.* | n=419, missing=91, classes=4, top powder (×256) |
| color | target | categorical | *Not specified.* | n=419, missing=92, classes=17, top white (×190) |
| instrument | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top Consumer Physics SCiO (×419) |
| instrument_code | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top Scio (×419) |
| api_url | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×419) |
| download_url | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×419) |
| article_url | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×419) |
| doi_dataset | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×419) |
| doi_publication | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×419) |
| license | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×419) |
| license_id | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top cc-by-4.0 (×419) |
| license_url | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×419) |
| rights_status | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top explicit_open (×419) |
| usage_scope | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top public_reuse_possible (×419) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top True (×419) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top NIR (×419) |
| axis_unit | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top nm (×419) |
| axis_min | metadata | numeric | *Not specified.* | n=419, missing=0, range 740–740, mean 740 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=419, missing=0, range 1070–1070, mean 1070 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=419, missing=0, range 331–331, mean 331 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top raw spectral data (×419) |
| decoder | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top pandas.read_excel/openpyxl (×419) |
| notes | metadata | categorical | *Not specified.* | n=419, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×419) |
| nr | metadata | numeric | *Not specified.* | n=419, missing=91, range 0–200, mean 77.75 ± 60.72 |
| other | metadata | categorical | *Not specified.* | n=419, missing=226, classes=78, top levamisole (×11) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://uvaauas.figshare.com/articles/dataset/Dataset_of_Near-Infrared_Spectral_Data_of_Illicit-Drugs_and_Forensic_Casework_Samples_Analyzed_by_Five_Portable_Spectrometers_Operating_in_Different_Wavelength_Ranges/21252300`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/21252300`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `faa99162bc90f4169a1f08a32386216a5186b015b7087ca51a141e5eb12586a2`
- **Processing hash:** `2080254cb52013727bbb923bef98d6816bbd178708a29366c476d9665f823b63` | **metadata hash:** `9575487f657a98df11980c8a69cd699d4879db4d217f249f4aef8cbc5d6e7826`
