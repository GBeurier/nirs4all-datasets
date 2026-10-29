# Datasheet — Tree leaf girdling reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Tree leaf girdling reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD tree leaf

## Composition

- **Alignment:** sample level; 2722 sample(s), 2731 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.003).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2731 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| treatment | target | categorical | *Not specified.* | n=2722, missing=0, classes=2, top control (×1551) |
| leaf_code | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=2722, top CON_001_JAN21_L100000 (×1) |
| camera | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=5, top Cam02 (×700) |
| manual_download | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top True (×2722) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\tree leaf (×2722) |
| manual_download_file | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top doi_10_5061_dryad_d51c5b01n__v20201112.zip::*_spectra.xlsx (×2722) |
| official_source_url | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.d51c5b01n (×2722) |
| standardization_batch | metadata | categorical | *Not specified.* | n=2722, missing=0, classes=1, top v0.8.58 (×2722) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.d51c5b01n`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.; Curation identity contract: 2722 codes sources pour 2731 lignes. Les 9 codes répétés ont chacun deux vecteurs spectraux strictement identiques ; ce ne sont pas des réacquisitions démontrées. Aucun retrait de ligne dans les sources.
- **Curated views:** M: 1 fields, Y: 1 fields, measurements: 0 fields, passport: 8 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `cab3a3eefbc30909366a8d5ef5a60968a4522b1055e161a72c2dfd9aa24d07b6`
- **Processing hash:** `ec7626759c3e25f39accd19ac933fe436c85a046e4d27a8fbdb9bba94382f736` | **metadata hash:** `65762de220571e90eb9ac8142bde579e7d058cb743b727ba4ebda2f7a98f2651`
