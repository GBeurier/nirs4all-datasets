# Datasheet — EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling (W18_Nitrogen_Deficiency)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** leaf
- **Description:** EcoSIS Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling (W18_Nitrogen_Deficiency). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, leaf
- **Contributor:** Purdue Leaf Spectral and Functional Trait Data used in PLSR modeling

## Composition

- **Alignment:** sample level; 987 sample(s), 987 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | 2018+2019_stress_six_leaf_traits_spec | *Not specified.* | NIR | 350–2500 nm | 987 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| W18_Nitrogen_Deficiency | target | numeric | *Not specified.* | n=987, missing=0, range 0–2, mean 1.713 ± 0.6207 |
| SpectralRep | metadata | numeric | *Not specified.* | n=987, missing=0, range 1–1, mean 1 ± 0 |
| Unique_ID | metadata | categorical | *Not specified.* | n=987, missing=0, classes=987, top E18_20180704_Black_walnut_p1_Control_Plantation_1 (×1) |
| Experiment_ID | metadata | categorical | *Not specified.* | n=987, missing=0, classes=4, top 2019_EEL (×326) |
| Data_Collection_Date | metadata | categorical | *Not specified.* | n=987, missing=0, classes=15, top 20180727 (×98) |
| Site_Name | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top EEL (×498) |
| Latitude | metadata | numeric | *Not specified.* | n=987, missing=0, range 40.42–40.43, mean 40.43 ± 0.004691 |
| Longitude | metadata | numeric | *Not specified.* | n=987, missing=0, range -87.04–-86.91, mean -86.98 ± 0.06194 |
| Common_name | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top Black_walnut (×839) |
| Genus | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top Juglans (×839) |
| Species | metadata | categorical | *Not specified.* | n=987, missing=0, classes=2, top nigra (×839) |
| Plant_ID | metadata | categorical | *Not specified.* | n=987, missing=0, classes=146, top p3 (×50) |
| E18_Fungal_Infection | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×815) |
| E18_SoilTypes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=4, top noTreatment (×815) |
| metadata_W18_Nitrogen_Deficiency | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| W18_Drought | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| E19_Fungal_Infection | metadata | categorical | *Not specified.* | n=987, missing=0, classes=5, top noTreatment (×661) |
| E19_Drought | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×661) |
| W19_Nitrogen_Deficiency | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×692) |
| W19_Salt_Deposition | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×692) |
| Foliar_Trait_Code | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top 1 (×449) |
| CO2_assimilation_rate | metadata | categorical | *Not specified.* | n=987, missing=0, classes=450, top noData (×538) |
| Specific_leaf_area | metadata | categorical | *Not specified.* | n=987, missing=0, classes=340, top noData (×647) |
| Leaf_water_content | metadata | categorical | *Not specified.* | n=987, missing=0, classes=341, top noData (×647) |
| Nitrogen | metadata | categorical | *Not specified.* | n=987, missing=0, classes=130, top noData (×791) |
| Sugars | metadata | categorical | *Not specified.* | n=987, missing=0, classes=197, top noData (×791) |
| Gallic_acid | metadata | categorical | *Not specified.* | n=987, missing=0, classes=198, top noData (×790) |
| dataset | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top EcoSIS (×987) |
| dataset_slug | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling (×987) |
| task_type | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top classification (×987) |
| trait_header | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top W18_Nitrogen_Deficiency (×987) |
| target_original_name | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top W18_Nitrogen_Deficiency (×987) |
| measurement_hint | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 2018+2019_stress_six_leaf_traits_spec (×987) |
| raw_label | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| reference_value | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| class_index | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top 2 (×793) |
| class_label | metadata | categorical | *Not specified.* | n=987, missing=0, classes=3, top noTreatment (×793) |
| n_points_original | metadata | numeric | *Not specified.* | n=987, missing=0, range 2151–2151, mean 2151 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top 1D (×987) |
| axis_note | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×987) |
| official_data_url | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top https://data.ecosis.org/dataset/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling (×987) |
| official_package_url | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top https://ecosis.org/package/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling (×987) |
| license | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Other (Open) (×987) |
| license_url | metadata | categorical | *Not specified.* | n=987, missing=987, classes=0, — |
| rights_status | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top explicit_open (×987) |
| usage_scope | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top public_reuse_possible (×987) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top True (×987) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top ecosis_purdue_leaf_spectral_functional_traits_plsr_v2_reflectance_nirs (×987) |
| notes | metadata | categorical | *Not specified.* | n=987, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×987) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/purdue-leaf-spectral-and-functional-trait-data-used-in-plsr-modeling`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 14 fields, Y: 1 fields, measurements: 10 fields, passport: 30 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `06ad372cc7b53c9b1406ea095bdd030e099f62db0ce0f1909c9e0dfc8e0b6966`
- **Processing hash:** `8c3d0f36d36f50560cea6965e09077c9923d88956f52f01f6efe085c1593d87f` | **metadata hash:** `cc14da0cbaf7e8aeeb00f8ea3ab029e84ab08d628e17e74527699e54b773088d`
