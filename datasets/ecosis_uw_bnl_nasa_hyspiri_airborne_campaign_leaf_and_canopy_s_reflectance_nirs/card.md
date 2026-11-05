# Datasheet — UW-BNL HyspIRI — leaf + canopy reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (reflectance). Origin database composed from 4 standardized v2.0 leaves: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
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
| latitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range 32.81–38.54, mean 35.66 ± 1.817 |
| longitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range -121.9–-115.4, mean -118.6 ± 1.838 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top source-provided coordinates when available (×2181) |
| year | metadata | numeric | *Not specified.* | n=2181, missing=0, range 2019–2019, mean 2019 ± 0 |
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
| LMA_gDW_cm2 | target | numeric | *Not specified.* | n=2181, missing=2107, range 0.003656–0.03929, mean 0.01636 ± 0.009912 |
| N_mass_g_g | target | numeric | *Not specified.* | n=2181, missing=1920, range 0.57–4.82, mean 1.877 ± 1.015 |
| SLA_cm2_g_DW | target | numeric | *Not specified.* | n=2181, missing=2107, range 25.45–273.5, mean 91.57 ± 60.06 |
| source_Unique_Sample_ID | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=2181, top CVARS_Row08_LemonTree_L1T7N_LC_R_41432 (×1) |
| source_Spectra_Name | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=2116, top CVARS_Plot1_CAAN4_L1T1N_LC_RG (×2) |
| source_Sample_Name | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1842, top MCON_Tower_PILA_L5M1 (×5) |
| source_Site | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=13, top KARE (×427) |
| source_Site_Long | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=13, top Kearney Agricultural Research and Extension Center (×427) |
| source_Sample_Date | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=65, top 6/7/15 (×110) |
| source_Latitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range 32.81–38.54, mean 35.66 ± 1.817 |
| source_Longitude | metadata | numeric | *Not specified.* | n=2181, missing=41, range -121.9–-115.4, mean -118.6 ± 1.838 |
| source_Instrument | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=3, top ASD_FS3 (×1248) |
| source_Acquisition_Method | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=5, top LC (×1664) |
| source_Measurement_Quantity | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=2, top Reflectance (×1823) |
| source_Leaf_or_Canopy | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=2, top leaf (×2025) |
| source_GasExchange_Leaf | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=2, top no (×1527) |
| source_Spectra_Units | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top Ratio (×2181) |
| source_Wavelength_Units | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top nanometers (×2181) |
| source_Spectral_Resolution | metadata | categorical | *Not specified.* | n=2181, missing=0, classes=1, top 1nm (×2181) |
| SpectralRep | metadata | numeric | *Not specified.* | n=2181, missing=1903, range 1–1, mean 1 ± 0 |
| Unique_Sample_ID | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=278, top CVARS_Plot1_CAAN4_L1T1N_LC_RG_41430 (×1) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=276, top CVARS_Plot1_CAAN4_L2M1O_LC_RG (×2) |
| Sample_Name | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=266, top CVARS_Plot1_CAAN4_L2M1O (×2) |
| Site | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=9, top SJJR (×75) |
| Site_Long | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=9, top San Jacinto James Reserve (×75) |
| Sample_Date | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=37, top 6/16/13 (×16) |
| Latitude | metadata | numeric | *Not specified.* | n=2181, missing=1911, range 33.52–37.12, mean 35.4 ± 1.652 |
| Longitude | metadata | numeric | *Not specified.* | n=2181, missing=1911, range -119.7–-116.1, mean -118.2 ± 1.375 |
| Instrument | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=3, top ASD_FS3 (×138) |
| Acquisition_Method | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top LC (×278) |
| Measurement_Quantity | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top Reflectance (×278) |
| Leaf_or_Canopy | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top leaf (×278) |
| GasExchange_Leaf | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=2, top yes (×175) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top Ratio (×278) |
| Wavelength_Units | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top nanometers (×278) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top 1nm (×278) |
| Spectra | metadata | categorical | *Not specified.* | n=2181, missing=2107, classes=74, top CVARS_Plot1_CAAN4_L1T1N_LC_RG (×1) |
| SLA_m2_kgDW | metadata | numeric | *Not specified.* | n=2181, missing=2107, range 2.545–27.35, mean 9.157 ± 6.006 |
| LMA_gDW_m2 | metadata | numeric | *Not specified.* | n=2181, missing=2107, range 36.56–392.9, mean 163.6 ± 99.12 |
| CHN_Sample_Name | metadata | categorical | *Not specified.* | n=2181, missing=1920, classes=258, top MCON_Tower_CADE27_L2T2chem (×2) |
| CHN_USDA_Species_Code | metadata | categorical | *Not specified.* | n=2181, missing=1920, classes=30, top CADE27 (×31) |
| CHN_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=2181, missing=1994, range 1–8, mean 1.711 ± 1.098 |
| CHN_Leaf_Number | metadata | numeric | *Not specified.* | n=2181, missing=1955, range 1–15, mean 2.363 ± 1.923 |
| CHN_Canopy_Position | metadata | categorical | *Not specified.* | n=2181, missing=1921, classes=3, top T (×174) |
| CHN_Leaf_Age | metadata | categorical | *Not specified.* | n=2181, missing=1922, classes=4, top 1 (×149) |
| CHN_Conifer_Broadleaf | metadata | categorical | *Not specified.* | n=2181, missing=1920, classes=2, top B (×149) |
| CHN_Year_Analyzed | metadata | numeric | *Not specified.* | n=2181, missing=1920, range 2014–2014, mean 2014 ± 0 |
| CHN_QC | metadata | categorical | *Not specified.* | n=2181, missing=2176, classes=1, top 1.0 (×5) |
| C_mass_g_g | metadata | numeric | *Not specified.* | n=2181, missing=1920, range 35.34–53.99, mean 46.69 ± 2.926 |
| CN_Ratio | metadata | numeric | *Not specified.* | n=2181, missing=1920, range 8.061–93.09, mean 32.53 ± 16.54 |
| CHN_Comments | metadata | categorical | *Not specified.* | n=2181, missing=2169, classes=12, top Leaf N seems a bit high (×1) |
| GE_Sample_Name | metadata | categorical | *Not specified.* | n=2181, missing=2139, classes=42, top CVARS_Plot1_CAAN4_L1T1_GE (×1) |
| GE_USDA_Species_Code | metadata | categorical | *Not specified.* | n=2181, missing=2139, classes=10, top CAAN4 (×9) |
| GE_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=2181, missing=2165, range 1–6, mean 2.562 ± 1.75 |
| GE_Leaf_Number | metadata | numeric | *Not specified.* | n=2181, missing=2142, range 1–8, mean 3.128 ± 2.238 |
| GE_Canopy_Position | metadata | categorical | *Not specified.* | n=2181, missing=2139, classes=3, top Top (×40) |
| GE_Leaf_Age | metadata | categorical | *Not specified.* | n=2181, missing=2166, classes=2, top New (×14) |
| GE_Rep | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 1–2, mean 1.048 ± 0.2155 |
| GE_Measurement_Date | metadata | categorical | *Not specified.* | n=2181, missing=2139, classes=14, top 4/12/14 (×7) |
| Leaf_Area_sq_cm | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 2–2, mean 2 ± 0 |
| Mean_Tair | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 16.04–31.54, mean 25.21 ± 3.155 |
| Mean_Tleaf | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 19.85–35.31, mean 27.58 ± 3.097 |
| PercCV_Tleaf | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.01202–2.717, mean 0.6437 ± 0.5638 |
| Mean_RH_R | metadata | numeric | *Not specified.* | n=2181, missing=2139, range -0.374–77.6, mean 53.61 ± 15.58 |
| Mean_RH_S | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 16.43–84.88, mean 60.79 ± 14.74 |
| Mean_VpdA | metadata | numeric | *Not specified.* | n=2181, missing=2140, range 0.6327–3.143, mean 1.558 ± 0.6106 |
| Mean_VpdL | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.4792–3.475, mean 1.796 ± 0.679 |
| PercCV_VpdL | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.37–11.76, mean 3.861 ± 3.032 |
| Mean_PARi | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 1999–2001, mean 2000 ± 0.486 |
| Mean_Ci_over_Ca | metadata | numeric | *Not specified.* | n=2181, missing=2140, range 0.5262–0.9468, mean 0.7597 ± 0.08308 |
| PercCV_Ci_Ca | metadata | numeric | *Not specified.* | n=2181, missing=2140, range 8.431–53.09, mean 24.81 ± 11.04 |
| Mean_Cond | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.1003–0.7444, mean 0.2284 ± 0.15 |
| PercCV_Cond | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 2.071–43.03, mean 13.76 ± 8.954 |
| Calculated_VIS_Leaf_Abs | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.8367–0.9572, mean 0.9069 ± 0.03528 |
| Mean_Fs | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 538–1277, mean 802.3 ± 170.2 |
| Mean_qP | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.3208–0.7213, mean 0.4972 ± 0.1137 |
| Mean_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.2735–0.4928, mean 0.4062 ± 0.05288 |
| Mean_PhiPS2 | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.1063–0.3519, mean 0.2068 ± 0.06464 |
| Max_ETR | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 127–371.3, mean 231.4 ± 77.54 |
| Max_Fs | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 544.8–1315, mean 864.1 ± 194.1 |
| Max_qP | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 0.3733–0.7427, mean 0.5359 ± 0.114 |
| Max_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 0.3636–0.5642, mean 0.4664 ± 0.05833 |
| Max_PhiPS2 | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 0.1472–0.419, mean 0.2544 ± 0.08076 |
| Meas_Photo_at_CO2R_400 | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 9.783–30.2, mean 16.74 ± 5.502 |
| Meas_CiCa_at_CO2R_400 | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0–0.879, mean 0.6026 ± 0.1509 |
| Mod_Photo_at_Ci_388 | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 10.11–59.63, mean 28.7 ± 12.42 |
| Mod_Photo_at_Ci_388_times_CiCa | metadata | numeric | *Not specified.* | n=2181, missing=2139, range -7.599–34.58, mean 15.8 ± 7.233 |
| Est_Photo_stomata_limit | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 1.844–37.14, mean 12.91 ± 9.396 |
| Est_Ci_colimit | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 38–907, mean 302.5 ± 252 |
| Fitted_Vcmax | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 32.69–277.2, mean 123.4 ± 68.39 |
| Fitted_Jmax | metadata | numeric | *Not specified.* | n=2181, missing=2145, range 96.99–284.9, mean 179.6 ± 58.72 |
| Fitted_Rd | metadata | numeric | *Not specified.* | n=2181, missing=2139, range -0.9303–4.283, mean 1.75 ± 0.8531 |
| RMSE_DEoptim | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.02592–2.107, mean 0.6858 ± 0.474 |
| RMSE_photo | metadata | numeric | *Not specified.* | n=2181, missing=2139, range 0.2116–7.329, mean 2.704 ± 1.449 |
| dataset | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top EcoSIS (×278) |
| dimensions | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top 1D (×278) |
| axis_note | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×278) |
| official_data_url | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×278) |
| official_package_url | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top https://ecosis.org/package/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×278) |
| license_url | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top http://www.opendefinition.org/licenses/cc-by (×278) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top True (×278) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=2181, missing=1903, classes=1, top ecosis_uw_bnl_nasa_hyspiri_airborne_campaign_leaf_and_canopy_s_reflectance_nirs (×278) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Original sample identifier retained under a prefixed/equivalent name; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 22 fields, Y: 5 fields, measurements: 35 fields, passport: 54 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `02a3558a3f6890c79a203824f01cee1c121830d18fff0adf3095f907cbb0299a`
- **Processing hash:** `fc070684c27ee8bc248141ad19e869ef989bfb2467888e64e91a0a266bf85998` | **metadata hash:** `2a74f4dddb4ed23078622f71b6c213bb6a56c855dffb6b34fda7c45be183d86b`
