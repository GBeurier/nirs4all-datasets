# Datasheet — ECOSTRESS manmade tir axis 85fbc8f6

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade tir axis 85fbc8f6. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 16 sample(s), 16 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade tir | source instruments vary by sample | other | 2–15.39 none | 16 | 2256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=16, missing=0, classes=2, top Brass plate (×15) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=16, missing=0, classes=16, top manmade.reflectancetarget.none.solid.tir.001682.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top manmade (×16) |
| material_type | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Manmade (×16) |
| site | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Labsphere, P.O. Box 70, Shaker Street, North Sutton, NH 03260(603) 927-4266 (×16) |
| country | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top N/A (×16) |
| species | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=16, missing=16, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=16, missing=0, classes=16, top Measurement made at center. Field Gold.Oct. 29 1997 to Oct. 30 1997. Original ASTER Spectral Library name was jpl.nicolet.manmade.target.none.solid.fg11097j.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top jpl.nicolet (×16) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Hemispherical Reflectance (×16) |
| signal_type | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Reflectence (percent) (×16) |
| axis_unit | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Wavelength (micrometers) (×16) |
| axis_min | metadata | numeric | *Not specified.* | n=16, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=16, missing=0, range 15.39–15.39, mean 15.39 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=16, missing=0, range 2256–2256, mean 2256 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×16) |
| citation | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×16) |
| license | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×16) |
| rights_status | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top manual_review_needed (×16) |
| usage_scope | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top private_use_only (×16) |
| notes | metadata | categorical | *Not specified.* | n=16, missing=0, classes=1, top none (×16) |

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
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 49 fields, measurements: 5 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `a3c748a19ac94918f14356dc3fd5b56b6aea4469459d8c6ff8b7bbdaef37588f`
- **Processing hash:** `043bef8704db342a217f66b6eb8836e6765e8fe007ed6967a03232a3462f2020` | **metadata hash:** `f19b27c8f6ca83c27e46abc273ed98350d332203a0973e4661d53ccc0fbe57a2`
