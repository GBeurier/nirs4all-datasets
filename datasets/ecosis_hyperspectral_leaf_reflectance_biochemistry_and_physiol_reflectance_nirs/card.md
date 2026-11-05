# Datasheet — Droughted and watered crops — canopy reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 118 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | canopy_spectra.csv | Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i | NIR | 350–2500 nm | 118 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Treatment | target | categorical | *Not specified.* | n=118, missing=0, classes=2, top watered (×59) |
| Plant_Age | target | numeric | *Not specified.* | n=118, missing=0, range 47–63, mean 53.38 ± 5.304 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top 8c9139b5-5f24-4925-8d7d-bb4453cfb68d (×118) |
| site | metadata | numeric | *Not specified.* | n=118, missing=0, range 2–17, mean 8.331 ± 4.676 |
| location | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Brookhaven National Laboratory (×118) |
| country | metadata | categorical | *Not specified.* | n=118, missing=118, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=118, missing=118, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=118, missing=118, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top source-provided coordinates when available (×118) |
| year | metadata | numeric | *Not specified.* | n=118, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=118, missing=0, classes=5, top 8/2/19 (×33) |
| species | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top CUPE (×118) |
| genus | metadata | categorical | *Not specified.* | n=118, missing=118, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=118, missing=118, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Leaf, Canopy (×118) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top canopy (×118) |
| instrument | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i (×118) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Proximal (×118) |
| signal_type | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top reflectance (×118) |
| axis_unit | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top nm (×118) |
| axis_min | metadata | numeric | *Not specified.* | n=118, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=118, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=118, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top 10.1093/jxb/erab255 \| 10.21232/UTK8zaW4 \| 10.21232/utk8zaw4 (×118) |
| citation | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Angela C Burnett Shawn P Serbin Kenneth J Davidson Kim S Ely Alistair Rogers. 2020. Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/UTK8zaW4 (×118) |
| license | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top Creative Commons Attribution (×118) |
| rights_status | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top explicit_open (×118) |
| usage_scope | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top public_reuse_possible (×118) |
| notes | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top EcoSIS package hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops, no interpolation applied by project. (×118) |
| source_uniquefield | metadata | categorical | *Not specified.* | n=118, missing=0, classes=118, top 2019-07-24_02_1_canopy (×1) |
| source_Location | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top field (×118) |
| source_Paired_Spectra | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top canopy (×118) |
| source_Plant | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top NA (×118) |
| source_Plot | metadata | numeric | *Not specified.* | n=118, missing=0, range 2–17, mean 8.331 ± 4.676 |
| source_Rep | metadata | numeric | *Not specified.* | n=118, missing=0, range 1–3, mean 2 ± 0.8269 |
| source_Species | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top CUPE (×118) |
| source_Days_Into_Treatment | metadata | numeric | *Not specified.* | n=118, missing=0, range 19–35, mean 25.38 ± 5.304 |
| source_Measurement_Date | metadata | categorical | *Not specified.* | n=118, missing=0, classes=5, top 8/2/19 (×33) |
| source_Instrument | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top SE_PSR_Plus (×118) |
| source_Pre_or_Post_Treatment | metadata | categorical | *Not specified.* | n=118, missing=0, classes=1, top post (×118) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M. Index fields examined: source_Rep. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 5 fields, Y: 2 fields, measurements: 1 fields, passport: 35 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Detection of the metabolic response to drought stress using hyperspectral reflectance — [10.1093/jxb/erab255](https://doi.org/10.1093/jxb/erab255)
- Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops — [10.21232/UTK8zaW4](https://doi.org/10.21232/UTK8zaW4)
- *Not specified.* — [10.21232/utk8zaw4](https://doi.org/10.21232/utk8zaw4)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `066280ad6b8709c6ce0a629829bcc9a8e688aeb01d9325c0f7fa2fceb4a9b55e`
- **Processing hash:** `b50532f4c3ee3258e6750145e591312e195de4126c54150b57e44f82738e2d68` | **metadata hash:** `9b337900680c36dbf52675342fc6f8d559c114faac3c09de37a861e57a962c86`
