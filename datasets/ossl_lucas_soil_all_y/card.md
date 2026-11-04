# Datasheet — OSSL LUCAS soil vis-NIR and MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** OSSL LUCAS soil vis-NIR and MIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** OSSL_NIRS

## Composition

- **Alignment:** sample level; 40175 sample(s), 80350 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_mir | recovered_spectra | unknown | NIR | 600–4000 none | 40175 | 1701 |
| X_visnir | recovered_spectra | unknown | NIR | 350–2500 none | 40175 | 1076 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=80350, missing=0, range 0–97.6, mean 5.486 ± 13.13 |
| cec_usda_a723_cmolc_kg | target | numeric | *Not specified.* | n=80350, missing=43564, range 1–234, mean 15.63 ± 14.12 |
| cf_usda_c236_w_pct | target | numeric | *Not specified.* | n=80350, missing=35054, range 0–90, mean 14.73 ± 11.97 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=80350, missing=35050, range 0–79, mean 17.97 ± 12.77 |
| ec_usda_a364_ds_m | target | numeric | *Not specified.* | n=80350, missing=36786, range 0.0031–9.69, mean 0.261 ± 0.3337 |
| k_ext_usda_a725_cmolc_kg | target | numeric | *Not specified.* | n=80350, missing=0, range 0–51.31, mean 0.9994 ± 1.146 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=80350, missing=0, range 0–3.86, mean 0.3016 ± 0.3686 |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=80350, missing=0, range 0.01–58.68, mean 4.63 ± 8.363 |
| p_ext_usda_a274_mg_kg | target | numeric | *Not specified.* | n=80350, missing=0, range 0–1366, mean 31.54 ± 32.65 |
| ph_cacl2_usda_a481_index | target | numeric | *Not specified.* | n=80350, missing=0, range 2.57–10, mean 5.675 ± 1.414 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=80350, missing=0, range 3.17–10.37, mean 6.16 ± 1.35 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=80350, missing=35050, range 0–100, mean 39.9 ± 25.91 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=80350, missing=35050, range 0–92, mean 37.5 ± 18.95 |
| ID_sample | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=40175, top b27ab24c14a301c1f2be8279db5dc60b (×2) |
| SpectralRep | metadata | numeric | *Not specified.* | n=80350, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=1, top OSSL snapshot v1.2 (×80350) |
| collection_name | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=2, top ossl_visnir (×40175) |
| dataset_code | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=1, top LUCAS.SSL (×80350) |
| dataset_owner | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=1, top European Soil Data Centre (ESDAC), European Commission, Joint Research Centre (×80350) |
| spectral_kind | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=2, top visnir (×40175) |
| scan_local_id | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=40175, top 2009.47142646 (×2) |
| scan_model_name | metadata | categorical | *Not specified.* | n=80350, missing=40175, classes=1, top Metrohm NIRS XDS RapidContent Analyzer (×40175) |
| scan_model_code | metadata | categorical | *Not specified.* | n=80350, missing=40175, classes=1, top Metrohm_NIRS_XDS_RapidContent_Analyzer (×40175) |
| scan_preparation | metadata | categorical | *Not specified.* | n=80350, missing=40175, classes=1, top Sieved <2 mm (×40175) |
| upper_depth_cm | metadata | numeric | *Not specified.* | n=80350, missing=0, range 0–0, mean 0 ± 0 |
| lower_depth_cm | metadata | numeric | *Not specified.* | n=80350, missing=0, range 20–20, mean 20 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=80350, missing=0, range 1076–1701, mean 1388 ± 312.5 |
| dimensions | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=1, top 1D (×80350) |
| wavelength_note | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=2, top ossl_visnir_350_2500_nm_step_2 (×40175) |
| active_status | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=1, top active (×80350) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=80350, missing=0, classes=2, top ossl_regression_743303ac \| ossl_soil_clay_tot_usda_a334_w_pct_lucas_nirs_ossl (×40175) |
| site_id | metadata | identifier | *Not specified.* | *Not specified.* |
| longitude | metadata | numeric | *Not specified.* | n=80350, missing=0, range -10.05–34.03, mean 10.3 ± 10.75 |
| latitude | metadata | numeric | *Not specified.* | n=80350, missing=0, range 34.69–69.96, mean 49.42 ± 7.562 |
| campaign_date_begin | metadata | datetime | *Not specified.* | *Not specified.* |
| campaign_date_end | metadata | datetime | *Not specified.* | *Not specified.* |
| location_error_m | metadata | numeric | *Not specified.* | n=80350, missing=0, range 1000–1000, mean 1000 ± 0 |
| campaign_year | metadata | numeric | *Not specified.* | n=80350, missing=0, range 2009–2015, mean 2012 ± 2.989 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 40175

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soillab_L1_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_visnir_L0_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soilsite_L0_v1.2.csv.gz`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite).; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 5 fields, Y: 13 fields, passport: 30 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `bb9bc03d8b56d1fa1b10dff54e7d600f8edcf351f9fbe11b5fbb0e38049624b8`
- **Processing hash:** `cebdc6b57c574487fbfa33551b0b84dfd63d977c28d639135c7957f4de0cf51c` | **metadata hash:** `5dd9ff81db1c777ae6f6c4776e0caf67f5d7b9955bcccb7ae70975ed5d006e8e`
