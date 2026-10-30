# Datasheet — ECOSTRESS vegetation vswir axis 4d4366d1

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS vegetation vswir axis 4d4366d1. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 325 sample(s), 343 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.055).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | vegetation vswir | source instruments vary by sample | other | 0.35–2.5 none | 343 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=343, missing=0, classes=56, top Arctostaphylos glandulosa 3 (×13) |
| type | target | categorical | *Not specified.* | n=343, missing=0, classes=2, top vegetation (×304) |
| class_label | target | categorical | *Not specified.* | n=343, missing=0, classes=2, top Shrub (×178) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=343, missing=0, classes=343, top vegetation.shrub.adenostoma.fasciculatum.vswir.vh033.ucsb.asd.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top vegetation (×343) |
| material_type | metadata | categorical | *Not specified.* | n=343, missing=0, classes=2, top vegetation (×304) |
| site | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=343, missing=0, classes=41, top USA, Massachusetts, Harvard Forest (×39) |
| country | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=343, missing=0, classes=9, top 11/2/2013 (×52) |
| species | metadata | categorical | *Not specified.* | n=343, missing=0, classes=2, top Shrub (×178) |
| genus | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=343, missing=343, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=343, missing=0, classes=2, top Samples were collected as part of the HyspIRI Airborne Campaign. 48 individual plants were sampled in three times in 2013 - spring summer and fall. The name of the sample includes a 1 2 or 3 which references a different individual of the species. Samples were taken to JPL and processed within 48 hours of collection. The same leaves were processed in the Nicolet and then measured using the ASD. (×304) |
| instrument | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top ucsb.asd (×343) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top Bidirectional reflectance (×343) |
| signal_type | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top Reflectance (percentage) (×343) |
| axis_unit | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top Wavelength (micrometers) (×343) |
| axis_min | metadata | numeric | *Not specified.* | n=343, missing=0, range 0.35–0.35, mean 0.35 ± 1.112e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=343, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=343, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×343) |
| citation | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×343) |
| license | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×343) |
| rights_status | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top manual_review_needed (×343) |
| usage_scope | metadata | categorical | *Not specified.* | n=343, missing=0, classes=1, top private_use_only (×343) |
| notes | metadata | categorical | *Not specified.* | n=343, missing=0, classes=343, top vegetation.shrub.adenostoma.fasciculatum.vswir.vh033.ucsb.asd.ancillary.txt (×1) |

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
- **Curated views:** M: 7 fields, Y: 3 fields, passport: 43 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `3820c056b80228f7201aca3f295abeb9989b3f198c6ddca45934ec8862ae927a`
- **Processing hash:** `3ac8ea4a3fcc7f855c18cf69efef62016a923577c6561315a07d9a29560bde62` | **metadata hash:** `1ff6bad411d36d70b8352fb53f6085b8b5d284d17dcc287d474e6d4e01ee03a1`
