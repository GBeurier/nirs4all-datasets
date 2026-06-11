# Datasheet — EcoSIS Leaf spectra, structural and biochemical leaf traits of eight crop species (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf spectra, structural and biochemical leaf traits of eight crop species (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 46 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf spectra, structural and biochemical leaf traits of eight crop species

## Composition

- **Alignment:** observation level; 184 sample(s), 184 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | BNL_2015glasshouse_SVC_Averaged_Interpolated_Spectra.csv | Spectravista Corporation HR-1024i | NIR | 350–2500 nm | 184 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | target | categorical | *Not specified.* | n=184, missing=0, classes=8, top HEAN3 (×40) |
| pot_size | target | numeric | *Not specified.* | n=184, missing=0, range 1–2, mean 1.511 ± 0.5012 |
| C_pc_dry | target | numeric | *Not specified.* | n=184, missing=1, range 28.56–45.94, mean 40.89 ± 2.657 |
| H_pc_dry | target | numeric | *Not specified.* | n=184, missing=1, range 3.165–6.66, mean 5.69 ± 0.438 |
| N_pc_dry | target | numeric | *Not specified.* | n=184, missing=1, range 0.705–6.075, mean 3.327 ± 1.32 |
| C_N_mass | target | numeric | *Not specified.* | n=184, missing=1, range 6.03–9.02, mean 7.21 ± 0.5055 |
| LMA_g_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 16.1–70.42, mean 37.94 ± 11.82 |
| H20_g_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 92.31–262.6, mean 159.2 ± 34.14 |
| C_N_m2 | target | numeric | *Not specified.* | n=184, missing=1, range 7.02–58.5, mean 14.94 ± 8.102 |
| DW_FW | target | numeric | *Not specified.* | n=184, missing=0, range 0.07837–0.3085, mean 0.1923 ± 0.04216 |
| C_g_m2 | target | numeric | *Not specified.* | n=184, missing=1, range 6.612–27.5, mean 15.42 ± 4.571 |
| N_g_m2 | target | numeric | *Not specified.* | n=184, missing=1, range 0.2453–2.805, mean 1.211 ± 0.5074 |
| cryo_mass_mg | target | numeric | *Not specified.* | n=184, missing=0, range 22.9–28.9, mean 26.22 ± 1.163 |
| protein_ug_extract | target | numeric | *Not specified.* | n=184, missing=0, range 165–1443, mean 763.7 ± 279.4 |
| starch_nmol_Glc_Extract | target | numeric | *Not specified.* | n=184, missing=2, range 14–8435, mean 2763 ± 1782 |
| glucose_nmol_Glc_extract | target | numeric | *Not specified.* | n=184, missing=0, range 68–1961, mean 516.4 ± 354 |
| fructose_nmol_Glc_extract | target | numeric | *Not specified.* | n=184, missing=0, range -3–915, mean 212.5 ± 185 |
| sucrose_nmol_Glc_extract | target | numeric | *Not specified.* | n=184, missing=0, range 14–2794, mean 866.1 ± 668.4 |
| amino_acid_nmol_extract | target | numeric | *Not specified.* | n=184, missing=4, range 24–1431, mean 385 ± 292.1 |
| nitrate_nmol_extract | target | numeric | *Not specified.* | n=184, missing=0, range -7–1414, mean 175.1 ± 274.6 |
| protein_ug_mg_fr | target | numeric | *Not specified.* | n=184, missing=0, range 6–54, mean 29.08 ± 10.37 |
| starch_nmol_Glc_mg_fr | target | numeric | *Not specified.* | n=184, missing=2, range 1–332, mean 105.5 ± 68.57 |
| glucose_nmol_Glc_mg_fr | target | numeric | *Not specified.* | n=184, missing=0, range 3–73, mean 19.7 ± 13.45 |
| fructose_nmol_Glc_mg_fr | target | numeric | *Not specified.* | n=184, missing=0, range 0–35, mean 8.12 ± 7.066 |
| sucrose_nmol_Glc_mg_fr | target | numeric | *Not specified.* | n=184, missing=0, range 1–105, mean 33.12 ± 25.63 |
| aa_nmol_mg_fr | target | numeric | *Not specified.* | n=184, missing=4, range 1–58, mean 14.67 ± 11.06 |
| nitrate_nmol_mg_fr | target | numeric | *Not specified.* | n=184, missing=0, range 0–52, mean 6.679 ± 10.28 |
| protein_ug_mg_DW | target | numeric | *Not specified.* | n=184, missing=0, range 45–277, mean 154.4 ± 52.61 |
| starch_nmol_Glc_mg_DW | target | numeric | *Not specified.* | n=184, missing=2, range 3–1391, mean 552.1 ± 337.8 |
| glucose_nmol_Glc_mg_DW | target | numeric | *Not specified.* | n=184, missing=0, range 11–397, mean 102.6 ± 66.82 |
| fructose_nmol_Glc_mg_DW | target | numeric | *Not specified.* | n=184, missing=0, range -1–328, mean 45.49 ± 47.76 |
| sucrose_nmol_Glc_mg_DW | target | numeric | *Not specified.* | n=184, missing=0, range 4–504, mean 166.3 ± 114 |
| aa_nmol_mg_DW | target | numeric | *Not specified.* | n=184, missing=4, range 6–250, mean 78.03 ± 56.25 |
| nitrate_nmol_mg_DW | target | numeric | *Not specified.* | n=184, missing=0, range -1–410, mean 41.55 ± 73.11 |
| protein_mg_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 1.31–12.07, mean 5.678 ± 2.197 |
| starch_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=2, range 0.09–56.73, mean 20.43 ± 13.24 |
| glucose_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 0.38–12.45, mean 3.945 ± 2.916 |
| fructose_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=0, range -0.02–8.41, mean 1.547 ± 1.338 |
| sucrose_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 0.11–17.49, mean 6.329 ± 4.484 |
| aa_umol_m2 | target | numeric | *Not specified.* | n=184, missing=4, range 0.14–14.64, mean 2.923 ± 2.392 |
| nitrate_umol_m2 | target | numeric | *Not specified.* | n=184, missing=0, range -0.05–9.45, mean 1.329 ± 2.115 |
| H2O_pc | target | numeric | *Not specified.* | n=184, missing=0, range 69.15–92.16, mean 80.77 ± 4.216 |
| TNC_nmol_Glc_mg | target | numeric | *Not specified.* | n=184, missing=2, range 134–1842, mean 865.6 ± 315.5 |
| all_sugar_nmol_Glc_mg | target | numeric | *Not specified.* | n=184, missing=0, range 48–758, mean 314.4 ± 165.4 |
| TNC_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=2, range 2.77–74.84, mean 32.2 ± 13.32 |
| all_sug_umol_Glc_m2 | target | numeric | *Not specified.* | n=184, missing=0, range 1.4–28.36, mean 11.82 ± 6.693 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top 8d4fa096-d8cd-4ba2-91b4-fe18c6877794 (×184) |
| site | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Upton, NY, USA (×184) |
| country | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top source-provided coordinates when available (×184) |
| year | metadata | numeric | *Not specified.* | n=184, missing=0, range 2018–2018, mean 2018 ± 0 |
| date | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=184, missing=184, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Leaf (×184) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top leaf (×184) |
| instrument | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Spectravista Corporation HR-1024i (×184) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Contact (×184) |
| signal_type | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top reflectance (×184) |
| axis_unit | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top nm (×184) |
| axis_min | metadata | numeric | *Not specified.* | n=184, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=184, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=184, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top 10.1093/jxb/erz061 \| 10.21232/C2GM2Z \| 10.21232/c2gm2z (×184) |
| citation | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Ely K.S. Serbin S.P. Lieberman-Cribbin W. Rogers A.. 2018. Leaf spectra, structural and biochemical leaf traits of eight crop species. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). doi:10.21232/C2GM2Z (×184) |
| license | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top Open Data Commons Attribution License (×184) |
| rights_status | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top explicit_open (×184) |
| usage_scope | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top public_reuse_possible (×184) |
| notes | metadata | categorical | *Not specified.* | n=184, missing=0, classes=1, top EcoSIS package leaf-spectra--structural-and-biochemical-leaf-traits-of-eight-crop-species, no interpolation applied by project. (×184) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-spectra--structural-and-biochemical-leaf-traits-of-eight-crop-species`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Kim S Ely, Angela C Burnett, Wil Lieberman-Cribbin, Shawn P Serbin, Alistair Rogers, Spectroscopy can predict key leaf traits associated with source–sink balance and carbon–nitrogen status, Journal of Experimental Botany, Volume 70, Issue 6, 1 March 2019, Pages 1789–1799 — [10.1093/jxb/erz061](https://doi.org/10.1093/jxb/erz061)
- Leaf spectra, structural and biochemical leaf traits of eight crop species — [10.21232/C2GM2Z](https://doi.org/10.21232/C2GM2Z)
- *Not specified.* — [10.21232/c2gm2z](https://doi.org/10.21232/c2gm2z)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0881ee48eaeb5fc60f11964822320cf5d307078347b9f2036420e746967bdff5`
- **Processing hash:** `b6e7262b0164612b37cd1e17d362806a86ad855e8df60f9882cc3241371278ae` | **metadata hash:** `d88cc5ca98535cb2f249342b2062e85968b0d0bb64c50b86291d5cfc7d1df896`
