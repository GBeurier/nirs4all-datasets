# Datasheet — boeuf_classe_adulteration_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** boeuf_classe_adulteration_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 60 sample(s), 60 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
| trait_description | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Classe d'adulteration du boeuf (codes bruts du dataset). (×60) |
| split | metadata | categorical | *Not specified.* | n=60, missing=0, classes=2, top train (×30) |
| spectro | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top MIR / FTIR (×60) |
| raw_label | metadata | categorical | *Not specified.* | n=60, missing=0, classes=5, top 1 (×12) |
| reference_value | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–5, mean 3 ± 1.426 |
| class_index | metadata | categorical | *Not specified.* | n=60, missing=0, classes=5, top 0 (×12) |
| dimensions | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=60, missing=0, range 470–470, mean 470 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Publication source: tous les spectres d'absorbance ont ete tronques sur 990-1895 cm^-1, axe lineaire reconstruit ici en ordre decroissant 1895->990 sur 470 variables. (×60) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 30, train: 30

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Beef.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Beef`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 21 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `95a7c320c336d6dfc466d3710febeeec71a17a642b2f70984328c6cda18e0e07`
- **Processing hash:** `f061b9177e9e7d2ccd22143c2b58a65ac77c17054aa2d46418efaa172b3276fb` | **metadata hash:** `5d60880b2dec23161383650a3f3b57b4b0e162dd37d3ebb2d1c1103b8afc1d47`
