# Datasheet — Nirpy Research black foam entropy smoothing NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research black foam entropy smoothing NIR. v2.0 standardized NIRS package: 3 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research NIR_black_foam_nirpy.zip

## Composition

- **Alignment:** sample level; 500 sample(s), 1500 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_absorbance | Nirpy Research black foam entropy smoothing NIR - absorbance | *Not specified.* | NIR | 901.8–1701 nm | 500 | 228 |
| X_reference_signal | Nirpy Research black foam entropy smoothing NIR - reference signal | *Not specified.* | NIR | 901.8–1701 nm | 500 | 228 |
| X_sample_signal | Nirpy Research black foam entropy smoothing NIR - sample signal | *Not specified.* | NIR | 901.8–1701 nm | 500 | 228 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_material | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top black_foam (×500) |
| host_date_time | metadata | categorical | *Not specified.* | n=500, missing=0, classes=500, top 18/11/23 @ 11:36:37 (×1) |
| system_temp_c | metadata | numeric | *Not specified.* | n=500, missing=0, range 29–36.81, mean 33.74 ± 2.244 |
| detector_temp_c | metadata | numeric | *Not specified.* | n=500, missing=0, range 24.1–33.44, mean 29.14 ± 2.78 |
| humidity_percent | metadata | numeric | *Not specified.* | n=500, missing=0, range 17.92–30.45, mean 22.75 ± 3.66 |
| lamp_pd | metadata | numeric | *Not specified.* | n=500, missing=0, range 3767–3780, mean 3772 ± 2.86 |
| serial_number | metadata | numeric | *Not specified.* | n=500, missing=0, range 6.1e+06–6.1e+06, mean 6.1e+06 ± 0 |
| scan_config_name | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top Column 1 (×500) |
| scan_config_type | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top Slew (×500) |
| start_wavelength_nm | metadata | numeric | *Not specified.* | n=500, missing=0, range 900–900, mean 900 ± 0 |
| end_wavelength_nm | metadata | numeric | *Not specified.* | n=500, missing=0, range 1700–1700, mean 1700 ± 0 |
| exposure_ms | metadata | numeric | *Not specified.* | n=500, missing=0, range 0.635–0.635, mean 0.635 ± 1.111e-16 |
| digital_resolution | metadata | numeric | *Not specified.* | n=500, missing=0, range 228–228, mean 228 ± 0 |
| pga_gain | metadata | numeric | *Not specified.* | n=500, missing=0, range 64–64, mean 64 ± 0 |
| total_measurement_time_sec | metadata | numeric | *Not specified.* | n=500, missing=0, range 1.6–1.611, mean 1.608 ± 0.00391 |
| absorbance_nonfinite_values_replaced | metadata | numeric | *Not specified.* | n=500, missing=0, range 0–5, mean 0.628 ± 0.8361 |
| repository_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×500) |
| blog_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://nirpyresearch.com/spectra-smoothing-based-on-information-entropy/ (×500) |
| license | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top MIT License (×500) |
| license_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×500) |
| rights_status | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top explicit_open (×500) |
| usage_scope | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top public_reuse_possible (×500) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top True (×500) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top NIR (×500) |
| axis_unit | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top nm (×500) |
| axis_min | metadata | numeric | *Not specified.* | n=500, missing=0, range 901.8–901.8, mean 901.8 ± 2.276e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=500, missing=0, range 1701–1701, mean 1701 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=500, missing=0, range 228–228, mean 228 ± 0 |
| target_status | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top no_sample_level_target_in_source (×500) |
| notes | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top Instrument CSV contains absorbance, sample signal, and reference signal, exported as aligned X blocks without smoothing or resampling. Non-finite absorbance values caused by zero sample signal are written as missing values. (×500) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/NIR_black_foam_nirpy.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://nirpyresearch.com/spectra-smoothing-based-on-information-entropy/`
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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `d1d035a1bec6ebae249ec86039954bbff36c8c3e5e807de698631ac4758e6d66`
- **Processing hash:** `640ec7e4f1dfb6a55f2f65c18f70aa3bb518c325f5b9bf68dacd1c075b932880` | **metadata hash:** `7135b6c2f337187367f36146010fdb9fc8486bd58be217c454601356a5d8ac54`
