# Datasheet — Tree leaf girdling reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Tree leaf girdling reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD tree leaf

## Composition

- **Alignment:** sample level; 2731 sample(s), 2731 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2731 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| treatment | target | categorical | *Not specified.* | n=2731, missing=0, classes=2, top control (×1557) |
| leaf_code | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=2722, top 'GRD-T1477-MAC01-L500000.asd.txt' (×2) |
| camera | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=5, top Cam02 (×700) |
| manual_download | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=1, top True (×2731) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\tree leaf (×2731) |
| manual_download_file | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=1, top doi_10_5061_dryad_d51c5b01n__v20201112.zip::*_spectra.xlsx (×2731) |
| official_source_url | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.d51c5b01n (×2731) |
| standardization_batch | metadata | categorical | *Not specified.* | n=2731, missing=0, classes=1, top v0.8.58 (×2731) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.d51c5b01n`
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
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `f53f0e23866cb7f562c5e1da0fc7bbb311513fcdae9864af3a8fc54495d0da8d`
- **Processing hash:** `1aed96204c8fad2b359e0142601dd891688b0ce87529b072f062e21840d225df` | **metadata hash:** `8a8e0d45809023c055ec7967e338bf87f44390c11fa6566a2e58b67e8a8ec40b`
