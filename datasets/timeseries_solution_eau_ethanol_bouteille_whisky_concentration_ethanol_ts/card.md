# Datasheet — solution_eau_ethanol_bouteille_whisky_concentration_ethanol_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** solution_eau_ethanol_bouteille_whisky_concentration_ethanol_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 524 sample(s), 1572 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 3–3 (mean 3).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 226–1101 none | 1572 | 1751 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| concentration_ethanol | target | numeric | *Not specified.* | n=1572, missing=0, range 0–3, mean 1.498 ± 1.117 |
| ID_sample | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=524, top EthanolConcentration_train_0001 (×3) |
| SpectralRep | metadata | numeric | *Not specified.* | n=1572, missing=0, range 1–3, mean 2 ± 0.8168 |
| dataset | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top EthanolConcentration (×1572) |
| product | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top solution_eau_ethanol_bouteille_whisky (×1572) |
| trait_header | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top concentration_ethanol (×1572) |
| trait_description | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top Concentration d'ethanol en pourcentage. (×1572) |
| split | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=2, top test (×789) |
| spectro | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top UV-visible / NIR (×1572) |
| raw_label | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=4, top E40 (×396) |
| reference_value | metadata | numeric | *Not specified.* | n=1572, missing=0, range 35–45, mean 39.49 ± 3.633 |
| class_index | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=4, top 2 (×396) |
| dimensions | metadata | numeric | *Not specified.* | n=1572, missing=0, range 3–3, mean 3 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=1572, missing=0, range 1751–1751, mean 1751 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=1572, missing=0, classes=1, top Axe spectral applique sur 226.0-1101.0 nm avec un pas de 0.5 nm, coherent avec 1751 variables. (×1572) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 263, train: 261

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/EthanolConcentration.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=EthanolConcentration`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
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
- **Content hash:** `8b39b7f12f0b485a62ad7d2497434d4d418d7edbae0f90b4611f795961273561`
- **Processing hash:** `07f241e451d58fb083c1e883f3adf5ca35fe7717eb27b1305ae1694bf305671b` | **metadata hash:** `36845d76deb8811449ea4d879b80a5dd33006fd993951094318f20bea7e5dc8d`
