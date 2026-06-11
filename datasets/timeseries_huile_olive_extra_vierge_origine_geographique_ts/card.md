# Datasheet — huile_olive_extra_vierge_origine_geographique_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** huile_olive_extra_vierge_origine_geographique_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** observation level; 60 sample(s), 60 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 799–1897 none | 60 | 570 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| origine_geographique | target | categorical | *Not specified.* | n=60, missing=0, classes=4, top 3 (×25) |
| ID_sample | metadata | categorical | *Not specified.* | n=60, missing=0, classes=60, top OliveOil_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top OliveOil (×60) |
| product | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top huile_olive_extra_vierge (×60) |
| trait_header | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top origine_geographique (×60) |
| trait_description | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Origine geographique de l'huile d'olive (codes bruts du dataset). (×60) |
| split | metadata | categorical | *Not specified.* | n=60, missing=0, classes=2, top train (×30) |
| spectro | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top FTIR (×60) |
| raw_label | metadata | categorical | *Not specified.* | n=60, missing=0, classes=4, top 4 (×25) |
| reference_value | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–4, mean 2.8 ± 1.162 |
| class_index | metadata | categorical | *Not specified.* | n=60, missing=0, classes=4, top 3 (×25) |
| dimensions | metadata | numeric | *Not specified.* | n=60, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=60, missing=0, range 570–570, mean 570 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=60, missing=0, classes=1, top Publication source: tous les spectres d'absorbance ont ete tronques sur 799-1897 cm^-1, axe lineaire reconstruit ici en ordre decroissant 1897->799 sur 570 variables. (×60) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): train: 30, test: 30

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/OliveOil.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=OliveOil`
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
- **Content hash:** `86d1cf75c412c1b1ea76952d631b8ed0d44ab0e627dd76f05e63acc1c3f51531`
- **Processing hash:** `0e35c420e99a51a9c3343506dafc5e7ef8bf7015ee908c54595087bae773500b` | **metadata hash:** `778e711ac61f161441661026fc25783b6aa0d9b6b5b7a2ce07cf3b35dcc24706`
