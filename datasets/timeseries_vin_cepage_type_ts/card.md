# Datasheet — vin_cepage_type_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** vin_cepage_type_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** observation level; 111 sample(s), 111 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 400–4000 none | 111 | 234 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| cepage_type | target | categorical | *Not specified.* | n=111, missing=0, classes=2, top 0 (×57) |
| ID_sample | metadata | categorical | *Not specified.* | n=111, missing=0, classes=111, top Wine_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=111, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top Wine (×111) |
| product | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top vin (×111) |
| trait_header | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top cepage_type (×111) |
| trait_description | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top Wine type (Cabernet Sauvignon vs Shiraz, raw dataset codes). (×111) |
| split | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top train (×57) |
| spectro | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top FTIR-ATR (×111) |
| raw_label | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top 1 (×57) |
| reference_value | metadata | numeric | *Not specified.* | n=111, missing=0, range 1–2, mean 1.486 ± 0.5021 |
| class_index | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top 0 (×57) |
| dimensions | metadata | numeric | *Not specified.* | n=111, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=111, missing=0, range 234–234, mean 234 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top User hypothesis: same spectral convention as Strawberry; interpolated linear axis applied here in decreasing order 4000->400 over 234 variables. (×111) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 57, test: 54

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Wine.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Wine`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Recovered from local initial-source exports; rights not cleared for redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `f1b7f6ef8c9cb679a035f2fe82088526ca5ef2d89fe5ebff142451ea7f786c68`
- **Processing hash:** `78826f045fad9b65a8b70cf6d2388aa91bd76c3fe2f2afb70d3ae42300d7a25e` | **metadata hash:** `42daa3bae145eda04fd90cf177dc589419f3e12123bf04dad307af9930004fa4`
