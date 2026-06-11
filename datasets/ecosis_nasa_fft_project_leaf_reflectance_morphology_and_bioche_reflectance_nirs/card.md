# Datasheet — EcoSIS NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NASA FFT Project Leaf Reflectance Morphology and Biochemistry for Northern Temperate Forests

## Composition

- **Alignment:** observation level; 1382 sample(s), 1382 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

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

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/nasa-fft-project-leaf-reflectance-morphology-and-biochemistry-for-northern-temperate-forests`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.745311.v1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `8ae9d328b648de5080373ebea5369728c6c29d6328b86fc4bcd8e2a0d3601708`
- **Processing hash:** `30b7f3671c73ab2731c976b5e64ff44d8c0cd84bc5ccfab3d1f70233b765c23f` | **metadata hash:** `ab56829e7fac136ad3ea04340abd2c8eab5fabb93bf9c75b3829c3416a5dfad0`
