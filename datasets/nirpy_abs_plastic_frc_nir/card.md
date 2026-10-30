# Datasheet — Nirpy Research ABS plastic FRC NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research ABS plastic FRC NIR. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research ABS_plastic.csv

## Composition

- **Alignment:** sample level; 500 sample(s), 500 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research ABS plastic FRC NIR - raw_numeric_signal_from_source | *Not specified.* | NIR | 901.9–1701 nm | 500 | 228 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_material | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top ABS_plastic (×500) |
| repository_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×500) |
| blog_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://nirpyresearch.com/optimal-spectra-smoothing-fourier-ring-correlation/ (×500) |
| license | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top MIT License (×500) |
| license_url | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×500) |
| rights_status | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top explicit_open (×500) |
| usage_scope | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top public_reuse_possible (×500) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top True (×500) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top NIR (×500) |
| axis_unit | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top nm (×500) |
| axis_min | metadata | numeric | *Not specified.* | n=500, missing=0, range 901.9–901.9, mean 901.9 ± 2.276e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=500, missing=0, range 1701–1701, mean 1701 ± 4.552e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=500, missing=0, range 228–228, mean 228 ± 0 |
| spectral_signal | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top raw_numeric_signal_from_source (×500) |
| target_status | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top no_sample_level_target_in_source (×500) |
| notes | metadata | categorical | *Not specified.* | n=500, missing=0, classes=1, top Source stores wavelength rows and scan columns. Converted by transposing to one scan per observation, no smoothing or resampling applied. (×500) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/ABS_plastic.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://nirpyresearch.com/optimal-spectra-smoothing-fourier-ring-correlation/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 23 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `60151bb4aef673a0a594acb3dc572a05c8fd780a730353a92038eeffa6f56135`
- **Processing hash:** `10d75ca416106a12bb0b3e2d3c831558ee60ef4329249ab46bd9b1acdbb0c8a3` | **metadata hash:** `1790773bc12a1b130af14e9a80cfe2ac451fe0e25c7848bd2ba0b33f5d30c2e9`
