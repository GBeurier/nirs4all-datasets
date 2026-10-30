# Datasheet — roche_type_roche_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** roche_type_roche_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** sample level; 70 sample(s), 70 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 0.4–14.01 none | 70 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| type_roche | target | categorical | *Not specified.* | n=70, missing=0, classes=4, top 0 (×26) |
| ID_sample | metadata | categorical | *Not specified.* | n=70, missing=0, classes=70, top Rock_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Rock (×70) |
| product | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top roche (×70) |
| trait_header | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top type_roche (×70) |
| trait_description | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Type de roche. (×70) |
| split | metadata | categorical | *Not specified.* | n=70, missing=0, classes=2, top test (×50) |
| spectro | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top reflectance spectrale (×70) |
| raw_label | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top 1 (×26) |
| reference_value | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top mafic (×26) |
| class_index | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top 0 (×26) |
| dimensions | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=70, missing=0, range 2844–2844, mean 2844 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Sources ASTER/ECOSTRESS: les spectres All de la bibliotheque ASTER ont 2844 valeurs de X, de 14.0110 a 0.4000 um. La partie VSWIR Beckman est documentee sur 0.4-2.5 um avec un pas de 0.001 um de 0.4 a 0.8 puis 0.004 um de 0.8 a 2.5, mais le vecteur bande-a-bande fusionne n'est pas fourni dans l'archive Rock, axe lineaire interpole applique ici en ordre decroissant 14.0110->0.4000 sur 2844 variables. (×70) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 50, train: 20

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Rock.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Rock`
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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `a12a0c85be957a61c91229fa1ee64534498b09605d8f38b65257dcc9cec3116d`
- **Processing hash:** `353039f970ec9b4579763bffa13034dbeac6dafb0d0ee6e95619bc5b5301639d` | **metadata hash:** `529d5492f08756c94bfef517eccda28b4c9d983735ec1454aaa842f25d98a3f0`
