# Datasheet — ECOSTRESS soil all axis 2228baf8

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis 2228baf8. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 7 sample(s), 7 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.01 none | 7 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=7, missing=0, classes=7, top Pale brown silty loam (×1) |
| class_label | target | categorical | *Not specified.* | n=7, missing=0, classes=4, top Inceptisol (×3) |
| subclass | target | categorical | *Not specified.* | n=7, missing=0, classes=7, top Fragiboralf (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=7, missing=0, classes=7, top soil.alfisol.fragiboralf.none.all.86p1994.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top soil (×7) |
| material_type | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top soil (×7) |
| site | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=7, missing=0, classes=7, top Bonner Co., Id. via USDA Soil Conservation service. (×1) |
| country | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=7, missing=7, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=7, missing=0, classes=7, top Pale brown silty loam (medial, typic). Original ASTER Spectral Library name was jhu.becknic.soil.alfisol.fragiboralf.coarse.86P1994.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top jhu.becknic (×7) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×7) |
| signal_type | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top Reflectance (percent) (×7) |
| axis_unit | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top Wavelength (micrometers) (×7) |
| axis_min | metadata | numeric | *Not specified.* | n=7, missing=0, range 0.4–0.4, mean 0.4 ± 5.996e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=7, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=7, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×7) |
| citation | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×7) |
| license | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×7) |
| rights_status | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top manual_review_needed (×7) |
| usage_scope | metadata | categorical | *Not specified.* | n=7, missing=0, classes=1, top private_use_only (×7) |
| notes | metadata | categorical | *Not specified.* | n=7, missing=0, classes=7, top soil.alfisol.fragiboralf.none.all.86p1994.jhu.becknic.ancillary.txt (×1) |

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

- **Conversion warnings:** *Not specified.*

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
- **Content hash:** `18096cd7dfe23b466562253747c5678887c9a61586fe852b8e4bba5733ba770c`
- **Processing hash:** `fe8f0e5ef64e4a7758ec085c517071aa2bb48d8213bbc91f9c287f3430a64a66` | **metadata hash:** `28695e39c56c62190fa30d7c0c9ffafec7429e8e69c35628618b1409c1fc9f2b`
