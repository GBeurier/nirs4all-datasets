# Datasheet — Nirpy Research plums outlier PCA NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research plums outlier PCA NIR. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research plums.csv

## Composition

- **Alignment:** sample level; 40 sample(s), 40 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research plums outlier PCA NIR - reflectance | *Not specified.* | NIR | 1100–2298 nm | 40 | 600 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_material | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top fresh_plum (×40) |
| repository_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×40) |
| blog_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://nirpyresearch.com/detecting-outliers-using-mahalanobis-distance-pca-python/ (×40) |
| license | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top MIT License (×40) |
| license_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×40) |
| rights_status | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top explicit_open (×40) |
| usage_scope | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top public_reuse_possible (×40) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top True (×40) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top NIR (×40) |
| axis_unit | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top nm (×40) |
| axis_min | metadata | numeric | *Not specified.* | n=40, missing=0, range 1100–1100, mean 1100 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=40, missing=0, range 2298–2298, mean 2298 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=40, missing=0, range 600–600, mean 600 ± 0 |
| spectral_signal | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top reflectance (×40) |
| target_status | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top no_sample_level_target_in_source (×40) |
| notes | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top Source blog uses these reflectance spectra for unsupervised PCA/outlier detection, no target vector is provided. (×40) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/plums.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://nirpyresearch.com/detecting-outliers-using-mahalanobis-distance-pca-python/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 0 fields, passport: 22 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `85aa1072572848cf933a7486e4153e75ec2570667668e05132247cf36177540c`
- **Processing hash:** `966ec21accab9a8e7b1e9c100785a93ff16f7eb15ccb190945467b41c31dbf4b` | **metadata hash:** `7afb4f19ed034aa472c3ca65f9099261880b3ab3b9cd5e6f0613fa44e4b137c2`
