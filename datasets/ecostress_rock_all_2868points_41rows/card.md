# Datasheet — ECOSTRESS rock all axis be345a03

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis be345a03. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 39 sample(s), 41 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.051).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.98 none | 41 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=41, missing=0, classes=36, top Hornblende Gneiss (×2) |
| class_label | target | categorical | *Not specified.* | n=41, missing=0, classes=2, top Metamorphic (×29) |
| subclass | target | categorical | *Not specified.* | n=41, missing=0, classes=11, top Gneis (×7) |
| particle_size | target | categorical | *Not specified.* | n=41, missing=0, classes=2, top Fine (×38) |
| measurement | target | categorical | *Not specified.* | n=41, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×40) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=41, missing=0, classes=41, top rock.metamorphic.gneis.coarse.all.gneiss6.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top rock (×41) |
| material_type | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top rock (×41) |
| site | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=41, missing=0, classes=39, top Sample No. 465, The Hunt and Salisbury Collection at the U.S.Geological Survey, Denver, Co. (×2) |
| country | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top N/A (×41) |
| species | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=41, missing=41, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=41, missing=0, classes=41, top Coarse grains of slightly lineated hornblende euhedra with anhedra of alkali feldspar make up the bulk of this rock. There are scattered grains of pyrite and possibly a trace of quartz as well. The modes were 69% hornblende, 30.4% feldspar and 0.6% opaques. Particle size was 500-1500 Micrometer. Original ASTER Spectral Library name was jhu.becknic.rock.metamorphic.gneiss.coarse.gneiss6.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top jhu.becknic (×41) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=41, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×40) |
| signal_type | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Reflectance (percent) (×41) |
| axis_unit | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Wavelength (micrometers) (×41) |
| axis_min | metadata | numeric | *Not specified.* | n=41, missing=0, range 0.4–0.4, mean 0.4 ± 5.62e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=41, missing=0, range 14.98–14.98, mean 14.98 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=41, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×41) |
| citation | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×41) |
| license | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×41) |
| rights_status | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top manual_review_needed (×41) |
| usage_scope | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top private_use_only (×41) |
| notes | metadata | categorical | *Not specified.* | n=41, missing=0, classes=6, top none (×36) |
| source_name | metadata | categorical | *Not specified.* | n=41, missing=0, classes=36, top Hornblende Gneiss (×2) |
| source_type | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top rock (×41) |
| source_class | metadata | categorical | *Not specified.* | n=41, missing=0, classes=2, top Metamorphic (×29) |
| source_subclass | metadata | categorical | *Not specified.* | n=41, missing=0, classes=11, top Gneis (×7) |
| source_particle_size | metadata | categorical | *Not specified.* | n=41, missing=0, classes=2, top Fine (×38) |
| source_sample_no | metadata | categorical | *Not specified.* | n=41, missing=0, classes=39, top gneiss6 (×2) |
| source_owner | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top JHU (×41) |
| source_wavelength_range | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top All (×41) |
| source_origin | metadata | categorical | *Not specified.* | n=41, missing=0, classes=39, top Sample No. 465, The Hunt and Salisbury Collection at the U.S.Geological Survey, Denver, Co. (×2) |
| source_collection_date | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top N/A (×41) |
| source_description | metadata | categorical | *Not specified.* | n=41, missing=0, classes=41, top Coarse grains of slightly lineated hornblende euhedra with anhedra of alkali feldspar make up the bulk of this rock. There are scattered grains of pyrite and possibly a trace of quartz as well. The modes were 69% hornblende, 30.4% feldspar and 0.6% opaques. Particle size was 500-1500 Micrometer. Original ASTER Spectral Library name was jhu.becknic.rock.metamorphic.gneiss.coarse.gneiss6.spectrum.txt (×1) |
| source_measurement | metadata | categorical | *Not specified.* | n=41, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×40) |
| source_first_column | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top X (×41) |
| source_second_column | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Y (×41) |
| source_x_units | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Wavelength (micrometers) (×41) |
| source_y_units | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top Reflectance (percent) (×41) |
| source_first_x_value | metadata | numeric | *Not specified.* | n=41, missing=0, range 14.98–14.98, mean 14.98 ± 0 |
| source_last_x_value | metadata | numeric | *Not specified.* | n=41, missing=0, range 0.4–0.4, mean 0.4 ± 5.62e-17 |
| source_number_of_x_values | metadata | numeric | *Not specified.* | n=41, missing=0, range 2868–2868, mean 2868 ± 0 |
| source_additional_information | metadata | categorical | *Not specified.* | n=41, missing=0, classes=6, top none (×36) |
| source_material_name | metadata | categorical | *Not specified.* | n=41, missing=0, classes=36, top Hornblende Gneiss (×2) |
| source_sample_type | metadata | categorical | *Not specified.* | n=41, missing=0, classes=1, top rock (×41) |
| source_source_file_name | metadata | categorical | *Not specified.* | n=41, missing=0, classes=41, top rock.metamorphic.gneis.coarse.all.gneiss6.jhu.becknic.spectrum.txt (×1) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 2 fields, Y: 5 fields, passport: 49 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `99308cefb9c0a9d5e691a059ede27cf72c06c8618a1173db059cd1ddf252a9be`
- **Processing hash:** `24446fce48307534e39a17fc8d4e940e0aad1ad7d46e0c4a32df51940361863f` | **metadata hash:** `81ca28580727658d965b2fecc38cd4f54d5d90a67fa724078f6c7dde50988511`
