# Datasheet — ECOSTRESS soil all axis be345a03

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis be345a03. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 4 sample(s), 4 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.98 none | 4 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=4, missing=0, classes=4, top Light yellowish brown interior dry gravelly loam (×1) |
| class_label | target | categorical | *Not specified.* | n=4, missing=0, classes=2, top Aridisol (×3) |
| subclass | target | categorical | *Not specified.* | n=4, missing=0, classes=3, top Salorthid (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top soil.aridisol.calciorthid.none.all.79p1536.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top soil (×4) |
| material_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top soil (×4) |
| site | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top 8 km north of Deir El zor, Syria via USDA Soil Conservationservice. (×1) |
| country | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top N/A (×4) |
| species | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top The parent material is alluvium from mixed material, alluvial fine material overlayed on gypsum sandy loam, uncultivated from terracettes in lake plains. Light yellowish brown interior dry gravelly loam. Original ASTER Spectral Library name was jhu.becknic.soil.aridisol.calciorthid.coarse.79P1536.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top jhu.becknic (×4) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×4) |
| signal_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Reflectance (percent) (×4) |
| axis_unit | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Wavelength (micrometers) (×4) |
| axis_min | metadata | numeric | *Not specified.* | n=4, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=4, missing=0, range 14.98–14.98, mean 14.98 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=4, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×4) |
| citation | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×4) |
| license | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×4) |
| rights_status | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top manual_review_needed (×4) |
| usage_scope | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top private_use_only (×4) |
| notes | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top soil.aridisol.calciorthid.none.all.79p1536.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `727065caefa76ebb3787a31560d4b7fe17fad2e94ab646d4aa2076f09942f04e`
- **Processing hash:** `d6095a9a557b96f5582ff77ba39d81714298b38d6510c883ed23d3674c2bd3a1` | **metadata hash:** `3ed3ac0e72c9924a0920676d002622e52fcdf9c47a14eea9366d3583a324c0ad`
