# Datasheet — Zenodo TwinSpectra FieldSpec RDF NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo TwinSpectra FieldSpec RDF NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** TwinSpectra Dataset

## Composition

- **Alignment:** sample level; 718 sample(s), 718 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ASD FieldSpec 4 Hi-Res | ASD FieldSpec 4 Hi-Res | NIR | 350–2500 nm | 718 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| group | target | categorical | *Not specified.* | n=718, missing=0, classes=6, top Rubber (×120) |
| file_url | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top https://zenodo.org/api/records/18471662/files/measurements_2151.csv/content (×718) |
| article_url | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340926004713 (×718) |
| doi_dataset | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top 10.5281/zenodo.18471662 (×718) |
| doi_publication | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top 10.1016/j.dib.2026.112920 (×718) |
| license | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×718) |
| license_id | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top cc-by-4.0 (×718) |
| license_url | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×718) |
| rights_status | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top explicit_open (×718) |
| usage_scope | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top public_reuse_possible (×718) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top True (×718) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top NIR (×718) |
| axis_unit | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top nm (×718) |
| axis_min | metadata | numeric | *Not specified.* | n=718, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=718, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=718, missing=0, range 2151–2151, mean 2151 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=718, missing=0, classes=1, top Refuse-derived fuel particle spectra with class labels and predefined subset folds. (×718) |
| id | metadata | categorical | *Not specified.* | n=718, missing=0, classes=358, top 575 (×4) |
| sample | metadata | numeric | *Not specified.* | n=718, missing=0, range 9–777, mean 386.8 ± 220.6 |
| fold | metadata | numeric | *Not specified.* | n=718, missing=0, range 0–4, mean 1.996 ± 1.415 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/18471662`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/18471662/files/measurements_2151.csv/content`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 23 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `522e1dd353c60786bae170b8af037198b7a5b49fa170642f17a2f04133f4a4e3`
- **Processing hash:** `ab85a4bb57ac4057ae9993f65403e6ca397caa98b1946ee7cc0e468c282f2c4d` | **metadata hash:** `f718c5e7e06443a83456f8c33ccc4f8d4a247bed9dede27c07307b3cae2b0c33`
