# Datasheet — ECOSTRESS soil all axis 1fb6fa59

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis 1fb6fa59. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 13 sample(s), 13 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.01 none | 13 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=13, missing=0, classes=13, top Brown to dark brown gravelly loam (×1) |
| class_label | target | categorical | *Not specified.* | n=13, missing=0, classes=6, top Alfisol (×5) |
| subclass | target | categorical | *Not specified.* | n=13, missing=0, classes=11, top Haplustalf (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top soil.alfisol.haploxeralf.none.all.87p313.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top soil (×13) |
| material_type | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top soil (×13) |
| site | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=13, missing=0, classes=10, top Klickitat Co., Wa. via USDA Soil Conservation service. (×3) |
| country | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top N/A (×13) |
| species | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top Brown to dark brown gravelly loam (medial-skeletal, frigid ultic). Original ASTER Spectral Library name was jhu.becknic.soil.alfisol.haploxeralf.coarse.87P313.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top jhu.becknic (×13) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×13) |
| signal_type | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Reflectance (percent) (×13) |
| axis_unit | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Wavelength (micrometers) (×13) |
| axis_min | metadata | numeric | *Not specified.* | n=13, missing=0, range 0.4–0.4, mean 0.4 ± 5.778e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=13, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=13, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×13) |
| citation | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×13) |
| license | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×13) |
| rights_status | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top manual_review_needed (×13) |
| usage_scope | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top private_use_only (×13) |
| notes | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top soil.alfisol.haploxeralf.none.all.87p313.jhu.becknic.ancillary.txt (×1) |

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
- **Curated views:** M: 1 fields, Y: 3 fields, measurements: 4 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `20a89d220df27412ac44cc0e069958437dffeeca1a010cbf29918f44549189d0`
- **Processing hash:** `2a02624b938f2abd247caa7ce50a2862cd2734d15d2e245bb0b1e43dbb71b727` | **metadata hash:** `68bef94391ee5a7ed8e16da52c97f1e4eb62eb25efed332ab2c7f69a8eadef3c`
