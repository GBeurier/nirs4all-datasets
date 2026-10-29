# Datasheet — ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 54 sample(s), 57 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.056).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | nonphotosyntheticvegetation vswir | source instruments vary by sample | other | 0.35–2.5 none | 57 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=57, missing=0, classes=28, top Calocedrus decrruens (×4) |
| type | target | categorical | *Not specified.* | n=57, missing=0, classes=2, top non photosynthetic vegetation (×54) |
| class_label | target | categorical | *Not specified.* | n=57, missing=0, classes=6, top bark (×18) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=57, missing=0, classes=57, top nonphotosyntheticvegetation.bark.abies.concolor.vswir.vh311.ucsb.asd.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top nonphotosyntheticvegetation (×57) |
| material_type | metadata | categorical | *Not specified.* | n=57, missing=0, classes=2, top non photosynthetic vegetation (×54) |
| site | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=57, missing=0, classes=7, top 37.04403333, -119.30225, WGS84 (×19) |
| country | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=57, missing=0, classes=4, top 5/10/2014 (×19) |
| species | metadata | categorical | *Not specified.* | n=57, missing=0, classes=6, top bark (×18) |
| genus | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=57, missing=57, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=57, missing=0, classes=11, top Samples were collected as part of the HyspIRI Airborne Campaign proposal titled: HyspIRI discrimination of plant species and functional types along a strong environmental temperature gradient. The same materials were processed in the Nicolet and then measured using the ASD. (×25) |
| instrument | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top ucsb.asd (×57) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Bidirectional reflectance (×57) |
| signal_type | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Reflectance (percentage) (×57) |
| axis_unit | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Wavelength (micrometers) (×57) |
| axis_min | metadata | numeric | *Not specified.* | n=57, missing=0, range 0.35–0.35, mean 0.35 ± 5.6e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=57, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=57, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×57) |
| citation | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×57) |
| license | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×57) |
| rights_status | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top manual_review_needed (×57) |
| usage_scope | metadata | categorical | *Not specified.* | n=57, missing=0, classes=1, top private_use_only (×57) |
| notes | metadata | categorical | *Not specified.* | n=57, missing=37, classes=20, top nonphotosyntheticvegetation.bark.acer.rubrum.vswir.acru-1-81.ucsb.asd.ancillary.txt (×1) |

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
- **Content hash:** `b9cf4c3a2987eb03e16b6e2b9f583a42ddc0498a053b3c8ed5c55f44744625e0`
- **Processing hash:** `0ae79984f0de0d169ce5662d3b3de0d24706842a3f582dd792aa4240caa14805` | **metadata hash:** `2cfe852341e7c2e02b81aed343beaa5d296d55a738bff5db8e9ddf3255ee24d8`
