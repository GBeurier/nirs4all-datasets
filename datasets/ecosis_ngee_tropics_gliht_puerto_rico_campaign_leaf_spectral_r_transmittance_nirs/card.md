# Datasheet — EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (transmittance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (transmittance). v2.0 standardized NIRS package: 1 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017

## Composition

- **Alignment:** observation level; 222 sample(s), 223 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.005).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ngee-tropics_puerto_rico_march2017_leaf_spectral_transmittance.csv | Spectra Vista Corporation, Spectral Evolution HR-1024i, PSR Plus | NIR | 350–2500 nm | 223 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Leaf_H2O_pc | target | numeric | *Not specified.* | n=222, missing=7, range 44.19–84.63, mean 60.61 ± 9.281 |
| SLA | target | numeric | *Not specified.* | n=222, missing=7, range -9999–297, mean 69.49 ± 691.6 |
| LMA | target | numeric | *Not specified.* | n=222, missing=7, range -9999–343.8, mean 56.04 ± 690.8 |
| Cmass | target | numeric | *Not specified.* | n=222, missing=62, range 358.2–553.1, mean 486 ± 31.09 |
| Nmass | target | numeric | *Not specified.* | n=222, missing=62, range 9.6–52.2, mean 20.67 ± 6.966 |
| CNratio | target | numeric | *Not specified.* | n=222, missing=62, range 9.03–50.98, mean 26.11 ± 8.78 |
| Carea | target | numeric | *Not specified.* | n=222, missing=62, range -9999–168.9, mean -11.84 ± 794.9 |
| Narea | target | numeric | *Not specified.* | n=222, missing=62, range -9999–4.57, mean -60.51 ± 790.6 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top 4d62bf32-4045-4fdf-87cc-8320076a453a (×222) |
| site | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top source-provided coordinates when available (×222) |
| year | metadata | numeric | *Not specified.* | n=222, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Leaf (×222) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top leaf (×222) |
| instrument | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Spectra Vista Corporation, Spectral Evolution HR-1024i, PSR Plus (×222) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Contact (×222) |
| signal_type | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top transmittance (×222) |
| axis_unit | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top nm (×222) |
| axis_min | metadata | numeric | *Not specified.* | n=222, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=222, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=222, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top 10.15486/ngt/1495202 \| 10.15486/ngt/1495204 (×222) |
| citation | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Shawn Serbin Ran Meng Jin Wu Kim Ely. 2019. NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). http://dx.doi.org/10.15486/ngt/1495204 (×222) |
| license | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Open Data Commons Attribution License (×222) |
| rights_status | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top explicit_open (×222) |
| usage_scope | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top public_reuse_possible (×222) |
| notes | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top EcoSIS package ngee-tropics-gliht-puerto-rico-campaign-leaf-spectral-reflectance-and-transmittance-march-2017, no interpolation applied by project. (×222) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-tropics-gliht-puerto-rico-campaign-leaf-spectral-reflectance-and-transmittance-march-2017`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- G-LiHT Campaign Leaf Spectral Reflectance and Transmittance, Mar2017: Puerto Rico — [10.15486/ngt/1495204](https://doi.org/10.15486/ngt/1495204)
- G-LiHT Campaign Leaf Mass Area and Water Content, Mar2017: Puerto Rico — [10.15486/ngt/1495202](https://doi.org/10.15486/ngt/1495202)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `3e1d84f809bd8c5a2bfb1d19c87eae38347913420a8cde02ee516601775270a4`
- **Processing hash:** `d883331b2331eca54e78f59b7613458e387e03b17a2617fb8298fa2922ec4866` | **metadata hash:** `23648fb8f3a0b6ce19857ebc4aa016c1d2394573bbc7518ef64d01e0f1bce73d`
