# Datasheet — EcoSIS Potato Virus Y detection in Solanum tuberosum, greenhouse plant-level means

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Potato Virus Y detection in Solanum tuberosum, greenhouse plant-level means. Origin database composed from 3 standardized v2.0 leaves: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Potato Virus Y Detection in Solanum tuberosum: Greenhouse Data

## Composition

- **Alignment:** sample level; 80 sample(s), 240 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 3–3 (mean 3).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | plantlevel_means_df_PID_Time1 | *Not specified.* | NIR | 350–2500 nm | 240 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| PVY_Strain | target | numeric | *Not specified.* | n=240, missing=0, range 0–3, mean 1.5 ± 1.12 |
| SpectralRep | metadata | numeric | *Not specified.* | n=240, missing=0, range 1–1, mean 1 ± 0 |
| Plant_ID | metadata | categorical | *Not specified.* | n=240, missing=0, classes=80, top P56 (×3) |
| idstr | metadata | categorical | *Not specified.* | n=240, missing=0, classes=80, top 56_mean (×3) |
| dataset | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top EcoSIS (×240) |
| n_points_original | metadata | numeric | *Not specified.* | n=240, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top 1D (×240) |
| axis_note | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×240) |
| official_data_url | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top https://data.ecosis.org/dataset/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data- (×240) |
| official_package_url | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top https://ecosis.org/package/potato-virus-y-detection-in-solanum-tuberosum--greenhouse-data- (×240) |
| license | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top Other (Public Domain) (×240) |
| rights_status | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top explicit_open (×240) |
| usage_scope | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top public_reuse_possible (×240) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top True (×240) |
| notes | metadata | categorical | *Not specified.* | n=240, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×240) |
| measurement_time | metadata | categorical | *Not specified.* | n=240, missing=0, classes=3, top time1 (×80) |

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

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 1 fields, Y: 1 fields, passport: 19 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `f4367959a640f9296971e0114ef501393923aa10b9cf64ed7df3a2b4cf3811c6`
- **Processing hash:** `929aed0cc29006f9244a124b4d81a08301c79758cf9f4cd13e675d0aac6d3715` | **metadata hash:** `c89b5b43bdc9788e0505effb0770aba39076b0bb8b6dd6482848c92575711692`
