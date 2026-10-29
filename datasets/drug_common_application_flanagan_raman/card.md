# Datasheet — Flanagan Raman common application classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** drug
- **Description:** Flanagan Raman common application classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, drug
- **Contributor:** Open-source Raman spectra of chemical compounds for API development

## Composition

- **Alignment:** sample level; 32 sample(s), 3510 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 100–145 (mean 109.7).
- **Documented technical repetitions:** 100–145.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Flanagan Raman common application classification | Raman instrument as documented by source article | Raman | 150–3425 cm-1 | 3510 | 3276 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| common_application | target | categorical | *Not specified.* | n=3510, missing=0, classes=2, top Intermediate (×2187) |
| SpectralRep | metadata | numeric | *Not specified.* | n=3510, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Flanagan Raman Dataset (×3510) |
| dataset_title | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Open-source Raman spectra of chemical compounds for API development (×3510) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Raman (×3510) |
| product | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top chemical compound / active pharmaceutical ingredient context (×3510) |
| trait_header | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top common_application (×3510) |
| trait_header_original | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Common Application (×3510) |
| task_type | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top classification (×3510) |
| raw_label | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=2, top Intermediate (×2187) |
| reference_value | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=2, top Intermediate (×2187) |
| class_index | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=2, top 0 (×2187) |
| class_label | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=2, top Intermediate (×2187) |
| n_points_original | metadata | numeric | *Not specified.* | n=3510, missing=0, range 3276–3276, mean 3276 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top 1D (×3510) |
| axis_note | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top source_common_axis_150_to_3426_cm-1_step_1 (×3510) |
| label | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=32, top Cyclohexane (×145) |
| compound_key | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=32, top cyclohexane (×145) |
| Compound | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=32, top Cyclohexane (×145) |
| Organic | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Y (×3510) |
| Solvent_Reagent | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=3, top Solvent (×2429) |
| Formula | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=30, top C4H11N (×211) |
| Approx_Raman_bands_deviation_of_2_cm_1_per_external_sources | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=31, top 186, 679, 1061, 1204, 1398, 1660, 2782, 2963 (×210) |
| Supplier_Product | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=25, top Scharlau - HPLC grade (×316) |
| Assay_pct | metadata | numeric | *Not specified.* | n=3510, missing=0, range 95–99.9, mean 99.24 ± 0.9525 |
| Exposure_secs | metadata | numeric | *Not specified.* | n=3510, missing=0, range 2–45, mean 11.74 ± 10.37 |
| Pixel_Fill_pct | metadata | numeric | *Not specified.* | n=3510, missing=0, range 40–73, mean 59.14 ± 8.471 |
| Samples | metadata | numeric | *Not specified.* | n=3510, missing=0, range 100–145, mean 110.5 ± 9.943 |
| compound_rep_index | metadata | numeric | *Not specified.* | n=3510, missing=0, range 1–145, mean 55.73 ± 32.41 |
| axis_unit | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top cm^-1 (×3510) |
| axis_min | metadata | numeric | *Not specified.* | n=3510, missing=0, range 150–150, mean 150 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3510, missing=0, range 3425–3425, mean 3425 ± 0 |
| license | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top CC BY 4.0 (×3510) |
| license_url | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×3510) |
| rights_status | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top explicit_open (×3510) |
| usage_scope | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top public_use_with_attribution (×3510) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top True (×3510) |
| publication_url | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top https://www.nature.com/articles/s41597-025-04848-6 (×3510) |
| notes | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Task-specific view of Flanagan Raman source common-axis data, no interpolation or resampling by standardization. (×3510) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.27931131`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://springernature.figshare.com/articles/dataset/Open-source_Raman_spectra_of_chemical_compounds_for_active_pharmaceutical_ingredient_development/27931131`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.nature.com/articles/s41597-025-04848-6`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: 32 produits, chacun échantillonné en flacon ; 100–145 acquisitions manuelles par produit. Le sample_id unique est créé en ajoutant un compteur de scan au composé. Le nombre de préparations indépendantes par produit n’est pas établi.
- **Curated views:** M: 6 fields, Y: 1 fields, passport: 33 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *Not specified.* — [10.1038/s41597-025-04848-6](https://doi.org/10.1038/s41597-025-04848-6)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Public redistribution of transformed X/Y/M is allowed under CC BY 4.0 with attribution, license link, and indication of modifications.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `c8bcb5329b3d558e4060db575711d207255f8b814936a790c972f66a8e86ecc2`
- **Processing hash:** `678931400d35128bbb7b390c4e438e10971194e78edf169ab9334b83b918c8cd` | **metadata hash:** `154c61afea4ede32d4ce0bde45351c2de08fcdc3e4d7c939a990dfac3f103aa5`
