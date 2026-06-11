# Datasheet — EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data

## Composition

- **Alignment:** observation level; 2415 sample(s), 2415 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra.csv | Analytical Spectral Devices, Spectral Evolution FieldSpec3, PSR-3500 | NIR | 350–2500 nm | 2415 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| USDA_Species_Code | target | categorical | *Not specified.* | n=2415, missing=24, classes=41, top SOLY2 (×163) |
| Target_Type | target | categorical | *Not specified.* | n=2415, missing=0, classes=6, top Vegetation (×2385) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top db21126e-7517-4fa2-a578-dfedb9df88bf (×2415) |
| site | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=13, top KARE (×433) |
| location | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top NASA HyspIRI Airborne Campaign (×2415) |
| country | metadata | categorical | *Not specified.* | n=2415, missing=2415, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=2415, missing=59, range 32.81–38.54, mean 35.6 ± 1.826 |
| longitude | metadata | numeric | *Not specified.* | n=2415, missing=59, range -121.9–-115.4, mean -118.5 ± 1.845 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top source-provided coordinates when available (×2415) |
| year | metadata | numeric | *Not specified.* | n=2415, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2415, missing=2415, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2415, missing=2415, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2415, missing=2415, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2415, missing=2415, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top Leaf, Canopy, Mineral, NPV, Reference, Rock, Soil (×2415) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top canopy (×2415) |
| instrument | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top Analytical Spectral Devices, Spectral Evolution FieldSpec3, PSR-3500 (×2415) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top Contact, Proximal (×2415) |
| signal_type | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top reflectance (×2415) |
| axis_unit | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top nm (×2415) |
| axis_min | metadata | numeric | *Not specified.* | n=2415, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2415, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2415, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top 10.1016/j.rse.2015.05.024 \| 10.1111/nph.16123 (×2415) |
| citation | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top Shawn P. Serbin Sean DuBois Andrew Jablonski Alexey Shiklomanov Ankur Desai Eric L. Kruger Philip A. Townsend. 2019. UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×2415) |
| license | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top Creative Commons Attribution (×2415) |
| rights_status | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top explicit_open (×2415) |
| usage_scope | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top public_reuse_possible (×2415) |
| notes | metadata | categorical | *Not specified.* | n=2415, missing=0, classes=1, top EcoSIS package uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data, no interpolation applied by project. (×2415) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Remotely estimating photosynthetic capacity, and its response to temperature, in vegetation canopies using imaging spectroscopy — [10.1016/j.rse.2015.05.024](https://doi.org/10.1016/j.rse.2015.05.024)
- From the Arctic to the tropics: multibiome prediction of leaf mass per area using leaf reflectance — [10.1111/nph.16123](https://doi.org/10.1111/nph.16123)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `3d6c17e9bf6ee7aec3d2e61466d9855f3a6039ab8b6b48282c671f2d0f9f6010`
- **Processing hash:** `4d3ac43feaa374b94ff290d6d48a4d010b5bdab522e8765bbc3c7ad8d5933337` | **metadata hash:** `cd2b53059e2d48c427eda812f5d545fe477ee55a73dad761bdab7d62560e5be8`
