# Datasheet — ossl neospectra nir soil all y

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ossl
- **Description:** ossl neospectra nir soil all y. v2.0 standardized NIRS package: 1 spectral source(s), 23 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ossl
- **Contributor:** OSSL_NIRS

## Composition

- **Alignment:** observation level; 8151 sample(s), 8151 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 1350–2550 none | 8151 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| oc_usda_c729_w_pct | target | numeric | *Not specified.* | n=8151, missing=0, range -0.028–53.88, mean 1.917 ± 3.078 |
| c_tot_usda_a622_w_pct | target | numeric | *Not specified.* | n=8151, missing=180, range 0.0161–53.88, mean 2.213 ± 3.142 |
| n_tot_usda_a623_w_pct | target | numeric | *Not specified.* | n=8151, missing=0, range 0–3.02, mean 0.159 ± 0.199 |
| s_tot_usda_a624_w_pct | target | numeric | *Not specified.* | n=8151, missing=180, range 0–18.38, mean 0.132 ± 0.9963 |
| ph_h2o_usda_a268_index | target | numeric | *Not specified.* | n=8151, missing=20, range 3.69–9.52, mean 6.313 ± 1.274 |
| bd_usda_a4_g_cm3 | target | numeric | *Not specified.* | n=8151, missing=4241, range 0.3004–2.033, mean 1.326 ± 0.2396 |
| clay_tot_usda_a334_w_pct | target | numeric | *Not specified.* | n=8151, missing=0, range 0–86.69, mean 20.43 ± 14.53 |
| silt_tot_usda_c62_w_pct | target | numeric | *Not specified.* | n=8151, missing=0, range 0–87.9, mean 38.52 ± 20.79 |
| sand_tot_usda_c60_w_pct | target | numeric | *Not specified.* | n=8151, missing=0, range 0.3–100, mean 41.05 ± 28.5 |
| caco3_usda_a54_w_pct | target | numeric | *Not specified.* | n=8151, missing=5343, range -0.5671–89.03, mean 6.386 ± 9.656 |
| efferv_usda_a479_class | target | categorical | *Not specified.* | n=8151, missing=197, classes=5, top none (×5688) |
| cec_usda_a723_cmolc_kg | target | numeric | *Not specified.* | n=8151, missing=20, range 0.134–190.1, mean 16.11 ± 13.12 |
| ca_ext_usda_a722_cmolc_kg | target | numeric | *Not specified.* | n=8151, missing=20, range 0–363.6, mean 20.07 ± 33.73 |
| mg_ext_usda_a724_cmolc_kg | target | numeric | *Not specified.* | n=8151, missing=20, range 0–82.14, mean 3.476 ± 4.947 |
| k_ext_usda_a725_cmolc_kg | target | numeric | *Not specified.* | n=8151, missing=20, range 0–11.25, mean 0.5317 ± 0.683 |
| na_ext_usda_a726_cmolc_kg | target | numeric | *Not specified.* | n=8151, missing=20, range 0–203, mean 1.359 ± 10.78 |
| wr_33kPa_usda_a415_w_pct | target | numeric | *Not specified.* | n=8151, missing=7431, range 1.003–127.9, mean 23.95 ± 14.96 |
| wr_1500kPa_usda_a417_w_pct | target | numeric | *Not specified.* | n=8151, missing=170, range 0.07522–96.14, mean 11.64 ± 7.671 |
| al_dith_usda_a65_w_pct | target | numeric | *Not specified.* | n=8151, missing=1282, range 0–2.285, mean 0.1832 ± 0.2615 |
| p_ext_usda_a652_mg_kg | target | numeric | *Not specified.* | n=8151, missing=5355, range 0–1359, mean 28.83 ± 64.82 |
| p_ext_usda_a1070_mg_kg | target | numeric | *Not specified.* | n=8151, missing=7889, range 0.3618–256.4, mean 25.99 ± 31.44 |
| k_ext_usda_a1065_mg_kg | target | numeric | *Not specified.* | n=8151, missing=7889, range 0–730.2, mean 167 ± 117.1 |
| ec_usda_a364_ds_m | target | numeric | *Not specified.* | n=8151, missing=4378, range 0.012–81.93, mean 1.423 ± 6.264 |
| ID_sample | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=2106, top 67922 (×19) |
| SpectralRep | metadata | numeric | *Not specified.* | n=8151, missing=0, range 1–19, mean 2.941 ± 1.963 |
| dataset | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top Neospectra database v1.2 (×8151) |
| collection_name | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top neospectra_nir (×8151) |
| dataset_code | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top NEOSPECTRA.NIR (×8151) |
| dataset_title | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top Neospectra NIR soil spectral library (×8151) |
| dataset_owner | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top USDA-NRCS-NSSC-KSSL, WCRC, UNL, iSDA (×8151) |
| dataset_slug | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top NEOSPECTRA.NIR (×8151) |
| task_type | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top regression (×8151) |
| trait_header | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top clay_tot_usda_a334_w_pct (×8151) |
| trait_header_original | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top clay.tot_usda.a334_w.pct (×8151) |
| spectral_kind | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top nir (×8151) |
| scan_local_id | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=8067, top NEO2_067922 (×4) |
| scan_lab | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=2, top KSSL (×5009) |
| scan_model_name | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=9, top NEO3 (×1132) |
| scan_model_code | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=9, top 21020076 (×1132) |
| scan_optics | metadata | categorical | *Not specified.* | n=8151, missing=8151, classes=0, — |
| scan_preparation | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top <2 mm (×8151) |
| country_iso3166 | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=4, top USA (×7971) |
| upper_depth_cm | metadata | numeric | *Not specified.* | n=8151, missing=0, range 0–210, mean 22.95 ± 36.34 |
| lower_depth_cm | metadata | numeric | *Not specified.* | n=8151, missing=0, range 1–254, mean 40.43 ± 45.76 |
| texture_class | metadata | categorical | *Not specified.* | n=8151, missing=1917, classes=136, top Silt loam (×1244) |
| pedon_taxa | metadata | categorical | *Not specified.* | n=8151, missing=618, classes=850, top Mixed, thermic Lamellic Ustipsamment (×254) |
| horizon_designation | metadata | categorical | *Not specified.* | n=8151, missing=297, classes=257, top A (×1306) |
| raw_label | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=2083, top 0.0 (×50) |
| reference_value | metadata | numeric | *Not specified.* | n=8151, missing=0, range 0–86.69, mean 20.43 ± 14.53 |
| class_index | metadata | categorical | *Not specified.* | n=8151, missing=8151, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=8151, missing=8151, classes=0, — |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=8151, missing=0, range 601–601, mean 601 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top 1D (×8151) |
| wavelength_note | metadata | categorical | *Not specified.* | n=8151, missing=0, classes=1, top neospectra_nir_1350_2550_nm_step_2 (×8151) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 8151

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_nir_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_soilsite_v1.2.csv.gz`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://storage.googleapis.com/soilspec4gg-public/neospectra_soillab_v1.2.csv.gz`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `8238c194c27b95b8955abbf9070ea1043181500687f9e9be6bd2dbd152a4916e`
- **Processing hash:** `8c86b608e46fa2dd770ca0a316a56569c803166018c1774c8d02ad6bc15e3da6` | **metadata hash:** `902df92da3f382b136a16f524b1f3544e9ab02ce2df633d601cd674fae79c29d`
