# Datasheet — spiritueux_whisky_bouteille_taux_ethanol_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** spiritueux_whisky_bouteille_taux_ethanol_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 1004 sample(s), 1004 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 226–1101 none | 1004 | 1751 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| taux_ethanol | target | numeric | *Not specified.* | n=1004, missing=0, range 0–3, mean 1.498 ± 1.119 |
| ID_sample | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1004, top EthanolLevel_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=1004, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top EthanolLevel (×1004) |
| product | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top spiritueux_whisky_bouteille (×1004) |
| trait_header | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top taux_ethanol (×1004) |
| trait_description | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top Niveau d'alcool du spiritueux. (×1004) |
| split | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=2, top train (×504) |
| spectro | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top vibrational spectroscopy (×1004) |
| raw_label | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=4, top 1 (×252) |
| reference_value | metadata | numeric | *Not specified.* | n=1004, missing=0, range 35–45, mean 39.49 ± 3.64 |
| class_index | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=4, top 0 (×252) |
| dimensions | metadata | numeric | *Not specified.* | n=1004, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=1004, missing=0, range 1751–1751, mean 1751 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=1004, missing=0, classes=1, top Axe spectral applique sur 226.0-1101.0 nm avec un pas de 0.5 nm, coherent avec 1751 variables. (×1004) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 500, train: 504

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/EthanolLevel.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=EthanolLevel`
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
- **Content hash:** `13edf11d4bb592f1efdd35ede632c0b1ff5db61114db13c0021a9f24f8c5bba5`
- **Processing hash:** `f16392e4c51256823d1af269d39e993fe6b1f5706ad1bb3828e5460d497da49d` | **metadata hash:** `1f7c42ca573bdc13157e58131ce488f1912a6e5021acbe1ba3208420111ba784`
