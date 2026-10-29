# Datasheet — puree_fraise_authenticite_ts

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

- **original** (documented, not applied): test: 370, train: 613

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Strawberry.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Strawberry`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `0ca7d61003e05f5756248dcf9d028b32a751ec5de06d54e8df82a0470246b6be`
- **Processing hash:** `eac0d48014158e5ef8ad2ddc44e5647af954cd070afaf890bf0b01e4ce2d9479` | **metadata hash:** `ec34e2571f34b06cb0d61f09423d934a0cb9665fc330e1c4cbe552a921f9fa67`
