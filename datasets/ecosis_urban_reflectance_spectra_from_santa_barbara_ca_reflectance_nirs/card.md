# Datasheet — Santa Barbara urban materials — reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Urban Reflectance Spectra from Santa Barbara, CA (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Urban Reflectance Spectra from Santa Barbara, CA

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 1065 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UrbanSpectraAndMeta.csv | Analytical Spectra Devices FieldSpec 3 | NIR | 350–2498 nm | 1065 | 1075 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Time | target | numeric | *Not specified.* | n=1065, missing=1065, range —, mean *Not specified.* ± *Not specified.* |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top 25463d25-37e8-4675-b339-8c05048d5561 (×1065) |
| site | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top Santa Barbara, California (×1065) |
| country | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1065, missing=0, range 34.01–34.46, mean 34.42 ± 0.08015 |
| longitude | metadata | numeric | *Not specified.* | n=1065, missing=0, range -119.9–119.9, mean -114.2 ± 36.3 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top source-provided coordinates when available (×1065) |
| year | metadata | numeric | *Not specified.* | n=1065, missing=0, range 2004–2004, mean 2004 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=7, top 2001_06_05 (×334) |
| species | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top Bark, Soil, Other, Canopy (×1065) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1065, missing=1065, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top Analytical Spectra Devices FieldSpec 3 (×1065) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top Proximal (×1065) |
| signal_type | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top reflectance (×1065) |
| axis_unit | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top nm (×1065) |
| axis_min | metadata | numeric | *Not specified.* | n=1065, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1065, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1065, missing=0, range 1075–1075, mean 1075 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top 10.21232/ezrqtdcw (×1065) |
| citation | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top M. Herold D.A. Roberts M.E. Gardner and P.E. Dennison. 2004. Urban Reflectance Spectra from Santa Barbara, CA. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1065) |
| license | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top not specified (×1065) |
| rights_status | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top manual_review_needed (×1065) |
| usage_scope | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top private_use_only (×1065) |
| notes | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top EcoSIS package urban-reflectance-spectra-from-santa-barbara--ca, no interpolation applied by project. (×1065) |
| source_Name | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1065, top frrkof.002- (×1) |
| source_Polygon_Unit_ID | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=23, top Dennison_Home (×106) |
| source_Sampling_Unit | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top polygon (×1065) |
| source_Level_1 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=2, top impervious (×888) |
| source_Level_2 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=6, top roof (×497) |
| source_Level_3 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=28, top comp_shingle (×353) |
| source_Level_4 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=45, top asphalt (×161) |
| source_Level_5 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=10, top new (×530) |
| source_Level_6 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=18, top roof (×486) |
| source_Level_7 | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=36, top COMP_SHINGLE_ROOF (×353) |
| source_Lat | metadata | numeric | *Not specified.* | n=1065, missing=0, range 34.01–34.46, mean 34.42 ± 0.08015 |
| source_Long | metadata | numeric | *Not specified.* | n=1065, missing=0, range -119.9–119.9, mean -114.2 ± 36.3 |
| source_Date | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=7, top 2001_06_05 (×334) |
| source_Scale | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top field (×1065) |
| source_source | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=1, top asd (×1065) |
| source_photo | metadata | categorical | *Not specified.* | n=1065, missing=0, classes=26, top none (×977) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/urban-reflectance-spectra-from-santa-barbara--ca`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 10 fields, Y: 0 fields, measurements: 0 fields, passport: 35 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.21232/ezrqtdcw](https://doi.org/10.21232/ezrqtdcw)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `e90e495010f6c5c0eb7a8e2641813c4e8fefae56f33fbb341a62a88d475eb2e3`
- **Processing hash:** `55cb996fa0b1be35c387a78ae469cc96ff8e812a0bc88534eb800e6516f454cf` | **metadata hash:** `c4a2b740967ad6287186e756e6c31c75910809fb19e4802d8cac665f4165d076`
