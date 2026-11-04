# Datasheet — ECOSTRESS vegetation vswir axis 4d4366d1

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS vegetation vswir axis 4d4366d1. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 210 sample(s), 210 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | vegetation vswir | source instruments vary by sample | other | 0.35–2.5 none | 210 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=210, missing=0, classes=74, top Bambusa beecheyana (×9) |
| class_label | target | categorical | *Not specified.* | n=210, missing=0, classes=3, top Tree (×185) |
| owner | target | categorical | *Not specified.* | n=210, missing=0, classes=2, top JPL (×206) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=210, missing=0, classes=210, top vegetation.grass.avena.fatua.vswir.vh352.ucsb.asd.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top vegetation (×210) |
| material_type | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top vegetation (×210) |
| site | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=210, missing=0, classes=164, top 34.12593, - 118.10983, WGS84 (×6) |
| country | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=210, missing=0, classes=6, top 10/3/2016 (×60) |
| species | metadata | categorical | *Not specified.* | n=210, missing=0, classes=3, top Tree (×185) |
| genus | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=210, missing=210, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=210, missing=0, classes=2, top Samples were collected at the Huntington Garden in San Marino California as part of a JPL Subcontract studying HyTES imagery. Samples were taken to JPL and processed within 48 hours of collection. The same leaves were processed in the Nicolet and then measured using the ASD. (×206) |
| instrument | metadata | categorical | *Not specified.* | n=210, missing=0, classes=2, top jpl.asd (×206) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Bidirectional reflectance (×210) |
| signal_type | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Reflectance (percentage) (×210) |
| axis_unit | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Wavelength (micrometer) (×210) |
| axis_min | metadata | numeric | *Not specified.* | n=210, missing=0, range 0.35–0.35, mean 0.35 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=210, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=210, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×210) |
| citation | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×210) |
| license | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×210) |
| rights_status | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top manual_review_needed (×210) |
| usage_scope | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top private_use_only (×210) |
| notes | metadata | categorical | *Not specified.* | n=210, missing=54, classes=156, top vegetation.shrub.gasteria.acinacifolia.vswir.jpl143.jpl.asd.ancillary.txt (×1) |
| source_name | metadata | categorical | *Not specified.* | n=210, missing=0, classes=74, top Bambusa beecheyana (×9) |
| source_type | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top vegetation (×210) |
| source_class | metadata | categorical | *Not specified.* | n=210, missing=0, classes=3, top Tree (×185) |
| source_genus | metadata | categorical | *Not specified.* | n=210, missing=0, classes=48, top Quercus (×25) |
| source_species | metadata | categorical | *Not specified.* | n=210, missing=0, classes=70, top beecheyana (×9) |
| source_sample_no | metadata | categorical | *Not specified.* | n=210, missing=0, classes=210, top VH352 (×1) |
| source_owner | metadata | categorical | *Not specified.* | n=210, missing=0, classes=2, top JPL (×206) |
| source_wavelength_range | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top VSWIR (×210) |
| source_origin | metadata | categorical | *Not specified.* | n=210, missing=0, classes=164, top 34.12593, - 118.10983, WGS84 (×6) |
| source_collection_date | metadata | categorical | *Not specified.* | n=210, missing=0, classes=6, top 10/3/2016 (×60) |
| source_description | metadata | categorical | *Not specified.* | n=210, missing=0, classes=2, top Samples were collected at the Huntington Garden in San Marino California as part of a JPL Subcontract studying HyTES imagery. Samples were taken to JPL and processed within 48 hours of collection. The same leaves were processed in the Nicolet and then measured using the ASD. (×206) |
| source_measurement | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Bidirectional reflectance (×210) |
| source_first_column | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top X (×210) |
| source_second_column | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Y (×210) |
| source_x_units | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Wavelength (micrometer) (×210) |
| source_y_units | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top Reflectance (percentage) (×210) |
| source_first_x_value | metadata | numeric | *Not specified.* | n=210, missing=0, range 0.35–0.35, mean 0.35 ± 0 |
| source_last_x_value | metadata | numeric | *Not specified.* | n=210, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| source_number_of_x_values | metadata | numeric | *Not specified.* | n=210, missing=0, range 2151–2151, mean 2151 ± 0 |
| source_additional_information | metadata | categorical | *Not specified.* | n=210, missing=54, classes=156, top vegetation.shrub.gasteria.acinacifolia.vswir.jpl143.jpl.asd.ancillary.txt (×1) |
| source_material_name | metadata | categorical | *Not specified.* | n=210, missing=0, classes=74, top Bambusa beecheyana (×9) |
| source_sample_type | metadata | categorical | *Not specified.* | n=210, missing=0, classes=1, top vegetation (×210) |
| source_source_file_name | metadata | categorical | *Not specified.* | n=210, missing=0, classes=210, top vegetation.grass.avena.fatua.vswir.vh352.ucsb.asd.spectrum.txt (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometer)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 7 fields, Y: 2 fields, passport: 43 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `660e6b3f01f54d26f8a6da22fca83c5b6fb85928ee8fb1b7f5d30ba31e305521`
- **Processing hash:** `d53bbca4915df07f58fd2bc262da23de4a3378e09a2e42a88c9994506bde2017` | **metadata hash:** `0b064698661b2dfa105ff77d41fdfbe7954e8e136cdf074369f44b0be8c12f97`
