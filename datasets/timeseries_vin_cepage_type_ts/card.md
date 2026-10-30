# Datasheet — vin_cepage_type_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** vin_cepage_type_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 111 sample(s), 111 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
| trait_description | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top Type de vin (Cabernet Sauvignon vs Shiraz, codes bruts du dataset). (×111) |
| split | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top train (×57) |
| spectro | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top FTIR-ATR (×111) |
| raw_label | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top 1 (×57) |
| reference_value | metadata | numeric | *Not specified.* | n=111, missing=0, range 1–2, mean 1.486 ± 0.5021 |
| class_index | metadata | categorical | *Not specified.* | n=111, missing=0, classes=2, top 0 (×57) |
| dimensions | metadata | numeric | *Not specified.* | n=111, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=111, missing=0, range 234–234, mean 234 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=111, missing=0, classes=1, top Hypothese utilisateur: meme convention spectrale que Strawberry, axe lineaire interpole applique ici en ordre decroissant 4000->400 sur 234 variables. (×111) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 57, test: 54

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Wine.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Wine`
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
- **Content hash:** `cbe59cf2c9c175969d47ea838d618e8ba8428ed8cb6bb34cbde6136e317f836c`
- **Processing hash:** `e4ab9f43d78add5f1d3a2a2046433cd27c0207354bd340ab31e417f632ac444c` | **metadata hash:** `a2ad440c3b521bf64dd1c2b9303c208275905348cdfd4404abeb7ad7ae3abcfe`
