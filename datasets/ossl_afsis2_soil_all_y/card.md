# Datasheet — OSSL AfSIS-II soil vis-NIR and MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** OSSL AfSIS-II soil vis-NIR and MIR. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 14 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** OSSL_NIRS

## Composition

- **Alignment:** sample level; 151 sample(s), 302 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_mir | recovered_spectra | unknown | NIR | 600–4000 none | 151 | 1701 |
| X_visnir | recovered_spectra | unknown | NIR | 350–2500 none | 151 | 1076 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| al_ext_usda_a1056_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 108–1672, mean 694.1 ± 332.5 |
| b_ext_mel3_mg_kg | target | numeric | *Not specified.* | n=302, missing=288, range 0.3–1, mean 0.7714 ± 0.2644 |
| c_tot_usda_a622_w_pct | target | numeric | *Not specified.* | n=302, missing=0, range 0.097–4.406, mean 0.8046 ± 0.7124 |
| ca_ext_usda_a1059_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 15–4833, mean 833.8 ± 895.2 |
| cu_ext_usda_a1063_mg_kg | target | numeric | *Not specified.* | n=302, missing=2, range 0.1–6.29, mean 1.128 ± 1.161 |
| fe_ext_usda_a1064_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 24–578, mean 135.9 ± 107.8 |
| k_ext_usda_a1065_mg_kg | target | numeric | *Not specified.* | n=302, missing=2, range 6–416, mean 63.73 ± 59.6 |
| mg_ext_usda_a1066_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 2–1351, mean 185.2 ± 216.1 |
| mn_ext_usda_a1067_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 0.7–509.9, mean 96.26 ± 97.96 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=302, missing=0, range 0.008–0.428, mean 0.06857 ± 0.06496 |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=302, missing=0, range 0.097–4.396, mean 0.8005 ± 0.7088 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=302, missing=0, range 4.1–8.32, mean 5.871 ± 0.7728 |
| s_ext_mel3_mg_kg | target | numeric | *Not specified.* | n=302, missing=0, range 1–84, mean 6.344 ± 9.989 |
| zn_ext_usda_a1073_mg_kg | target | numeric | *Not specified.* | n=302, missing=26, range 0.09–30.8, mean 1.526 ± 3.337 |
| ID_sample | metadata | categorical | *Not specified.* | n=302, missing=0, classes=151, top e4003f03c9444aaae892bbd452c507cd (×2) |
| SpectralRep | metadata | numeric | *Not specified.* | n=302, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top OSSL snapshot v1.2 (×302) |
| collection_name | metadata | categorical | *Not specified.* | n=302, missing=0, classes=2, top ossl_visnir (×151) |
| dataset_code | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top AFSIS2.SSL (×302) |
| dataset_owner | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top the World Agroforestry Centre (ICRAF) and Rothamsted Research (RRES) (×302) |
| spectral_kind | metadata | categorical | *Not specified.* | n=302, missing=0, classes=2, top visnir (×151) |
| scan_local_id | metadata | categorical | *Not specified.* | n=302, missing=0, classes=151, top GHBADISTDF3D5DFG (×2) |
| scan_model_name | metadata | categorical | *Not specified.* | n=302, missing=151, classes=1, top Bruker Alpha 1 ZnSe (×151) |
| scan_model_code | metadata | categorical | *Not specified.* | n=302, missing=151, classes=1, top Bruker_Alpha_1_ZnSe (×151) |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=302, missing=0, range 1076–1701, mean 1388 ± 313 |
| dimensions | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top 1D (×302) |
| wavelength_note | metadata | categorical | *Not specified.* | n=302, missing=0, classes=2, top ossl_visnir_350_2500_nm_step_2 (×151) |
| active_status | metadata | categorical | *Not specified.* | n=302, missing=0, classes=1, top active (×302) |
| replaces_dataset_id | metadata | categorical | *Not specified.* | n=302, missing=0, classes=2, top ossl_regression_f27317d6 (×151) |
| site_id | metadata | identifier | *Not specified.* | *Not specified.* |
| longitude | metadata | numeric | *Not specified.* | n=302, missing=302, range —, mean *Not specified.* ± *Not specified.* |
| latitude | metadata | numeric | *Not specified.* | n=302, missing=302, range —, mean *Not specified.* ± *Not specified.* |
| campaign_date_begin | metadata | datetime | *Not specified.* | *Not specified.* |
| campaign_date_end | metadata | datetime | *Not specified.* | *Not specified.* |
| location_error_m | metadata | numeric | *Not specified.* | n=302, missing=302, range —, mean *Not specified.* ± *Not specified.* |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 151

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soillab_L1_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_visnir_L0_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/ossl_soilsite_L0_v1.2.csv.gz`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite).; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 14 fields, passport: 31 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `046780e08a0f406ec68efe2a9af74058a5b56509f5809ee4371dfd7b18d2b4e3`
- **Processing hash:** `a3ea8ac850dc155141d668284eb1a6d1b60ff37a733bd76f9b22cc346f919a12` | **metadata hash:** `a75fcab3b690d7e4df9cd8e74b9a9a6f7d067a0b731da9fd9b8732693b0dc91f`
