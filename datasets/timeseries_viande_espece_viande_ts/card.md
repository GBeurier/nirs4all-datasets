# Datasheet — viande_espece_viande_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** viande_espece_viande_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 120 sample(s), 120 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 1000–1800 none | 120 | 448 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| espece_viande | target | numeric | *Not specified.* | n=120, missing=0, range 0–2, mean 1 ± 0.8199 |
| ID_sample | metadata | categorical | *Not specified.* | n=120, missing=0, classes=120, top Meat_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=120, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top Meat (×120) |
| product | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top viande (×120) |
| trait_header | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top espece_viande (×120) |
| trait_description | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top Espece de viande (chicken / pork / turkey, codes bruts du dataset). (×120) |
| split | metadata | categorical | *Not specified.* | n=120, missing=0, classes=2, top train (×60) |
| spectro | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top FTIR-ATR (×120) |
| raw_label | metadata | categorical | *Not specified.* | n=120, missing=0, classes=3, top 1 (×40) |
| reference_value | metadata | numeric | *Not specified.* | n=120, missing=0, range 1–3, mean 2 ± 0.8199 |
| class_index | metadata | categorical | *Not specified.* | n=120, missing=0, classes=3, top 0 (×40) |
| dimensions | metadata | numeric | *Not specified.* | n=120, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=120, missing=0, range 448–448, mean 448 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=120, missing=0, classes=1, top Publication source: spectres MIR-ATR acquis sur 800-4000 cm^-1 puis tronques sur 1000-1800 cm^-1, axe lineaire reconstruit ici en ordre decroissant 1800->1000 sur 448 variables. (×120) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 60, train: 60

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Meat.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Meat`
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
- **Content hash:** `6ef0b09913f7b5b1ef9c563a47ff85dc7d6a08fcf5a5335e2501820354fe6321`
- **Processing hash:** `ea9f7c2b50d629b94382bef59e2e4fcbe9cffc50439f1bf5482a66d8e0255d25` | **metadata hash:** `eb6088d57d9533441b70b3e692f65f4be2490d3391393a34e0a40b9e609cf37f`
