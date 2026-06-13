# Datasheet — boeuf_classe_adulteration_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** boeuf_classe_adulteration_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** observation level; 60 sample(s), 60 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 990–1895 none | 60 | 470 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| classe_adulteration | target | categorical | *Not specified.* | n=60, missing=0, classes=5, top 0 (×12) |
| ID_sample | metadata | categorical | *Not specified.* | n=60, missing=0, classes=60, top Beef_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Beef (×60) |
| product | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top boeuf (×60) |
| trait_header | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top classe_adulteration (×60) |
| trait_description | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Beef adulteration class (raw dataset codes). (×60) |
| split | metadata | categorical | *Not specified.* | n=60, missing=0, classes=2, top train (×30) |
| spectro | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top MIR / FTIR (×60) |
| raw_label | metadata | categorical | *Not specified.* | n=60, missing=0, classes=5, top 1 (×12) |
| reference_value | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–5, mean 3 ± 1.426 |
| class_index | metadata | categorical | *Not specified.* | n=60, missing=0, classes=5, top 0 (×12) |
| dimensions | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=60, missing=0, range 470–470, mean 470 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Publication source: all absorbance spectra were truncated to 990-1895 cm^-1; linear axis reconstructed here in decreasing order 1895->990 over 470 variables. (×60) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 30, test: 30

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Beef.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Beef`
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
- **Content hash:** `5fd813dc2c1ea392f5293a55a30631f024a5c2f4a6889a06794aa38a60945f24`
- **Processing hash:** `f95a8b543e596d08b9ab9be00e54e7c00e3173ea35ce57143cb44cf26a44ad60` | **metadata hash:** `6dc36041af95718d19766068839dc6eb5ef66d4cb1229edcfc7fdf0f3f4f16a0`
