# Datasheet — ECOSTRESS manmade tir axis 93ae36e3

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade tir axis 93ae36e3. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 10 sample(s), 10 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade tir | source instruments vary by sample | other | 2–14.01 none | 10 | 2223 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=10, missing=0, classes=6, top Flat Black Paint (×4) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top manmade.generalconstructionmaterial.paint.solid.tir.1246.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top manmade (×10) |
| material_type | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Manmade (×10) |
| site | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=10, missing=0, classes=4, top The Testor Corp., 620 Buckbee St., Rockford, IL 61104 (×4) |
| country | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top N/A (×10) |
| species | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Metallic silver spray enamel paintCollected by JPL Original ASTER Spectral Library name was jpl.nicolet.manmade.construction.paint.solid.1246.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top jpl.nicolet (×10) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Hemispherical reflectance (×10) |
| signal_type | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Reflectance (percent) (×10) |
| axis_unit | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Wavelength (micrometers) (×10) |
| axis_min | metadata | numeric | *Not specified.* | n=10, missing=0, range 2–2, mean 2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=10, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=10, missing=0, range 2223–2223, mean 2223 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×10) |
| citation | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×10) |
| license | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×10) |
| rights_status | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top manual_review_needed (×10) |
| usage_scope | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top private_use_only (×10) |
| notes | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top none (×10) |

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
- **Curated views:** M: 1 fields, Y: 1 fields, passport: 48 fields, measurements: 5 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `713d706762bdf95b105d4af635c7800a55b0fd08245069f8682998898b698419`
- **Processing hash:** `0729236d8a0c3acc6d87298ed09bbecfc6fa6284c925a0ed5aed6a5675edf608` | **metadata hash:** `af6ac9ae3e2ec428dfdbf844601ec6c0ba6503ae2f0f37dd11577fdb7a9a44ff`
