# Datasheet — UvA Figshare illicit-drugs ASD FieldSpec averaged NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** figshare
- **Description:** UvA Figshare illicit-drugs ASD FieldSpec averaged NIR. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, figshare
- **Contributor:** Dataset of Near-Infrared Spectral Data of Illicit-Drugs and Forensic Casework Samples

## Composition

- **Alignment:** sample level; 390 sample(s), 390 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ASD FieldSpec averaged NIR | ASD FieldSpec | NIR | 350–2500 nm | 390 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| component | target | categorical | *Not specified.* | n=390, missing=1, classes=69, top cocaine (×144) |
| set | target | categorical | *Not specified.* | n=390, missing=1, classes=7, top PAM (×104) |
| salt_form | target | categorical | *Not specified.* | n=390, missing=247, classes=4, top HCl (×118) |
| matrix | target | categorical | *Not specified.* | n=390, missing=1, classes=3, top powder (×317) |
| color | target | categorical | *Not specified.* | n=390, missing=2, classes=16, top white (×251) |
| instrument | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top ASD FieldSpec (×390) |
| instrument_code | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top ASD (×390) |
| api_url | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top https://api.figshare.com/v2/articles/21252300 (×390) |
| download_url | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top https://ndownloader.figshare.com/files/37664664 (×390) |
| article_url | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922008654 (×390) |
| doi_dataset | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top 10.21942/uva.21252300.v2 (×390) |
| doi_publication | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top 10.1016/j.dib.2022.108660 (×390) |
| license | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×390) |
| license_id | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top cc-by-4.0 (×390) |
| license_url | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×390) |
| rights_status | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top explicit_open (×390) |
| usage_scope | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top public_reuse_possible (×390) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top True (×390) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top NIR (×390) |
| axis_unit | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top nm (×390) |
| axis_min | metadata | numeric | *Not specified.* | n=390, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=390, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=390, missing=0, range 2151–2151, mean 2151 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top absorbance (×390) |
| decoder | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top pandas.read_excel/openpyxl (×390) |
| notes | metadata | categorical | *Not specified.* | n=390, missing=0, classes=1, top Averaged-per-sample Excel files from Figshare ZIP, raw replicate files retained in ZIP but not exported in this standardized pass. (×390) |
| nr | metadata | numeric | *Not specified.* | n=390, missing=1, range 0–133, mean 52.08 ± 40.01 |
| other | metadata | categorical | *Not specified.* | n=390, missing=138, classes=124, top levamisole (×11) |

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
- **Content hash:** `09d13b13cd8c77ca3f86dd8c815582d48ce1065e5051cba202c8b6728987b28e`
- **Processing hash:** `162e4d7cfba3ad946b99870856dec028fab1a82f9d1d2c8775b2e2fe2b72aab7` | **metadata hash:** `8d717f785e9968da14c6cf5c157f5b6ac0385547d33c119632ce616a28716b75`
