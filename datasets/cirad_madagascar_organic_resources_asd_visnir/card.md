# Datasheet — Madagascar organic resources — ASD + XDS-standardized Vis-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cirad
- **Description:** CIRAD Madagascar organic resources ASD vis-NIR, native and XDS-standardized. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 20 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cirad
- **Contributor:** Spectroscopic VIS-NIR analysis of organic resources from Madagascar

## Composition

- **Alignment:** sample level; 1000 sample(s), 2000 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_native | ASD non-standardized absorbance | ASD | NIR | 400–2498 nm | 1000 | 1050 |
| X_xds_standardized | ASD standardized on XDS absorbance | ASD | NIR | 400–2498 nm | 1000 | 1050 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| TOC | target | numeric | *Not specified.* | n=2000, missing=1642, range 2–47.25, mean 23.62 ± 9.986 |
| TOM | target | numeric | *Not specified.* | n=2000, missing=1642, range 4.2–96.9, mean 46.7 ± 19.65 |
| ASH | target | numeric | *Not specified.* | n=2000, missing=1828, range 2.747–98.5, mean 55.81 ± 22.03 |
| SOL | target | numeric | *Not specified.* | n=2000, missing=1828, range 0.1404–71.24, mean 17.19 ± 10.77 |
| HEM | target | numeric | *Not specified.* | n=2000, missing=1828, range 0.0001–31.17, mean 9.339 ± 7.203 |
| CEL | target | numeric | *Not specified.* | n=2000, missing=1828, range 0.0001–45.38, mean 9.862 ± 8.32 |
| LIC | target | numeric | *Not specified.* | n=2000, missing=1828, range 0.0823–39.43, mean 7.834 ± 7.241 |
| TN | target | numeric | *Not specified.* | n=2000, missing=1642, range 0.0001–99.2, mean 21.98 ± 13.95 |
| totP | target | numeric | *Not specified.* | n=2000, missing=1826, range 0.242–158.2, mean 13.23 ± 19.7 |
| totK | target | numeric | *Not specified.* | n=2000, missing=1826, range 0.647–151.6, mean 14.28 ± 16.53 |
| totCa | target | numeric | *Not specified.* | n=2000, missing=1870, range 0.197–137.7, mean 42.98 ± 39.33 |
| totMg | target | numeric | *Not specified.* | n=2000, missing=1868, range 0.682–23.12, mean 7.656 ± 4.33 |
| Cd | target | numeric | *Not specified.* | n=2000, missing=1922, range 0.0001–3.28, mean 0.968 ± 0.8013 |
| Cr | target | numeric | *Not specified.* | n=2000, missing=1924, range 4.83–293.5, mean 84.18 ± 79.84 |
| Cu | target | numeric | *Not specified.* | n=2000, missing=1924, range 5.51–540.5, mean 109.9 ± 148.9 |
| Ni | target | numeric | *Not specified.* | n=2000, missing=1924, range 3.56–64.13, mean 23.29 ± 18.01 |
| Pb | target | numeric | *Not specified.* | n=2000, missing=1924, range 0.0001–3982, mean 429.2 ± 800.7 |
| Zn | target | numeric | *Not specified.* | n=2000, missing=1924, range 39.38–2221, mean 559.1 ± 572.4 |
| OR_category | target | categorical | *Not specified.* | n=2000, missing=0, classes=4, top Animal (×1726) |
| OR_origin | target | categorical | *Not specified.* | n=2000, missing=0, classes=18, top poultry (×680) |
| composition_metadata_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://dataverse.cirad.fr/dataset.xhtml?persistentId=doi:10.18167/DVN1/YRMQ52 (×2000) |
| api_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://dataverse.cirad.fr/api/datasets/:persistentId/?persistentId=doi:10.18167/DVN1/SZSTBD (×2000) |
| article_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340922005510 (×2000) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top 10.18167/DVN1/SZSTBD (×2000) |
| doi_composition_metadata | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top 10.18167/DVN1/YRMQ52 (×2000) |
| doi_publication | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top 10.1016/j.dib.2022.108102 (×2000) |
| license | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (×2000) |
| license_id | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top cc-by-nc-sa-4.0 (×2000) |
| license_url | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top https://creativecommons.org/licenses/by-nc-sa/4.0/ (×2000) |
| rights_status | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top explicit_open_noncommercial_sharealike (×2000) |
| usage_scope | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top internal_benchmark_only_until_license_review (×2000) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top False (×2000) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top VIS-NIR (×2000) |
| axis_unit | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top nm (×2000) |
| axis_min | metadata | numeric | *Not specified.* | n=2000, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2000, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2000, missing=0, range 1050–1050, mean 1050 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top ASD (×2000) |
| signal_type | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top absorbance (×2000) |
| standardized_on_xds | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=2, top NO (×1000) |
| decoder | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top pandas.read_excel/openpyxl (×2000) |
| notes | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=1, top CC BY-NC-SA source, many chemical targets are sparse. Variable dictionary sheets retained in source workbooks. (×2000) |
| Collection_date | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=108, top 2011-08-26 00:00:00 (×92) |
| Town | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=6, top Mahajanga (×1456) |
| Township | metadata | categorical | *Not specified.* | n=2000, missing=170, classes=35, top Belobaka (×198) |
| Animal_Development`_stages | metadata | categorical | *Not specified.* | n=2000, missing=1144, classes=6, top adult (×420) |
| Animal_Age(days) | metadata | categorical | *Not specified.* | n=2000, missing=1704, classes=44, top 36.0 (×18) |
| Animal_Sex | metadata | categorical | *Not specified.* | n=2000, missing=916, classes=3, top female (×658) |
| Adult_Type | metadata | categorical | *Not specified.* | n=2000, missing=1468, classes=6, top laying hen (×202) |
| Exploitation_Type | metadata | categorical | *Not specified.* | n=2000, missing=236, classes=2, top farm (×1422) |
| Feed_RiceBran | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1140) |
| Feed_BlackEyedPeas | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1230) |
| Feed_IndustrializedFeedstuff | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×884) |
| Feed_HomemadeFeedstuff | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1454) |
| Feed_Weeds | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1226) |
| Feed_Maizestalk | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1612) |
| Feed_Fodder | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1562) |
| Feed_KitchenWaste | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1590) |
| Feed_CottonResidues | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1582) |
| Feed_peanutsfoliage | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1576) |
| Feed_sweetpotato&pumpkin&cassava | metadata | categorical | *Not specified.* | n=2000, missing=386, classes=2, top no (×1576) |
| OR_Nature | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=19, top manure (×790) |
| OR_Name | metadata | categorical | *Not specified.* | n=2000, missing=494, classes=3, top slurry (×746) |
| Litter/No_litter | metadata | categorical | *Not specified.* | n=2000, missing=500, classes=2, top no (×928) |
| Littter_Rice_straw | metadata | categorical | *Not specified.* | n=2000, missing=1564, classes=2, top no (×392) |
| Litter_Grass | metadata | categorical | *Not specified.* | n=2000, missing=1564, classes=2, top no (×428) |
| Litter_Woodchip | metadata | categorical | *Not specified.* | n=2000, missing=1564, classes=2, top yes (×392) |
| Litter_Fodder | metadata | categorical | *Not specified.* | n=2000, missing=1564, classes=2, top no (×418) |
| Sample_type | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=7, top Composite (×1716) |
| Composted/Non_conposted | metadata | categorical | *Not specified.* | n=2000, missing=0, classes=2, top nc (×1788) |
| OR_age(days) | metadata | categorical | *Not specified.* | n=2000, missing=1912, classes=13, top 1825 (×14) |
| OR_Stage | metadata | categorical | *Not specified.* | n=2000, missing=1952, classes=3, top mature (×22) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- CIRAD Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.18167/DVN1/SZSTBD`
- CIRAD Dataverse — kind `dataverse`, access `open`, license *Not specified.*: `10.18167/DVN1/YRMQ52`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 31 fields, Y: 20 fields, measurements: 0 fields, passport: 25 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `11ebd414d317c46ea8f84d762e0a23c6be87c31892162ec2239a9e03c5101a9b`
- **Processing hash:** `be169c9d5c8ebc7bcf61c11a6c29e0c9eabc57b45c425b27c0de62596004f541` | **metadata hash:** `e0c5e5fc53ab048973a679220575af81fd36d9488b99db154a5dc2fd2181a984`
