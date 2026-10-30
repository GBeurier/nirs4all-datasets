# Datasheet — EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (Starch)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops (Starch). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops

## Composition

- **Alignment:** sample level; 654 sample(s), 654 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra | SE_PSR_Plus | NIR | 350–2500 nm | 654 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Starch | target | numeric | *Not specified.* | n=654, missing=0, range 0.00614–200.9, mean 27.2 ± 31.72 |
| SpectralRep | metadata | numeric | *Not specified.* | n=654, missing=0, range 1–1, mean 1 ± 0 |
| uniquefield | metadata | categorical | *Not specified.* | n=654, missing=0, classes=654, top 2018-03-19_17 (×1) |
| Glucose | metadata | numeric | *Not specified.* | n=654, missing=5, range 0.01264–24.23, mean 5.835 ± 4.963 |
| Fructose | metadata | numeric | *Not specified.* | n=654, missing=1, range 0.2065–13.56, mean 2.366 ± 1.833 |
| Sucrose | metadata | numeric | *Not specified.* | n=654, missing=5, range 0.8231–44.5, mean 9.462 ± 8.013 |
| LDP_Fructan | metadata | numeric | *Not specified.* | n=654, missing=600, range 0.01275–2.006, mean 0.4575 ± 0.4055 |
| HDP_Fructan | metadata | categorical | *Not specified.* | n=654, missing=646, classes=8, top 1.10284464 (×1) |
| Amino_Acids | metadata | numeric | *Not specified.* | n=654, missing=10, range 0.1126–36.16, mean 4.096 ± 5.143 |
| Protein | metadata | numeric | *Not specified.* | n=654, missing=0, range 2.78–33.25, mean 7.428 ± 2.274 |
| ABA | metadata | numeric | *Not specified.* | n=654, missing=56, range 0.2882–6.733e+04, mean 1002 ± 3663 |
| Proline | metadata | numeric | *Not specified.* | n=654, missing=3, range 0.1427–44.85, mean 2.197 ± 3.525 |
| LMA | metadata | numeric | *Not specified.* | n=654, missing=0, range 14.93–92.29, mean 45.55 ± 15.96 |
| RWC | metadata | numeric | *Not specified.* | n=654, missing=0, range 41.52–94.06, mean 79.33 ± 8.582 |
| Elemental_C | metadata | numeric | *Not specified.* | n=654, missing=169, range 0.4387–47.2, mean 18.62 ± 8.754 |
| Elemental_N | metadata | numeric | *Not specified.* | n=654, missing=169, range 0.6373–6.147, mean 1.875 ± 1.042 |
| Asat | metadata | numeric | *Not specified.* | n=654, missing=519, range -0.46–43.28, mean 19.36 ± 9.948 |
| gs | metadata | numeric | *Not specified.* | n=654, missing=519, range 0.01–0.77, mean 0.2259 ± 0.1619 |
| Ci | metadata | numeric | *Not specified.* | n=654, missing=519, range -157.9–515.3, mean 199.7 ± 118.4 |
| Tr | metadata | numeric | *Not specified.* | n=654, missing=519, range 0.21–11.06, mean 4.49 ± 2.459 |
| VPDleaf | metadata | numeric | *Not specified.* | n=654, missing=519, range 1.04–4.21, mean 2.364 ± 0.7338 |
| Tleaf | metadata | numeric | *Not specified.* | n=654, missing=519, range 23.03–31.47, mean 26.96 ± 1.973 |
| CO2s | metadata | numeric | *Not specified.* | n=654, missing=519, range 378.7–400.3, mean 390.3 ± 4.596 |
| H2Os | metadata | numeric | *Not specified.* | n=654, missing=519, range 4–18.31, mean 12.1 ± 3.545 |
| RHs | metadata | numeric | *Not specified.* | n=654, missing=519, range 10.17–58.53, mean 36.25 ± 12.93 |
| flow | metadata | numeric | *Not specified.* | n=654, missing=519, range 299.5–500.6, mean 433.3 ± 94.7 |
| Qin | metadata | numeric | *Not specified.* | n=654, missing=519, range 1498–1802, mean 1700 ± 141.7 |
| Location | metadata | categorical | *Not specified.* | n=654, missing=0, classes=2, top glasshouse (×495) |
| Paired_Spectra | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top leaf (×654) |
| Plant | metadata | numeric | *Not specified.* | n=654, missing=159, range 17–168, mean 96.09 ± 45.79 |
| Plot | metadata | categorical | *Not specified.* | n=654, missing=495, classes=12, top 2.0 (×15) |
| Rep | metadata | categorical | *Not specified.* | n=654, missing=495, classes=3, top 1.0 (×54) |
| Species | metadata | categorical | *Not specified.* | n=654, missing=0, classes=6, top CUPE (×269) |
| Treatment | metadata | categorical | *Not specified.* | n=654, missing=0, classes=2, top watered (×339) |
| Plant_Age | metadata | numeric | *Not specified.* | n=654, missing=0, range 35–127, mean 82.7 ± 30.91 |
| Days_Into_Treatment | metadata | numeric | *Not specified.* | n=654, missing=0, range 3–37, mean 19.13 ± 8.603 |
| Measurement_Date | metadata | categorical | *Not specified.* | n=654, missing=0, classes=31, top 7/19/19 (×36) |
| Instrument | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top SE_PSR_Plus (×654) |
| Pre_or_Post_Treatment | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top post (×654) |
| dataset | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top EcoSIS (×654) |
| dataset_slug | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×654) |
| task_type | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top regression (×654) |
| trait_header | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top Starch (×654) |
| target_original_name | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top Starch (×654) |
| measurement_hint | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top leaf_spectra (×654) |
| raw_label | metadata | categorical | *Not specified.* | n=654, missing=0, classes=654, top 35.06428706 (×1) |
| reference_value | metadata | numeric | *Not specified.* | n=654, missing=0, range 0.00614–200.9, mean 27.2 ± 31.72 |
| class_index | metadata | categorical | *Not specified.* | n=654, missing=654, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=654, missing=654, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=654, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top 1D (×654) |
| axis_note | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×654) |
| official_data_url | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×654) |
| official_package_url | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top https://ecosis.org/package/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×654) |
| license | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top Creative Commons Attribution (×654) |
| license_url | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×654) |
| rights_status | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top explicit_open (×654) |
| usage_scope | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top public_reuse_possible (×654) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top True (×654) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top ecosis_hyperspectral_leaf_reflectance_biochemistry_and_physiol_reflectance_nirs (×654) |
| notes | metadata | categorical | *Not specified.* | n=654, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×654) |

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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M Champs d’index examinés : Rep. Le nombre de niveaux d’un facteur Rep n’est pas utilisé comme nombre de spectres par échantillon.
- **Curated views:** M: 12 fields, Y: 1 fields, passport: 34 fields, measurements: 21 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `2615bdd37474a7dca288551d4646dbea7981a49baf953756ffcd9fb94ea0eea1`
- **Processing hash:** `92d313405d0daaf6475883b0ca61b41d8eb9626a02f96ffcf62dd7cc9426f5e5` | **metadata hash:** `9f4c5afcec5488cda13fc72111491fa03f6e6ce889594b3cf85941cd9fd6cfb5`
