# Datasheet — ECOSTRESS rock all axis aa24fdf9

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis aa24fdf9. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 30 sample(s), 30 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.405–14.05 none | 30 | 2530 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=30, missing=0, classes=5, top Rhyolite (×23) |
| class_label | target | categorical | *Not specified.* | n=30, missing=0, classes=3, top Igneous (×23) |
| subclass | target | categorical | *Not specified.* | n=30, missing=0, classes=3, top Felsic (×27) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=30, missing=0, classes=30, top rock.igneous.felsic.solid.all.ap-936-10.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top rock (×30) |
| material_type | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Rock (×30) |
| site | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Iberian Pyrite Belt, Spain (×30) |
| country | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=30, missing=30, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=30, missing=0, classes=30, top Rhyolite, freshSample was Whole Rock Chips. Original ASTER Spectral Library name was usgs.perknic.rock.igneous.felsic.solid.rhy10.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top usgs.perknic (×30) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Directional Hemispherical Reflectance (×30) |
| signal_type | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Reflectance (percent) (×30) |
| axis_unit | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Wavelength (micrometers) (×30) |
| axis_min | metadata | numeric | *Not specified.* | n=30, missing=0, range 0.405–0.405, mean 0.405 ± 1.129e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=30, missing=0, range 14.05–14.05, mean 14.05 ± 3.613e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=30, missing=0, range 2530–2530, mean 2530 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×30) |
| citation | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×30) |
| license | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×30) |
| rights_status | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top manual_review_needed (×30) |
| usage_scope | metadata | categorical | *Not specified.* | n=30, missing=0, classes=1, top private_use_only (×30) |
| notes | metadata | categorical | *Not specified.* | n=30, missing=0, classes=30, top rock.igneous.felsic.solid.all.ap-936-10.usgs.perknic.ancillary.txt (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `3116eab1b6632bec21104665ed962de3aeda035df0ed7796212678d73538fdef`
- **Processing hash:** `000fd7a18ef5589e45433f4a70d375f543c2708eefdebfda418b09c50d8fa197` | **metadata hash:** `ab331c0495e707a6d935d096b13e215aeac44f2a789bdb31b3cebaf35da59d83`
