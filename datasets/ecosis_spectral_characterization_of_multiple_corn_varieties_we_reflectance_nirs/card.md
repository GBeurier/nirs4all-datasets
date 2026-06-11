# Datasheet — EcoSIS Spectral Characterization of Multiple Corn Varieties: West Madison Agricultural Station 2014 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Spectral Characterization of Multiple Corn Varieties: West Madison Agricultural Station 2014 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Spectral Characterization of Multiple Corn Varieties: West Madison Agricultural Station 2014

## Composition

- **Alignment:** observation level; 288 sample(s), 288 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | West_Madison_corn_spectra.csv | Analytical Spectral Devices Inc.  ASD FieldSpec 3 | NIR | 350–2500 nm | 288 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Variety | target | categorical | *Not specified.* | n=288, missing=0, classes=24, top 22734 (×12) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top 6962916e-074f-45af-b243-b41c1a87ade5 (×288) |
| site | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top source-provided coordinates when available (×288) |
| year | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top Leaf (×288) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top Analytical Spectral Devices Inc. ASD FieldSpec 3 (×288) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top Contact (×288) |
| signal_type | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top reflectance (×288) |
| axis_unit | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top nm (×288) |
| axis_min | metadata | numeric | *Not specified.* | n=288, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=288, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=288, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=288, missing=288, classes=0, — |
| license | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top not specified (×288) |
| rights_status | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top manual_review_needed (×288) |
| usage_scope | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top private_use_only (×288) |
| notes | metadata | categorical | *Not specified.* | n=288, missing=0, classes=1, top EcoSIS package spectral-characterization-of-multiple-corn-varieties--west-madison-agricultural-station-2014, no interpolation applied by project. (×288) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/spectral-characterization-of-multiple-corn-varieties--west-madison-agricultural-station-2014`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `ec26778844dad1549630fa0d2316583fb2d35d2323ae0cea863fd821e4155baa`
- **Processing hash:** `f817f7ae1bc5409b62fb0c549343270e52655d53e44e836252dd134b9700f0c8` | **metadata hash:** `f9eef4f7031f67bd65d99c8234e003b9c9e1e89c505e60068e61e94d17c549b0`
