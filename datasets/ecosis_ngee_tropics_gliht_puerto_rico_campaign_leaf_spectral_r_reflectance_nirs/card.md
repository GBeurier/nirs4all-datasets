# Datasheet — EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017

## Composition

- **Alignment:** observation level; 302 sample(s), 357 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.182).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ngee-tropics_puerto_rico_march2017_leaf_spectral_reflectance.csv | Spectra Vista Corporation, Spectral Evolution HR-1024i, PSR Plus | NIR | 350–2500 nm | 357 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Leaf_H2O_pc | target | numeric | *Not specified.* | n=302, missing=14, range 44.19–84.63, mean 59.97 ± 8.997 |
| SLA | target | numeric | *Not specified.* | n=302, missing=14, range -9999–309.2, mean 80.09 ± 597.9 |
| LMA | target | numeric | *Not specified.* | n=302, missing=14, range -9999–343.8, mean 68.02 ± 597.2 |
| Overlap_Matching_Type | target | categorical | *Not specified.* | n=302, missing=0, classes=2, top Reflectance (×253) |
| Cmass | target | numeric | *Not specified.* | n=302, missing=92, range 237.8–553.1, mean 485.7 ± 34.65 |
| Nmass | target | numeric | *Not specified.* | n=302, missing=92, range 7.7–52.2, mean 20.69 ± 6.68 |
| CNratio | target | numeric | *Not specified.* | n=302, missing=92, range 9.03–50.98, mean 25.84 ± 8.331 |
| Carea | target | numeric | *Not specified.* | n=302, missing=92, range -9999–168.9, mean 2.792 ± 693.9 |
| Narea | target | numeric | *Not specified.* | n=302, missing=92, range -9999–4.57, mean -45.63 ± 690.1 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top 2f70d9da-e48b-4772-8b50-a371a4a58b48 (×302) |
| site | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top source-provided coordinates when available (×302) |
| year | metadata | numeric | *Not specified.* | n=302, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=302, missing=302, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top Leaf (×302) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top leaf (×302) |
| instrument | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top Spectra Vista Corporation, Spectral Evolution HR-1024i, PSR Plus (×302) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top Contact (×302) |
| signal_type | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top reflectance (×302) |
| axis_unit | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top nm (×302) |
| axis_min | metadata | numeric | *Not specified.* | n=302, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=302, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=302, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top 10.15486/ngt/1495202 \| 10.15486/ngt/1495204 (×302) |
| citation | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top Shawn Serbin Ran Meng Jin Wu Kim Ely. 2019. NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). http://dx.doi.org/10.15486/ngt/1495204 (×302) |
| license | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top Open Data Commons Attribution License (×302) |
| rights_status | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top explicit_open (×302) |
| usage_scope | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top public_reuse_possible (×302) |
| notes | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top EcoSIS package ngee-tropics-gliht-puerto-rico-campaign-leaf-spectral-reflectance-and-transmittance-march-2017, no interpolation applied by project. (×302) |

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
- **Content hash:** `54fc6f9930878cab8e3c7b8029f9479a39d1c3088aecb2a467a58caccb119975`
- **Processing hash:** `44e7bd0309bfedcf9026c531fa559eb56ee5fdd60c39e34895ab6b035f239b51` | **metadata hash:** `631f47d66b446837d3a22f6770c9453f7eecbf5a475948b7a3e59f0b4760bebf`
