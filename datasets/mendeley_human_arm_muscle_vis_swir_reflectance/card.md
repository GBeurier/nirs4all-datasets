# Datasheet — Mendeley human arm muscle Vis-SWIR reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley human arm muscle Vis-SWIR reflectance. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** A dataset of Visible - Short Wave InfraRed reflectance spectra collected in-vivo on the dorsal and ventral aspect of arms

## Composition

- **Alignment:** sample level; 40 sample(s), 2000 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 50–50 (mean 50).
- **Documented technical repetitions:** 50.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | reflectance | ASD FieldSpec 4 Standard-Res | MIR | 450–2500 nm | 2000 | 2051 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| muscle_class | target | categorical | *Not specified.* | n=2000, missing=0, classes=2, top Biceps (×1000) |
| arm_aspect | target | categorical | *Not specified.* | n=2000, missing=0, classes=2, top ventral_arm (×1000) |
| subject_id | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=20, top S1 (×100) |
| arm_aspect_code | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=2, top B (×1000) |
| replicate_index_within_subject_aspect | metadata | numeric | *Not specified.* | n=2000, missing=0, range 1–50, mean 25.5 ± 14.43 |
| age_years | metadata | numeric | *Not specified.* | n=2000, missing=0, range 24–89, mean 58.85 ± 18.25 |
| sex_code | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=2, top 0 (×1100) |
| weight_kg | metadata | numeric | *Not specified.* | n=2000, missing=0, range 50–97, mean 75.1 ± 11.38 |
| height_cm | metadata | numeric | *Not specified.* | n=2000, missing=0, range 160–191, mean 170.4 ± 7.555 |
| bmi | metadata | numeric | *Not specified.* | n=2000, missing=0, range 19.53–33.56, mean 25.82 ± 3.448 |
| sex_label | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=2, top male (×1100) |
| metadata_source_file | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top Table.csv (×2000) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top 10.17632/24pg3ywxs5.1 (×2000) |
| article_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340920313627 (×2000) |
| pmc_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://pmc.ncbi.nlm.nih.gov/articles/PMC7683223/ (×2000) |
| doi_publication | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top 10.1016/j.dib.2020.106480 (×2000) |
| related_article | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://doi.org/10.1038/s41598-019-44896-8 (×2000) |
| license | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×2000) |
| license_id | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top cc-by-4.0 (×2000) |
| license_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top http://creativecommons.org/licenses/by/4.0 (×2000) |
| rights_status | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top explicit_open (×2000) |
| usage_scope | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top public_reuse_possible (×2000) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top True (×2000) |
| instrument_name | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top ASD FieldSpec 4 Standard-Res (×2000) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top Vis-SWIR (×2000) |
| signal_type | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top reflectance (×2000) |
| axis_unit | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top nm (×2000) |
| axis_min | metadata | numeric | *Not specified.* | n=2000, missing=0, range 450–450, mean 450 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2000, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2000, missing=0, range 2051–2051, mean 2051 ± 0 |
| decoder | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top pandas.read_csv for Eigenvector DataSet Object CSV export, matio.whosmat inspected MATLAB source (×2000) |
| notes | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top No direct personal identifiers, subject IDs are source pseudonyms S1-S20. (×2000) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/24pg3ywxs5/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://pmc.ncbi.nlm.nih.gov/articles/PMC7683223/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `http://creativecommons.org/licenses/by/4.0`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: 20 sujets, 40 unités sujet × face, 50 spectres chacune. Le suffixe de scan du sample_id exporté est retiré uniquement pour ce contrat vérifié.
- **Curated views:** M: 5 fields, Y: 2 fields, passport: 31 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Mendeley public API reports dataset license CC BY 4.0. Article page is CC BY-NC-ND, but repository dataset license is CC BY 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `885348b13af4d48f0d3a06e31751bab7097daf09160e504134fa93dc54864efa`
- **Processing hash:** `6397e123d962068f0208d5bc2553c1927b2c0733f9dbbfbb1a2db27222ae4df3` | **metadata hash:** `610f3f04d9142093d0d5c72fcb61e6c677fecbbf40eed316c24018d4afdaa551`
