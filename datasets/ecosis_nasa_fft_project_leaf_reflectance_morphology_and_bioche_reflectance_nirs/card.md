# Datasheet — EcoSIS NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests

## Composition

- **Alignment:** sample level; 1382 sample(s), 1382 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NASA_FFT_LC_Refl_Spectra_v4.csv | ASD FieldSpec Pro | NIR | 350–2500 nm | 1382 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=1382, missing=0, classes=66, top ABBA (×133) |
| LMA_QC | target | numeric | *Not specified.* | n=1382, missing=401, range 1–2, mean 1.025 ± 0.1577 |
| H2O_perc | target | numeric | *Not specified.* | n=1382, missing=401, range -9.999e+05–91.05, mean -1979 ± 4.513e+04 |
| LDMC_g_g | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–0.8251, mean -19.99 ± 451.3 |
| EWT_gDW_cm2 | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–0.1374, mean -20.37 ± 451.2 |
| SLA_cm2_gDW | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–573.8, mean 148.9 ± 341.5 |
| SLA_m2_kgDW | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–57.38, mean 5.716 ± 319.9 |
| LMA_gDW_m2 | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–346.3, mean 89.13 ± 329.6 |
| LMA_gDW_cm2 | target | numeric | *Not specified.* | n=1382, missing=401, range -9999–0.03463, mean -10.18 ± 319.2 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top 791c77e6-5484-4088-a287-ed87a7d01732 (×1382) |
| site | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=14, top DC (×190) |
| location | metadata | categorical | *Not specified.* | n=1382, missing=1382, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=1382, missing=1382, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1382, missing=22, range 39.56–47.84, mean 44.36 ± 2.356 |
| longitude | metadata | numeric | *Not specified.* | n=1382, missing=22, range -92.83–-73.74, mean -86.68 ± 6.227 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top source-provided coordinates when available (×1382) |
| year | metadata | numeric | *Not specified.* | n=1382, missing=0, range 2014–2014, mean 2014 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1382, missing=1382, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=66, top ABBA (×133) |
| genus | metadata | categorical | *Not specified.* | n=1382, missing=1382, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1382, missing=1382, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Leaf (×1382) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top leaf (×1382) |
| instrument | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top ASD FieldSpec Pro (×1382) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Contact (×1382) |
| signal_type | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top reflectance (×1382) |
| axis_unit | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top nm (×1382) |
| axis_min | metadata | numeric | *Not specified.* | n=1382, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1382, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1382, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top 10.1111/nph.16123 \| 10.21232/C2WC75 \| 10.6084/m9.figshare.745311.v1 (×1382) |
| citation | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Shawn P. Serbin Philip A. Townsend. 2014. NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1382) |
| license | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Creative Commons Attribution (×1382) |
| rights_status | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top explicit_open (×1382) |
| usage_scope | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top public_reuse_possible (×1382) |
| notes | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top EcoSIS package nasa-fft-project-leaf-reflectance-morphology-and-biochemistry-for-northern-temperate-forests, no interpolation applied by project. (×1382) |
| source_SampleID | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1382, top AK01_ACRU_B_2009 (×1) |
| source_Spectra_Name | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1366, top DC05_PIRE_MN_LC_REFL (×2) |
| source_Site | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=14, top DC (×190) |
| source_Site_Name | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=14, top Madison / Dane County (×190) |
| source_State | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=5, top Wisconsin (×742) |
| source_Plot | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=142, top NC14 (×24) |
| source_Latitude | metadata | numeric | *Not specified.* | n=1382, missing=22, range 39.56–47.84, mean 44.36 ± 2.356 |
| source_Longitude | metadata | numeric | *Not specified.* | n=1382, missing=22, range -92.83–-73.74, mean -86.68 ± 6.227 |
| source_Height | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=3, top T (×550) |
| source_Age | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=7, top NA (×786) |
| source_Height_Age | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=17, top T (×312) |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top ASD_LeafClip (×1382) |
| source_Measurement | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Reflectance (×1382) |
| source_Sample_Name | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1366, top DC05_PIRE_MN (×2) |
| source_Sample_Year | metadata | numeric | *Not specified.* | n=1382, missing=0, range 2008–2010, mean 2009 ± 0.6663 |
| source_Sample_Type | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Vegetation (×1382) |
| source_Instrumentation | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top ASD FieldSpec 3 (×1382) |
| source_Calibration | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Spectralon Ratio (×1382) |
| source_Wavelengths | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Nanometers (×1382) |
| source_Column_Units | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Fraction_0_to_1 (×1382) |
| source_Project | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top NASA Forest Functional Types (×1382) |
| source_PI | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top Philip A. Townsend (×1382) |
| source_Affiliation | metadata | categorical | *Not specified.* | n=1382, missing=0, classes=1, top FERST - University of Wisconsin Madison (×1382) |
| source_Comments | metadata | categorical | *Not specified.* | n=1382, missing=1287, classes=22, top FIRST ROUND OF SAMPLES (×20) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/nasa-fft-project-leaf-reflectance-morphology-and-biochemistry-for-northern-temperate-forests`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.745311.v1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 10 fields, Y: 8 fields, passport: 41 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests — [10.21232/C2WC75](https://doi.org/10.21232/C2WC75)
- Serbin et al. (2019) — [10.1111/nph.16123](https://doi.org/10.1111/nph.16123)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `075fffc4a4f4a065519013046392614769c357e04dfb82fda0c184ec7c04e232`
- **Processing hash:** `34f107150f38e748f7d34412fa8da73507f8f433fa87ef242d9f10ef08ec8631` | **metadata hash:** `22f140968adf43428957b81688f62fce44d5603da4c65c463d13a4b49b014e8b`
