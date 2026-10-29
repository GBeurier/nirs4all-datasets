# Datasheet — Zenodo milk composition NIR transmittance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo milk composition NIR transmittance. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** Near-infrared spectra dataset of milk composition in transmittance mode

## Composition

- **Alignment:** sample level; 1224 sample(s), 1224 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | spectra | *Not specified.* | NIR | 960–1690 nm | 1224 | 256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Fat | target | numeric | *Not specified.* | n=1224, missing=0, range 1.54–7.6, mean 3.525 ± 0.8127 |
| Prot | target | numeric | *Not specified.* | n=1224, missing=0, range 2.63–4.34, mean 3.424 ± 0.3396 |
| Lact | target | numeric | *Not specified.* | n=1224, missing=0, range 3.98–5.1, mean 4.701 ± 0.1595 |
| SCC | target | numeric | *Not specified.* | n=1224, missing=0, range 5–3975, mean 178.7 ± 372.1 |
| Urea | target | numeric | *Not specified.* | n=1224, missing=0, range 9–44, mean 27.6 ± 5.398 |
| Milk_yield | target | numeric | *Not specified.* | n=1224, missing=0, range 6.16–27.77, mean 13.25 ± 3.374 |
| file_url | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top https://zenodo.org/api/records/8263430/files/data_table.csv/content (×1224) |
| article_url | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S235234092300834X (×1224) |
| doi_dataset | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top 10.5281/zenodo.8263430 (×1224) |
| doi_publication | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top 10.1016/j.dib.2023.109767 (×1224) |
| license | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×1224) |
| license_id | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top cc-by-4.0 (×1224) |
| license_url | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×1224) |
| rights_status | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top explicit_open (×1224) |
| usage_scope | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top public_reuse_possible (×1224) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top True (×1224) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top NIR (×1224) |
| axis_unit | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top nm (×1224) |
| axis_min | metadata | numeric | *Not specified.* | n=1224, missing=0, range 960–960, mean 960 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1690–1690, mean 1690 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1224, missing=0, range 256–256, mean 256 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=1, top Trans_Tot columns are the normalized transmittance spectra, raw dark, sample and white references remain in the source CSV. (×1224) |
| Cow_ID | metadata | categorical | *Not specified.* | n=1224, missing=0, classes=41, top 59130 (×55) |
| Milk_Interv | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1685–6.518e+04, mean 3.111e+04 ± 8299 |
| SET | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1–8, mean 4.065 ± 2.603 |
| Time_Dark | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1.496e+09–1.501e+09, mean 1.498e+09 ± 1.9e+06 |
| Time_Milk | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1.496e+09–1.501e+09, mean 1.498e+09 ± 1.9e+06 |
| Time_PrevMilk | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1.496e+09–1.501e+09, mean 1.498e+09 ± 1.899e+06 |
| Time_Sample | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1.496e+09–1.501e+09, mean 1.498e+09 ± 1.9e+06 |
| Time_White | metadata | numeric | *Not specified.* | n=1224, missing=0, range 1.496e+09–1.501e+09, mean 1.498e+09 ± 1.9e+06 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/8263430`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/8263430/files/data_table.csv/content`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 6 fields, Y: 6 fields, passport: 21 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `726713f76741ceca1c4bc7a12eb77af7a46959d5885ad7eb8c1dff646b830cb3`
- **Processing hash:** `5d4370756faa09d743f8789b3d29c9f40d554bc95752153a0c032e4b3fc99842` | **metadata hash:** `6e17727e298e854ae721eeab5f1b03ca5998dc1528b3468796a1c0c528b2003c`
