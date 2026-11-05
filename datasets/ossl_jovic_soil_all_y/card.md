# Datasheet — OSSL Jovic soils — Vis-NIR + MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** OSSL Jovic soil vis-NIR and MIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** NIRS DB

## Composition

- **Alignment:** sample level; 135 sample(s), 180 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_mir | recovered_spectra | unknown | NIR | 600–4000 none | 45 | 1701 |
| X_visnir | recovered_spectra | unknown | NIR | 350–2500 nm | 135 | 1076 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| c_tot_usda_a622_w_pct | target | numeric | *Not specified.* | n=180, missing=90, range 1.425–7.061, mean 3.467 ± 1.481 |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=180, missing=90, range 0–21.99, mean 5.327 ± 6.499 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=180, missing=0, range 5.533–60.81, mean 27.69 ± 13.46 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=180, missing=90, range 0.049–0.493, mean 0.1947 ± 0.1121 |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=180, missing=90, range 1.302–5.016, mean 2.827 ± 0.9647 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=180, missing=90, range 5.38–9.177, mean 7.414 ± 0.8691 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=180, missing=0, range 9.027–92.27, mean 46.56 ± 23.72 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=180, missing=0, range 1.227–53.39, mean 25.84 ± 12.48 |
| ID_sample | metadata | categorical | *Not specified.* | n=180, missing=0, classes=135, top 96c7805e64f45618ce67528fea6a4b9f (×2) |
| SpectralRep | metadata | numeric | *Not specified.* | n=180, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top OSSL snapshot v1.2 (×180) |
| collection_name | metadata | categorical | *Not specified.* | n=180, missing=0, classes=2, top ossl_visnir (×135) |
| dataset_code | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top SERBIA.SSL (×180) |
| dataset_owner | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top Jović et al. (2019) (×180) |
| spectral_kind | metadata | categorical | *Not specified.* | n=180, missing=0, classes=2, top visnir (×135) |
| scan_local_id | metadata | categorical | *Not specified.* | n=180, missing=0, classes=135, top 136 (×2) |
| scan_model_name | metadata | categorical | *Not specified.* | n=180, missing=135, classes=1, top ThermoFisher Nicolet Nexus 670 (×45) |
| scan_model_code | metadata | categorical | *Not specified.* | n=180, missing=135, classes=1, top ThermoFisher_Nicolet_Nexus_670 (×45) |
| scan_optics | metadata | categorical | *Not specified.* | n=180, missing=135, classes=1, top DTGS detector, DRIFT accessory, Gold background (×45) |
| scan_preparation | metadata | categorical | *Not specified.* | n=180, missing=135, classes=1, top Finelly ground <80 mesh (×45) |
| country_iso3166 | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top SRB (×180) |
| pedon_taxa | metadata | categorical | *Not specified.* | n=180, missing=0, classes=5, top Psamments (×36) |
| horizon_designation | metadata | numeric | *Not specified.* | n=180, missing=0, range 1–3, mean 1.75 ± 0.8315 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=180, missing=0, range 1076–1701, mean 1232 ± 271.4 |
| dimensions | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top 1D (×180) |
| wavelength_note | metadata | categorical | *Not specified.* | n=180, missing=0, classes=2, top ossl_visnir_350_2500_nm_step_2 (×135) |
| active_status | metadata | categorical | *Not specified.* | n=180, missing=0, classes=1, top active (×180) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=180, missing=0, classes=2, top ossl_regression_adbc04c8 \| ossl_soil_clay_tot_usda_a334_w_pct_jovic_nirs_ossl (×135) |
| site_id | metadata | identifier | *Not specified.* | *Not specified.* |
| longitude | metadata | numeric | *Not specified.* | n=180, missing=0, range 19.13–21.16, mean 19.82 ± 0.5237 |
| latitude | metadata | numeric | *Not specified.* | n=180, missing=0, range 44.54–46.07, mean 45.33 ± 0.357 |
| campaign_date_begin | metadata | datetime | *Not specified.* | *Not specified.* |
| campaign_date_end | metadata | datetime | *Not specified.* | *Not specified.* |
| location_error_m | metadata | numeric | *Not specified.* | n=180, missing=0, range 111–111, mean 111 ± 0 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 135

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soillab_L1_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_visnir_L0_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soilsite_L0_v1.2.csv.gz`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite).; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 4 fields, Y: 8 fields, measurements: 0 fields, passport: 32 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `38d1d53105ca22dcadab899edac7d21e599712ff1408e70321f5f980d816a9d0`
- **Processing hash:** `3ad5a399829c13b5d2bfa0d542604df41ac056bf6c7f1ebbe7692e4a820bceb3` | **metadata hash:** `275c76cdabcc99f2f9f83395fde8935549d2d712bfbe53889f5f1b36be4052ab`
