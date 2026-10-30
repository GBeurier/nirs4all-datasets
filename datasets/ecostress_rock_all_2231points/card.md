# Datasheet — ECOSTRESS rock all axis 20b176d4

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 20b176d4. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 27 sample(s), 27 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.05 none | 27 | 2231 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=27, missing=0, classes=4, top Basalt (×16) |
| class_label | target | categorical | *Not specified.* | n=27, missing=0, classes=2, top Igneous (×20) |
| subclass | target | categorical | *Not specified.* | n=27, missing=0, classes=2, top Mafic (×20) |
| owner | target | categorical | *Not specified.* | n=27, missing=0, classes=2, top Lawrence Rowan, USGS Reston (×20) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=27, missing=0, classes=27, top rock.igneous.mafic.solid.all.me10b.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top rock (×27) |
| material_type | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Rock (×27) |
| site | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=27, missing=0, classes=20, top Southeastern Idaho (×7) |
| country | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top N/A (×27) |
| species | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=27, missing=0, classes=27, top Basalt, fresh surfaceSample was Whole rock chips. Original ASTER Spectral Library name was usgs.perknic.rock.igneous.mafic.solid.me10b.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top usgs.perknic (×27) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Directional Hemispherical Reflectance (×27) |
| signal_type | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Reflectance (percent) (×27) |
| axis_unit | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Wavelength (micrometers) (×27) |
| axis_min | metadata | numeric | *Not specified.* | n=27, missing=0, range 0.4–0.4, mean 0.4 ± 5.657e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=27, missing=0, range 14.05–14.05, mean 14.05 ± 1.81e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=27, missing=0, range 2231–2231, mean 2231 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×27) |
| citation | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×27) |
| license | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×27) |
| rights_status | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top manual_review_needed (×27) |
| usage_scope | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top private_use_only (×27) |
| notes | metadata | categorical | *Not specified.* | n=27, missing=0, classes=21, top none (×7) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 1 fields, Y: 3 fields, passport: 50 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `db4dd99a7c4950a0d75030787b9f50f927facc2cc55bddeaf40a4519a4f21764`
- **Processing hash:** `c213b75d83ac82ef7f1ee9c7055222c8fb67cd08af2925c7bd9cc2b4d6c0cd43` | **metadata hash:** `f9cb31b76a2c93d7d7dd46a835d8b5ebf3fdb8a5b59f4e0e8227381b4859401b`
