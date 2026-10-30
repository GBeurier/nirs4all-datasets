# Datasheet — Zenodo NeoSpectra soil NIR CC-BY

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo NeoSpectra soil NIR CC-BY. v2.0 standardized NIRS package: 1 spectral source(s), 10 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** Near-infrared soil spectral library using NeoSpectra Handheld NIR Analyzer

## Composition

- **Alignment:** sample level; 7790 sample(s), 7790 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NeoSpectra handheld NIR | NeoSpectra Handheld NIR Analyzer | NIR | 1350–2550 nm | 7790 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=7790, missing=8, range 0.0176–53.88, mean 1.963 ± 3.135 |
| c_tot_usda_a622_w_pct | target | numeric | *Not specified.* | n=7790, missing=0, range 0.0161–53.88, mean 2.236 ± 3.17 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=7790, missing=0, range 0–3.02, mean 0.1614 ± 0.2023 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=7790, missing=0, range 0–76.97, mean 19.91 ± 13.99 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=7790, missing=0, range 0.3–100, mean 41.33 ± 28.52 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=7790, missing=0, range 0–87.9, mean 38.76 ± 20.63 |
| bd_usda_a4_g_cm3 | target | numeric | *Not specified.* | n=7790, missing=3633, range 0.2021–2.033, mean 1.316 ± 0.2428 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=7790, missing=0, range 3.69–9.52, mean 6.334 ± 1.279 |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=7790, missing=5085, range 0.00656–89.03, mean 6.593 ± 9.747 |
| k_ext_usda_a725_cmolc_kg | target | numeric | *Not specified.* | n=7790, missing=0, range 0–11.25, mean 0.5415 ± 0.6907 |
| api_url | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top https://zenodo.org/api/records/13122321 (×7790) |
| file_url | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top https://zenodo.org/api/records/13122321/files/1976_NSlibrary_withmetadata.csv/content (×7790) |
| doi_dataset | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top 10.5281/zenodo.13122321 (×7790) |
| doi_publication | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top 10.1016/j.dib.2024.111910 (×7790) |
| license | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×7790) |
| license_id | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top cc-by-4.0 (×7790) |
| license_url | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×7790) |
| rights_status | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top explicit_open (×7790) |
| usage_scope | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top public_reuse_possible (×7790) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top True (×7790) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top NIR (×7790) |
| axis_unit | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top nm (×7790) |
| axis_min | metadata | numeric | *Not specified.* | n=7790, missing=0, range 1350–1350, mean 1350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=7790, missing=0, range 2550–2550, mean 2550 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=7790, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top Zenodo CC-BY subset of NeoSpectra soil library, possible content overlap with broader OSSL NeoSpectra active datasets. (×7790) |
| id_layer_uuid_txt | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1976, top 88c49f7e0b6402f3d2b178ac225e6b2d (×19) |
| dataset_code_ascii_txt | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1, top Neospectra (×7790) |
| id_scan_local_c | metadata | categorical | *Not specified.* | n=7790, missing=0, classes=1976, top 115599 (×19) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/13122321`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/13122321/files/1976_NSlibrary_withmetadata.csv/content`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 10 fields, passport: 23 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `e90178b7788cbb2921bf2734042e5e1bdcf687bd86a8662e26b131391e09ab40`
- **Processing hash:** `41374d44afae2757cea2d8326752850254fddb2e5a534b1cc2cd1b8d01cd96fb` | **metadata hash:** `2b307fa83a3c2c6384366149591a9da32ff51a6fec66d8a00488532eff72dd2a`
