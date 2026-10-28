# Datasheet — Dryad tree tissue nonstructural carbohydrates NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad tree tissue nonstructural carbohydrates NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 1270 sample(s), 1270 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad tree tissue nonstructural carbohydrates NIR | *Not specified.* | NIR | 1–1154 index | 1270 | 1154 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TG*10 | target | numeric | *Not specified.* | n=1270, missing=1090, range 80.9–148.9, mean 112 ± 20.59 |
| Sugars | target | numeric | *Not specified.* | n=1270, missing=1090, range 0–10.13, mean 2.345 ± 2.103 |
| Starch | target | numeric | *Not specified.* | n=1270, missing=1090, range 0–17.87, mean 3.784 ± 3.448 |
| NSC | target | numeric | *Not specified.* | n=1270, missing=1090, range 0.1682–20.09, mean 6.125 ± 4.191 |
| analysis_date | metadata | categorical | *Not specified.* | n=1270, missing=1, classes=15, top january 31 2014 (×128) |
| tissue | metadata | categorical | *Not specified.* | n=1270, missing=1, classes=4, top root (×357) |
| site | metadata | categorical | *Not specified.* | n=1270, missing=1, classes=5, top Mont-Saint-Hilaire, Quebec (×647) |
| species | metadata | categorical | *Not specified.* | n=1270, missing=1, classes=85, top Betula alleghaniensis (×64) |
| time | metadata | numeric | *Not specified.* | n=1270, missing=17, range 0–2, mean 0.8228 ± 0.8301 |
| nsc_probe | metadata | categorical | *Not specified.* | n=1270, missing=1090, classes=180, top 111_2 (×1) |
| nsc_tissue | metadata | categorical | *Not specified.* | n=1270, missing=1090, classes=4, top leaves (×61) |
| nsc_place | metadata | categorical | *Not specified.* | n=1270, missing=1090, classes=4, top Temperate forest (×67) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.jd2cb`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Manual download preserved as provenance; public reuse follows source Dryad dataset terms.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `54ddbb4dce4278d40a4a1550d99466bd35ab3ad12219523a71e9cfc6d65b4a92`
- **Processing hash:** `ac1cf76d147e111c5b9cdfdd38ffd522be9efe4a4552833b4399739e7cea5838` | **metadata hash:** `c5d4daf34048b9ad13c18e2d84d55e9d1c2308f1e4faac98461f6543ced338ed`
