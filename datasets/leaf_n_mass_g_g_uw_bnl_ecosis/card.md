# Datasheet — EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (N_mass_g_g)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data (N_mass_g_g). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** UW-BNL NASA HyspIRI Airborne Campaign Leaf and Canopy Spectra and Trait Data

## Composition

- **Alignment:** sample level; 261 sample(s), 358 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.372).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra | SpecEvo_PSM3500 | NIR | 350–2500 nm | 358 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| N_mass_g_g | target | numeric | *Not specified.* | n=261, missing=0, range 0.57–4.82, mean 1.877 ± 1.015 |
| SpectralRep | metadata | numeric | *Not specified.* | n=261, missing=0, range 1–1, mean 1 ± 0 |
| Unique_Sample_ID | metadata | categorical | *Not specified.* | n=261, missing=0, classes=261, top CVARS_Plot1_CAAN4_L1T1N_LC_RG_41430 (×1) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=261, missing=0, classes=260, top MCON_Tower_CADE27_L2T2chem_LC_R (×2) |
| Sample_Name | metadata | categorical | *Not specified.* | n=261, missing=0, classes=258, top MCON_Tower_CADE27_L2T2chem (×2) |
| Site | metadata | categorical | *Not specified.* | n=261, missing=0, classes=9, top SJJR (×70) |
| Site_Long | metadata | categorical | *Not specified.* | n=261, missing=0, classes=9, top San Jacinto James Reserve (×70) |
| Sample_Date | metadata | categorical | *Not specified.* | n=261, missing=0, classes=37, top 6/16/13 (×16) |
| USDA_Species_Code | metadata | categorical | *Not specified.* | n=261, missing=0, classes=29, top CADE27 (×31) |
| Latitude | metadata | numeric | *Not specified.* | n=261, missing=8, range 33.52–37.12, mean 35.43 ± 1.65 |
| Longitude | metadata | numeric | *Not specified.* | n=261, missing=8, range -119.7–-116.1, mean -118.2 ± 1.382 |
| Instrument | metadata | categorical | *Not specified.* | n=261, missing=0, classes=3, top ASD_FS3 (×131) |
| Acquisition_Method | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top LC (×261) |
| Measurement_Quantity | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top Reflectance (×261) |
| Leaf_or_Canopy | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top leaf (×261) |
| GasExchange_Leaf | metadata | categorical | *Not specified.* | n=261, missing=0, classes=2, top yes (×162) |
| Target_Type | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top Vegetation (×261) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top Ratio (×261) |
| Wavelength_Units | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top nanometers (×261) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top 1nm (×261) |
| Spectra | metadata | categorical | *Not specified.* | n=261, missing=204, classes=57, top CVARS_Plot1_CAAN4_L1T1N_LC_RG (×1) |
| SLA_cm2_g_DW | metadata | numeric | *Not specified.* | n=261, missing=204, range 25.45–273.5, mean 92.41 ± 59.65 |
| SLA_m2_kgDW | metadata | numeric | *Not specified.* | n=261, missing=204, range 2.545–27.35, mean 9.241 ± 5.965 |
| LMA_gDW_cm2 | metadata | numeric | *Not specified.* | n=261, missing=204, range 0.003656–0.03929, mean 0.01609 ± 0.009936 |
| LMA_gDW_m2 | metadata | numeric | *Not specified.* | n=261, missing=204, range 36.56–392.9, mean 160.9 ± 99.36 |
| CHN_Sample_Name | metadata | categorical | *Not specified.* | n=261, missing=0, classes=258, top MCON_Tower_CADE27_L2T2chem (×2) |
| CHN_USDA_Species_Code | metadata | categorical | *Not specified.* | n=261, missing=0, classes=30, top CADE27 (×31) |
| CHN_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=261, missing=74, range 1–8, mean 1.711 ± 1.098 |
| CHN_Leaf_Number | metadata | numeric | *Not specified.* | n=261, missing=35, range 1–15, mean 2.363 ± 1.923 |
| CHN_Canopy_Position | metadata | categorical | *Not specified.* | n=261, missing=1, classes=3, top T (×174) |
| CHN_Leaf_Age | metadata | categorical | *Not specified.* | n=261, missing=2, classes=4, top 1 (×149) |
| CHN_Conifer_Broadleaf | metadata | categorical | *Not specified.* | n=261, missing=0, classes=2, top B (×149) |
| CHN_Year_Analyzed | metadata | numeric | *Not specified.* | n=261, missing=0, range 2014–2014, mean 2014 ± 0 |
| CHN_QC | metadata | categorical | *Not specified.* | n=261, missing=256, classes=1, top 1.0 (×5) |
| C_mass_g_g | metadata | numeric | *Not specified.* | n=261, missing=0, range 35.34–53.99, mean 46.69 ± 2.926 |
| CN_Ratio | metadata | numeric | *Not specified.* | n=261, missing=0, range 8.061–93.09, mean 32.53 ± 16.54 |
| CHN_Comments | metadata | categorical | *Not specified.* | n=261, missing=249, classes=12, top Leaf N seems a bit high (×1) |
| GE_Sample_Name | metadata | categorical | *Not specified.* | n=261, missing=222, classes=39, top CVARS_Plot1_CAAN4_L1T1_GE (×1) |
| GE_USDA_Species_Code | metadata | categorical | *Not specified.* | n=261, missing=222, classes=10, top CAAN4 (×7) |
| GE_Tree_Plant_Number | metadata | numeric | *Not specified.* | n=261, missing=248, range 1–6, mean 2.692 ± 1.888 |
| GE_Leaf_Number | metadata | numeric | *Not specified.* | n=261, missing=225, range 1–8, mean 3.25 ± 2.285 |
| GE_Canopy_Position | metadata | categorical | *Not specified.* | n=261, missing=222, classes=2, top Top (×38) |
| GE_Leaf_Age | metadata | categorical | *Not specified.* | n=261, missing=248, classes=1, top New (×13) |
| GE_Rep | metadata | numeric | *Not specified.* | n=261, missing=222, range 1–2, mean 1.051 ± 0.2235 |
| GE_Measurement_Date | metadata | categorical | *Not specified.* | n=261, missing=222, classes=13, top 4/12/14 (×7) |
| Leaf_Area_sq_cm | metadata | numeric | *Not specified.* | n=261, missing=222, range 2–2, mean 2 ± 0 |
| Mean_Tair | metadata | numeric | *Not specified.* | n=261, missing=222, range 16.04–31.54, mean 25.17 ± 3.205 |
| Mean_Tleaf | metadata | numeric | *Not specified.* | n=261, missing=222, range 19.85–35.31, mean 27.51 ± 3.134 |
| PercCV_Tleaf | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.01202–1.664, mean 0.5667 ± 0.4571 |
| Mean_RH_R | metadata | numeric | *Not specified.* | n=261, missing=222, range 24.91–77.6, mean 54.47 ± 13.03 |
| Mean_RH_S | metadata | numeric | *Not specified.* | n=261, missing=222, range 32.12–84.88, mean 61.28 ± 13.07 |
| Mean_VpdA | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.6327–3.143, mean 1.516 ± 0.5705 |
| Mean_VpdL | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.4792–3.475, mean 1.768 ± 0.6376 |
| PercCV_VpdL | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.37–11.76, mean 3.615 ± 2.87 |
| Mean_PARi | metadata | numeric | *Not specified.* | n=261, missing=222, range 1999–2001, mean 2000 ± 0.489 |
| Mean_Ci_over_Ca | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.5262–0.9468, mean 0.7628 ± 0.08169 |
| PercCV_Ci_Ca | metadata | numeric | *Not specified.* | n=261, missing=222, range 8.431–53.09, mean 25.16 ± 11.2 |
| Mean_Cond | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.1003–0.7444, mean 0.2228 ± 0.1505 |
| PercCV_Cond | metadata | numeric | *Not specified.* | n=261, missing=222, range 2.071–34.54, mean 13.12 ± 7.919 |
| Calculated_VIS_Leaf_Abs | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.8367–0.9572, mean 0.9054 ± 0.03589 |
| Mean_Fs | metadata | numeric | *Not specified.* | n=261, missing=222, range 538–1277, mean 789.6 ± 167.5 |
| Mean_qP | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.3208–0.7213, mean 0.4887 ± 0.1131 |
| Mean_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.2735–0.4928, mean 0.4033 ± 0.05269 |
| Mean_PhiPS2 | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.1063–0.3519, mean 0.2015 ± 0.06315 |
| Max_ETR | metadata | numeric | *Not specified.* | n=261, missing=228, range 127–371.3, mean 224 ± 75.15 |
| Max_Fs | metadata | numeric | *Not specified.* | n=261, missing=228, range 544.8–1315, mean 843.4 ± 187.8 |
| Max_qP | metadata | numeric | *Not specified.* | n=261, missing=228, range 0.3733–0.7427, mean 0.5269 ± 0.1138 |
| Max_Fv_Prime_over_Fm_Prime | metadata | numeric | *Not specified.* | n=261, missing=228, range 0.3636–0.5642, mean 0.4608 ± 0.0566 |
| Max_PhiPS2 | metadata | numeric | *Not specified.* | n=261, missing=228, range 0.1472–0.419, mean 0.2469 ± 0.07872 |
| Meas_Photo_at_CO2R_400 | metadata | numeric | *Not specified.* | n=261, missing=222, range 9.783–30.2, mean 16.16 ± 5.075 |
| Meas_CiCa_at_CO2R_400 | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.391–0.879, mean 0.617 ± 0.1203 |
| Mod_Photo_at_Ci_388 | metadata | numeric | *Not specified.* | n=261, missing=222, range 10.11–59.63, mean 27.56 ± 11.83 |
| Mod_Photo_at_Ci_388_times_CiCa | metadata | numeric | *Not specified.* | n=261, missing=222, range 7.769–32.29, mean 15.61 ± 5.38 |
| Est_Photo_stomata_limit | metadata | numeric | *Not specified.* | n=261, missing=222, range 1.844–36.05, mean 11.95 ± 8.705 |
| Est_Ci_colimit | metadata | numeric | *Not specified.* | n=261, missing=228, range 38–907, mean 308.1 ± 262.8 |
| Fitted_Vcmax | metadata | numeric | *Not specified.* | n=261, missing=222, range 32.69–277.2, mean 118.6 ± 66.54 |
| Fitted_Jmax | metadata | numeric | *Not specified.* | n=261, missing=228, range 96.99–284.9, mean 174.1 ± 55.81 |
| Fitted_Rd | metadata | numeric | *Not specified.* | n=261, missing=222, range -0.9303–4.283, mean 1.831 ± 0.8119 |
| RMSE_DEoptim | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.02592–2.107, mean 0.6984 ± 0.4876 |
| RMSE_photo | metadata | numeric | *Not specified.* | n=261, missing=222, range 0.2116–7.329, mean 2.629 ± 1.457 |
| dataset | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top EcoSIS (×261) |
| dataset_slug | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×261) |
| task_type | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top regression (×261) |
| trait_header | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top N_mass_g_g (×261) |
| target_original_name | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top N_mass_g_g (×261) |
| measurement_hint | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top UW-BNL_NASA_HyspIRI_Airborne_Campaign_Compiled_Leaf_and_Canopy_Spectra (×261) |
| raw_label | metadata | categorical | *Not specified.* | n=261, missing=0, classes=171, top 1.12 (×5) |
| reference_value | metadata | numeric | *Not specified.* | n=261, missing=0, range 0.57–4.82, mean 1.877 ± 1.015 |
| class_index | metadata | categorical | *Not specified.* | n=261, missing=261, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=261, missing=261, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=261, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top 1D (×261) |
| axis_note | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×261) |
| official_data_url | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top https://data.ecosis.org/dataset/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×261) |
| official_package_url | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top https://ecosis.org/package/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data (×261) |
| license | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top Creative Commons Attribution (×261) |
| license_url | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×261) |
| rights_status | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top explicit_open (×261) |
| usage_scope | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top public_reuse_possible (×261) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top True (×261) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top ecosis_uw_bnl_nasa_hyspiri_airborne_campaign_leaf_and_canopy_s_reflectance_nirs (×261) |
| notes | metadata | categorical | *Not specified.* | n=261, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×261) |

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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques. Champs d’index examinés : GE_Rep. Le nombre de niveaux d’un facteur Rep n’est pas utilisé comme nombre de spectres par échantillon.
- **Curated views:** M: 19 fields, Y: 1 fields, measurements: 38 fields, passport: 51 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `75aa2f49f99c89d0c0e71159b1fa7b238ebf4ffc341489ed9677775d9c11f51a`
- **Processing hash:** `9db9eae2ed76c900134472e062d9638b64477e62fc61cc8c179dbc64fca28f02` | **metadata hash:** `98b70e5329974b79730274662e2aef6ca63c0197e9a7e8964102d4a3a70ba8a0`
