# Datasheet — ECOSTRESS vegetation all axis 6fbcd0b0

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS vegetation all axis 6fbcd0b0. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 3 sample(s), 3 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | vegetation all | source instruments vary by sample | other | 0.302–14 none | 3 | 550 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=3, missing=0, classes=3, top Grass (×1) |
| class_label | target | categorical | *Not specified.* | n=3, missing=0, classes=2, top tree (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top vegetation.grass.unknown.unknown.all.grass.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top vegetation (×3) |
| material_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top vegetation (×3) |
| site | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top The entire spectral range was measured at Johns Hopkins University--see file vegetata.doc for details. (×1) |
| country | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Unknown (×3) |
| species | metadata | categorical | *Not specified.* | n=3, missing=0, classes=2, top tree (×2) |
| genus | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Green Rye grass. Spectra were assembled from two segments, the bidirectional VNIR and SWIR comprising segment one and the hemispherical MWIR and TIR comprising segment two. The VNIR/SWIR spectrum was measured in the laboratory at JHU with a GER IRIS Mark IV using a large piece of sod. The grass was illuminated from directly above and measured at a reflectance angle of 60 degrees to avoid viewing the thatch. (×1) |
| instrument | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top jhu.becknic (×3) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Bidirectional and directional hemispherical reflectance. (×3) |
| signal_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Reflectance (percent) (×3) |
| axis_unit | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Wavelength (micrometers) (×3) |
| axis_min | metadata | numeric | *Not specified.* | n=3, missing=0, range 0.302–0.302, mean 0.302 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3, missing=0, range 14–14, mean 14 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3, missing=0, range 550–550, mean 550 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×3) |
| citation | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×3) |
| license | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×3) |
| rights_status | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top manual_review_needed (×3) |
| usage_scope | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top private_use_only (×3) |
| notes | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top None. (×3) |
| source_name | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Grass (×1) |
| source_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top vegetation (×3) |
| source_class | metadata | categorical | *Not specified.* | n=3, missing=0, classes=2, top tree (×2) |
| source_genus | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Unknown (×3) |
| source_species | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Unknown (×3) |
| source_sample_no | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top grass (×1) |
| source_owner | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top JHU (×3) |
| source_wavelength_range | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top All (×3) |
| source_origin | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top The entire spectral range was measured at Johns Hopkins University--see file vegetata.doc for details. (×1) |
| source_collection_date | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Unknown (×3) |
| source_description | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Green Rye grass. Spectra were assembled from two segments, the bidirectional VNIR and SWIR comprising segment one and the hemispherical MWIR and TIR comprising segment two. The VNIR/SWIR spectrum was measured in the laboratory at JHU with a GER IRIS Mark IV using a large piece of sod. The grass was illuminated from directly above and measured at a reflectance angle of 60 degrees to avoid viewing the thatch. (×1) |
| source_measurement | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Bidirectional and directional hemispherical reflectance. (×3) |
| source_first_column | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top X (×3) |
| source_second_column | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Y (×3) |
| source_x_units | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Wavelength (micrometers) (×3) |
| source_y_units | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Reflectance (percent) (×3) |
| source_first_x_value | metadata | numeric | *Not specified.* | n=3, missing=0, range 0.302–0.302, mean 0.302 ± 0 |
| source_last_x_value | metadata | numeric | *Not specified.* | n=3, missing=0, range 14–14, mean 14 ± 0 |
| source_number_of_x_values | metadata | numeric | *Not specified.* | n=3, missing=0, range 550–550, mean 550 ± 0 |
| source_additional_information | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top None. (×3) |
| source_material_name | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Grass (×1) |
| source_sample_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top vegetation (×3) |
| source_source_file_name | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top vegetation.grass.unknown.unknown.all.grass.jhu.becknic.spectrum.txt (×1) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 2 fields, Y: 2 fields, passport: 47 fields, measurements: 4 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `93c44037e3bf1d29c9c4936ad9f7861549a4d10c84d44281dadbc3c3739996c9`
- **Processing hash:** `96ce8b8492623d1a9f8168633a091110dd8914d4807fbe2aed1d023814085a14` | **metadata hash:** `29628752b5e0b367d2f8a719cfee98f4e9cf419a26e88896cd3560871a48f9fd`
