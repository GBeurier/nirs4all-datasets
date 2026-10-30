# Datasheet — UvA Figshare illicit-drugs Viavi MicroNIR averaged NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** UvA Figshare illicit-drugs Viavi MicroNIR averaged NIR. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 424 sample(s), 424 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Viavi MicroNIR averaged NIR | Viavi MicroNIR | NIR | 908.1–1676 nm | 424 | 125 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=424, missing=0, classes=83, top cocaine (×147) |
| set | target | categorical | *Not specified.* | n=424, missing=0, classes=7, top PAM (×104) |
| salt_form | target | categorical | *Not specified.* | n=424, missing=275, classes=4, top HCl (×121) |
| matrix | target | categorical | *Not specified.* | n=424, missing=0, classes=2, top powder (×353) |
| color | target | categorical | *Not specified.* | n=424, missing=0, classes=16, top white (×288) |
| instrument | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top Viavi MicroNIR (×424) |
| instrument_code | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top MicroNIR (×424) |
| api_url | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×424) |
| download_url | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×424) |
| article_url | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×424) |
| doi_dataset | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×424) |
| doi_publication | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×424) |
| license | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×424) |
| license_id | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top cc-by-4.0 (×424) |
| license_url | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×424) |
| rights_status | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top explicit_open (×424) |
| usage_scope | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top public_reuse_possible (×424) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top True (×424) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top NIR (×424) |
| axis_unit | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top nm (×424) |
| axis_min | metadata | numeric | *Not specified.* | n=424, missing=0, range 908.1–908.1, mean 908.1 ± 1.138e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=424, missing=0, range 1676–1676, mean 1676 ± 2.276e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=424, missing=0, range 125–125, mean 125 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top absorbance (×424) |
| decoder | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top pandas.read_excel/openpyxl (×424) |
| notes | metadata | categorical | *Not specified.* | n=424, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×424) |
| nr | metadata | numeric | *Not specified.* | n=424, missing=0, range 1–133, mean 49.34 ± 39.5 |
| other | metadata | categorical | *Not specified.* | n=424, missing=172, classes=124, top levamisole (×11) |

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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 4 fields, passport: 29 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `22fe5e8ceb192f5f97c4e395fcc2b9190ddd69aa832d80214a4d8af9860132fb`
- **Processing hash:** `325012b2b29eaa1d728a1426924623602e74d803fa38f945a2214b105fee50cf` | **metadata hash:** `5a8f12f9194be1a93d3e7187703d20ec1e72bf52f0202b41ab71ef98fbf0bceb`
