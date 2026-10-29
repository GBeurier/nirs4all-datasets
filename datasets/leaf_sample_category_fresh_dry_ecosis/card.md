# Datasheet — EcoSIS Fresh and Dry Spectra of Several Plant Tissues and Chemical and Phenological Constituents (Sample_category)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Fresh and Dry Spectra of Several Plant Tissues and Chemical and Phenological Constituents (Sample_category). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Fresh and Dry Spectra of Several Plant Tissues and Chemical and Phenological Constituents

## Composition

- **Alignment:** sample level; 74 sample(s), 75 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.014).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | elvidge_spectra_values | Beckman UV-5240 Spectrophotometer | NIR | 0.4–2.5 nm | 75 | 826 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Sample_category | target | categorical | *Not specified.* | n=74, missing=0, classes=2, top 1 (×59) |
| SpectralRep | metadata | numeric | *Not specified.* | n=74, missing=0, range 1–1, mean 1 ± 0 |
| Sample Code | metadata | categorical | *Not specified.* | n=74, missing=0, classes=74, top CDE001 (×1) |
| Sample Name | metadata | categorical | *Not specified.* | n=74, missing=0, classes=74, top Spruce Cellulose (×1) |
| Latin Species | metadata | categorical | *Not specified.* | n=74, missing=15, classes=8, top Platanus racemosa (×11) |
| Sample Type | metadata | categorical | *Not specified.* | n=74, missing=0, classes=23, top Purified Powder (×15) |
| Sample category | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top Plant Tissue (×59) |
| Instrument | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Beckman UV-5240 Spectrophotometer (×74) |
| Foreoptic | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Integrating Sphere (×74) |
| dataset | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top EcoSIS (×74) |
| dataset_slug | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents (×74) |
| task_type | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top classification (×74) |
| trait_header | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Sample_category (×74) |
| target_original_name | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Sample category (×74) |
| measurement_hint | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top elvidge_spectra_values (×74) |
| raw_label | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top Plant Tissue (×59) |
| reference_value | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top Plant Tissue (×59) |
| class_index | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top 1 (×59) |
| class_label | metadata | categorical | *Not specified.* | n=74, missing=0, classes=2, top Plant Tissue (×59) |
| n_points_original | metadata | numeric | *Not specified.* | n=74, missing=0, range 826–826, mean 826 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top 1D (×74) |
| axis_note | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×74) |
| official_data_url | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top https://data.ecosis.org/dataset/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents (×74) |
| official_package_url | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top https://ecosis.org/package/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents (×74) |
| license | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Other (Open) (×74) |
| license_url | metadata | categorical | *Not specified.* | n=74, missing=74, classes=0, — |
| rights_status | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top explicit_open (×74) |
| usage_scope | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top public_reuse_possible (×74) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top True (×74) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=74, missing=74, classes=0, — |
| notes | metadata | categorical | *Not specified.* | n=74, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×74) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
- **Curated views:** M: 2 fields, Y: 1 fields, measurements: 2 fields, passport: 32 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Other (Open).
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f6d86aecd69494337fd7bdf6ecad3adbe10464d0206cb05162255ec82b711e5f`
- **Processing hash:** `b5616f5897e575467c88372d2e5d0f23e0adb9c15a5a54a7fc158d1f73875ceb` | **metadata hash:** `c6373af3fa6c8410400778d6992d5288f2485580a56d5edeaf0d3f67e564a855`
