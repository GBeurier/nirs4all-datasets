# Datasheet — Droughted and watered crops — leaf reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS hyperspectral leaf reflectance, biochemistry and physiology of droughted and watered crops (leaf spectra). Origin database composed from 3 standardized v2.0 leaves: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Hyperspectral leaf reflectance, biochemistry, and physiology of droughted and watered crops

## Composition

- **Alignment:** sample level; 665 sample(s), 665 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra | SE_PSR_Plus | NIR | 350–2500 nm | 665 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=665, missing=0, range 14.93–92.29, mean 45.44 ± 15.96 |
| Protein | target | numeric | *Not specified.* | n=665, missing=7, range 2.78–33.25, mean 7.418 ± 2.271 |
| Starch | target | numeric | *Not specified.* | n=665, missing=11, range 0.00614–200.9, mean 27.2 ± 31.72 |
| SpectralRep | metadata | numeric | *Not specified.* | n=665, missing=0, range 1–1, mean 1 ± 0 |
| uniquefield | metadata | categorical | *Not specified.* | n=665, missing=0, classes=665, top 2018-03-19_17 (×1) |
| Glucose | metadata | numeric | *Not specified.* | n=665, missing=12, range 0.01264–24.23, mean 5.806 ± 4.961 |
| Fructose | metadata | numeric | *Not specified.* | n=665, missing=8, range 0.2065–13.56, mean 2.355 ± 1.832 |
| Sucrose | metadata | numeric | *Not specified.* | n=665, missing=12, range 0.8231–44.5, mean 9.424 ± 8.004 |
| LDP_Fructan | metadata | numeric | *Not specified.* | n=665, missing=610, range 0.01275–2.006, mean 0.4505 ± 0.4051 |
| HDP_Fructan | metadata | categorical | *Not specified.* | n=665, missing=657, classes=8, top 1.10284464 (×1) |
| Amino_Acids | metadata | numeric | *Not specified.* | n=665, missing=17, range 0.1126–36.16, mean 4.102 ± 5.129 |
| ABA | metadata | numeric | *Not specified.* | n=665, missing=61, range 0.2882–6.733e+04, mean 1017 ± 3655 |
| Proline | metadata | numeric | *Not specified.* | n=665, missing=7, range 0.1427–44.85, mean 2.222 ± 3.537 |
| RWC | metadata | numeric | *Not specified.* | n=665, missing=1, range 41.52–94.06, mean 79.41 ± 8.555 |
| Elemental_C | metadata | numeric | *Not specified.* | n=665, missing=170, range 0.4387–47.2, mean 18.46 ± 8.761 |
| Elemental_N | metadata | numeric | *Not specified.* | n=665, missing=170, range 0.6373–6.147, mean 1.88 ± 1.037 |
| Asat | metadata | numeric | *Not specified.* | n=665, missing=525, range -0.46–43.28, mean 18.91 ± 10.11 |
| gs | metadata | numeric | *Not specified.* | n=665, missing=525, range 0.01–0.77, mean 0.2199 ± 0.1623 |
| Ci | metadata | numeric | *Not specified.* | n=665, missing=525, range -157.9–515.3, mean 199.9 ± 119.6 |
| Tr | metadata | numeric | *Not specified.* | n=665, missing=525, range 0.21–11.06, mean 4.386 ± 2.486 |
| VPDleaf | metadata | numeric | *Not specified.* | n=665, missing=525, range 1.04–4.21, mean 2.375 ± 0.7232 |
| Tleaf | metadata | numeric | *Not specified.* | n=665, missing=525, range 23.03–31.47, mean 26.98 ± 1.949 |
| CO2s | metadata | numeric | *Not specified.* | n=665, missing=525, range 378.7–400.3, mean 390.5 ± 4.691 |
| H2Os | metadata | numeric | *Not specified.* | n=665, missing=525, range 4–18.31, mean 12.02 ± 3.508 |
| RHs | metadata | numeric | *Not specified.* | n=665, missing=525, range 10.17–58.53, mean 36.03 ± 12.75 |
| flow | metadata | numeric | *Not specified.* | n=665, missing=525, range 299.5–500.6, mean 431.4 ± 95.35 |
| Qin | metadata | numeric | *Not specified.* | n=665, missing=525, range 1498–1802, mean 1697 ± 142.7 |
| Location | metadata | categorical | *Not specified.* | n=665, missing=0, classes=2, top glasshouse (×505) |
| Paired_Spectra | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top leaf (×665) |
| Plant | metadata | numeric | *Not specified.* | n=665, missing=160, range 17–168, mean 96.02 ± 45.85 |
| Plot | metadata | categorical | *Not specified.* | n=665, missing=505, classes=12, top 2.0 (×15) |
| Rep | metadata | categorical | *Not specified.* | n=665, missing=505, classes=3, top 1.0 (×54) |
| Species | metadata | categorical | *Not specified.* | n=665, missing=0, classes=6, top CUPE (×272) |
| Treatment | metadata | categorical | *Not specified.* | n=665, missing=0, classes=2, top watered (×340) |
| Plant_Age | metadata | numeric | *Not specified.* | n=665, missing=0, range 35–127, mean 82.85 ± 30.89 |
| Days_Into_Treatment | metadata | numeric | *Not specified.* | n=665, missing=0, range 3–37, mean 19.13 ± 8.584 |
| Measurement_Date | metadata | categorical | *Not specified.* | n=665, missing=0, classes=31, top 7/19/19 (×36) |
| Instrument | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top SE_PSR_Plus (×665) |
| Pre_or_Post_Treatment | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top post (×665) |
| dataset | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top EcoSIS (×665) |
| n_points_original | metadata | numeric | *Not specified.* | n=665, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top 1D (×665) |
| axis_note | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×665) |
| official_data_url | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×665) |
| official_package_url | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top https://ecosis.org/package/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops (×665) |
| license | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top Creative Commons Attribution (×665) |
| license_url | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×665) |
| rights_status | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top explicit_open (×665) |
| usage_scope | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top public_reuse_possible (×665) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top True (×665) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top ecosis_hyperspectral_leaf_reflectance_biochemistry_and_physiol_reflectance_nirs (×665) |
| notes | metadata | categorical | *Not specified.* | n=665, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×665) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/hyperspectral-leaf-reflectance--biochemistry--and-physiology-of-droughted-and-watered-crops`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M. Index fields examined: Rep. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 12 fields, Y: 3 fields, measurements: 18 fields, passport: 25 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `e27fe56e499c6c86f5d0129969e3369dae7b336664f14db157f9d6bdb329a57a`
- **Processing hash:** `db458ffe8684931af07b5817327498e9c4d7bd55967a41beffaa0f3bc2a05c1b` | **metadata hash:** `3b805a8cea61812ce1126abdecc95b20b965c4e6b9f470b1f5e488952347371e`
