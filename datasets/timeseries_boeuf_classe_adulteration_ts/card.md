# Datasheet — Beef — meat spectra (UCR/UEA)

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
| source_zip | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top https://www.timeseriesclassification.com/aeon-toolkit/Beef.zip (×60) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 30, train: 30

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Beef.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Beef`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 21 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `a4c87ab9ca50a0882b402540a715a60848b814b22f7b15ea9943cbbc1d172fd9`
- **Processing hash:** `55868fecefcfb38acad583cbee15af64955a45668745e086a970dff3134d163b` | **metadata hash:** `e8228e0c88df187ab818e5af004bcc3e835d14c54cb6e90b8c3e39c248a09e1b`
