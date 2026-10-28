# Datasheet — Mendeley black PMMA transmissivity UV-Vis-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley black PMMA transmissivity UV-Vis-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Spectral radiative properties of black PMMA

## Composition

- **Alignment:** observation level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | black PMMA UV-Vis-NIR transmissivity | *Not specified.* | NIR | 0.25–2.6 none | 2 | 2351 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_temperature_C | target | numeric | *Not specified.* | n=2, missing=0, range 50–73, mean 61.5 ± 16.26 |
| api_url | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/8wpgzrp33s/snapshot/1 (×2) |
| files_api_url | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/8wpgzrp33s/files?folder_id=root&version=1&$start=0&$limit=1000 (×2) |
| article_url | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922003079 (×2) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top 10.17632/8wpgzrp33s.1 (×2) |
| license | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×2) |
| license_id | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top cc-by-4.0 (×2) |
| license_url | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×2) |
| rights_status | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top explicit_open (×2) |
| usage_scope | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top public_reuse_possible (×2) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top True (×2) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top UV-Vis-NIR (×2) |
| axis_unit | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top um (×2) |
| axis_min | metadata | numeric | *Not specified.* | n=2, missing=0, range 0.25–0.25, mean 0.25 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2, missing=0, range 2.6–2.6, mean 2.6 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2, missing=0, range 2351–2351, mean 2351 ± 0 |
| measured_property | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Transmissivity_pct (×2) |
| notes | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top UV-Vis-NIR transmissivity subset of black PMMA spectral radiative properties, other optical property files remain in raw source. (×2) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/8wpgzrp33s/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/8wpgzrp33s/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/8wpgzrp33s/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'um' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `05eced625d48cccc66b163e0aca994eecd799cf53b862da4dfe59f1f50aa1c8b`
- **Processing hash:** `ddcc830403de1c4be1f3153400432433d0c904f3c9a927aeaf57f2b5cc95cb9f` | **metadata hash:** `160555cf6f5db069b51bae9fc27e941b9c8a495aa9efd3ea7731ad5f72f50446`
