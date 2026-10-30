# Datasheet — EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data

## Composition

- **Alignment:** sample level; 2181 sample(s), 2415 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.107).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra.csv | Analytical Spectral Devices, Spectral Evolution FieldSpec3, PSR-3500 | NIR | 350–2500 nm | 2415 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| USDA_Species_Code | target | categorical | *Not specified.* | n=2181, missing=24, classes=41, top SOLY2 (×141) |
| Target_Type | target | categorical | *Not specified.* | n=2181, missing=0, classes=6, top Vegetation (×2151) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top db21126e-7517-4fa2-a578-dfedb9df88bf (×2181) |
| site | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=13, top KARE (×427) |
| location | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top NASA HyspIRI Airborne Campaign (×2181) |
| country | metadata | categorical | *Not specified.* | n=2181, missing=2181, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range 32.81–38.54, mean 35.66 ± 1.817 |
| longitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range -121.9–-115.4, mean -118.6 ± 1.838 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top source-provided coordinates when available (×2181) |
| year | metadata | numeric | *Not specified.* | n=2181, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2181, missing=2181, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2181, missing=2181, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2181, missing=2181, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2181, missing=2181, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Leaf, Canopy, Mineral, NPV, Reference, Rock, Soil (×2181) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top canopy (×2181) |
| instrument | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Analytical Spectral Devices, Spectral Evolution FieldSpec3, PSR-3500 (×2181) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Contact, Proximal (×2181) |
| signal_type | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top reflectance (×2181) |
| axis_unit | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top nm (×2181) |
| axis_min | metadata | numeric | *Not specified.* | n=2181, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2181, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2181, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top 10.1016/j.rse.2015.05.024 \| 10.1111/nph.16123 (×2181) |
| citation | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Shawn P. Serbin Sean DuBois Andrew Jablonski Alexey Shiklomanov Ankur Desai Eric L. Kruger Philip A. Townsend. 2019. UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×2181) |
| license | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Creative Commons Attribution (×2181) |
| rights_status | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top explicit_open (×2181) |
| usage_scope | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top public_reuse_possible (×2181) |
| notes | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top EcoSIS package uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data, no interpolation applied by project. (×2181) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon original conservé sous un nom préfixé/équivalent ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
- **Curated views:** M: 11 fields, Y: 2 fields, passport: 34 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `95dad6ec5c795398dc3be46ab4b5e6bda06826c3cf22d3ccfe0201c71d93db2e`
- **Processing hash:** `bdabf780cf590008980be8cba75601aab698c1ee9b60bbf5950c389522c9653e` | **metadata hash:** `f384b2447813dd8c5df603bb617bee363304e733e6068a578ad0010ffe923c0a`
