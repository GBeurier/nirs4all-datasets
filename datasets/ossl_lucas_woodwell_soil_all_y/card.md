# Datasheet — OSSL LUCAS Woodwell soil vis-NIR and MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** OSSL LUCAS Woodwell soil vis-NIR and MIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 12 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** OSSL_NIRS

## Composition

- **Alignment:** sample level; 589 sample(s), 1178 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_mir | recovered_spectra | unknown | NIR | 600–4000 none | 589 | 1701 |
| X_visnir | recovered_spectra | unknown | NIR | 350–2500 none | 589 | 1076 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–66.9, mean 4.707 ± 10.56 |
| cec_usda_a723_cmolc_kg | target | numeric | *Not specified.* | n=1178, missing=0, range 1–193.1, mean 20.53 ± 22.19 |
| cf_usda_c236_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–65, mean 14.34 ± 11.74 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–79, mean 21.54 ± 17.8 |
| k_ext_usda_a725_cmolc_kg | target | numeric | *Not specified.* | n=1178, missing=0, range 0–37.56, mean 1.314 ± 2.666 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–3.34, mean 0.3236 ± 0.5073 |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0.1–53.42, mean 5.231 ± 9.769 |
| p_ext_usda_a274_mg_kg | target | numeric | *Not specified.* | n=1178, missing=0, range 0–288, mean 23.8 ± 30.86 |
| ph_cacl2_usda_a481_index | target | numeric | *Not specified.* | n=1178, missing=0, range 2.85–7.84, mean 5.694 ± 1.372 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=1178, missing=0, range 3.55–8.55, mean 6.306 ± 1.315 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–98, mean 38.58 ± 28.48 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=1178, missing=0, range 0–83, mean 32.58 ± 18.7 |
| ID_sample | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=589, top 917158aeab35339a96567ca8882da8f2 (×2) |
| SpectralRep | metadata | numeric | *Not specified.* | n=1178, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=1, top OSSL snapshot v1.2 (×1178) |
| collection_name | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top ossl_visnir (×589) |
| dataset_code | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=1, top LUCAS.WOODWELL.SSL (×1178) |
| dataset_owner | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=1, top European Soil Data Centre (ESDAC), European Commission, Joint Research Centre (×1178) |
| spectral_kind | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top visnir (×589) |
| scan_local_id | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=589, top 11070 (×2) |
| scan_model_name | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top Metrohm NIRS XDS RapidContent Analyzer (×589) |
| scan_model_code | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top Metrohm_NIRS_XDS_RapidContent_Analyzer (×589) |
| scan_optics | metadata | categorical | *Not specified.* | n=1178, missing=589, classes=1, top KBr beamsplitter, Gold mirror, Mirror background (×589) |
| scan_preparation | metadata | categorical | *Not specified.* | n=1178, missing=589, classes=1, top Sieved <2 mm (×589) |
| upper_depth_cm | metadata | numeric | *Not specified.* | n=1178, missing=0, range 0–0, mean 0 ± 0 |
| lower_depth_cm | metadata | numeric | *Not specified.* | n=1178, missing=0, range 20–20, mean 20 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=1178, missing=0, range 1076–1701, mean 1388 ± 312.6 |
| dimensions | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=1, top 1D (×1178) |
| wavelength_note | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top ossl_visnir_350_2500_nm_step_2 (×589) |
| active_status | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=1, top active (×1178) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=1178, missing=0, classes=2, top ossl_regression_e9e5102c (×589) |
| site_id | metadata | identifier | *Not specified.* | *Not specified.* |
| longitude | metadata | numeric | *Not specified.* | n=1178, missing=0, range -9.153–30.97, mean 13.85 ± 10.43 |
| latitude | metadata | numeric | *Not specified.* | n=1178, missing=0, range 36.8–69.25, mean 49.22 ± 8.715 |
| campaign_date_begin | metadata | datetime | *Not specified.* | *Not specified.* |
| campaign_date_end | metadata | datetime | *Not specified.* | *Not specified.* |
| location_error_m | metadata | numeric | *Not specified.* | n=1178, missing=0, range 1000–1000, mean 1000 ± 0 |
| campaign_year | metadata | numeric | *Not specified.* | n=1178, missing=0, range 2009–2009, mean 2009 ± 0 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 589

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soillab_L1_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_visnir_L0_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soilsite_L0_v1.2.csv.gz`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite).; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 4 fields, Y: 12 fields, passport: 32 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `da6ec347d3d8b4336669ec1c3f06080ecbe640e2e9098270f6decd1f9be1a7e1`
- **Processing hash:** `0550362e7ed6628a8657b36e355b0fd898933be52896372a95767206a0c16adb` | **metadata hash:** `6e48b2b2e2ee3b00582c41c6439ec14b73e40fdee74383b124552a6802501f41`
