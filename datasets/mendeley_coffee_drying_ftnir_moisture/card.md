# Datasheet — Mendeley coffee drying FT-NIR moisture

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley coffee drying FT-NIR moisture. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Fourier Transform Near Infrared (FT-NIR) spectral monitoring of parchment coffee beans during drying

## Composition

- **Alignment:** sample level; 20 sample(s), 73 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–5 (mean 3.65).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | FT-NIR spectra | FT-NIR spectrometer | NIR | 4000–1.2e+04 cm-1 | 73 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Moisture_WB | target | numeric | *Not specified.* | n=73, missing=0, range 8.5–52.49, mean 32.29 ± 17.63 |
| sample_group | metadata | categorical | *Not specified.* | n=73, missing=0, classes=20, top M 10 (×5) |
| replicate | metadata | numeric | *Not specified.* | n=73, missing=0, range 1–5, mean 2.438 ± 1.178 |
| api_url | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/snapshot/1 (×73) |
| files_api_url | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/files?folder_id=root&version=1&$start=0&$limit=1000 (×73) |
| doi_dataset | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top 10.17632/7c6gx7rr6d.1 (×73) |
| license | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×73) |
| license_id | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top cc-by-4.0 (×73) |
| license_url | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×73) |
| rights_status | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top explicit_open (×73) |
| usage_scope | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top public_reuse_possible (×73) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top True (×73) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top FT-NIR (×73) |
| axis_unit | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top cm^-1 (×73) |
| axis_min | metadata | numeric | *Not specified.* | n=73, missing=0, range 1.2e+04–1.2e+04, mean 1.2e+04 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=73, missing=0, range 4000–4000, mean 4000 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=73, missing=0, range 2001–2001, mean 2001 ± 0 |
| moisture_standard_deviation | metadata | numeric | *Not specified.* | n=73, missing=0, range 0.1029–2.019, mean 0.5485 ± 0.463 |
| moisture_coefficient_of_variation_pct | metadata | numeric | *Not specified.* | n=73, missing=0, range 0.2026–4.11, mean 2.009 ± 1.138 |
| notes | metadata | categorical | *Not specified.* | n=73, missing=0, classes=1, top Unprocessed FT-NIR spectra of parchment coffee during drying, sample columns without moisture target were excluded from X/Y/M. (×73) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/7c6gx7rr6d/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: 20 groups M 1…M 20 aligned with moisture references; 1–5 indexed spectra per group, 73 in total. The converter explicitly treats the suffix as a replicate. Whether it is strictly technical rather than an independent preparation remains undocumented.
- **Curated views:** M: 1 fields, Y: 1 fields, measurements: 2 fields, passport: 21 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `c3b77c320d1e2ebb12e900b661d4c54e0866f5cd0b9f54da4371157e2e9cbdfa`
- **Processing hash:** `d690212cdb28b7874295a8b24fcc3ecfe8efa14d820bb64d08707476f32b8cce` | **metadata hash:** `6a0790012b5b20e186efa7689ab6fa59e5162309942297fe2c72ae3760628d0a`
