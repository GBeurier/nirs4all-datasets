# Datasheet — ECOSTRESS rock all axis 8a8a144c

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 8a8a144c. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 83 sample(s), 83 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 2–15.39 none | 83 | 2257 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=83, missing=0, classes=81, top Quartzite (×2) |
| class_label | target | categorical | *Not specified.* | n=83, missing=0, classes=3, top Igneous (×38) |
| subclass | target | categorical | *Not specified.* | n=83, missing=0, classes=21, top Felsic (×11) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=83, missing=0, classes=83, top rock.igneous.alkalic.solid.all.ward17.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top rock (×83) |
| material_type | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Rock (×83) |
| site | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=83, missing=0, classes=82, top Ward's Collection of American Rocks. Sample locality - Portland, Middlesex County, Connecticut. (×2) |
| country | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top N/A (×83) |
| species | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=83, missing=83, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=83, missing=0, classes=83, top A very fine-grained, porphyritic rock, light gray in color.Geologic age - Tertiary (Post-Oligocene).Collected by: Ward's Natural Science Original ASTER Spectral Library name was jpl.nicolet.rock.igneous.alkalic.solid.ward17.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top jpl.nicolet (×83) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Hemispherical reflectance (×83) |
| signal_type | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Reflectance (percent) (×83) |
| axis_unit | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Wavelength (micrometers) (×83) |
| axis_min | metadata | numeric | *Not specified.* | n=83, missing=0, range 2–2, mean 2 ± 2.234e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=83, missing=0, range 15.39–15.39, mean 15.39 ± 1.787e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=83, missing=0, range 2257–2257, mean 2257 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×83) |
| citation | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×83) |
| license | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×83) |
| rights_status | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top manual_review_needed (×83) |
| usage_scope | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top private_use_only (×83) |
| notes | metadata | categorical | *Not specified.* | n=83, missing=0, classes=1, top none (×83) |

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
- **Curated views:** M: 1 fields, Y: 3 fields, passport: 49 fields, measurements: 4 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `a8bd54d23e261651ae3277c1245f4cfa112ff28003684ee34036bc6b827bff2b`
- **Processing hash:** `ebee39cb955e33e44adaee32b2407d0bfe38192757dd20fcb7bb111cf1484160` | **metadata hash:** `c66aa7d08dd62b8ea95bb84a989abea426002727e8b479a76ae8780426d04112`
