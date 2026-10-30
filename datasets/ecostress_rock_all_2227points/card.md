# Datasheet — ECOSTRESS rock all axis d9555baa

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis d9555baa. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 9 sample(s), 9 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–13.9 none | 9 | 2227 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=9, missing=0, classes=2, top Altered volcanic tuff (×8) |
| subclass | target | categorical | *Not specified.* | n=9, missing=0, classes=2, top Felsic (×8) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=9, missing=0, classes=9, top rock.igneous.felsic.solid.all.cup1.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top rock (×9) |
| material_type | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Rock (×9) |
| site | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Cuprite, Nevada (×9) |
| country | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top N/A (×9) |
| species | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=9, missing=9, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=9, missing=0, classes=9, top Altered volcanic tuff, whiteSample was Whole rock chips. Original ASTER Spectral Library name was usgs.perknic.rock.igneous.felsic.solid.cup1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top usgs.perknic (×9) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Directional Hemispherical Reflectance (×9) |
| signal_type | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Reflectance (percent) (×9) |
| axis_unit | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Wavelength (micrometers) (×9) |
| axis_min | metadata | numeric | *Not specified.* | n=9, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=9, missing=0, range 13.9–13.9, mean 13.9 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=9, missing=0, range 2227–2227, mean 2227 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×9) |
| citation | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×9) |
| license | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×9) |
| rights_status | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top manual_review_needed (×9) |
| usage_scope | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top private_use_only (×9) |
| notes | metadata | categorical | *Not specified.* | n=9, missing=0, classes=1, top none (×9) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 0 fields, Y: 2 fields, measurements: 4 fields, passport: 50 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `f567c363ca084eaeb20b97f06e61b41fd538a26a3487a384e6778d92d2ad593c`
- **Processing hash:** `c24fe233e335d7152de5d5b989f8e264860cdf5d15798c334882656ff34b16a4` | **metadata hash:** `3c71b01e2b2565dc73abcfddd2cdf0eddfc68f7d1ac9d5a6ad836262ccb4903e`
