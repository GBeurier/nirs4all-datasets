# Datasheet — ECOSTRESS vegetation tir axis 1389b1f1

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS vegetation tir axis 1389b1f1. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 324 sample(s), 342 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.056).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | vegetation tir | source instruments vary by sample | other | 2.501–15.39 none | 342 | 1737 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=342, missing=0, classes=56, top Arctostaphylos glandulosa 3 (×13) |
| type | target | categorical | *Not specified.* | n=342, missing=0, classes=2, top vegetation (×304) |
| class_label | target | categorical | *Not specified.* | n=342, missing=0, classes=2, top Shrub (×178) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=342, missing=0, classes=342, top vegetation.shrub.adenostoma.fasciculatum.tir.vh033.ucsb.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top vegetation (×342) |
| material_type | metadata | categorical | *Not specified.* | n=342, missing=0, classes=2, top vegetation (×304) |
| site | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=342, missing=0, classes=41, top USA, Massachusetts, Harvard Forest (×38) |
| country | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=342, missing=0, classes=9, top 11/2/2013 (×52) |
| species | metadata | categorical | *Not specified.* | n=342, missing=0, classes=2, top Shrub (×178) |
| genus | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=342, missing=342, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=342, missing=0, classes=2, top Samples were collected as part of the HyspIRI Airborne Campaign. 48 individual plants were sampled in three times in 2013 - spring summer and fall. The name of the sample includes a 1 2 or 3 which references a different individual of the species. Samples were taken to JPL and processed within 48 hours of collection. The same leaves were processed in the Nicolet and then measured using the ASD. (×304) |
| instrument | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top ucsb.nicolet (×342) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top Hemispherical reflectance (×342) |
| signal_type | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top Reflectance (percentage) (×342) |
| axis_unit | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top Wavelength (micrometers) (×342) |
| axis_min | metadata | numeric | *Not specified.* | n=342, missing=0, range 2.501–2.501, mean 2.501 ± 4.447e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=342, missing=0, range 15.39–15.39, mean 15.39 ± 1.779e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=342, missing=0, range 1737–1737, mean 1737 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×342) |
| citation | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×342) |
| license | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×342) |
| rights_status | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top manual_review_needed (×342) |
| usage_scope | metadata | categorical | *Not specified.* | n=342, missing=0, classes=1, top private_use_only (×342) |
| notes | metadata | categorical | *Not specified.* | n=342, missing=0, classes=342, top vegetation.shrub.adenostoma.fasciculatum.tir.vh033.ucsb.nicolet.ancillary.txt (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques. La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 7 fields, Y: 3 fields, measurements: 3 fields, passport: 43 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- The ECOSTRESS spectral library version 1.0 — [10.1016/j.rse.2019.05.015](https://doi.org/10.1016/j.rse.2019.05.015)
- The ASTER Spectral Library Version 2.0 — [10.1016/j.rse.2008.11.007](https://doi.org/10.1016/j.rse.2008.11.007)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Official ECOSTRESS page requests citation and states copyright/all rights reserved; converted matrices are private/internal until redistribution rights are clarified.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `cc39cebdd5e0ed04fa0b72da8763fe80a2902bab1e2f0112134d4b9c83626f2e`
- **Processing hash:** `229f413ba8c81a44071539164b20f8f4e52eb49c17b1b2462d6b3b5f3586741d` | **metadata hash:** `807e9068547797fb1dee3b341b9d9f04689ab6449c32c78b729fd421489d7994`
