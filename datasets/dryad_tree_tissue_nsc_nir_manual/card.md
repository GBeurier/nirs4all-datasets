# Datasheet — Tree tissues — nonstructural carbohydrates, NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad tree tissue nonstructural carbohydrates NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 180 sample(s), 180 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad tree tissue nonstructural carbohydrates NIR | *Not specified.* | NIR | 1–1154 index | 180 | 1154 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TG*10 | target | numeric | *Not specified.* | n=180, missing=0, range 80.9–148.9, mean 112 ± 20.59 |
| Sugars | target | numeric | *Not specified.* | n=180, missing=0, range 0–10.13, mean 2.345 ± 2.103 |
| Starch | target | numeric | *Not specified.* | n=180, missing=0, range 0–17.87, mean 3.784 ± 3.448 |
| NSC | target | numeric | *Not specified.* | n=180, missing=0, range 0.1682–20.09, mean 6.125 ± 4.191 |
| analysis_date | metadata | categorical | *Not specified.* | n=180, missing=0, classes=15, top january 20 2014 (×26) |
| tissue | metadata | categorical | *Not specified.* | n=180, missing=0, classes=4, top leaves (×61) |
| site | metadata | categorical | *Not specified.* | n=180, missing=0, classes=5, top Mont-Saint-Hilaire, Quebec (×61) |
| species | metadata | categorical | *Not specified.* | n=180, missing=0, classes=73, top Juglans cinerea (×9) |
| time | metadata | numeric | *Not specified.* | n=180, missing=3, range 0–2, mean 0.5367 ± 0.7687 |
| nsc_probe | metadata | categorical | *Not specified.* | n=180, missing=0, classes=180, top 111_2 (×1) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\tree tissue (×180) |
| manual_download_file | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top spectra_data.csv \| NSC_data.csv \| info_samples.csv (×180) |
| official_source_url | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.jd2cb (×180) |
| manual_download | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top True (×180) |
| source_sample_id | metadata | categorical | *Not specified.* | n=180, missing=0, classes=180, top 631B2 (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.jd2cb`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 5 fields, Y: 4 fields, measurements: 1 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `e3785ca8a285cab3540f7c3640e4b8f790ef4c937d1d815fd115ec66279d2319`
- **Processing hash:** `1bd62b0d65762e9e17de76ce8658d68a248f99990bd2ad618fce2867857a294a` | **metadata hash:** `d1b70306a3701a6e872a52398b0624460bf71e86b7c9d4b0e1c34b4ce75debf6`
