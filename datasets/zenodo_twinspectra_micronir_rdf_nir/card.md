# Datasheet — Zenodo TwinSpectra microNIR RDF NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo TwinSpectra microNIR RDF NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** TwinSpectra Dataset

## Composition

- **Alignment:** sample level; 720 sample(s), 720 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Viavi microNIR | Viavi microNIR | NIR | 908.1–1676 nm | 720 | 125 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| group | target | categorical | *Not specified.* | n=720, missing=0, classes=6, top PC (×120) |
| file_url | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top https://zenodo.org/api/records/18471662/files/measurements_125.csv/content (×720) |
| article_url | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340926004713 (×720) |
| doi_dataset | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top 10.5281/zenodo.18471662 (×720) |
| doi_publication | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top 10.1016/j.dib.2026.112920 (×720) |
| license | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×720) |
| license_id | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top cc-by-4.0 (×720) |
| license_url | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×720) |
| rights_status | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top explicit_open (×720) |
| usage_scope | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top public_reuse_possible (×720) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top True (×720) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top NIR (×720) |
| axis_unit | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top nm (×720) |
| axis_min | metadata | numeric | *Not specified.* | n=720, missing=0, range 908.1–908.1, mean 908.1 ± 1.138e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=720, missing=0, range 1676–1676, mean 1676 ± 2.275e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=720, missing=0, range 125–125, mean 125 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=720, missing=0, classes=1, top Refuse-derived fuel particle spectra with class labels and predefined subset folds. (×720) |
| id | metadata | categorical | *Not specified.* | n=720, missing=0, classes=360, top 302 (×2) |
| sample | metadata | numeric | *Not specified.* | n=720, missing=0, range 0–719, mean 359.5 ± 208 |
| fold | metadata | numeric | *Not specified.* | n=720, missing=0, range 0–4, mean 2 ± 1.415 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/18471662`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/18471662/files/measurements_125.csv/content`
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
- **Content hash:** `615e1b09c24dcbfe76eab1628031f5ec35381a0a2c0a770fead7907f338bf9b2`
- **Processing hash:** `4866f70e1b4fdd389b66a6403d9d715dc86eb101eb4ba4f9546df9735b43ec34` | **metadata hash:** `57311eda5eb5a407fe8ec9071272867850b3ba43d343c9d06592ad3820faaeab`
