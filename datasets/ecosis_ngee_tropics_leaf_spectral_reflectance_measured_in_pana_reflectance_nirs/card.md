# Datasheet — NGEE Tropics Panama 2016 — leaf reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016 (reflectance). Origin database composed from 2 standardized v2.0 leaves: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016

## Composition

- **Alignment:** sample level; 708 sample(s), 709 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.001).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ngee-tropics_panama_2016_svc_feb_mar_apr_leaf_spectra.csv | Spectra Vista Corporation, Spectral Evolution HR-1024i | NIR | 350–2500 nm | 709 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| H20_pc | target | numeric | *Not specified.* | n=708, missing=124, range 29.3–82.44, mean 55.77 ± 7.224 |
| LMA_gDW_m2 | target | numeric | *Not specified.* | n=708, missing=124, range 22.01–204.9, mean 106.7 ± 30.86 |
| SLA_cm2_gDW | target | numeric | *Not specified.* | n=708, missing=124, range 48.8–454.4, mean 104.8 ± 45.67 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top 78a97d90-36b1-4e4b-9c93-7e2db590f154 (×708) |
| site | metadata | categorical | *Not specified.* | n=708, missing=0, classes=2, top PA-SLZ (×487) |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top source-provided coordinates when available (×708) |
| year | metadata | numeric | *Not specified.* | n=708, missing=0, range 2019–2019, mean 2019 ± 0 |
| plant_part | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Leaf (×708) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top leaf (×708) |
| instrument | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Spectra Vista Corporation, Spectral Evolution HR-1024i (×708) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Contact (×708) |
| signal_type | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top reflectance (×708) |
| axis_unit | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top nm (×708) |
| axis_min | metadata | numeric | *Not specified.* | n=708, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=708, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=708, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top 10.1111/nph.16029 \| 10.15486/ngt/1411867 \| 10.15486/ngt/1411971 \| 10.15486/ngt/1411972 \| 10.15486/ngt/1411973 \| 10.15486/ngt/1478523 \| 10.15486/ngt/1478647 \| 10.15486/ngt/1507766 (×708) |
| citation | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Shawn Serbin Kim Ely Alistair Rogers Turin Dickman Matteo Detto Jin Wu Brett Wolfe Nate McDowell Charlotte Grossiord Sean Michaletz Adam Collins. 2019. NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). http://dx.doi.org/10.15486/ngt/1478523 (×708) |
| license | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Open Data Commons Attribution License (×708) |
| rights_status | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top explicit_open (×708) |
| usage_scope | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top public_reuse_possible (×708) |
| notes | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top EcoSIS package ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016, no interpolation applied by project. (×708) |
| Narea_g_m2 | target | numeric | *Not specified.* | n=708, missing=522, range -9999–3.35, mean -51.84 ± 733.3 |
| source_Sample_ID | metadata | categorical | *Not specified.* | n=708, missing=0, classes=708, top BNL10401 (×1) |
| source_Site | metadata | categorical | *Not specified.* | n=708, missing=0, classes=2, top PA-SLZ (×487) |
| source_Sample_Date | metadata | categorical | *Not specified.* | n=708, missing=0, classes=10, top 20160421 (×153) |
| source_Spectra_Name | metadata | categorical | *Not specified.* | n=708, missing=0, classes=708, top BNL10401 (×1) |
| source_BNL_Barcode | metadata | categorical | *Not specified.* | n=708, missing=0, classes=708, top BNL10401 (×1) |
| source_Instrument | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top SVC_HR-1024i (×708) |
| source_Foreoptic | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Fiber_1_LC_RP (×708) |
| source_Collection_Units | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Radiance (×708) |
| source_Spectra_Units | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Percent_Reflectance_0_100 (×708) |
| source_Spectra_Type | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Leaf (×708) |
| source_Reflectance_Type | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Absolute (×708) |
| source_White_Reference_Standard | metadata | categorical | *Not specified.* | n=708, missing=0, classes=2, top 99AA10-0614-0826 SRS-99-020 (×437) |
| source_Spectral_Resolution | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top 1nm (×708) |
| source_Wavelength | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Nanometer (×708) |
| source_Interpolation_Method | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Linear (×708) |
| source_Overlap_Handling | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Removed (×708) |
| source_Overlap_Removal | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Post_processing (×708) |
| source_Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Radiance (×708) |
| source_Duplicate_flag | metadata | numeric | *Not specified.* | n=708, missing=124, range 1–1, mean 1 ± 0 |
| source_Chem_type | metadata | categorical | *Not specified.* | n=708, missing=124, classes=1, top CHN (×584) |
| SpectralRep | metadata | numeric | *Not specified.* | n=708, missing=522, range 1–1, mean 1 ± 0 |
| Sample_ID | metadata | categorical | *Not specified.* | n=708, missing=522, classes=186, top BNL10401 (×1) |
| Site | metadata | categorical | *Not specified.* | n=708, missing=522, classes=2, top PA-SLZ (×107) |
| Sample_Date | metadata | categorical | *Not specified.* | n=708, missing=522, classes=10, top 20160214 (×24) |
| Spectra_Name | metadata | categorical | *Not specified.* | n=708, missing=522, classes=186, top BNL10401 (×1) |
| BNL_Barcode | metadata | categorical | *Not specified.* | n=708, missing=522, classes=186, top BNL10401 (×1) |
| Instrument | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top SVC_HR-1024i (×186) |
| Foreoptic | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Fiber_1_LC_RP (×186) |
| Collection_Units | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Radiance (×186) |
| Spectra_Units | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Percent_Reflectance_0_100 (×186) |
| Spectra_Type | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Leaf (×186) |
| Reflectance_Type | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Absolute (×186) |
| White_Reference_Standard | metadata | categorical | *Not specified.* | n=708, missing=522, classes=2, top 99AA10-0614-0827 SRS-99-020 (×118) |
| Spectral_Resolution | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top 1nm (×186) |
| Wavelength | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Nanometer (×186) |
| Interpolation_Method | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Linear (×186) |
| Overlap_Handling | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Removed (×186) |
| Overlap_Removal | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Post_processing (×186) |
| Overlap_Matching_Type | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top Radiance (×186) |
| Date | metadata | categorical | *Not specified.* | n=708, missing=522, classes=10, top 2/14/16 (×24) |
| Location | metadata | categorical | *Not specified.* | n=708, missing=522, classes=2, top PA-SLZ (×108) |
| Species_Code | metadata | categorical | *Not specified.* | n=708, missing=522, classes=26, top MICOBO (×16) |
| Latin_genus | metadata | categorical | *Not specified.* | n=708, missing=522, classes=25, top Miconia (×16) |
| Latin_species | metadata | categorical | *Not specified.* | n=708, missing=522, classes=25, top borealis (×16) |
| Genus_species | metadata | categorical | *Not specified.* | n=708, missing=522, classes=26, top Miconia borealis (×16) |
| Gasex_typeOrSequence | metadata | categorical | *Not specified.* | n=708, missing=522, classes=2, top ACi (×149) |
| TleafDegC_canopy | metadata | numeric | *Not specified.* | n=708, missing=671, range 23.8–29.7, mean 26.14 ± 1.181 |
| TleafDegCpreSpec | metadata | numeric | *Not specified.* | n=708, missing=527, range 26.4–32.8, mean 29.58 ± 1.653 |
| TleafDegCpostSpec | metadata | numeric | *Not specified.* | n=708, missing=526, range 27.2–36.3, mean 30.88 ± 1.881 |
| Photo_num | metadata | categorical | *Not specified.* | n=708, missing=529, classes=176, top ?Shawn's phone (×3) |
| Canopy_position | metadata | categorical | *Not specified.* | n=708, missing=522, classes=2, top sunlit (×159) |
| General_Comments | metadata | categorical | *Not specified.* | n=708, missing=696, classes=6, top leaf temperatures before and after spectra reading may be missing or inaccurate (×7) |
| Cmass_pc | metadata | numeric | *Not specified.* | n=708, missing=522, range 37.64–54.06, mean 49.15 ± 3.593 |
| Nmass_pc | metadata | numeric | *Not specified.* | n=708, missing=522, range 1.06–5.66, mean 2.204 ± 0.9319 |
| CNratio | metadata | numeric | *Not specified.* | n=708, missing=522, range 7.94–49.39, mean 25.3 ± 8.212 |
| Carea_g_m2 | metadata | numeric | *Not specified.* | n=708, missing=522, range -9999–94.3, mean -6.286 ± 736.9 |
| Duplicate_flag | metadata | numeric | *Not specified.* | n=708, missing=523, range 1–1, mean 1 ± 0 |
| Chem_type | metadata | categorical | *Not specified.* | n=708, missing=523, classes=1, top CHN (×185) |
| LWP_coll_time | metadata | categorical | *Not specified.* | n=708, missing=671, classes=34, top 7:50 (×3) |
| LWP_time | metadata | numeric | *Not specified.* | n=708, missing=692, range -9999–-9999, mean -9999 ± 0 |
| LWP_bar | metadata | numeric | *Not specified.* | n=708, missing=671, range 6–28.5, mean 17.11 ± 5.307 |
| LWP_comment | metadata | categorical | *Not specified.* | n=708, missing=706, classes=2, top ? from phloem (×1) |
| dataset | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top EcoSIS (×186) |
| dimensions | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top 1D (×186) |
| axis_note | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×186) |
| official_data_url | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 (×186) |
| official_package_url | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top https://ecosis.org/package/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 (×186) |
| license_url | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top http://www.opendefinition.org/licenses/odc-by (×186) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top True (×186) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=708, missing=522, classes=1, top ecosis_ngee_tropics_leaf_spectral_reflectance_measured_in_pana_reflectance_nirs (×186) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 13 fields, Y: 4 fields, measurements: 10 fields, passport: 51 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Leaf spectra, Feb2016-April2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1478523](https://doi.org/10.15486/ngt/1478523)
- Leaf water potential, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1507766](https://doi.org/10.15486/ngt/1507766)
- 2016 Panama ENSO Non-Structural Carbohydrates (NSC), Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI — [10.15486/ngt/1478647](https://doi.org/10.15486/ngt/1478647)
- CO2 response (ACi) gas exchange, calculated Vcmax & Jmax parameters, Feb2016-May2016, PA-SLZ, PA-PNM: Panama — [10.15486/ngt/1411867](https://doi.org/10.15486/ngt/1411867)
- Leaf mass area, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1411973](https://doi.org/10.15486/ngt/1411973)
- Diurnal leaf gas exchange survey, Feb2016-May2016, PA-SLZ, PA-PNM: Panama — [10.15486/ngt/1411972](https://doi.org/10.15486/ngt/1411972)
- Leaf sample detail, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1411971](https://doi.org/10.15486/ngt/1411971)
- Leaf reflectance spectroscopy captures variation in carboxylation capacity across species, canopy environment and leaf age in lowland moist tropical forests — [10.1111/nph.16029](https://doi.org/10.1111/nph.16029)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `1e1f2416a0c7dd6821119c1b835d79c0479a12294ed3a9751024e45735f910d5`
- **Processing hash:** `2019e0ea55ac747f40a5a26096571f95d2d788c970a1af85769da2543e4ad716` | **metadata hash:** `06810957f19a702ce3d4646f39e322676222abebc6549e5e060f093341872893`
