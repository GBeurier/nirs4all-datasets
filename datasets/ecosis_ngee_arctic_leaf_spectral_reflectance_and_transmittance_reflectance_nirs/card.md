# Datasheet — EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 10 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska

## Composition

- **Alignment:** observation level; 199 sample(s), 199 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NGEE-Arctic_Barrow_2016_SVCHR1024i_Leaf_Spectral_Reflectance.csv | Spectra Vista Corporation HR-1024i | NIR | 350–2500 nm | 199 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| USDA_Species_Code | target | categorical | *Not specified.* | n=199, missing=0, classes=6, top CAAQ (×46) |
| C_mass_mg_g | target | numeric | *Not specified.* | n=199, missing=0, range -9999–626.8, mean -968.1 ± 3587 |
| C_mass_g_g | target | numeric | *Not specified.* | n=199, missing=0, range -9999–62.7, mean -775.1 ± 2652 |
| N_mass_mg_g | target | numeric | *Not specified.* | n=199, missing=0, range -9999–44.6, mean -1335 ± 3441 |
| N_mass_g_g | target | numeric | *Not specified.* | n=199, missing=0, range -9999–4.5, mean -1354 ± 3434 |
| LMA_g_m2 | target | numeric | *Not specified.* | n=199, missing=0, range -9999–112.8, mean -82.91 ± 1230 |
| C_area_g_m2 | target | numeric | *Not specified.* | n=199, missing=0, range -9999–50.88, mean -1480 ± 3598 |
| N_area_g_m2 | target | numeric | *Not specified.* | n=199, missing=0, range -9999–3.56, mean -1506 ± 3587 |
| CN_ratio | target | numeric | *Not specified.* | n=199, missing=0, range -9999–63.19, mean -1338 ± 3440 |
| USDA_Species_Code_aux | target | categorical | *Not specified.* | n=199, missing=0, classes=6, top CAAQ (×46) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top 0abf3f1f-eb51-4ae6-add8-e8f37f2a664b (×199) |
| site | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top Barrow (Utqiagvik) Environmental Observatory (×199) |
| location | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top source-provided coordinates when available (×199) |
| year | metadata | numeric | *Not specified.* | n=199, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=199, missing=0, classes=12, top 20160718 (×27) |
| species | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=199, missing=199, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top Leaf (×199) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top leaf (×199) |
| instrument | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×199) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top Contact (×199) |
| signal_type | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top reflectance (×199) |
| axis_unit | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top nm (×199) |
| axis_min | metadata | numeric | *Not specified.* | n=199, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=199, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=199, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top 10.5440/1336809 \| 10.5440/1336812 \| 10.5440/1437044 \| 10.5440/1482338 (×199) |
| citation | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top Shawn Serbin Wil Lieberman-Cribbin Kim Ely Alistair Rogers. 2019. NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). https://doi.org/10.5440/1437044 (×199) |
| license | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top not specified (×199) |
| rights_status | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top manual_review_needed (×199) |
| usage_scope | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top private_use_only (×199) |
| notes | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top EcoSIS package ngee-arctic-leaf-spectral-reflectance-and-transmittance-data-2014-to-2016-utqiagvik--barrow--alaska, no interpolation applied by project. (×199) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-leaf-spectral-reflectance-and-transmittance-data-2014-to-2016-utqiagvik--barrow--alaska`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- NGEE Arctic Leaf Spectral Reflectance and Transmittance, Barrow, Alaska, 2014-2016 — [10.5440/1437044](https://doi.org/10.5440/1437044)
- Leaf Mass Area, Leaf Carbon and Nitrogen Content, Barrow, Alaska, 2012-2016 — [10.5440/1336812](https://doi.org/10.5440/1336812)
- Leaf Photosynthetic Parameters Vcmax and Jmax and Supporting Gas Exchange Data, Barrow, Alaska, 2012-2016 — [10.5440/1336809](https://doi.org/10.5440/1336809)
- Leaf Photosynthetic Parameters: Quantum Yield, Convexity, Respiration, Gross CO2 Assimilation Rate and Raw Gas Exchange Data, Barrow, Alaska, 2016 — [10.5440/1482338](https://doi.org/10.5440/1482338)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `760b2e35047f9da4fa6231019aa7d3563fe25bda214fc5bd0251e0f919977d46`
- **Processing hash:** `8e296bfe6a68b589a192c23a576a8c63da8f657632d33a5b3864826ff7b354ba` | **metadata hash:** `b8983db4093d726b546235c93f60a28841bfea864d0527a881d9c1f6805b8482`
