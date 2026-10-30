# Datasheet — EcoSIS Leaf spectra of boreal tree species from Alberta potted tree experiment (Initial)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Leaf spectra of boreal tree species from Alberta potted tree experiment (Initial). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Leaf spectra of boreal tree species from Alberta potted tree experiment

## Composition

- **Alignment:** sample level; 3235 sample(s), 3235 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | RooftopSCReflectance | *Not specified.* | NIR | 350–1130 nm | 3235 | 781 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Initial | target | numeric | *Not specified.* | n=3235, missing=0, range 0–5, mean 2.664 ± 1.488 |
| SpectralRep | metadata | numeric | *Not specified.* | n=3235, missing=0, range 1–1, mean 1 ± 0 |
| ID | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=3235, top 20151112Pg1 (×1) |
| Date | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=27, top 2016519 (×180) |
| Latitude | metadata | numeric | *Not specified.* | n=3235, missing=0, range 53.53–53.53, mean 53.53 ± 0 |
| Longitude | metadata | numeric | *Not specified.* | n=3235, missing=0, range -113.5–-113.5, mean -113.5 ± 0 |
| FullName | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top Pinus banksiana (×735) |
| Genus | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=4, top Picea (×1428) |
| Species | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top banksiana (×735) |
| metadata_Initial | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top Pb (×735) |
| Individual | metadata | numeric | *Not specified.* | n=3235, missing=0, range 1–30, mean 14.84 ± 8.485 |
| dataset | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top EcoSIS (×3235) |
| dataset_slug | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment (×3235) |
| task_type | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top classification (×3235) |
| trait_header | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Initial (×3235) |
| target_original_name | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Initial (×3235) |
| measurement_hint | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top RooftopSCReflectance (×3235) |
| raw_label | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top Pb (×735) |
| reference_value | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top Pb (×735) |
| class_index | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top 2 (×735) |
| class_label | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=6, top Pb (×735) |
| n_points_original | metadata | numeric | *Not specified.* | n=3235, missing=0, range 781–781, mean 781 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top 1D (×3235) |
| axis_note | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×3235) |
| official_data_url | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top https://data.ecosis.org/dataset/leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment (×3235) |
| official_package_url | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top https://ecosis.org/package/leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment (×3235) |
| license | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×3235) |
| license_url | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by-sa (×3235) |
| rights_status | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top explicit_open (×3235) |
| usage_scope | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top public_reuse_possible (×3235) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top True (×3235) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top ecosis_leaf_spectra_of_boreal_tree_species_from_alberta_potted_reflectance_nirs (×3235) |
| notes | metadata | categorical | *Not specified.* | n=3235, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×3235) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/leaf-spectra-of-boreal-tree-species-from-alberta-potted-tree-experiment`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 4 fields, Y: 1 fields, passport: 32 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Creative Commons Attribution Share-Alike.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `9cd5d156be9e1270497059607aa59a790db8b22237f166efb4c055bbd79733db`
- **Processing hash:** `23589e39a4b70cb72758e05550de2b4be543cf70be481c69478621f4217cd90d` | **metadata hash:** `a681c99e21ccc8c9f15cca9c6fe3e73d74c63a5e92c1ac29dff44d7df150e0c4`
