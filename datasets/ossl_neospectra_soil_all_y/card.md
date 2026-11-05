# Datasheet — OSSL NeoSpectra soils — NIR + MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** OSSL NeoSpectra soil NIR and MIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 23 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** OSSL_NIRS

## Composition

- **Alignment:** sample level; 2106 sample(s), 10127 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–19 (mean 2.481).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_mir | recovered_spectra | unknown | NIR | 600–4000 none | 1976 | 1701 |
| X_nir | recovered_spectra | unknown | NIR | 1350–2550 none | 8151 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=10127, missing=0, range -0.028–53.88, mean 1.946 ± 3.021 |
| c_tot_usda_a622_w_pct | target | numeric | *Not specified.* | n=10127, missing=180, range 0.0161–53.88, mean 2.233 ± 3.08 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=10127, missing=0, range 0–3.02, mean 0.1614 ± 0.1963 |
| s_tot_usda_a624_w_pct | target | numeric | *Not specified.* | n=10127, missing=180, range 0–18.38, mean 0.1315 ± 1.003 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=10127, missing=20, range 3.69–9.52, mean 6.307 ± 1.273 |
| bd_usda_a4_g_cm3 | target | numeric | *Not specified.* | n=10127, missing=5275, range 0.3004–2.033, mean 1.323 ± 0.2398 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=10127, missing=0, range 0–86.69, mean 20.3 ± 14.39 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=10127, missing=0, range 0–87.9, mean 38.45 ± 20.66 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=10127, missing=0, range 0.3–100, mean 41.24 ± 28.42 |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=10127, missing=6636, range -0.5671–89.03, mean 6.306 ± 9.631 |
| efferv_usda_a479_class | target | categorical | *Not specified.* | n=10127, missing=200, classes=5, top none (×7113) |
| cec_usda_a723_cmolc_kg | target | numeric | *Not specified.* | n=10127, missing=20, range 0.134–190.1, mean 16.14 ± 12.94 |
| ca_ext_usda_a722_cmolc_kg | target | numeric | *Not specified.* | n=10127, missing=20, range 0–363.6, mean 20.05 ± 33.49 |
| mg_ext_usda_a724_cmolc_kg | target | numeric | *Not specified.* | n=10127, missing=20, range 0–82.14, mean 3.44 ± 4.877 |
| k_ext_usda_a725_cmolc_kg | target | numeric | *Not specified.* | n=10127, missing=20, range 0–11.25, mean 0.5371 ± 0.6938 |
| na_ext_usda_a726_cmolc_kg | target | numeric | *Not specified.* | n=10127, missing=20, range 0–203, mean 1.27 ± 10.35 |
| wr_33kPa_usda_a415_w_pct | target | numeric | *Not specified.* | n=10127, missing=9239, range 1.003–127.9, mean 23.6 ± 14.79 |
| wr_1500kPa_usda_a417_w_pct | target | numeric | *Not specified.* | n=10127, missing=195, range 0.07522–96.14, mean 11.57 ± 7.573 |
| al_dith_usda_a65_w_pct | target | numeric | *Not specified.* | n=10127, missing=1485, range 0–2.285, mean 0.1799 ± 0.2583 |
| p_ext_usda_a652_mg_kg | target | numeric | *Not specified.* | n=10127, missing=6623, range 0–1359, mean 30.27 ± 68.86 |
| p_ext_usda_a1070_mg_kg | target | numeric | *Not specified.* | n=10127, missing=9789, range 0.3618–256.4, mean 26.28 ± 32.24 |
| k_ext_usda_a1065_mg_kg | target | numeric | *Not specified.* | n=10127, missing=9789, range 0–730.2, mean 171.2 ± 121.9 |
| ec_usda_a364_ds_m | target | numeric | *Not specified.* | n=10127, missing=5412, range 0.012–81.93, mean 1.341 ± 5.993 |
| ID_sample | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2106, top 67922 (×20) |
| SpectralRep | metadata | numeric | *Not specified.* | n=10127, missing=0, range 1–19, mean 2.562 ± 1.922 |
| dataset | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=1, top Neospectra database v1.2 (×10127) |
| collection_name | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top neospectra_nir (×8151) |
| dataset_code | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top NEOSPECTRA.NIR (×8151) |
| dataset_owner | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=1, top USDA-NRCS-NSSC-KSSL, WCRC, UNL, iSDA (×10127) |
| spectral_kind | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top nir (×8151) |
| scan_local_id | metadata | categorical | *Not specified.* | n=10127, missing=1976, classes=8067, top NEO2_067922 (×4) |
| scan_lab | metadata | categorical | *Not specified.* | n=10127, missing=1976, classes=2, top KSSL (×5009) |
| scan_model_name | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=10, top Bruker Vertex 70 with HTS-XT accessory (×1976) |
| scan_model_code | metadata | categorical | *Not specified.* | n=10127, missing=1976, classes=9, top 21020076 (×1132) |
| scan_optics | metadata | categorical | *Not specified.* | n=10127, missing=8151, classes=1, top KSSL SOPs (×1976) |
| scan_preparation | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top <2 mm (×8151) |
| country_iso3166 | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=4, top USA (×9947) |
| upper_depth_cm | metadata | numeric | *Not specified.* | n=10127, missing=0, range 0–210, mean 21.6 ± 35.22 |
| lower_depth_cm | metadata | numeric | *Not specified.* | n=10127, missing=0, range 1–254, mean 38.71 ± 44.44 |
| texture_class | metadata | categorical | *Not specified.* | n=10127, missing=2453, classes=136, top Silt loam (×1535) |
| pedon_taxa | metadata | categorical | *Not specified.* | n=10127, missing=802, classes=850, top Mixed, thermic Lamellic Ustipsamment (×306) |
| horizon_designation | metadata | categorical | *Not specified.* | n=10127, missing=356, classes=257, top A (×1702) |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=10127, missing=0, range 601–1701, mean 815.6 ± 435.9 |
| dimensions | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=1, top 1D (×10127) |
| wavelength_note | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top neospectra_nir_1350_2550_nm_step_2 (×8151) |
| active_status | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=1, top active (×10127) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=10127, missing=0, classes=2, top ossl_regression_b031e1af \| ossl_soil_ph_h2o_usda_a268_index_neospectra_nirs_ossl (×8151) |
| site_id | metadata | identifier | *Not specified.* | *Not specified.* |
| longitude | metadata | numeric | *Not specified.* | n=10127, missing=10127, range —, mean *Not specified.* ± *Not specified.* |
| latitude | metadata | numeric | *Not specified.* | n=10127, missing=10127, range —, mean *Not specified.* ± *Not specified.* |
| campaign_date_begin | metadata | datetime | *Not specified.* | *Not specified.* |
| campaign_date_end | metadata | datetime | *Not specified.* | *Not specified.* |
| location_error_m | metadata | numeric | *Not specified.* | n=10127, missing=10127, range —, mean *Not specified.* ± *Not specified.* |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 2106

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_nir_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_soilsite_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_soillab_v1.2.csv.gz`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite).; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 10 fields, Y: 23 fields, measurements: 0 fields, passport: 30 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Recovered from local initial-source exports; rights not cleared for redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `5c7f05f7eb2f0b463deef9be81410a5f57b1a32264a6a676c3c98468b0abc0fc`
- **Processing hash:** `2db467dcbfe0900066be5519de6cf605d2d525c6467a4fae22bd2869a81eebcf` | **metadata hash:** `dfe8e2b6d22c3b12c9075a57b7e41c4368c5373d864342a36db82f426563f84f`
