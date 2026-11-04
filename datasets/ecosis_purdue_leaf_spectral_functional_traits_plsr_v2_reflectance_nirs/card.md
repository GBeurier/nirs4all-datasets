# Datasheet — EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2

## Composition

- **Alignment:** sample level; 987 sample(s), 987 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | 2018+2019_stress_six_leaf_traits_spec.csv | Spectravista Corporation HR-1024i | NIR | 350–2500 nm | 987 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Data_Collection_Date | target | categorical | *Not specified.* | n=987, missing=0, classes=15, top 20180727 (×98) |
| Genus | target | categorical | *Not specified.* | n=987, missing=0, classes=2, top Juglans (×839) |
| Species | target | categorical | *Not specified.* | n=987, missing=0, classes=2, top nigra (×839) |
| Plant_ID | target | categorical | *Not specified.* | n=987, missing=0, classes=146, top p3 (×50) |
| E18_SoilTypes | target | categorical | *Not specified.* | n=987, missing=0, classes=4, top noTreatment (×815) |
| Foliar_Trait_Code | target | categorical | *Not specified.* | n=987, missing=0, classes=3, top 1 (×449) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 119086c5-0492-4bb6-b508-aabf2dd49614 (×987) |
| site | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top West Lafayette, IN, USA (×987) |
| country | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=987, missing=0, range 40.42–40.43, mean 40.43 ± 0.004691 |
| longitude | metadata | numeric | *Not specified.* | n=987, missing=0, range -87.04–-86.91, mean -86.98 ± 0.06194 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top source-provided coordinates when available (×987) |
| year | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top USDA NIFA (2016-2023) / CAFS (2021-2024) / HTIRC (2018-2021) (×987) |
| date | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top nigra (×839) |
| genus | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top Juglans (×839) |
| family | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Leaf (×987) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top leaf (×987) |
| instrument | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Spectravista Corporation HR-1024i (×987) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Contact (×987) |
| signal_type | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top reflectance (×987) |
| axis_unit | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top nm (×987) |
| axis_min | metadata | numeric | *Not specified.* | n=987, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=987, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=987, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 10.21232/bCRYo6R2 (×987) |
| citation | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Minjee Park Lorenzo Cotrozzi Geoffrey M Williams Matthew D Ginzel Michael V Mickelbart Douglass F Jacobs John J Couture. USDA NIFA (2016-2023) / CAFS (2021-2024) / HTIRC (2018-2021). Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/bCRYo6R2 (×987) |
| license | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Other (Open) (×987) |
| rights_status | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top explicit_open (×987) |
| usage_scope | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top public_reuse_possible (×987) |
| notes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top EcoSIS package purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling-v2, no interpolation applied by project. (×987) |
| source_Unique_ID | metadata | categorical | *Not specified.* | n=987, missing=0, classes=987, top E18_20180704_Black_walnut_p1_Control_Plantation_1 (×1) |
| source_Experiment_ID | metadata | categorical | *Not specified.* | n=987, missing=0, classes=4, top 2019_EEL (×326) |
| source_Site_Name | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top EEL (×498) |
| source_Latitude | metadata | numeric | *Not specified.* | n=987, missing=0, range 40.42–40.43, mean 40.43 ± 0.004691 |
| source_Longitude | metadata | numeric | *Not specified.* | n=987, missing=0, range -87.04–-86.91, mean -86.98 ± 0.06194 |
| source_Common_name | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top Black_walnut (×839) |
| source_E18_Fungal_Infection | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×815) |
| source_W18_Nitrogen_Deficiency | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| source_W18_Drought | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| source_E19_Fungal_Infection | metadata | categorical | *Not specified.* | n=987, missing=0, classes=5, top noTreatment (×661) |
| source_E19_Drought | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×661) |
| source_W19_Nitrogen_Deficiency | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×692) |
| source_W19_Salt_Deposition | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×692) |
| source_CO2_assimilation_rate | metadata | categorical | *Not specified.* | n=987, missing=0, classes=450, top noData (×538) |
| source_Specific_leaf_area | metadata | categorical | *Not specified.* | n=987, missing=0, classes=340, top noData (×647) |
| source_Leaf_water_content | metadata | categorical | *Not specified.* | n=987, missing=0, classes=341, top noData (×647) |
| source_Nitrogen | metadata | categorical | *Not specified.* | n=987, missing=0, classes=130, top noData (×791) |
| source_Sugars | metadata | categorical | *Not specified.* | n=987, missing=0, classes=197, top noData (×791) |
| source_Gallic_acid | metadata | categorical | *Not specified.* | n=987, missing=0, classes=198, top noData (×790) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling-v2`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Unique source identifier including experiment and date; grouped by the source column retained in M. Exported multiplicity does not prove the number of scans averaged upstream.
- **Curated views:** M: 12 fields, Y: 5 fields, passport: 31 fields, measurements: 6 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 — [10.21232/bCRYo6R2](https://doi.org/10.21232/bCRYo6R2)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `3058cc9a4aeab89a9d917116d80e51d1a5bb90ff763a4add1c728af55157c751`
- **Processing hash:** `edb63058634577023461a0bd75a1a85cebd0daa32d15505784fed2fe37ee596c` | **metadata hash:** `6167b12ee5c02f2b65ddea9cf397e4710b45e2ef986776c519155fd23850d716`
