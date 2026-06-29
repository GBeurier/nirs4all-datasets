# Private datasets to upload to Dataverse

_122 private/anonymized dataset(s) are catalogued but **not yet uploaded** to a personal
Dataverse (no DOI). Their metadata + metrics are public in the catalog/site, but a consumer cannot
`get()` their bytes until they are uploaded and a token-gated DOI is minted. 0 already on Dataverse._

## Upload one
```bash
n4a-datasets publish <id> --collection <your-collection> --contact-email you@example.org
```
Needs a Dataverse token (see [PUBLISHING.md](PUBLISHING.md)); first publish mints the DOI, which is
written back into `catalog/datasets/<id>.yaml` so this list shrinks automatically.

## Pending uploads (122)
| id | name | tier | license | origin(s) | samples | validation |
|----|------|------|---------|-----------|--------:|------------|
| `cgl_nir_grain_eigenvector` | CGL_NIR grain protein Eigenvector | private | LicenseRef-not-cleared | script, url | 231 | ⏳ pending |
| `corn_eigenvector_nir` | CORN Eigenvector NIR | private | LicenseRef-not-cleared | script, url | 80 | ⏳ pending |
| `diesel_fuels_nir_eigenvector` | Diesel fuels NIR Eigenvector | private | LicenseRef-not-cleared | script, url | 784 | ⏳ pending |
| `ecosis_2014_cedar_creek_esr_grassland_biodiversity_experiment_reflectance_nirs` | EcoSIS 2014 Cedar Creek ESR Grassland Biodiversity Experiment: Leaf-level Contact Data: Trait Predictions (reflectance) | private | LicenseRef-not-cleared | script, url | 831 | ⏳ pending |
| `ecosis_2018_talladega_national_forest_leaf_level_reflectance_s_reflectance_nirs` | EcoSIS 2018 Talladega National Forest: Leaf level Reflectance Spectra and Foliar Traits (reflectance) | private | LicenseRef-not-cleared | script, url | 156 | ⏳ pending |
| `ecosis_2019_plosone_wheat_hessian_fly_ms_reflectance_nirs` | EcoSIS 2019 PLOSONE wheat hessian fly ms (reflectance) | private | LicenseRef-not-cleared | script, url | 74 | ⏳ pending |
| `ecosis_3d_canopy_level_spectra_reflectance_nirs` | EcoSIS 3D LMA Canopy Level Spectra (reflectance) | private | LicenseRef-not-cleared | script, url | 59 | ⏳ pending |
| `ecosis_3d_leaf_level_spectra_reflectance_nirs` | EcoSIS 3D LMA Leaf Level Spectra (reflectance) | private | LicenseRef-not-cleared | script, url | 1485 | ⏳ pending |
| `ecosis_calcareous_grassland_species_over_growing_season_at_the_reflectance_nirs` | EcoSIS Calcareous grassland species over growing season at the leaf level (reflectance) | private | LicenseRef-not-cleared | script, url | 1100 | ⏳ pending |
| `ecosis_common_milkweed_leaf_responses_to_water_stress_and_elev_reflectance_nirs` | EcoSIS Common Milkweed Leaf Responses to Water Stress and Elevated Temperature (reflectance) | private | LicenseRef-not-cleared | script, url | 735 | ⏳ pending |
| `ecosis_fine_scale_vnir_hyperspectral_canopy_reflectances_from_reflectance_nirs` | EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance) | private | LicenseRef-not-cleared | script, url | 2850 | ⏳ pending |
| `ecosis_fresh_leaf_spectra_to_estimate_leaf_morphology_and_bioc_reflectance_nirs` | EcoSIS Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests (reflectance) | private | LicenseRef-not-cleared | script, url | 2363 | ⏳ pending |
| `ecosis_leaf_reflectance_and_traits_of_plants_sampled_along_a_w_reflectance_nirs` | EcoSIS Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD) (reflectance) | private | LicenseRef-not-cleared | script, url | 190 | ⏳ pending |
| `ecosis_leaf_reflectance_and_tratis_of_floating_and_emergent_ma_reflectance_nirs` | EcoSIS Leaf reflectance and tratis of floating and emergent macrophytes (reflectance) | private | LicenseRef-not-cleared | script, url | 325 | ⏳ pending |
| `ecosis_ngee_arctic_leaf_spectral_reflectance_and_transmittance_reflectance_nirs` | EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (reflectance) | private | LicenseRef-not-cleared | script, url | 199 | ⏳ pending |
| `ecosis_ngee_arctic_leaf_spectral_reflectance_and_transmittance_transmittance_nirs` | EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (transmittance) | private | LicenseRef-not-cleared | script, url | 31 | ⏳ pending |
| `ecosis_ngee_arctic_leaf_spectral_reflectance_utqiagvik_barrow_reflectance_nirs` | EcoSIS NGEE Arctic Leaf Spectral Reflectance Utqiagvik (Barrow) Alaska 2013 (reflectance) | private | LicenseRef-not-cleared | script, url | 69 | ⏳ pending |
| `ecosis_purdue_leaf_spectral_functional_traits_plsr_v2_reflectance_nirs` | EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling v2 (reflectance) | private | LicenseRef-not-cleared | script, url | 987 | ⏳ pending |
| `ecosis_spectra_from_in_situ_deciduous_leaves_and_leaves_collec_reflectance_nirs` | EcoSIS Spectra from in situ deciduous leaves and leaves collected for nitrogen analysis throughout autumn (reflectance) | private | LicenseRef-not-cleared | script, url | 1013 | ⏳ pending |
| `ecosis_spectral_characterization_of_multiple_corn_varieties_we_reflectance_nirs` | EcoSIS Spectral Characterization of Multiple Corn Varieties: West Madison Agricultural Station 2014 (reflectance) | private | LicenseRef-not-cleared | script, url | 288 | ⏳ pending |
| `ecosis_urban_materials_spectral_library_reflectance_nirs` | EcoSIS Urban Materials Spectral Library reflectance | private | LicenseRef-not-cleared | script, url | 60 | ⏳ pending |
| `ecosis_urban_reflectance_spectra_from_santa_barbara_ca_reflectance_nirs` | EcoSIS Urban Reflectance Spectra from Santa Barbara, CA (reflectance) | private | LicenseRef-not-cleared | script, url | 1065 | ⏳ pending |
| `ecosis_varietal_discrimination_and_detection_of_pvy_in_solanum_reflectance_nirs` | EcoSIS Varietal Discrimination and Detection of PVY in Solanum tuberosum: Hawaii 2014 (reflectance) | private | LicenseRef-not-cleared | script, url | 761 | ⏳ pending |
| `ecostress_lunar_tir_2124points` | ECOSTRESS lunar tir axis 69ac2056 | private | LicenseRef-not-cleared | script, url | 17 | ⏳ pending |
| `ecostress_manmade_all_491points` | ECOSTRESS manmade all axis 21e24555 | private | LicenseRef-not-cleared | script, url | 14 | ⏳ pending |
| `ecostress_manmade_all_536points` | ECOSTRESS manmade all axis ec3e1c20 | private | LicenseRef-not-cleared | script, url | 22 | ⏳ pending |
| `ecostress_manmade_all_551points` | ECOSTRESS manmade all axis 0d1ca66e | private | LicenseRef-not-cleared | script, url | 6 | ⏳ pending |
| `ecostress_manmade_all_561points` | ECOSTRESS manmade all axis 4a5262f7 | private | LicenseRef-not-cleared | script, url | 3 | ⏳ pending |
| `ecostress_manmade_tir_2223points` | ECOSTRESS manmade tir axis 93ae36e3 | private | LicenseRef-not-cleared | script, url | 10 | ⏳ pending |
| `ecostress_manmade_tir_2256points` | ECOSTRESS manmade tir axis 85fbc8f6 | private | LicenseRef-not-cleared | script, url | 16 | ⏳ pending |
| `ecostress_meteorites_tir_2287points` | ECOSTRESS meteorites tir axis d3032c60 | private | LicenseRef-not-cleared | script, url | 55 | ⏳ pending |
| `ecostress_mineral_all_2231points` | ECOSTRESS mineral all axis 20b176d4 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_mineral_all_2752points` | ECOSTRESS mineral all axis adc9f614 | private | LicenseRef-not-cleared | script, url | 17 | ⏳ pending |
| `ecostress_mineral_tir_2256points` | ECOSTRESS mineral tir axis 85fbc8f6 | private | LicenseRef-not-cleared | script, url | 150 | ⏳ pending |
| `ecostress_mineral_tir_2287points_113rows` | ECOSTRESS mineral tir axis 02866850 | private | LicenseRef-not-cleared | script, url | 113 | ⏳ pending |
| `ecostress_mineral_tir_2287points_14rows` | ECOSTRESS mineral tir axis d3032c60 | private | LicenseRef-not-cleared | script, url | 10 | ⏳ pending |
| `ecostress_mineral_tir_2287points_207rows` | ECOSTRESS mineral tir axis 02866850 | private | LicenseRef-not-cleared | script, url | 125 | ⏳ pending |
| `ecostress_mineral_tir_2287points_2rows_mineral_oxide_none_fine_tir_chromite` | ECOSTRESS mineral tir axis cbf25a1b | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_mineral_tir_2287points_2rows_mineral_silicate_phyllosilicate_fine_tir_illsmec` | ECOSTRESS mineral tir axis 02866850 | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_mineral_tir_2287points_5rows` | ECOSTRESS mineral tir axis d3032c60 | private | LicenseRef-not-cleared | script, url | 5 | ⏳ pending |
| `ecostress_mineral_vswir_2101points` | ECOSTRESS mineral vswir axis 61f98690 | private | LicenseRef-not-cleared | script, url | 148 | ⏳ pending |
| `ecostress_mineral_vswir_826points` | ECOSTRESS mineral vswir axis 158dfad5 | private | LicenseRef-not-cleared | script, url | 160 | ⏳ pending |
| `ecostress_nonphotosyntheticvegetation_tir_1736points_47rows` | ECOSTRESS nonphotosyntheticvegetation tir axis d3f7b526 | private | LicenseRef-not-cleared | script, url | 47 | ⏳ pending |
| `ecostress_nonphotosyntheticvegetation_tir_1736points_4rows` | ECOSTRESS nonphotosyntheticvegetation tir axis d3f7b526 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_nonphotosyntheticvegetation_tir_1737points` | ECOSTRESS nonphotosyntheticvegetation tir axis 1389b1f1 | private | LicenseRef-not-cleared | script, url | 7 | ⏳ pending |
| `ecostress_nonphotosyntheticvegetation_vswir_2151points_4rows` | ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_nonphotosyntheticvegetation_vswir_2151points_57rows` | ECOSTRESS nonphotosyntheticvegetation vswir axis 4d4366d1 | private | LicenseRef-not-cleared | script, url | 54 | ⏳ pending |
| `ecostress_rock_all_2227points` | ECOSTRESS rock all axis d9555baa | private | LicenseRef-not-cleared | script, url | 9 | ⏳ pending |
| `ecostress_rock_all_2231points` | ECOSTRESS rock all axis 20b176d4 | private | LicenseRef-not-cleared | script, url | 27 | ⏳ pending |
| `ecostress_rock_all_2257points` | ECOSTRESS rock all axis 8a8a144c | private | LicenseRef-not-cleared | script, url | 83 | ⏳ pending |
| `ecostress_rock_all_2530points` | ECOSTRESS rock all axis aa24fdf9 | private | LicenseRef-not-cleared | script, url | 30 | ⏳ pending |
| `ecostress_rock_all_2826points` | ECOSTRESS rock all axis 8cf1b56d | private | LicenseRef-not-cleared | script, url | 35 | ⏳ pending |
| `ecostress_rock_all_2844points_29rows` | ECOSTRESS rock all axis 4cb30554 | private | LicenseRef-not-cleared | script, url | 29 | ⏳ pending |
| `ecostress_rock_all_2844points_2rows` | ECOSTRESS rock all axis 5431484a | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_rock_all_2844points_46rows` | ECOSTRESS rock all axis 1fb6fa59 | private | LicenseRef-not-cleared | script, url | 46 | ⏳ pending |
| `ecostress_rock_all_2844points_4rows` | ECOSTRESS rock all axis 5a744ba8 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_rock_all_2844points_8rows` | ECOSTRESS rock all axis 2228baf8 | private | LicenseRef-not-cleared | script, url | 8 | ⏳ pending |
| `ecostress_rock_all_2868points_14rows` | ECOSTRESS rock all axis e7e7baa6 | private | LicenseRef-not-cleared | script, url | 14 | ⏳ pending |
| `ecostress_rock_all_2868points_28rows` | ECOSTRESS rock all axis d24e4e1f | private | LicenseRef-not-cleared | script, url | 28 | ⏳ pending |
| `ecostress_rock_all_2868points_2rows` | ECOSTRESS rock all axis 66af2adc | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_rock_all_2868points_41rows` | ECOSTRESS rock all axis be345a03 | private | LicenseRef-not-cleared | script, url | 39 | ⏳ pending |
| `ecostress_rock_all_2868points_4rows_rock_metamorphic_gneis_coarse_all_gneiss4` | ECOSTRESS rock all axis 8e148055 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_rock_all_2868points_4rows_rock_metamorphic_schist_fine_all_schist1` | ECOSTRESS rock all axis e2c8c295 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_rock_tir_2148points` | ECOSTRESS rock tir axis 16aa20e0 | private | LicenseRef-not-cleared | script, url | 5 | ⏳ pending |
| `ecostress_rock_vswir_2101points` | ECOSTRESS rock vswir axis 61f98690 | private | LicenseRef-not-cleared | script, url | 83 | ⏳ pending |
| `ecostress_soil_all_2844points_13rows` | ECOSTRESS soil all axis 1fb6fa59 | private | LicenseRef-not-cleared | script, url | 13 | ⏳ pending |
| `ecostress_soil_all_2844points_2rows` | ECOSTRESS soil all axis 7258ef46 | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_soil_all_2844points_3rows` | ECOSTRESS soil all axis 5431484a | private | LicenseRef-not-cleared | script, url | 3 | ⏳ pending |
| `ecostress_soil_all_2844points_7rows` | ECOSTRESS soil all axis 2228baf8 | private | LicenseRef-not-cleared | script, url | 7 | ⏳ pending |
| `ecostress_soil_all_2868points_2rows` | ECOSTRESS soil all axis e7e7baa6 | private | LicenseRef-not-cleared | script, url | 2 | ⏳ pending |
| `ecostress_soil_all_2868points_4rows` | ECOSTRESS soil all axis be345a03 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_soil_all_2868points_6rows` | ECOSTRESS soil all axis d24e4e1f | private | LicenseRef-not-cleared | script, url | 6 | ⏳ pending |
| `ecostress_soil_tir_2124points` | ECOSTRESS soil tir axis 69ac2056 | private | LicenseRef-not-cleared | script, url | 17 | ⏳ pending |
| `ecostress_soil_tir_2223points` | ECOSTRESS soil tir axis 2895e351 | private | LicenseRef-not-cleared | script, url | 11 | ⏳ pending |
| `ecostress_vegetation_all_550points` | ECOSTRESS vegetation all axis 6fbcd0b0 | private | LicenseRef-not-cleared | script, url | 3 | ⏳ pending |
| `ecostress_vegetation_tir_1736points` | ECOSTRESS vegetation tir axis d3f7b526 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `ecostress_vegetation_tir_1737points_138rows` | ECOSTRESS vegetation tir axis 8b6bc3b9 | private | LicenseRef-not-cleared | script, url | 138 | ⏳ pending |
| `ecostress_vegetation_tir_1737points_342rows` | ECOSTRESS vegetation tir axis 1389b1f1 | private | LicenseRef-not-cleared | script, url | 324 | ⏳ pending |
| `ecostress_vegetation_vswir_2151points_210rows` | ECOSTRESS vegetation vswir axis 4d4366d1 | private | LicenseRef-not-cleared | script, url | 210 | ⏳ pending |
| `ecostress_vegetation_vswir_2151points_343rows` | ECOSTRESS vegetation vswir axis 4d4366d1 | private | LicenseRef-not-cleared | script, url | 325 | ⏳ pending |
| `ecostress_water_all_965points` | ECOSTRESS water all axis 21cbe3b0 | private | LicenseRef-not-cleared | script, url | 4 | ⏳ pending |
| `flanagan_api_compounds_raman` | Flanagan API compounds Raman | private | LicenseRef-not-cleared | figshare, script, url | 3510 | ⏳ pending |
| `grapevine_leaftraits_multisensor_nir` | Grapevine LeafTraits multisensor NIR | private | LicenseRef-not-cleared | script | 2079 | ⏳ pending |
| `manure21_nir_all_y` | MANURE21 NIR all chemistry targets | private | LicenseRef-not-cleared | script | 490 | ⏳ pending |
| `ohpl_beer_nir` | Beer original extract OHPL NIR | private | LicenseRef-not-cleared | script, url | 60 | ⏳ pending |
| `ohpl_soil_nir` | Soil organic matter OHPL NIR | private | LicenseRef-not-cleared | script, url | 108 | ⏳ pending |
| `ohpl_wheat_nir` | Wheat protein OHPL NIR | private | LicenseRef-not-cleared | script, url | 100 | ⏳ pending |
| `openspecy_ftir` | OpenSpecy FTIR spectral library subset | private | LicenseRef-not-cleared | script, url | 5000 | ⏳ pending |
| `openspecy_raman` | OpenSpecy RAMAN spectral library subset | private | LicenseRef-not-cleared | script, url | 5000 | ⏳ pending |
| `ossl_afsis1_visnir_soil_all_y` | ossl afsis1 visnir soil all y | private | LicenseRef-not-cleared | script, url | 1904 | ⏳ pending |
| `ossl_afsis2_mir_soil_all_y` | ossl afsis2 mir soil all y | private | LicenseRef-not-cleared | script, url | 151 | ⏳ pending |
| `ossl_afsis2_visnir_soil_all_y` | ossl afsis2 visnir soil all y | private | LicenseRef-not-cleared | script, url | 151 | ⏳ pending |
| `ossl_cassl_visnir_soil_all_y` | ossl cassl visnir soil all y | private | LicenseRef-not-cleared | script, url | 1578 | ⏳ pending |
| `ossl_garrett_visnir_soil_all_y` | ossl garrett visnir soil all y | private | LicenseRef-not-cleared | script, url | 184 | ⏳ pending |
| `ossl_icraf_visnir_soil_all_y` | ossl icraf visnir soil all y | private | LicenseRef-not-cleared | script, url | 3776 | ⏳ pending |
| `ossl_jovic_mir_soil_all_y` | ossl jovic mir soil all y | private | LicenseRef-not-cleared | script, url | 45 | ⏳ pending |
| `ossl_jovic_visnir_soil_all_y` | ossl jovic visnir soil all y | private | LicenseRef-not-cleared | script, url | 135 | ⏳ pending |
| `ossl_kellogg_visnir_soil_all_y` | ossl kellogg visnir soil all y | private | LicenseRef-not-cleared | script, url | 85669 | ⏳ pending |
| `ossl_lucas_mir_soil_all_y` | ossl lucas mir soil all y | private | LicenseRef-not-cleared | script, url | 40175 | ⏳ pending |
| `ossl_lucas_visnir_soil_all_y` | ossl lucas visnir soil all y | private | LicenseRef-not-cleared | script, url | 40175 | ⏳ pending |
| `ossl_lucas_woodwell_mir_soil_all_y` | ossl lucas woodwell mir soil all y | private | LicenseRef-not-cleared | script, url | 589 | ⏳ pending |
| `ossl_lucas_woodwell_visnir_soil_all_y` | ossl lucas woodwell visnir soil all y | private | LicenseRef-not-cleared | script, url | 589 | ⏳ pending |
| `ossl_neospectra_mir_soil_all_y` | ossl neospectra mir soil all y | private | LicenseRef-not-cleared | script, url | 1976 | ⏳ pending |
| `ossl_neospectra_nir_soil_all_y` | ossl neospectra nir soil all y | private | LicenseRef-not-cleared | script, url | 8151 | ⏳ pending |
| `ossl_schiedung_visnir_soil_all_y` | ossl schiedung visnir soil all y | private | LicenseRef-not-cleared | script, url | 259 | ⏳ pending |
| `perten_cereals_nir` | Perten cereals NIR | private | LicenseRef-not-cleared | script, zenodo | 450 | ⏳ pending |
| `pharmaceutical_tablets_nir_shootout_eigenvector` | Pharmaceutical tablets NIR Shootout Eigenvector | private | LicenseRef-not-cleared | script, url | 655 | ⏳ pending |
| `plastic_polymer_name_grouped_flopp_e_ftir` | FLOPP-e FTIR polymer classification | private | LicenseRef-not-cleared | figshare, script, url | 195 | ⏳ pending |
| `plastic_polymer_name_grouped_flopp_ftir` | FLOPP FTIR polymer classification | private | LicenseRef-not-cleared | figshare, script, url | 186 | ⏳ pending |
| `pnnl_quant_ir` | PNNL/NIST Quantitative Infrared Database private-use subset | private | LicenseRef-not-cleared | script, url | 20 | ⏳ pending |
| `rruff_ir` | RRUFF IR mineral spectral library common-axis subset | private | LicenseRef-not-cleared | script, url | 347 | ⏳ pending |
| `rruff_raman` | RRUFF RAMAN mineral spectral library common-axis subset | private | LicenseRef-not-cleared | script, url | 85 | ⏳ pending |
| `timeseries_boeuf_classe_adulteration_ts` | boeuf_classe_adulteration_ts | private | LicenseRef-not-cleared | script, url | 60 | ⏳ pending |
| `timeseries_cafe_instantane_espece_cafe_ts` | cafe_instantane_espece_cafe_ts | private | LicenseRef-not-cleared | script, url | 56 | ⏳ pending |
| `timeseries_huile_olive_extra_vierge_origine_geographique_ts` | huile_olive_extra_vierge_origine_geographique_ts | private | LicenseRef-not-cleared | script, url | 60 | ⏳ pending |
| `timeseries_puree_fraise_authenticite_ts` | puree_fraise_authenticite_ts | private | LicenseRef-not-cleared | script, url | 983 | ⏳ pending |
| `timeseries_roche_type_roche_ts` | roche_type_roche_ts | private | LicenseRef-not-cleared | script, url | 70 | ⏳ pending |
| `timeseries_solution_eau_ethanol_bouteille_whisky_concentration_ethanol_ts` | solution_eau_ethanol_bouteille_whisky_concentration_ethanol_ts | private | LicenseRef-not-cleared | script, url | 1572 | ⏳ pending |
| `timeseries_spiritueux_whisky_bouteille_taux_ethanol_ts` | spiritueux_whisky_bouteille_taux_ethanol_ts | private | LicenseRef-not-cleared | script, url | 1004 | ⏳ pending |
| `timeseries_viande_espece_viande_ts` | viande_espece_viande_ts | private | LicenseRef-not-cleared | script, url | 120 | ⏳ pending |
| `timeseries_vin_cepage_type_ts` | vin_cepage_type_ts | private | LicenseRef-not-cleared | script, url | 111 | ⏳ pending |
| `ucph_tablet_nir` | UCPH tablet NIR | private | LicenseRef-not-cleared | script, url | 310 | ⏳ pending |
