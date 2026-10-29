# Datasheet — EcoSIS NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016 (Narea_g_m2)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016 (Narea_g_m2). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016

## Composition

- **Alignment:** sample level; 186 sample(s), 187 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.005).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ngee-tropics_panama_2016_svc_feb_mar_apr_leaf_spectra | SVC_HR-1024i | NIR | 350–2500 nm | 187 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Narea_g_m2 | target | numeric | *Not specified.* | n=186, missing=0, range -9999–3.35, mean -51.84 ± 733.3 |
| SpectralRep | metadata | numeric | *Not specified.* | n=186, missing=0, range 1–1, mean 1 ± 0 |
| Sample_ID | metadata | categorical | *Not specified.* | n=186, missing=0, classes=186, top BNL10401 (×1) |
| Site | metadata | categorical | *Not specified.* | n=186, missing=0, classes=2, top PA-SLZ (×107) |
| Sample_Date | metadata | categorical | *Not specified.* | n=186, missing=0, classes=10, top 20160214 (×24) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=186, missing=0, classes=186, top BNL10401 (×1) |
| BNL_Barcode | metadata | categorical | *Not specified.* | n=186, missing=0, classes=186, top BNL10401 (×1) |
| Instrument | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top SVC_HR-1024i (×186) |
| Foreoptic | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Fiber_1_LC_RP (×186) |
| Collection_Units | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Radiance (×186) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Percent_Reflectance_0_100 (×186) |
| Spectra_Type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Leaf (×186) |
| Reflectance_Type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Absolute (×186) |
| White_Reference_Standard | metadata | categorical | *Not specified.* | n=186, missing=0, classes=2, top 99AA10-0614-0827 SRS-99-020 (×118) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top 1nm (×186) |
| Wavelength | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Nanometer (×186) |
| Interpolation_Method | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Linear (×186) |
| Overlap_Handling | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Removed (×186) |
| Overlap_Removal | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Post_processing (×186) |
| Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Radiance (×186) |
| Date | metadata | categorical | *Not specified.* | n=186, missing=0, classes=10, top 2/14/16 (×24) |
| Location | metadata | categorical | *Not specified.* | n=186, missing=0, classes=2, top PA-SLZ (×108) |
| Species_Code | metadata | categorical | *Not specified.* | n=186, missing=0, classes=26, top MICOBO (×16) |
| Latin_genus | metadata | categorical | *Not specified.* | n=186, missing=0, classes=25, top Miconia (×16) |
| Latin_species | metadata | categorical | *Not specified.* | n=186, missing=0, classes=25, top borealis (×16) |
| Genus_species | metadata | categorical | *Not specified.* | n=186, missing=0, classes=26, top Miconia borealis (×16) |
| Gasex_typeOrSequence | metadata | categorical | *Not specified.* | n=186, missing=0, classes=2, top ACi (×149) |
| TleafDegC_canopy | metadata | numeric | *Not specified.* | n=186, missing=149, range 23.8–29.7, mean 26.14 ± 1.181 |
| TleafDegCpreSpec | metadata | numeric | *Not specified.* | n=186, missing=5, range 26.4–32.8, mean 29.58 ± 1.653 |
| TleafDegCpostSpec | metadata | numeric | *Not specified.* | n=186, missing=4, range 27.2–36.3, mean 30.88 ± 1.881 |
| Photo_num | metadata | categorical | *Not specified.* | n=186, missing=7, classes=176, top ?Shawn's phone (×3) |
| Canopy_position | metadata | categorical | *Not specified.* | n=186, missing=0, classes=2, top sunlit (×159) |
| General_Comments | metadata | categorical | *Not specified.* | n=186, missing=174, classes=6, top leaf temperatures before and after spectra reading may be missing or inaccurate (×7) |
| Cmass_pc | metadata | numeric | *Not specified.* | n=186, missing=0, range 37.64–54.06, mean 49.15 ± 3.593 |
| Nmass_pc | metadata | numeric | *Not specified.* | n=186, missing=0, range 1.06–5.66, mean 2.204 ± 0.9319 |
| CNratio | metadata | numeric | *Not specified.* | n=186, missing=0, range 7.94–49.39, mean 25.3 ± 8.212 |
| Carea_g_m2 | metadata | numeric | *Not specified.* | n=186, missing=0, range -9999–94.3, mean -6.286 ± 736.9 |
| Duplicate_flag | metadata | numeric | *Not specified.* | n=186, missing=1, range 1–1, mean 1 ± 0 |
| Chem_type | metadata | categorical | *Not specified.* | n=186, missing=1, classes=1, top CHN (×185) |
| H20_pc | metadata | numeric | *Not specified.* | n=186, missing=1, range 35.62–82.44, mean 57.71 ± 7.88 |
| LMA_gDW_m2 | metadata | numeric | *Not specified.* | n=186, missing=1, range 22.01–185.2, mean 96.41 ± 33.64 |
| SLA_cm2_gDW | metadata | numeric | *Not specified.* | n=186, missing=1, range 53.98–454.4, mean 124.2 ± 67.83 |
| LWP_coll_time | metadata | categorical | *Not specified.* | n=186, missing=149, classes=34, top 7:50 (×3) |
| LWP_time | metadata | numeric | *Not specified.* | n=186, missing=170, range -9999–-9999, mean -9999 ± 0 |
| LWP_bar | metadata | numeric | *Not specified.* | n=186, missing=149, range 6–28.5, mean 17.11 ± 5.307 |
| LWP_comment | metadata | categorical | *Not specified.* | n=186, missing=184, classes=2, top ? from phloem (×1) |
| dataset | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top EcoSIS (×186) |
| dataset_slug | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 (×186) |
| task_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top regression (×186) |
| trait_header | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Narea_g_m2 (×186) |
| target_original_name | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Narea_g_m2 (×186) |
| measurement_hint | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top ngee-tropics_panama_2016_svc_feb_mar_apr_leaf_spectra (×186) |
| raw_label | metadata | categorical | *Not specified.* | n=186, missing=0, classes=122, top 2.07 (×4) |
| reference_value | metadata | numeric | *Not specified.* | n=186, missing=0, range -9999–3.35, mean -51.84 ± 733.3 |
| class_index | metadata | categorical | *Not specified.* | n=186, missing=186, classes=0, — |
| class_label | metadata | categorical | *Not specified.* | n=186, missing=186, classes=0, — |
| n_points_original | metadata | numeric | *Not specified.* | n=186, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top 1D (×186) |
| axis_note | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×186) |
| official_data_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 (×186) |
| official_package_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top https://ecosis.org/package/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 (×186) |
| license | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Open Data Commons Attribution License (×186) |
| license_url | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top http://www.opendefinition.org/licenses/odc-by (×186) |
| rights_status | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top explicit_open (×186) |
| usage_scope | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top public_reuse_possible (×186) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top True (×186) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top ecosis_ngee_tropics_leaf_spectral_reflectance_measured_in_pana_reflectance_nirs (×186) |
| notes | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×186) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
- **Curated views:** M: 13 fields, Y: 1 fields, measurements: 14 fields, passport: 46 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Open Data Commons Attribution License.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `8fe999b16cbf2add827c8371b069688f288e6f4871da0acea577855c24a2ee8a`
- **Processing hash:** `cef685657d065b7243acb0132fd9713909be8d95df225bd132a0802657d4c399` | **metadata hash:** `7ccbbd17fdd9a8a724c767f64c6fe7b4e1f95c700df08e433abc455c79ba7151`
