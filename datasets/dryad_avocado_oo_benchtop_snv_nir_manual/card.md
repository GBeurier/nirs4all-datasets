# Datasheet — Dryad Hawaii avocado bench-top SNV NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad Hawaii avocado bench-top SNV NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 199 sample(s), 199 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad Hawaii avocado bench-top SNV NIR | *Not specified.* | NIR | 1000–2400 nm | 199 | 445 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Variety | target | categorical | *Not specified.* | n=199, missing=0, classes=3, top Sharwil (×115) |
| variety | metadata | categorical | *Not specified.* | n=199, missing=0, classes=3, top Sharwil (×115) |
| instrument_context | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top bench_top_NIRQuest_2022_SNV (×199) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\advocado (×199) |
| manual_download_file | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top OO_All199_ave_SNV.xlsx (×199) |
| official_source_url | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.98sf7m0rj (×199) |
| manual_download | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top True (×199) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.98sf7m0rj`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `7e4d415ba906d1b85f2d42880e65dc763e86234c84c699c044f494515ebe9a44`
- **Processing hash:** `7a2c5face65100616fd6fee78c161ab8790053032889bf7623d3f42e2a6cc076` | **metadata hash:** `4d51973506d6af791a85241c0960e8293d270bc9bec8b1277bc242db20c40699`
