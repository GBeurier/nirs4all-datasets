# Datasheet — EcoSIS 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits

## Composition

- **Alignment:** sample level; 156 sample(s), 156 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | tall_2018_ecosis_spectra.csv | Spectra Vista Corporation SVC HR-1024i Spectroradiometer with an attached LC-RP-Pro leaf clip foreoptic | NIR | 338.9–2509 nm | 156 | 992 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Genus | target | categorical | *Not specified.* | n=156, missing=0, classes=5, top Quercus (×63) |
| Species | target | categorical | *Not specified.* | n=156, missing=0, classes=10, top falcate (×18) |
| Sample_Height | target | numeric | *Not specified.* | n=156, missing=0, range 2.5–30.32, mean 13.93 ± 7.255 |
| DBH | target | numeric | *Not specified.* | n=156, missing=0, range 18.3–62.3, mean 38.63 ± 10.3 |
| LMA | target | numeric | *Not specified.* | n=156, missing=0, range 34.22–326, mean 106.2 ± 81.52 |
| N | target | numeric | *Not specified.* | n=156, missing=117, range 0.55–2.64, mean 1.738 ± 0.554 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top bb0d7efd-c65b-44e0-a014-839a9ddd9a35 (×156) |
| site | metadata | categorical | *Not specified.* | n=156, missing=156, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Talladega National Forest (TALL) NEON Field Site (×156) |
| country | metadata | categorical | *Not specified.* | n=156, missing=156, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=156, missing=0, range 4.617e+05–4.639e+05, mean 4.632e+05 ± 682.7 |
| longitude | metadata | numeric | *Not specified.* | n=156, missing=0, range 3.645e+06–3.648e+06, mean 3.646e+06 ± 876.4 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top source-provided coordinates when available (×156) |
| year | metadata | numeric | *Not specified.* | n=156, missing=0, range 2018–2018, mean 2018 ± 0 |
| date | metadata | categorical | *Not specified.* | n=156, missing=0, classes=10, top 20180514 (×24) |
| species | metadata | categorical | *Not specified.* | n=156, missing=0, classes=10, top falcate (×18) |
| genus | metadata | categorical | *Not specified.* | n=156, missing=0, classes=5, top Quercus (×63) |
| family | metadata | categorical | *Not specified.* | n=156, missing=156, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Leaf (×156) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top leaf (×156) |
| instrument | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Spectra Vista Corporation SVC HR-1024i Spectroradiometer with an attached LC-RP-Pro leaf clip foreoptic (×156) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Contact (×156) |
| signal_type | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top reflectance (×156) |
| axis_unit | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top nm (×156) |
| axis_min | metadata | numeric | *Not specified.* | n=156, missing=0, range 338.9–338.9, mean 338.9 ± 5.703e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=156, missing=0, range 2509–2509, mean 2509 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=156, missing=0, range 992–992, mean 992 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top 10.21232/dep7jvyq \| 10.21232/kRB5Gjgi (×156) |
| citation | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Aaron G. Kamoske Kyla M. Dahlin Shawn P. Serbin and Scott C. Stark. 2018. 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/kRB5Gjgi (×156) |
| license | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top Other (Public Domain) (×156) |
| rights_status | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top explicit_open (×156) |
| usage_scope | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top public_reuse_possible (×156) |
| notes | metadata | categorical | *Not specified.* | n=156, missing=0, classes=1, top EcoSIS package 2018-talladega-national-forest--leaf-level-reflectance-spectra-and-foliar-traits, no interpolation applied by project. (×156) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2018-talladega-national-forest--leaf-level-reflectance-spectra-and-foliar-traits`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 4 fields, Y: 6 fields, passport: 30 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits — [10.21232/kRB5Gjgi](https://doi.org/10.21232/kRB5Gjgi)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `216bc8d216de3fab94cf2b72b3a9f912fd974184955c1a7f4323d6460b21dcf5`
- **Processing hash:** `ab7a1f80c22f609afa92a8bb340ecb77aed732e22911528925c1ba58f6b4aabb` | **metadata hash:** `8e59798902eb92f138b41f233a50949cf7b86267ada78888a67c8adda2054579`
