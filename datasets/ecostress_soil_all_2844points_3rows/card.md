# Datasheet — ECOSTRESS soil all axis 5431484a

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis 5431484a. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 3 sample(s), 3 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.01 none | 3 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=3, missing=0, classes=3, top Reddish brown fine sandy loam (×1) |
| class_label | target | categorical | *Not specified.* | n=3, missing=0, classes=2, top Alfisol (×2) |
| subclass | target | categorical | *Not specified.* | n=3, missing=0, classes=2, top Paleustalf (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top soil.alfisol.paleustalf.none.all.87p1087.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top soil (×3) |
| material_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top soil (×3) |
| site | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top Lubbock Co., Tx. via USDA Soil Conservation service. (×1) |
| country | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top N/A (×3) |
| species | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=3, missing=3, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top The parent material is eolian from broad plain in level or undulating uplands. Reddish brown fine sandy loam (fine-loamy, mixed, thermic aridic). Original ASTER Spectral Library name was jhu.becknic.soil.alfisol.paleustalf.coarse.87P1087.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top jhu.becknic (×3) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×3) |
| signal_type | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Reflectance (percent) (×3) |
| axis_unit | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Wavelength (micrometers) (×3) |
| axis_min | metadata | numeric | *Not specified.* | n=3, missing=0, range 0.4–0.4, mean 0.4 ± 6.799e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=3, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3, missing=0, range 2844–2844, mean 2844 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×3) |
| citation | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×3) |
| license | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×3) |
| rights_status | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top manual_review_needed (×3) |
| usage_scope | metadata | categorical | *Not specified.* | n=3, missing=0, classes=1, top private_use_only (×3) |
| notes | metadata | categorical | *Not specified.* | n=3, missing=0, classes=3, top soil.alfisol.paleustalf.none.all.87p1087.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `55a2ee5a73d6aee035a1e76578dc9280e7ce5e093cc86c4033cadc0751332d14`
- **Processing hash:** `a43eefc0a13b8ee02f94bd824d41f6f7b35a47821da926966ae2c0b35fdfbc66` | **metadata hash:** `e40c1b5930fb6f13ebdb210df53196514695a89b6dfa02170028afd37e07617f`
