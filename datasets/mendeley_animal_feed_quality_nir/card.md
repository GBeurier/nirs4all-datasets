# Datasheet — Mendeley animal feed quality NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley animal feed quality NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Near infrared spectral Dataset of Animal Feed

## Composition

- **Alignment:** sample level; 25 sample(s), 25 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NIR spectra | *Not specified.* | NIR | 999.9–2500 nm | 25 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| IVOMD | target | numeric | *Not specified.* | n=25, missing=0, range 50.34–64.58, mean 56.5 ± 4.014 |
| IVDMD | target | numeric | *Not specified.* | n=25, missing=0, range 48.56–60.36, mean 54.14 ± 3.335 |
| NDF | target | numeric | *Not specified.* | n=25, missing=0, range 22.1–49.77, mean 27.36 ± 5.961 |
| ADF | target | numeric | *Not specified.* | n=25, missing=0, range 15.3–18.95, mean 17.48 ± 0.9589 |
| api_url | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/r6fjtx943d/snapshot/1 (×25) |
| files_api_url | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/r6fjtx943d/files?folder_id=root&version=1&$start=0&$limit=1000 (×25) |
| doi_dataset | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top 10.17632/r6fjtx943d.1 (×25) |
| license | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×25) |
| license_id | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top cc-by-4.0 (×25) |
| license_url | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×25) |
| rights_status | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top explicit_open (×25) |
| usage_scope | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top public_reuse_possible (×25) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top True (×25) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top NIR (×25) |
| axis_unit | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top nm (×25) |
| axis_min | metadata | numeric | *Not specified.* | n=25, missing=0, range 999.9–999.9, mean 999.9 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=25, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=25, missing=0, range 1557–1557, mean 1557 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=25, missing=0, classes=1, top NIR spectra of animal feed samples with IVOMD, IVDMD, NDF and ADF quality parameters. (×25) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/r6fjtx943d/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/r6fjtx943d/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/r6fjtx943d/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 4 fields, measurements: 0 fields, passport: 20 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Mendeley Data record is licensed CC BY 4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `ce76bf58f02b3a1ad568937fe2389c0421cd0e184c6031c5b724c50e3b0efa95`
- **Processing hash:** `66fb06664c54c801c684fa3908dd13c34d24482555e215e07e0ce74fabd3e0d4` | **metadata hash:** `8718522ebc1eb3d627a9f8bb94731038c81c827d19146ad3081152e5e77e77d6`
