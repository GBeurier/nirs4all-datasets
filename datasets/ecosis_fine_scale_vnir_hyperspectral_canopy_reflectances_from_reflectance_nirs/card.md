# Datasheet — Virginia successional forests — canopy VNIR reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 2850 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra and Metadata.csv | Headwall Photonics Nano-Hyperspec | NIR | 449.7–949.7 nm | 2850 | 226 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Row_No | target | categorical | *Not specified.* | n=2850, missing=0, classes=2850, top 1 (×1) |
| Individual | target | numeric | *Not specified.* | n=2850, missing=0, range 1–65, mean 26.22 ± 17.93 |
| DOY | target | numeric | *Not specified.* | n=2850, missing=0, range 134–249, mean 189.9 ± 45.69 |
| Reading | target | numeric | *Not specified.* | n=2850, missing=0, range 1–15, mean 8 ± 4.321 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 54647cde-1d77-44b4-83fc-af21f2d0304f (×2850) |
| site | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm (×2850) |
| location | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm, Virginia (×2850) |
| country | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 39°03'52.2" N (×2850) |
| longitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 78°03'28.9" W (×2850) |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top source-provided coordinates when available (×2850) |
| year | metadata | numeric | *Not specified.* | n=2850, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top umbellata, davurica, maackii, altissima, triacanthos, pomifera, nigra, virginiana (×2850) |
| genus | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Elaeagnus, Rhamnus, Lonicera, Ailanthus, Gleditsia, Maclura, Juglans, Juniperus (×2850) |
| family | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Canopy (×2850) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top canopy (×2850) |
| instrument | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Headwall Photonics Nano-Hyperspec (×2850) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Pixel (×2850) |
| signal_type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top reflectance (×2850) |
| axis_unit | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top nm (×2850) |
| axis_min | metadata | numeric | *Not specified.* | n=2850, missing=0, range 449.7–449.7, mean 449.7 ± 1.706e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=2850, missing=0, range 949.7–949.7, mean 949.7 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2850, missing=0, range 226–226, mean 226 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman Howard Epstein Xi Yang. 2020. Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×2850) |
| license | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Creative Commons Non-Commercial (Any) (×2850) |
| rights_status | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top explicit_restricted (×2850) |
| usage_scope | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top private_use_only (×2850) |
| notes | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top EcoSIS package fine-scale-vnir-hyperspectral-canopy-reflectances-from-virginia-successional-forests, no interpolation applied by project. (×2850) |
| source_Primary | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=9, top Rh_da (×645) |
| source_Field | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=3, top EM (×1140) |
| source_Acquisition_Method | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Pixel (×2850) |
| source_Sample_Platform | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top UAV (×2850) |
| source_Measurement_Venue | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top outdoor (×2850) |
| source_Target_Type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Canopy (×2850) |
| source_Measurement_Quantity | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Reflectance (×2850) |
| source_Measurement_Units | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top % (×2850) |
| source_Wavelength_Units | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top nm (×2850) |
| source_Target_Status | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Live (×2850) |
| source_Light_Source | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Sun (×2850) |
| source_Foreoptic_Type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Foreoptic (×2850) |
| source_Foreoptic_Field_of_View | metadata | numeric | *Not specified.* | n=2850, missing=0, range 11.5–11.5, mean 11.5 ± 0 |
| source_Processing_Averaged | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Processing_Interpolated | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Processing_Resampled | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Instrument_Manufacturer | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Headwall Photonics (×2850) |
| source_Instrument_Model | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Nano-hyperspec (×2850) |
| source_Theme | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Ecology, Phenology (×2850) |
| source_Ecosystem_Type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Forest (×2850) |
| source_Latitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 39°03'52.2" N (×2850) |
| source_Longitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 78°03'28.9" W (×2850) |
| source_geojson | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| source_Location_Name | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm (×2850) |
| source_Sample_Collection_Date | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 2020 (×2850) |
| source_Common_Name | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top autumn olive, dahurian buckthorn, bush honeysuckle, tree of heaven, honey locust, osage orange, black walnut, eastern red cedar (×2850) |
| source_Latin_Genus | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Elaeagnus, Rhamnus, Lonicera, Ailanthus, Gleditsia, Maclura, Juglans, Juniperus (×2850) |
| source_Latin_Species | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top umbellata, davurica, maackii, altissima, triacanthos, pomifera, nigra, virginiana (×2850) |
| source_USDA_Symbol | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| source_Vegetation_Type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top tree, shrub, evergreen, deciduous (×2850) |
| source_Author | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman (×2850) |
| source_Author_Email | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top ksh5s@virginia.edu (×2850) |
| source_Maintainer | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman (×2850) |
| source_Maintainer_Email | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top ksh5s@virginia.edu (×2850) |
| source_Acquisition_Method_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Pixel (×2850) |
| source_Sample_Platform_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top UAV (×2850) |
| source_Measurement_Venue_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top outdoor (×2850) |
| source_Target_Type_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Canopy (×2850) |
| source_Measurement_Quantity_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Reflectance (×2850) |
| source_Measurement_Units_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top % (×2850) |
| source_Wavelength_Units_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top nm (×2850) |
| source_Target_Status_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Live (×2850) |
| source_Light_Source_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Sun (×2850) |
| source_Foreoptic_Type_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Foreoptic (×2850) |
| source_Foreoptic_Field_of_View_aux | metadata | numeric | *Not specified.* | n=2850, missing=0, range 11.5–11.5, mean 11.5 ± 0 |
| source_Processing_Averaged_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Processing_Interpolated_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Processing_Resampled_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top No (×2850) |
| source_Instrument_Manufacturer_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Headwall Photonics (×2850) |
| source_Instrument_Model_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Nano-hyperspec (×2850) |
| source_Theme_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Ecology, Phenology (×2850) |
| source_Ecosystem_Type_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Forest (×2850) |
| source_Latitude_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 39°03'52.2" N (×2850) |
| source_Longitude_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 78°03'28.9" W (×2850) |
| source_geojson_aux | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| source_Location_Name_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm (×2850) |
| source_Sample_Collection_Date_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 2020 (×2850) |
| source_Common_Name_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top autumn olive, dahurian buckthorn, bush honeysuckle, tree of heaven, honey locust, osage orange, black walnut, eastern red cedar (×2850) |
| source_Latin_Genus_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Elaeagnus, Rhamnus, Lonicera, Ailanthus, Gleditsia, Maclura, Juglans, Juniperus (×2850) |
| source_Latin_Species_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top umbellata, davurica, maackii, altissima, triacanthos, pomifera, nigra, virginiana (×2850) |
| source_USDA_Symbol_aux | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| source_Vegetation_Type_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top tree, shrub, evergreen, deciduous (×2850) |
| source_Author_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman (×2850) |
| source_Author_Email_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top ksh5s@virginia.edu (×2850) |
| source_Maintainer_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman (×2850) |
| source_Maintainer_Email_aux | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top ksh5s@virginia.edu (×2850) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fine-scale-vnir-hyperspectral-canopy-reflectances-from-virginia-successional-forests`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 2 fields, Y: 2 fields, measurements: 0 fields, passport: 60 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is restricted or non-commercial; public redistribution of derived X/Y/M is not cleared in this pass.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `cac2e66467d0995de21b30379aa4eff418d65df27bd5ede488b77146196399e1`
- **Processing hash:** `b35e16dc71283c5e2bcca939131c1d660833c68e9a373161357db3c7094df18c` | **metadata hash:** `29d6010407a6734ecc06d2fc24b6dd4d163c790fd0dfa3bf37ddc00665a87d82`
