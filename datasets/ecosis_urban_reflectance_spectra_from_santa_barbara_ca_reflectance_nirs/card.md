# Datasheet — EcoSIS Urban Reflectance Spectra from Santa Barbara, CA (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Urban Reflectance Spectra from Santa Barbara, CA (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Urban Reflectance Spectra from Santa Barbara, CA

## Composition

- **Alignment:** observation level; 1 sample(s), 1065 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1065–1065 (mean 1065).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UrbanSpectraAndMeta.csv | Analytical Spectra Devices FieldSpec 3 | NIR | 350–2498 nm | 1065 | 1075 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Time | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top 20_11 (×1) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 25463d25-37e8-4675-b339-8c05048d5561 (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Santa Barbara, California (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1, missing=0, range 34.41–34.41, mean 34.41 ± 0 |
| longitude | metadata | numeric | *Not specified.* | n=1, missing=0, range -119.7–-119.7, mean -119.7 ± 0 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2004–2004, mean 2004 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 2001_06_05 (×1) |
| species | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Bark, Soil, Other, Canopy (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Analytical Spectra Devices FieldSpec 3 (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Proximal (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 1075–1075, mean 1075 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.21232/ezrqtdcw (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top M. Herold D.A. Roberts M.E. Gardner and P.E. Dennison. 2004. Urban Reflectance Spectra from Santa Barbara, CA. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top not specified (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top manual_review_needed (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top private_use_only (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package urban-reflectance-spectra-from-santa-barbara--ca, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/urban-reflectance-spectra-from-santa-barbara--ca`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `61feca6eb7c7e65048906ceba7e3d0b61b3c7cc40b0253bc8fbf6a52b3ecf849`
- **Processing hash:** `acec472d42987f56775dbf11e2371347170c83f09218863acf6998a777472607` | **metadata hash:** `30631cd9d3146d70b3b0568fbeaca22b931a86902ab590228222980c06f6685c`
