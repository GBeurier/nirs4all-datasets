# Datasheet — EcoSIS Potato Virus Y Detection in Solanum tuberosum: Greenhouse Data (PVY_Strain)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Potato Virus Y Detection in Solanum tuberosum: Greenhouse Data (PVY_Strain). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Potato Virus Y Detection in Solanum tuberosum: Greenhouse Data

## Composition

- **Alignment:** sample level; 80 sample(s), 80 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | plantlevel_means_df_PID_Time1 | *Not specified.* | NIR | 350–2500 nm | 80 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| PVY_Strain | target | numeric | *Not specified.* | n=80, missing=0, range 0–3, mean 1.5 ± 1.125 |
| SpectralRep | metadata | numeric | *Not specified.* | n=80, missing=0, range 1–1, mean 1 ± 0 |
| Plant_ID | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top P56 (×1) |
| idstr | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top 56_mean (×1) |
| metadata_PVY_Strain | metadata | categorical | *Not specified.* | n=80, missing=0, classes=4, top NO (×20) |
| dataset | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top EcoSIS (×80) |
| dataset_slug | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data- (×80) |
| task_type | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top classification (×80) |
| trait_header | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top PVY_Strain (×80) |
| target_original_name | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top PVY_Strain (×80) |
| measurement_hint | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top plantlevel_means_df_PID_Time1 (×80) |
| raw_label | metadata | categorical | *Not specified.* | n=80, missing=0, classes=4, top NO (×20) |
| reference_value | metadata | categorical | *Not specified.* | n=80, missing=0, classes=4, top NO (×20) |
| class_index | metadata | categorical | *Not specified.* | n=80, missing=0, classes=4, top 1 (×20) |
| class_label | metadata | categorical | *Not specified.* | n=80, missing=0, classes=4, top NO (×20) |
| n_points_original | metadata | numeric | *Not specified.* | n=80, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top 1D (×80) |
| axis_note | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×80) |
| official_data_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://data.ecosis.org/dataset/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data- (×80) |
| official_package_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://ecosis.org/package/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data- (×80) |
| license | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top Other (Public Domain) (×80) |
| license_url | metadata | categorical | *Not specified.* | n=80, missing=80, classes=0, — |
| rights_status | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top explicit_open (×80) |
| usage_scope | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top public_reuse_possible (×80) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top True (×80) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=80, missing=80, classes=0, — |
| notes | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×80) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data-`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data-`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data-`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 2 fields, passport: 30 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Other (Public Domain).
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `a48f55cb3b5b5aedcb6f6f37dcc64284ee90b19f3260718dabb3cbe8ba3f2831`
- **Processing hash:** `b25337d5ac953ba03552eadeb9f5dcaf0a2ed72dd263d8b0e390705f84e8e55f` | **metadata hash:** `5b1f147913c4d1ba7fadb88567e854a0fac5e62efa17434bf97cc702bcb089d3`
