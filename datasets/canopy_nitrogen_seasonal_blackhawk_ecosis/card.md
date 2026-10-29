# Datasheet — EcoSIS Seasonal canopy spectra and traits, Blackhawk Island, WI (nitrogen)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** canopy
- **Description:** EcoSIS Seasonal canopy spectra and traits, Blackhawk Island, WI (nitrogen). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
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
| nitrogen | target | numeric | *Not specified.* | n=80, missing=0, range 0.6096–4.69, mean 2.281 ± 0.7039 |
| SpectralRep | metadata | numeric | *Not specified.* | n=80, missing=0, range 1–1, mean 1 ± 0 |
| plot_id | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top bhi2018_p002 (×1) |
| plot_num | metadata | numeric | *Not specified.* | n=80, missing=0, range 2–235, mean 80.3 ± 68.39 |
| sample_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=29, top 20180518 (×5) |
| dbh_m | metadata | numeric | *Not specified.* | n=80, missing=2, range 0.319–1.168, mean 0.6181 ± 0.1707 |
| image_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=8, top 20180604 (×11) |
| calcium | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.02536–3.262, mean 0.9321 ± 0.6781 |
| lignin | metadata | numeric | *Not specified.* | n=80, missing=0, range 2.445–23.22, mean 12.31 ± 4.621 |
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
| trait_header | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top nitrogen (×80) |
| target_original_name | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top nitrogen (×80) |
| measurement_hint | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top bhi2018_plot_spectra (×80) |
| raw_label | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top 2.4356835290286245 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.6096–4.69, mean 2.281 ± 0.7039 |
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
- **Curated views:** M: 9 fields, Y: 1 fields, measurements: 9 fields, passport: 31 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `57b370aa9e20a4469cd5193553fdfd5661f3041e924cbf68e72517cad11b607b`
- **Processing hash:** `48212471dc0069d93280c3672d7d2652537f35a4fdd096b06de1210179fb0dcd` | **metadata hash:** `5bff0c27543f80286c4f57a35ce03be74516029cb8cd768623bd7097d14e5d07`
