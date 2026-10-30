# Datasheet — cafe_instantane_espece_cafe_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** cafe_instantane_espece_cafe_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 56 sample(s), 56 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 800–1900 none | 56 | 286 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| espece_cafe | target | numeric | *Not specified.* | n=56, missing=0, range 0–1, mean 0.4821 ± 0.5042 |
| ID_sample | metadata | categorical | *Not specified.* | n=56, missing=0, classes=56, top Coffee_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=56, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top Coffee (×56) |
| product | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top cafe_instantane (×56) |
| trait_header | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top espece_cafe (×56) |
| trait_description | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top Espece de cafe (Arabica vs Robusta, codes bruts du dataset). (×56) |
| split | metadata | categorical | *Not specified.* | n=56, missing=0, classes=2, top train (×28) |
| spectro | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top MIR / FTIR (×56) |
| raw_label | metadata | categorical | *Not specified.* | n=56, missing=0, classes=2, top 0 (×29) |
| reference_value | metadata | numeric | *Not specified.* | n=56, missing=0, range 0–1, mean 0.4821 ± 0.5042 |
| class_index | metadata | categorical | *Not specified.* | n=56, missing=0, classes=2, top 0 (×29) |
| dimensions | metadata | numeric | *Not specified.* | n=56, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=56, missing=0, range 286–286, mean 286 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top Publication source: spectres DRIFT tronques sur 800-1900 cm^-1, axe lineaire reconstruit ici en ordre decroissant 1900->800 sur 286 variables. (×56) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 28, test: 28

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Coffee.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Coffee`
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
- **Content hash:** `3a7228bdcc74bcb39c448f889c8c8257787d02f61188b838778dc02902a82e0e`
- **Processing hash:** `5f95b995c3d1c6d3ef38a3c1d3b75939f0674e272491df9f07f951d37e3905de` | **metadata hash:** `46f56188691b8a736aa018f85042af2946b99797d33ec00bccd0f75ae6af44c9`
