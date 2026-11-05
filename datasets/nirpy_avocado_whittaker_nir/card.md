# Datasheet — Avocado — NIR (Nirpy Whittaker series)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research avocado Whittaker smoothing NIR. v2.0 standardized NIRS package: 3 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research NIR_avocado_spectra_nirpy.zip

## Composition

- **Alignment:** sample level; 100 sample(s), 300 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_absorbance | Nirpy Research avocado Whittaker smoothing NIR - absorbance | *Not specified.* | NIR | 901.8–1701 nm | 100 | 228 |
| X_reference_signal | Nirpy Research avocado Whittaker smoothing NIR - reference signal | *Not specified.* | NIR | 901.8–1701 nm | 100 | 228 |
| X_sample_signal | Nirpy Research avocado Whittaker smoothing NIR - sample signal | *Not specified.* | NIR | 901.8–1701 nm | 100 | 228 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_material | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top Hass_avocado (×100) |
| host_date_time | metadata | categorical | *Not specified.* | n=100, missing=0, classes=100, top 10/9/21 @ 14:36:23 (×1) |
| system_temp_c | metadata | numeric | *Not specified.* | n=100, missing=0, range 27.37–29.57, mean 28.46 ± 0.6909 |
| detector_temp_c | metadata | numeric | *Not specified.* | n=100, missing=0, range 24.21–25.3, mean 24.9 ± 0.2259 |
| humidity_percent | metadata | numeric | *Not specified.* | n=100, missing=0, range 22.54–25.62, mean 24.17 ± 0.7883 |
| lamp_pd | metadata | numeric | *Not specified.* | n=100, missing=0, range 3778–3785, mean 3780 ± 1.92 |
| serial_number | metadata | numeric | *Not specified.* | n=100, missing=0, range 6.1e+06–6.1e+06, mean 6.1e+06 ± 0 |
| scan_config_name | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top Column 1 (×100) |
| scan_config_type | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top Slew (×100) |
| start_wavelength_nm | metadata | numeric | *Not specified.* | n=100, missing=0, range 900–900, mean 900 ± 0 |
| end_wavelength_nm | metadata | numeric | *Not specified.* | n=100, missing=0, range 1700–1700, mean 1700 ± 0 |
| exposure_ms | metadata | numeric | *Not specified.* | n=100, missing=0, range 0.635–0.635, mean 0.635 ± 2.232e-16 |
| digital_resolution | metadata | numeric | *Not specified.* | n=100, missing=0, range 228–228, mean 228 ± 0 |
| pga_gain | metadata | numeric | *Not specified.* | n=100, missing=0, range 64–64, mean 64 ± 0 |
| total_measurement_time_sec | metadata | numeric | *Not specified.* | n=100, missing=0, range 1.582–1.653, mean 1.618 ± 0.02674 |
| absorbance_nonfinite_values_replaced | metadata | numeric | *Not specified.* | n=100, missing=0, range 0–2, mean 0.32 ± 0.5664 |
| repository_url | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×100) |
| blog_url | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top https://nirpyresearch.com/optimising-regularisation-parameters-whittaker-smoothing/ (×100) |
| license | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top MIT License (×100) |
| license_url | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×100) |
| rights_status | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top explicit_open (×100) |
| usage_scope | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top public_reuse_possible (×100) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top True (×100) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top NIR (×100) |
| axis_unit | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top nm (×100) |
| axis_min | metadata | numeric | *Not specified.* | n=100, missing=0, range 901.8–901.8, mean 901.8 ± 2.285e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=100, missing=0, range 1701–1701, mean 1701 ± 6.856e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=100, missing=0, range 228–228, mean 228 ± 0 |
| target_status | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top no_sample_level_target_in_source (×100) |
| notes | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top Instrument CSV contains absorbance, sample signal, and reference signal, exported as aligned X blocks without smoothing or resampling. Non-finite absorbance values caused by zero sample signal are written as missing values. (×100) |
| source_archive | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top NIR_avocado_spectra_nirpy.zip (×100) |
| source_member_file | metadata | categorical | *Not specified.* | n=100, missing=0, classes=100, top Avocado_spectra/Column 1_059287_20210910_143623.csv (×1) |
| source_scan_number | metadata | numeric | *Not specified.* | n=100, missing=0, range 5.929e+04–5.939e+04, mean 5.934e+04 ± 29.01 |
| source_scan_date | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top 20210910 (×100) |
| source_scan_time | metadata | numeric | *Not specified.* | n=100, missing=0, range 1.436e+05–1.44e+05, mean 1.438e+05 ± 102.8 |
| source_use_case | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top Whittaker smoothing tutorial (×100) |
| source_context | metadata | categorical | *Not specified.* | n=100, missing=0, classes=1, top 100 NIR spectra of one Hass avocado with absorbance, sample signal, and reference signal. (×100) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/NIR_avocado_spectra_nirpy.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://nirpyresearch.com/optimising-regularisation-parameters-whittaker-smoothing/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 7 fields, Y: 0 fields, measurements: 0 fields, passport: 33 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `51d0400fa821a0dd7736ee1405b24377fd7d008652e801adfc814d6529231e59`
- **Processing hash:** `c0be3de7c3989205fcfdc7d1a1072a7fa5e7b4b2acec0ba2fd53f8191ff8c1d7` | **metadata hash:** `bc39daf6d7749e61842d3267978b70a131720a32647d0fb9d180a3f682e509a3`
