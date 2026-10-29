# Datasheet — ECOSTRESS soil tir axis 69ac2056

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil tir axis 69ac2056. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 17 sample(s), 17 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil tir | source instruments vary by sample | other | 2.079–14.01 none | 17 | 2124 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top 60051.19 (×1) |
| subclass | target | categorical | *Not specified.* | n=17, missing=0, classes=3, top Highland (×8) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top soil.lunar.highland.fine.tir.60051_19.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top soil (×17) |
| material_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Soil (×17) |
| site | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=17, missing=0, classes=4, top Apollo 16 landing site via the NASA Lunar Sample Repository at JohnsonSpace Center, Houston, TX. (×8) |
| country | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top N/A (×17) |
| species | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top This sample is one of a suite of relatively more aluminous and lower iron and titanium soils at the Apollo 16 site, and has the second oldest exposure age of the four soils of that suite (Is/FeO=57). Original ASTER Spectral Library name was jhu.becknic.soil.lunar.highlands.fine.60051.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top jhu.becknic (×17) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×17) |
| signal_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Reflectance (percent) (×17) |
| axis_unit | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Wavelength (micrometers) (×17) |
| axis_min | metadata | numeric | *Not specified.* | n=17, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=17, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=17, missing=0, range 2124–2124, mean 2124 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×17) |
| citation | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×17) |
| license | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×17) |
| rights_status | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top manual_review_needed (×17) |
| usage_scope | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top private_use_only (×17) |
| notes | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top none (×17) |

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
- **Curated views:** M: 1 fields, Y: 2 fields, passport: 49 fields, measurements: 4 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `d863d59d67e4824060e499a05262c46d16910dc592bd7627072c97213417dc6a`
- **Processing hash:** `3ad3385081eb6ecefcdc6cb11dc50a6dcdfe40c94a6970149ce8b9a9c87f6a78` | **metadata hash:** `9e13fa50adc5686f1d2abebb1ecbc65a146d0024b2c6ff904ebc56415e6b515d`
