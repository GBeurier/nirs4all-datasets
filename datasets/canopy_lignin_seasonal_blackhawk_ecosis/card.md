# Datasheet — EcoSIS Seasonal canopy spectra and traits, Blackhawk Island, WI (lignin)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** canopy
- **Description:** EcoSIS Seasonal canopy spectra and traits, Blackhawk Island, WI (lignin). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, canopy
- **Contributor:** Seasonal canopy spectra and traits, Blackhawk Island, WI

## Composition

- **Alignment:** sample level; 80 sample(s), 80 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | bhi2018_plot_spectra | *Not specified.* | NIR | 407.1–2389 nm | 80 | 187 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| lignin | target | numeric | *Not specified.* | n=80, missing=0, range 2.445–23.22, mean 12.31 ± 4.621 |
| SpectralRep | metadata | numeric | *Not specified.* | n=80, missing=0, range 1–1, mean 1 ± 0 |
| plot_id | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top bhi2018_p002 (×1) |
| plot_num | metadata | numeric | *Not specified.* | n=80, missing=0, range 2–235, mean 80.3 ± 68.39 |
| sample_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=29, top 20180518 (×5) |
| dbh_m | metadata | numeric | *Not specified.* | n=80, missing=2, range 0.319–1.168, mean 0.6181 ± 0.1707 |
| image_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=8, top 20180604 (×11) |
| nitrogen | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.6096–4.69, mean 2.281 ± 0.7039 |
| calcium | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.02536–3.262, mean 0.9321 ± 0.6781 |
| metadata_lignin | metadata | numeric | *Not specified.* | n=80, missing=0, range 2.445–23.22, mean 12.31 ± 4.621 |
| phosphorus | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.07227–0.4436, mean 0.1865 ± 0.06907 |
| potassium | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.004003–2.337, mean 0.8451 ± 0.4847 |
| tot_phenolics | metadata | numeric | *Not specified.* | n=80, missing=0, range 2.456–20.29, mean 8.803 ± 4.742 |
| chl_a_mmol_m2 | metadata | numeric | *Not specified.* | n=80, missing=0, range 24.19–556.2, mean 340 ± 134.1 |
| lma_g_m2 | metadata | numeric | *Not specified.* | n=80, missing=0, range 38.37–147.7, mean 89.44 ± 20.55 |
| genus | metadata | categorical | *Not specified.* | n=80, missing=0, classes=7, top Quercus (×26) |
| species | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top rubra (×14) |
| usda_code | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top QURU (×14) |
| common_name | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top Red oak (×14) |
| veg_type | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top tree (×80) |
| latitude | metadata | numeric | *Not specified.* | n=80, missing=0, range 43.65–43.65, mean 43.65 ± 0.002262 |
| longitude | metadata | numeric | *Not specified.* | n=80, missing=0, range -89.8–-89.79, mean -89.79 ± 0.002561 |
| dataset | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top EcoSIS (×80) |
| dataset_slug | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top seasonal-canopy-spectra-and-traits--blackhawk-island--wi (×80) |
| task_type | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top regression (×80) |
| trait_header | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top lignin (×80) |
| target_original_name | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top lignin (×80) |
| measurement_hint | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top bhi2018_plot_spectra (×80) |
| raw_label | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top 8.3655370499412 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=80, missing=0, range 2.445–23.22, mean 12.31 ± 4.621 |
| class_index | metadata | categorical | *Not specified.* | n=80, missing=80, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=80, missing=80, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=80, missing=0, range 187–187, mean 187 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top 1D (×80) |
| axis_note | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×80) |
| official_data_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://data.ecosis.org/dataset/seasonal-canopy-spectra-and-traits--blackhawk-island--wi (×80) |
| official_package_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://ecosis.org/package/seasonal-canopy-spectra-and-traits--blackhawk-island--wi (×80) |
| license | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top Open Data Commons Public Domain Dedication and License (PDDL) (×80) |
| license_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top http://www.opendefinition.org/licenses/odc-pddl (×80) |
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

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/seasonal-canopy-spectra-and-traits--blackhawk-island--wi`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=seasonal-canopy-spectra-and-traits--blackhawk-island--wi`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/seasonal-canopy-spectra-and-traits--blackhawk-island--wi`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 9 fields, Y: 1 fields, passport: 31 fields, measurements: 9 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** PDDL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Open Data Commons Public Domain Dedication and License (PDDL).
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `2d5abbb9e548e3f8ed689425d40dc0536b72763bb23ab735f44cdcad2ffcbdef`
- **Processing hash:** `4a327678f700c370daa3d52ef6370a00b3e2a311a13f7e7241c6b38a08b4aa73` | **metadata hash:** `82a099c9f0534e6f3e8869d3abc5fc4359671055979569c191e1a40d04b9c1d9`
