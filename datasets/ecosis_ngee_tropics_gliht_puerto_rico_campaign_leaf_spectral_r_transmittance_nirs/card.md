# Datasheet — EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (transmittance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017 (transmittance). v2.0 standardized NIRS package: 1 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Tropics GLiHT Puerto Rico Campaign Leaf Spectral Reflectance and Transmittance March 2017

## Composition

- **Alignment:** sample level; 222 sample(s), 223 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.005).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
| source_SampleID | metadata | categorical | *Not specified.* | n=222, missing=0, classes=222, top BNL12862T (×1) |
| source_QA_QC_Flag | metadata | categorical | *Not specified.* | n=222, missing=222, classes=0, — |
| source_Comments | metadata | categorical | *Not specified.* | n=222, missing=218, classes=1, top High water content, real? (×4) |
| source_Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Spectra Vista Corporation (×222) |
| source_Instrument_Model | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top HR-1024i (×222) |
| source_Instrument_Serial_Number | metadata | numeric | *Not specified.* | n=222, missing=0, range 2041–2041, mean 2041 ± 0 |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top SVC_Integrating_Sphere (×222) |
| source_Collection_Units | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Raw_DN (×222) |
| source_Spectra_Units | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Percent_Transmittance_0_100 (×222) |
| source_Spectra_Type | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Leaf (×222) |
| source_Reflectance_Transmittance_Type | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Relative (×222) |
| source_Measurement | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Transmittance (×222) |
| source_White_Reference_Standard | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top SVC_IS_Spectralon_Standard (×222) |
| source_Spectral_Resolution | metadata | numeric | *Not specified.* | n=222, missing=0, range 1–1, mean 1 ± 0 |
| source_Wavelength_Units | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Nanometer (×222) |
| source_Interpolation_Method | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Linear (×222) |
| source_Overlap_Handling | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Removed (×222) |
| source_Overlap_Removal | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Post_processing (×222) |
| source_Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=222, missing=0, classes=1, top Raw_DN (×222) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-tropics-gliht-puerto-rico-campaign-leaf-spectral-reflectance-and-transmittance-march-2017`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 0 fields, Y: 8 fields, passport: 48 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `d67338b6ec53448fd434859835b5244429260f8cea46b12b9ae0b7e508526749`
- **Processing hash:** `2ccb901f7d537915100a87a3e8ad28531c7505f90fc53e330374ac0d1da0db1e` | **metadata hash:** `875eb2a9863ccae9131532b4f0d8dbeefb9aef355c6964f75489905c8bcd5ccc`
