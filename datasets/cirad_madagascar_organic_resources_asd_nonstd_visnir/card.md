# Datasheet — CIRAD Madagascar organic resources ASD non-standardized VIS-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cirad
- **Description:** CIRAD Madagascar organic resources ASD non-standardized VIS-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 20 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cirad
- **Contributor:** Spectroscopic VIS-NIR analysis of organic resources from Madagascar

## Composition

- **Alignment:** sample level; 1000 sample(s), 1000 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ASD non-standardized absorbance | ASD | NIR | 400–2498 nm | 1000 | 1050 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TOC | target | numeric | *Not specified.* | n=1000, missing=821, range 2–47.25, mean 23.62 ± 10 |
| TOM | target | numeric | *Not specified.* | n=1000, missing=821, range 4.2–96.9, mean 46.7 ± 19.68 |
| ASH | target | numeric | *Not specified.* | n=1000, missing=914, range 2.747–98.5, mean 55.81 ± 22.1 |
| SOL | target | numeric | *Not specified.* | n=1000, missing=914, range 0.1404–71.24, mean 17.19 ± 10.8 |
| HEM | target | numeric | *Not specified.* | n=1000, missing=914, range 0.0001–31.17, mean 9.339 ± 7.225 |
| CEL | target | numeric | *Not specified.* | n=1000, missing=914, range 0.0001–45.38, mean 9.862 ± 8.344 |
| LIC | target | numeric | *Not specified.* | n=1000, missing=914, range 0.0823–39.43, mean 7.834 ± 7.262 |
| TN | target | numeric | *Not specified.* | n=1000, missing=821, range 0.0001–99.2, mean 21.98 ± 13.97 |
| totP | target | numeric | *Not specified.* | n=1000, missing=913, range 0.242–158.2, mean 13.23 ± 19.76 |
| totK | target | numeric | *Not specified.* | n=1000, missing=913, range 0.647–151.6, mean 14.28 ± 16.58 |
| totCa | target | numeric | *Not specified.* | n=1000, missing=935, range 0.197–137.7, mean 42.98 ± 39.49 |
| totMg | target | numeric | *Not specified.* | n=1000, missing=934, range 0.682–23.12, mean 7.656 ± 4.347 |
| Cd | target | numeric | *Not specified.* | n=1000, missing=961, range 0.0001–3.28, mean 0.968 ± 0.8066 |
| Cr | target | numeric | *Not specified.* | n=1000, missing=962, range 4.83–293.5, mean 84.18 ± 80.38 |
| Cu | target | numeric | *Not specified.* | n=1000, missing=962, range 5.51–540.5, mean 109.9 ± 149.9 |
| Ni | target | numeric | *Not specified.* | n=1000, missing=962, range 3.56–64.13, mean 23.29 ± 18.13 |
| Pb | target | numeric | *Not specified.* | n=1000, missing=962, range 0.0001–3982, mean 429.2 ± 806.1 |
| Zn | target | numeric | *Not specified.* | n=1000, missing=962, range 39.38–2221, mean 559.1 ± 576.2 |
| OR_category | target | categorical | *Not specified.* | n=1000, missing=0, classes=4, top Animal (×863) |
| OR_origin | target | categorical | *Not specified.* | n=1000, missing=0, classes=18, top poultry (×340) |
| composition_metadata_url | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top https://dataverse.cirad.fr/dataset.xhtml?persistentId=doi:10.18167/DVN1/YRMQ52 (×1000) |
| api_url | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top https://dataverse.cirad.fr/api/datasets/:persistentId/?persistentId=doi:10.18167/DVN1/SZSTBD (×1000) |
| article_url | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922005510 (×1000) |
| doi_dataset | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top 10.18167/DVN1/SZSTBD (×1000) |
| doi_composition_metadata | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top 10.18167/DVN1/YRMQ52 (×1000) |
| doi_publication | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top 10.1016/j.dib.2022.108102 (×1000) |
| license | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (×1000) |
| license_id | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top cc-by-nc-sa-4.0 (×1000) |
| license_url | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top https://creativecommons.org/licenses/by-nc-sa/4.0/ (×1000) |
| rights_status | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top explicit_open_noncommercial_sharealike (×1000) |
| usage_scope | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top internal_benchmark_only_until_license_review (×1000) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top False (×1000) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top VIS-NIR (×1000) |
| axis_unit | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top nm (×1000) |
| axis_min | metadata | numeric | *Not specified.* | n=1000, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1000, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1000, missing=0, range 1050–1050, mean 1050 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top ASD (×1000) |
| signal_type | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top absorbance (×1000) |
| standardized_on_xds | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top NO (×1000) |
| decoder | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top pandas.read_excel/openpyxl (×1000) |
| notes | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=1, top CC BY-NC-SA source, many chemical targets are sparse. Variable dictionary sheets retained in source workbooks. (×1000) |
| Collection_date | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=108, top 2011-08-26 00:00:00 (×46) |
| Town | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=6, top Mahajanga (×728) |
| Township | metadata | categorical | *Not specified.* | n=1000, missing=85, classes=35, top Belobaka (×99) |
| Animal_Development`_stages | metadata | categorical | *Not specified.* | n=1000, missing=572, classes=6, top adult (×210) |
| Animal_Age(days) | metadata | categorical | *Not specified.* | n=1000, missing=852, classes=44, top 36.0 (×9) |
| Animal_Sex | metadata | categorical | *Not specified.* | n=1000, missing=458, classes=3, top female (×329) |
| Adult_Type | metadata | categorical | *Not specified.* | n=1000, missing=734, classes=6, top laying hen (×101) |
| Exploitation_Type | metadata | categorical | *Not specified.* | n=1000, missing=118, classes=2, top farm (×711) |
| Feed_RiceBran | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×570) |
| Feed_BlackEyedPeas | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×615) |
| Feed_IndustrializedFeedstuff | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×442) |
| Feed_HomemadeFeedstuff | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×727) |
| Feed_Weeds | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×613) |
| Feed_Maizestalk | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×806) |
| Feed_Fodder | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×781) |
| Feed_KitchenWaste | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×795) |
| Feed_CottonResidues | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×791) |
| Feed_peanutsfoliage | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×788) |
| Feed_sweetpotato&pumpkin&cassava | metadata | categorical | *Not specified.* | n=1000, missing=193, classes=2, top no (×788) |
| OR_Nature | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=19, top manure (×395) |
| OR_Name | metadata | categorical | *Not specified.* | n=1000, missing=247, classes=3, top slurry (×373) |
| Litter/No_litter | metadata | categorical | *Not specified.* | n=1000, missing=250, classes=2, top no (×464) |
| Littter_Rice_straw | metadata | categorical | *Not specified.* | n=1000, missing=782, classes=2, top no (×196) |
| Litter_Grass | metadata | categorical | *Not specified.* | n=1000, missing=782, classes=2, top no (×214) |
| Litter_Woodchip | metadata | categorical | *Not specified.* | n=1000, missing=782, classes=2, top yes (×196) |
| Litter_Fodder | metadata | categorical | *Not specified.* | n=1000, missing=782, classes=2, top no (×209) |
| Sample_type | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=7, top Composite (×858) |
| Composted/Non_conposted | metadata | categorical | *Not specified.* | n=1000, missing=0, classes=2, top nc (×894) |
| OR_age(days) | metadata | categorical | *Not specified.* | n=1000, missing=956, classes=13, top 1825 (×7) |
| OR_Stage | metadata | categorical | *Not specified.* | n=1000, missing=976, classes=3, top mature (×11) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- CIRAD Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.18167/DVN1/SZSTBD`
- CIRAD Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.18167/DVN1/YRMQ52`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by-nc-sa/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 30 fields, Y: 20 fields, passport: 26 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** CIRAD Dataverse API reports CC BY-NC-SA 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `d9ef48d3d47b86cafcf71a9a5a1d774d5e4c72f15bae4406417afaa263665ce8`
- **Processing hash:** `7d47f4d0a866ddf5d4552accfaf354537ba22b3a0e87552b0779d34ebab7532b` | **metadata hash:** `4e41c8c7579794b6e20bd0cea96d2147d0f42d0383d9df7c6e32baeb2cb9d432`
