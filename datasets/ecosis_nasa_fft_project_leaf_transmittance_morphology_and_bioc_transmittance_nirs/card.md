# Datasheet — NASA FFT temperate forest leaves — transmittance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NASA FFT Project Leaf Transmittance Morphology and Biochemistry for Northern Temperate Forests (transmittance). v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NASA FFT Project Leaf Transmittance Morphology and Biochemistry for Northern Temperate Forests

## Composition

- **Alignment:** sample level; 765 sample(s), 765 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NASA_FFT_IS_Tran_Spectra_v4.csv | *Not specified.* | NIR | 350–2500 nm | 765 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=765, missing=0, classes=57, top QURU (×67) |
| CN_QC | target | numeric | *Not specified.* | n=765, missing=317, range 1–2, mean 1.009 ± 0.09417 |
| Nmass_perc | target | numeric | *Not specified.* | n=765, missing=317, range 0.699–4.398, mean 2.129 ± 0.8771 |
| Cmass_perc | target | numeric | *Not specified.* | n=765, missing=317, range 42.62–53.65, mean 49.66 ± 1.911 |
| CNRatio | target | numeric | *Not specified.* | n=765, missing=317, range 10.52–68.62, mean 28.11 ± 12.4 |
| LMA_QC | target | numeric | *Not specified.* | n=765, missing=51, range 1–2, mean 1.017 ± 0.1286 |
| H2O_perc | target | numeric | *Not specified.* | n=765, missing=51, range -9.999e+05–91.05, mean -2741 ± 5.289e+04 |
| LDMC_g_g | target | numeric | *Not specified.* | n=765, missing=51, range -9999–0.8251, mean -27.61 ± 528.9 |
| EWT_gDW_cm2 | target | numeric | *Not specified.* | n=765, missing=51, range -9999–0.1374, mean -27.99 ± 528.8 |
| SLA_cm2_gDW | target | numeric | *Not specified.* | n=765, missing=51, range -9999–573.8, mean 140.8 ± 393.9 |
| SLA_m2_kgDW | target | numeric | *Not specified.* | n=765, missing=51, range -9999–57.38, mean 1.476 ± 374.9 |
| LMA_gDW_m2 | target | numeric | *Not specified.* | n=765, missing=51, range -9999–328.2, mean 86.62 ± 383.9 |
| LMA_gDW_cm2 | target | numeric | *Not specified.* | n=765, missing=51, range -9999–0.03282, mean -13.99 ± 374.2 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top 12ad69ce-71bf-436d-ab66-98e4eae30307 (×765) |
| site | metadata | categorical | *Not specified.* | n=765, missing=0, classes=10, top NC (×159) |
| location | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=765, missing=13, range 39.56–47.74, mean 44.12 ± 2.781 |
| longitude | metadata | numeric | *Not specified.* | n=765, missing=13, range -92.83–-78.42, mean -87.9 ± 4.917 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top source-provided coordinates when available (×765) |
| year | metadata | numeric | *Not specified.* | n=765, missing=0, range 2014–2014, mean 2014 ± 0 |
| date | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=765, missing=0, classes=57, top QURU (×67) |
| genus | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Leaf (×765) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top leaf (×765) |
| instrument | metadata | categorical | *Not specified.* | n=765, missing=765, classes=0, — |
| acquisition_mode | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Contact (×765) |
| signal_type | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top transmittance (×765) |
| axis_unit | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top nm (×765) |
| axis_min | metadata | numeric | *Not specified.* | n=765, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=765, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=765, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top 10.1111/nph.16123 \| 10.21232/C2WC75 \| 10.6084/m9.figshare.745311.v1 (×765) |
| citation | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Shawn P. Serbin Philip A. Townsend. 2014. NASA FFT Project Leaf Transmittance Morphology and Biochemistry for Northern Temperate Forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×765) |
| license | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Open Data Commons Attribution License (×765) |
| rights_status | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top explicit_open (×765) |
| usage_scope | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top public_reuse_possible (×765) |
| notes | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top EcoSIS package nasa-fft-project-leaf-transmittance-morphology-and-biochemistry-for-northern-temperate-forests, no interpolation applied by project. (×765) |
| source_SampleID | metadata | categorical | *Not specified.* | n=765, missing=0, classes=765, top BH02_ACRU_B_2008 (×1) |
| source_Spectra_Name | metadata | categorical | *Not specified.* | n=765, missing=0, classes=765, top BH02_ACRU_B_IS_TRAN (×1) |
| source_Site | metadata | categorical | *Not specified.* | n=765, missing=0, classes=10, top NC (×159) |
| source_Site_Name | metadata | categorical | *Not specified.* | n=765, missing=0, classes=10, top Flambeau River SF / Cheq. NF (×159) |
| source_State | metadata | categorical | *Not specified.* | n=765, missing=0, classes=3, top Wisconsin (×488) |
| source_Plot | metadata | categorical | *Not specified.* | n=765, missing=0, classes=83, top NC14 (×24) |
| source_Latitude | metadata | numeric | *Not specified.* | n=765, missing=13, range 39.56–47.74, mean 44.12 ± 2.781 |
| source_Longitude | metadata | numeric | *Not specified.* | n=765, missing=13, range -92.83–-78.42, mean -87.9 ± 4.917 |
| source_Height | metadata | categorical | *Not specified.* | n=765, missing=0, classes=3, top T (×294) |
| source_Age | metadata | categorical | *Not specified.* | n=765, missing=0, classes=6, top NA (×462) |
| source_Height_Age | metadata | categorical | *Not specified.* | n=765, missing=0, classes=16, top T (×177) |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top ASD_Integrating_Sphere (×765) |
| source_Measurement | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Transmittance (×765) |
| source_Sample_Name | metadata | categorical | *Not specified.* | n=765, missing=0, classes=765, top BH02_ACRU_B (×1) |
| source_Sample_Year | metadata | numeric | *Not specified.* | n=765, missing=0, range 2008–2010, mean 2008 ± 0.4084 |
| source_Sample_Type | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Vegetation (×765) |
| source_Instrumentation | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top ASD FieldSpec 3 (×765) |
| source_Calibration | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Spectralon Ratio (×765) |
| source_Wavelengths | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Nanometers (×765) |
| source_Column_Units | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Percent (×765) |
| source_Project | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top NASA Forest Functional Types (×765) |
| source_PI | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top Philip A. Townsend (×765) |
| source_Affiliation | metadata | categorical | *Not specified.* | n=765, missing=0, classes=1, top FERST - University of Wisconsin Madison (×765) |
| source_Comments | metadata | categorical | *Not specified.* | n=765, missing=763, classes=2, top LOW SAMPLE WEIGHT (×1) |
| source_Comments_aux | metadata | categorical | *Not specified.* | n=765, missing=737, classes=13, top CHANGED FROM ACSA TO ACSM (×9) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/nasa-fft-project-leaf-transmittance-morphology-and-biochemistry-for-northern-temperate-forests`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.745311.v1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 10 fields, Y: 11 fields, measurements: 2 fields, passport: 41 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests — [10.21232/C2WC75](https://doi.org/10.21232/C2WC75)
- Serbin et al. (2019) — [10.1111/nph.16123](https://doi.org/10.1111/nph.16123)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `9cf5ba7f83ad131c5fa11dac4ed6ad65acc9a1ec1e6bc9318461b08694b84091`
- **Processing hash:** `deab7456cc14444041295b51d84ca1399205d246e4f40cdcf92285f63e4e5850` | **metadata hash:** `749db1e6ae75f9773e437cd75c4d5f708218abfe7285be38e707bed7b0cc3fb4`
