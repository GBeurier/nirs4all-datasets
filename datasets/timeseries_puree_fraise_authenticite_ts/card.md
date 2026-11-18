# Datasheet — Strawberry — puree spectra (UCR/UEA)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** puree_fraise_authenticite_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 983 sample(s), 983 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | MIR | 400–4000 none | 983 | 235 |

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
| source_zip | metadata | categorical | *Not specified.* | n=983, missing=0, classes=1, top https://www.timeseriesclassification.com/aeon-toolkit/Strawberry.zip (×983) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 613, test: 370

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Strawberry.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Strawberry`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; Spectral declaration for X: The archive documents the spectroscopy technique, but the standardized numeric headers do not establish original per-channel coordinates. Preserve all channel labels without assigning a physical unit; no grid is reconstructed. Evidence: https://www.timeseriesclassification.com/description.php?Dataset=Strawberry
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

- **Content version:** 1.2.1 | **schema/protocol:** 2.0
- **Content hash:** `73356e602376b7b5c969ac7523797f1eedd49081bc5aeb5e4e212bdad66387a1`
- **Processing hash:** `968d9475a16279189748d7fb0da62d80e2332247ef160c499e9ebd50a116f208` | **metadata hash:** `9d3def8641e8231127852e4b2fbd99abc56f77971da42aebc6ddf4b301e74160`
