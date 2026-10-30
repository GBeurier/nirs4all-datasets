# Datasheet — EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (LMA_gDW_cm2)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (LMA_gDW_cm2). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data

## Composition

- **Alignment:** sample level; 74 sample(s), 97 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.311).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra | SpecEvo_PSM3500 | NIR | 350–2500 nm | 97 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA_gDW_cm2 | target | numeric | *Not specified.* | n=74, missing=0, range 0.003656–0.03929, mean 0.01636 ± 0.009912 |
| SpectralRep | metadata | numeric | *Not specified.* | n=74, missing=0, range 1–1, mean 1 ± 0 |
| Unique_Sample_ID | metadata | categorical | *Not specified.* | n=74, missing=0, classes=74, top CVARS_Plot1_CAAN4_L1T1N_LC_RG_41430 (×1) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=74, missing=0, classes=74, top CVARS_Plot1_CAAN4_L1T1N_LC_RG (×1) |
| Sample_Name | metadata | categorical | *Not specified.* | n=74, missing=0, classes=71, top MCON_Tower_QUKE_L1T1 (×2) |
| Site | metadata | categorical | *Not specified.* | n=74, missing=0, classes=7, top SJER (×24) |
| Site_Long | metadata | categorical | *Not specified.* | n=74, missing=0, classes=7, top San Joaquin Experimental Range (×24) |
| Sample_Date | metadata | categorical | *Not specified.* | n=74, missing=0, classes=20, top 3/26/13 (×9) |
| USDA_Species_Code | metadata | categorical | *Not specified.* | n=74, missing=0, classes=18, top QUDO (×7) |
| Latitude | metadata | numeric | *Not specified.* | n=74, missing=1, range 33.52–37.12, mean 35.52 ± 1.688 |
| Longitude | metadata | numeric | *Not specified.* | n=74, missing=1, range -119.7–-116.2, mean -118.4 ± 1.373 |
| Instrument | metadata | categorical | *Not specified.* | n=74, missing=0, classes=3, top ASD_FS3 (×42) |
| Acquisition_Method | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top LC (×74) |
| Measurement_Quantity | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Reflectance (×74) |
| Leaf_or_Canopy | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top leaf (×74) |
| GasExchange_Leaf | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top yes (×51) |
| Target_Type | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Vegetation (×74) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Ratio (×74) |
| Wavelength_Units | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top nanometers (×74) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top 1nm (×74) |
| Spectra | metadata | categorical | *Not specified.* | n=74, missing=0, classes=74, top CVARS_Plot1_CAAN4_L1T1N_LC_RG (×1) |
| SLA_cm2_g_DW | metadata | numeric | *Not specified.* | n=74, missing=0, range 25.45–273.5, mean 91.57 ± 60.06 |
| SLA_m2_kgDW | metadata | numeric | *Not specified.* | n=74, missing=0, range 2.545–27.35, mean 9.157 ± 6.006 |
| LMA_gDW_m2 | metadata | numeric | *Not specified.* | n=74, missing=0, range 36.56–392.9, mean 163.6 ± 99.12 |
| CHN_Sample_Name | metadata | categorical | *Not specified.* | n=74, missing=17, classes=57, top CVARS_Plot1_CAAN4_L1T1N (×1) |
| CHN_USDA_Species_Code | metadata | categorical | *Not specified.* | n=74, missing=17, classes=17, top Grape (×6) |
| CHN_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=74, missing=33, range 1–4, mean 1.78 ± 1.013 |
| CHN_Leaf_Number | metadata | numeric | *Not specified.* | n=74, missing=28, range 1–8, mean 2.022 ± 1.795 |
| CHN_Canopy_Position | metadata | categorical | *Not specified.* | n=74, missing=17, classes=3, top T (×47) |
| CHN_Leaf_Age | metadata | categorical | *Not specified.* | n=74, missing=17, classes=2, top New (×34) |
| CHN_Conifer_Broadleaf | metadata | categorical | *Not specified.* | n=74, missing=17, classes=2, top B (×48) |
| CHN_Year_Analyzed | metadata | numeric | *Not specified.* | n=74, missing=17, range 2014–2014, mean 2014 ± 0 |
| CHN_QC | metadata | numeric | *Not specified.* | n=74, missing=72, range 1–1, mean 1 ± 0 |
| C_mass_g_g | metadata | numeric | *Not specified.* | n=74, missing=17, range 40.72–51.76, mean 46.84 ± 2.311 |
| N_mass_g_g | metadata | numeric | *Not specified.* | n=74, missing=17, range 0.57–4.82, mean 2.367 ± 1.065 |
| CN_Ratio | metadata | numeric | *Not specified.* | n=74, missing=17, range 8.896–90.81, mean 25.33 ± 15.16 |
| CHN_Comments | metadata | categorical | *Not specified.* | n=74, missing=72, classes=2, top Leaf N seems a bit high (×1) |
| GE_Sample_Name | metadata | categorical | *Not specified.* | n=74, missing=60, classes=14, top CVARS_Plot1_CAAN4_L1T1_GE (×1) |
| GE_USDA_Species_Code | metadata | categorical | *Not specified.* | n=74, missing=60, classes=4, top Grape (×5) |
| GE_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=74, missing=68, range 1–4, mean 2 ± 1.265 |
| GE_Leaf_Number | metadata | numeric | *Not specified.* | n=74, missing=61, range 1–8, mean 3.077 ± 2.532 |
| GE_Canopy_Position | metadata | categorical | *Not specified.* | n=74, missing=60, classes=3, top Top (×12) |
| GE_Leaf_Age | metadata | categorical | *Not specified.* | n=74, missing=65, classes=2, top New (×8) |
| GE_Rep | metadata | numeric | *Not specified.* | n=74, missing=60, range 1–1, mean 1 ± 0 |
| GE_Measurement_Date | metadata | categorical | *Not specified.* | n=74, missing=60, classes=8, top 6/8/13 (×4) |
| Leaf_Area_sq_cm | metadata | numeric | *Not specified.* | n=74, missing=60, range 2–2, mean 2 ± 0 |
| Mean_Tair | metadata | numeric | *Not specified.* | n=74, missing=60, range 19.4–28.41, mean 24.18 ± 2.506 |
| Mean_Tleaf | metadata | numeric | *Not specified.* | n=74, missing=60, range 24.76–31.17, mean 28.15 ± 1.972 |
| PercCV_Tleaf | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.288–2.717, mean 1.069 ± 0.6073 |
| Mean_RH_R | metadata | numeric | *Not specified.* | n=74, missing=60, range -0.374–77.6, mean 58.58 ± 19.61 |
| Mean_RH_S | metadata | numeric | *Not specified.* | n=74, missing=60, range 16.43–81.76, mean 66.3 ± 16.57 |
| Mean_VpdA | metadata | numeric | *Not specified.* | n=74, missing=61, range 0.8498–3.128, mean 1.481 ± 0.5706 |
| Mean_VpdL | metadata | numeric | *Not specified.* | n=74, missing=60, range 1.012–3.46, mean 1.847 ± 0.5748 |
| PercCV_VpdL | metadata | numeric | *Not specified.* | n=74, missing=60, range 1.265–10.89, mean 4.835 ± 3.508 |
| Mean_PARi | metadata | numeric | *Not specified.* | n=74, missing=60, range 1999–2001, mean 2000 ± 0.4248 |
| Mean_Ci_over_Ca | metadata | numeric | *Not specified.* | n=74, missing=61, range 0.5262–0.8214, mean 0.7119 ± 0.08398 |
| PercCV_Ci_Ca | metadata | numeric | *Not specified.* | n=74, missing=61, range 15.04–46.62, mean 28.75 ± 10.24 |
| Mean_Cond | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.1003–0.4674, mean 0.2016 ± 0.1072 |
| PercCV_Cond | metadata | numeric | *Not specified.* | n=74, missing=60, range 2.071–43.03, mean 19.18 ± 11.14 |
| Calculated_VIS_Leaf_Abs | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.8367–0.9524, mean 0.8952 ± 0.03949 |
| Mean_Fs | metadata | numeric | *Not specified.* | n=74, missing=60, range 604.7–1219, mean 851.2 ± 178.8 |
| Mean_qP | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.3603–0.708, mean 0.5177 ± 0.1192 |
| Mean_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.3582–0.4928, mean 0.4318 ± 0.04339 |
| Mean_PhiPS2 | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.1415–0.3519, mean 0.2287 ± 0.06892 |
| Max_ETR | metadata | numeric | *Not specified.* | n=74, missing=60, range 136.5–367.6, mean 249 ± 83.72 |
| Max_Fs | metadata | numeric | *Not specified.* | n=74, missing=60, range 613.4–1289, mean 892.6 ± 205.1 |
| Max_qP | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.3733–0.7427, mean 0.5544 ± 0.1178 |
| Max_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.3989–0.5642, mean 0.49 ± 0.05843 |
| Max_PhiPS2 | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.1516–0.419, mean 0.2765 ± 0.08646 |
| Meas_Photo_at_CO2R_400 | metadata | numeric | *Not specified.* | n=74, missing=60, range 10.27–29.31, mean 18.28 ± 6.26 |
| Meas_CiCa_at_CO2R_400 | metadata | numeric | *Not specified.* | n=74, missing=60, range 0–0.7363, mean 0.5089 ± 0.1813 |
| Mod_Photo_at_Ci_388 | metadata | numeric | *Not specified.* | n=74, missing=60, range 13.89–59.63, mean 35.59 ± 13.63 |
| Mod_Photo_at_Ci_388_times_CiCa | metadata | numeric | *Not specified.* | n=74, missing=60, range -7.599–34.58, mean 16.4 ± 9.884 |
| Est_Photo_stomata_limit | metadata | numeric | *Not specified.* | n=74, missing=60, range 3.662–37.14, mean 19.19 ± 10.41 |
| Est_Ci_colimit | metadata | numeric | *Not specified.* | n=74, missing=60, range 51–843, mean 244.2 ± 211.2 |
| Fitted_Vcmax | metadata | numeric | *Not specified.* | n=74, missing=60, range 59.45–276.4, mean 149.7 ± 66.76 |
| Fitted_Jmax | metadata | numeric | *Not specified.* | n=74, missing=60, range 120.3–284.9, mean 198.6 ± 65.72 |
| Fitted_Rd | metadata | numeric | *Not specified.* | n=74, missing=60, range -0.9303–4.283, mean 1.646 ± 1.277 |
| RMSE_DEoptim | metadata | numeric | *Not specified.* | n=74, missing=60, range 0.1–2.107, mean 0.8309 ± 0.541 |
| RMSE_photo | metadata | numeric | *Not specified.* | n=74, missing=60, range 2.481–7.329, mean 3.615 ± 1.428 |
| dataset | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top EcoSIS (×74) |
| dataset_slug | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×74) |
| task_type | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top regression (×74) |
| trait_header | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top LMA_gDW_cm2 (×74) |
| target_original_name | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top LMA_gDW_cm2 (×74) |
| measurement_hint | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra (×74) |
| raw_label | metadata | categorical | *Not specified.* | n=74, missing=0, classes=66, top 0.009567142 (×2) |
| reference_value | metadata | numeric | *Not specified.* | n=74, missing=0, range 0.003656–0.03929, mean 0.01636 ± 0.009912 |
| class_index | metadata | categorical | *Not specified.* | n=74, missing=74, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=74, missing=74, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=74, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top 1D (×74) |
| axis_note | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×74) |
| official_data_url | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×74) |
| official_package_url | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top https://ecosis.org/package/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×74) |
| license | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Creative Commons Attribution (×74) |
| license_url | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×74) |
| rights_status | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top explicit_open (×74) |
| usage_scope | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top public_reuse_possible (×74) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top True (×74) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top ecosis_uw_bnl_nasa_hyspiri_airborne_campaign_leaf_and_canopy_s_reflectance_nirs (×74) |
| notes | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×74) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 20 fields, Y: 1 fields, measurements: 38 fields, passport: 50 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Creative Commons Attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `7e573bd3205435cc08358539cee50cba48773c1f596014b75e3c04e7059cdaa3`
- **Processing hash:** `5172c1394ebcf8ce8f2f2353e442b7d618384d85748a9c8f847b12416bd6ac46` | **metadata hash:** `fe84e3278141e130379f1d6a00267194734344859218eea486a1fcaff4ee6367`
