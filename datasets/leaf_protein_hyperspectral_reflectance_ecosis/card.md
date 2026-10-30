# Datasheet — EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (Protein)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (Protein). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops

## Composition

- **Alignment:** sample level; 658 sample(s), 658 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra | SE_PSR_Plus | NIR | 350–2500 nm | 658 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Protein | target | numeric | *Not specified.* | n=658, missing=0, range 2.78–33.25, mean 7.418 ± 2.271 |
| SpectralRep | metadata | numeric | *Not specified.* | n=658, missing=0, range 1–1, mean 1 ± 0 |
| uniquefield | metadata | categorical | *Not specified.* | n=658, missing=0, classes=658, top 2018-03-19_17 (×1) |
| Glucose | metadata | numeric | *Not specified.* | n=658, missing=5, range 0.01264–24.23, mean 5.806 ± 4.961 |
| Fructose | metadata | numeric | *Not specified.* | n=658, missing=1, range 0.2065–13.56, mean 2.355 ± 1.832 |
| Sucrose | metadata | numeric | *Not specified.* | n=658, missing=5, range 0.8231–44.5, mean 9.424 ± 8.004 |
| LDP_Fructan | metadata | numeric | *Not specified.* | n=658, missing=603, range 0.01275–2.006, mean 0.4505 ± 0.4051 |
| HDP_Fructan | metadata | categorical | *Not specified.* | n=658, missing=650, classes=8, top 1.10284464 (×1) |
| Starch | metadata | numeric | *Not specified.* | n=658, missing=4, range 0.00614–200.9, mean 27.2 ± 31.72 |
| Amino_Acids | metadata | numeric | *Not specified.* | n=658, missing=10, range 0.1126–36.16, mean 4.102 ± 5.129 |
| ABA | metadata | numeric | *Not specified.* | n=658, missing=56, range 0.2882–6.733e+04, mean 1020 ± 3661 |
| Proline | metadata | numeric | *Not specified.* | n=658, missing=3, range 0.1427–44.85, mean 2.227 ± 3.544 |
| LMA | metadata | numeric | *Not specified.* | n=658, missing=0, range 14.93–92.29, mean 45.48 ± 15.94 |
| RWC | metadata | numeric | *Not specified.* | n=658, missing=0, range 41.52–94.06, mean 79.36 ± 8.574 |
| Elemental_C | metadata | numeric | *Not specified.* | n=658, missing=169, range 0.4387–47.2, mean 18.55 ± 8.763 |
| Elemental_N | metadata | numeric | *Not specified.* | n=658, missing=169, range 0.6373–6.147, mean 1.878 ± 1.04 |
| Asat | metadata | numeric | *Not specified.* | n=658, missing=519, range -0.46–43.28, mean 18.93 ± 10.14 |
| gs | metadata | numeric | *Not specified.* | n=658, missing=519, range 0.01–0.77, mean 0.2204 ± 0.1627 |
| Ci | metadata | numeric | *Not specified.* | n=658, missing=519, range -157.9–515.3, mean 199.9 ± 120 |
| Tr | metadata | numeric | *Not specified.* | n=658, missing=519, range 0.21–11.06, mean 4.389 ± 2.495 |
| VPDleaf | metadata | numeric | *Not specified.* | n=658, missing=519, range 1.04–4.21, mean 2.372 ± 0.7254 |
| Tleaf | metadata | numeric | *Not specified.* | n=658, missing=519, range 23.03–31.47, mean 26.98 ± 1.955 |
| CO2s | metadata | numeric | *Not specified.* | n=658, missing=519, range 378.7–400.3, mean 390.5 ± 4.704 |
| H2Os | metadata | numeric | *Not specified.* | n=658, missing=519, range 4–18.31, mean 12.04 ± 3.515 |
| RHs | metadata | numeric | *Not specified.* | n=658, missing=519, range 10.17–58.53, mean 36.09 ± 12.78 |
| flow | metadata | numeric | *Not specified.* | n=658, missing=519, range 299.5–500.6, mean 430.9 ± 95.52 |
| Qin | metadata | numeric | *Not specified.* | n=658, missing=519, range 1498–1802, mean 1696 ± 142.9 |
| Location | metadata | categorical | *Not specified.* | n=658, missing=0, classes=2, top glasshouse (×499) |
| Paired_Spectra | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top leaf (×658) |
| Plant | metadata | numeric | *Not specified.* | n=658, missing=159, range 17–168, mean 95.87 ± 45.69 |
| Plot | metadata | categorical | *Not specified.* | n=658, missing=499, classes=12, top 2.0 (×15) |
| Rep | metadata | categorical | *Not specified.* | n=658, missing=499, classes=3, top 1.0 (×54) |
| Species | metadata | categorical | *Not specified.* | n=658, missing=0, classes=6, top CUPE (×269) |
| Treatment | metadata | categorical | *Not specified.* | n=658, missing=0, classes=2, top watered (×339) |
| Plant_Age | metadata | numeric | *Not specified.* | n=658, missing=0, range 35–127, mean 82.87 ± 30.89 |
| Days_Into_Treatment | metadata | numeric | *Not specified.* | n=658, missing=0, range 3–37, mean 19.17 ± 8.598 |
| Measurement_Date | metadata | categorical | *Not specified.* | n=658, missing=0, classes=31, top 7/19/19 (×36) |
| Instrument | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top SE_PSR_Plus (×658) |
| Pre_or_Post_Treatment | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top post (×658) |
| dataset | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top EcoSIS (×658) |
| dataset_slug | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×658) |
| task_type | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top regression (×658) |
| trait_header | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top Protein (×658) |
| target_original_name | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top Protein (×658) |
| measurement_hint | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top leaf_spectra (×658) |
| raw_label | metadata | categorical | *Not specified.* | n=658, missing=0, classes=658, top 33.24544142 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=658, missing=0, range 2.78–33.25, mean 7.418 ± 2.271 |
| class_index | metadata | categorical | *Not specified.* | n=658, missing=658, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=658, missing=658, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=658, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top 1D (×658) |
| axis_note | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×658) |
| official_data_url | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×658) |
| official_package_url | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top https://ecosis.org/package/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×658) |
| license | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top Creative Commons Attribution (×658) |
| license_url | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×658) |
| rights_status | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top explicit_open (×658) |
| usage_scope | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top public_reuse_possible (×658) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top True (×658) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top ecosis_hyperspectral_leaf_reflectance_biochemistry_and_physiol_reflectance_nirs (×658) |
| notes | metadata | categorical | *Not specified.* | n=658, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×658) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M. Index fields examined: Rep. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 12 fields, Y: 1 fields, measurements: 21 fields, passport: 34 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Creative Commons Attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `45791a21db38895c99e710a46e1c83f8aa3db54f1f2b867568ea529483a6819a`
- **Processing hash:** `4a2db3d33ac59a3fc309a64cc5803d5b1b5b922db4c7df87fdf85bdcfcacc1f5` | **metadata hash:** `b8a33473272ae8e18096f61e6f8d2a95bf6a0af691efedaf0eb93a2cfcf0bc72`
