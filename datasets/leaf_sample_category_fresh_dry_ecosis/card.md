# Datasheet — Plant tissues — fresh + dry reflectance (EcoSIS)

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
| X | elvidge_spectra_values | Beckman UV-5240 Spectrophotometer | NIR | 400–2500 nm | 75 | 826 |

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
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.; X: native axis unit 'um' is normalized to nm (multiply coordinates by 1000); original axis headers and measured values remain unchanged in the raw bundle.; Spectral declaration for X: The Elvidge EcoSIS resource records its native optical axis in micrometers. The standardized card incorrectly called the unchanged 0.4-2.5 coordinates nm. Normalize canonical coordinates to nm while retaining the original numeric raw headers and every measurement. Evidence: https://data.ecosis.org/dataset/fresh-and-dry-spectra-of-several-plant-tissues-and-chemical-and-phenological-constituents, https://ris.utwente.nl/ws/files/276844036/Plant_phenolics_and_absorption_features_in_vegetation_reflectance_spectra_near_1.66_m.pdf
- **Curated views:** M: 2 fields, Y: 1 fields, passport: 32 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.1 | **schema/protocol:** 2.0
- **Content hash:** `443705aab062304d58c96549c5d807002e9d09dd9ac8df7943079ffc82937abf`
- **Processing hash:** `eb8422369390f25415b705d5069e8ff412826069997ffc4e4a7c6db5faac9ec8` | **metadata hash:** `684ba7e1458e45e0d23a8f1ef3557e654dd61ed13680dfdc8117041b8595e20e`
