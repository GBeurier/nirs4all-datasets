# Datasheet — puree_fraise_authenticite_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** puree_fraise_authenticite_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** observation level; 983 sample(s), 983 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 400–4000 none | 983 | 235 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| authenticite | target | numeric | *Not specified.* | n=983, missing=0, range 0–1, mean 0.6429 ± 0.4794 |
| ID_sample | metadata | categorical | *Not specified.* | n=983, missing=0, classes=983, top Strawberry_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=983, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top Strawberry (×983) |
| product | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top puree_fraise (×983) |
| trait_header | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top authenticite (×983) |
| trait_description | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top Authentique vs non-fraise/adultere (codes bruts du dataset). (×983) |
| split | metadata | categorical | *Not specified.* | n=983, missing=0, classes=2, top train (×613) |
| spectro | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top FTIR-ATR (×983) |
| raw_label | metadata | categorical | *Not specified.* | n=983, missing=0, classes=2, top 2 (×632) |
| reference_value | metadata | numeric | *Not specified.* | n=983, missing=0, range 1–2, mean 1.643 ± 0.4794 |
| class_index | metadata | categorical | *Not specified.* | n=983, missing=0, classes=2, top 1 (×632) |
| dimensions | metadata | numeric | *Not specified.* | n=983, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=983, missing=0, range 235–235, mean 235 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top Publication source: spectres enregistres sur 400-4000 cm^-1, le dataset exporte contient 235 variables, donc un axe lineaire interpole est applique ici en ordre decroissant 4000->400. (×983) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 613, test: 370

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Strawberry.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Strawberry`
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
- **Content hash:** `07da8d32a48caa45bbe16af3aca0f99734b76b4a2c93112a9d54cf3ba7cd0f78`
- **Processing hash:** `deb102adccd5ad454c358e23e06c6503676d0d596a2b9a26918ab154271678a5` | **metadata hash:** `b0fd1116a49140327bfbb1ecdc970251283131e1633ec2f8879c03be73541fa0`
