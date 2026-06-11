# Datasheet — EcoSIS Fresh-leaf CABO spectra from herbarium project v2 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fresh-leaf CABO spectra from herbarium project v2 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 50 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fresh-leaf CABO spectra from herbarium project v2

## Composition

- **Alignment:** observation level; 609 sample(s), 609 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | fresh_spec_avg.csv | Spectra Vista Corporation HR-1024i | NIR | 400–2400 nm | 609 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=609, missing=0, classes=66, top Populus tremuloides Michaux (×102) |
| LatinGenus | target | categorical | *Not specified.* | n=609, missing=0, classes=43, top Acer (×137) |
| LatinSpecies | target | categorical | *Not specified.* | n=609, missing=0, classes=60, top tremuloides (×102) |
| Discoloration | target | numeric | *Not specified.* | n=609, missing=0, range 0–4, mean 0.514 ± 0.8112 |
| GrowthForm | target | categorical | *Not specified.* | n=609, missing=0, classes=4, top tree (×500) |
| LMA | target | numeric | *Not specified.* | n=609, missing=5, range 0.02339–0.2179, mean 0.07725 ± 0.03666 |
| LDMC | target | numeric | *Not specified.* | n=609, missing=7, range 154.8–573, mean 403.6 ± 64.04 |
| EWT | target | numeric | *Not specified.* | n=609, missing=72, range 0.04433–0.2585, mean 0.09904 ± 0.03405 |
| EWT_rehydrated | target | numeric | *Not specified.* | n=609, missing=7, range 0.04878–0.2815, mean 0.1111 ± 0.03639 |
| N | target | numeric | *Not specified.* | n=609, missing=0, range 0.8833–5.618, mean 2.119 ± 0.591 |
| C | target | numeric | *Not specified.* | n=609, missing=0, range 39.54–53.6, mean 48.15 ± 2.165 |
| NDF | target | numeric | *Not specified.* | n=609, missing=8, range 11.05–61.47, mean 29.85 ± 8.118 |
| ADF | target | numeric | *Not specified.* | n=609, missing=12, range 7.972–34.66, mean 19.4 ± 4.435 |
| ADL | target | numeric | *Not specified.* | n=609, missing=12, range 1.145–21.8, mean 8.998 ± 3.446 |
| solubles | target | numeric | *Not specified.* | n=609, missing=8, range 38.53–88.95, mean 70.15 ± 8.119 |
| hemicellulose | target | numeric | *Not specified.* | n=609, missing=12, range 2.773–34.1, mean 10.49 ± 4.806 |
| cellulose | target | numeric | *Not specified.* | n=609, missing=12, range 5.19–25.77, mean 10.4 ± 3.144 |
| lignin | target | numeric | *Not specified.* | n=609, missing=12, range 0.918–21.47, mean 8.681 ± 3.407 |
| chlA | target | numeric | *Not specified.* | n=609, missing=45, range 1.242–15.5, mean 5.986 ± 2.194 |
| chlB | target | numeric | *Not specified.* | n=609, missing=45, range 0.486–5.293, mean 2.034 ± 0.7655 |
| car | target | numeric | *Not specified.* | n=609, missing=45, range 0.193–3.048, mean 1.25 ± 0.4387 |
| Al | target | numeric | *Not specified.* | n=609, missing=1, range 0–0.379, mean 0.05587 ± 0.04452 |
| Ca | target | numeric | *Not specified.* | n=609, missing=0, range 1.639–36.54, mean 11.29 ± 6.027 |
| Cu | target | numeric | *Not specified.* | n=609, missing=1, range 0–0.052, mean 0.007842 ± 0.005935 |
| Fe | target | numeric | *Not specified.* | n=609, missing=1, range 0.01497–0.262, mean 0.07533 ± 0.03879 |
| K | target | numeric | *Not specified.* | n=609, missing=1, range 1.058–36.18, mean 7.09 ± 4.446 |
| Mg | target | numeric | *Not specified.* | n=609, missing=0, range 0.482–7.862, mean 2.484 ± 0.9127 |
| Mn | target | numeric | *Not specified.* | n=609, missing=0, range 0–1.023, mean 0.1734 ± 0.1896 |
| Na | target | numeric | *Not specified.* | n=609, missing=1, range 0–4.872, mean 0.8504 ± 0.7072 |
| P | target | numeric | *Not specified.* | n=609, missing=0, range 0.2228–7.178, mean 1.762 ± 1.027 |
| Zn | target | numeric | *Not specified.* | n=609, missing=0, range 0.001424–0.647, mean 0.07226 ± 0.08392 |
| N_area | target | numeric | *Not specified.* | n=609, missing=5, range 5.151e-05–0.0002801, mean 0.0001513 ± 4.333e-05 |
| C_area | target | numeric | *Not specified.* | n=609, missing=5, range 0.00109–0.01102, mean 0.00376 ± 0.001933 |
| solubles_area | target | numeric | *Not specified.* | n=609, missing=13, range 0.001542–0.01589, mean 0.005426 ± 0.002623 |
| hemicellulose_area | target | numeric | *Not specified.* | n=609, missing=17, range 0.000118–0.002964, mean 0.0007963 ± 0.0004665 |
| cellulose_area | target | numeric | *Not specified.* | n=609, missing=17, range 0.000199–0.002419, mean 0.000804 ± 0.0004278 |
| lignin_area | target | numeric | *Not specified.* | n=609, missing=17, range 5.548e-05–0.002528, mean 0.0007092 ± 0.0005231 |
| chlA_area | target | numeric | *Not specified.* | n=609, missing=49, range 1.195e-05–0.0001246, mean 4.21e-05 ± 1.201e-05 |
| chlB_area | target | numeric | *Not specified.* | n=609, missing=49, range 3.989e-06–4.255e-05, mean 1.432e-05 ± 4.133e-06 |
| car_area | target | numeric | *Not specified.* | n=609, missing=49, range 2.923e-06–2.45e-05, mean 8.732e-06 ± 2.367e-06 |
| Al_area | target | numeric | *Not specified.* | n=609, missing=6, range 0–4.039e-06, mean 3.98e-07 ± 3.326e-07 |
| Ca_area | target | numeric | *Not specified.* | n=609, missing=5, range 3.834e-06–0.0003779, mean 8.497e-05 ± 5.555e-05 |
| Cu_area | target | numeric | *Not specified.* | n=609, missing=6, range 0–4.368e-07, mean 5.147e-08 ± 3.547e-08 |
| Fe_area | target | numeric | *Not specified.* | n=609, missing=6, range 1.459e-07–1.711e-06, mean 5.174e-07 ± 2.374e-07 |
| K_area | target | numeric | *Not specified.* | n=609, missing=6, range 1.482e-05–0.0002228, mean 4.867e-05 ± 2.63e-05 |
| Mg_area | target | numeric | *Not specified.* | n=609, missing=5, range 3.179e-06–8.179e-05, mean 1.867e-05 ± 1.011e-05 |
| Mn_area | target | numeric | *Not specified.* | n=609, missing=5, range 0–1.62e-05, mean 1.322e-06 ± 1.785e-06 |
| Na_area | target | numeric | *Not specified.* | n=609, missing=6, range 0–6.958e-05, mean 7.822e-06 ± 1.062e-05 |
| P_area | target | numeric | *Not specified.* | n=609, missing=5, range 3.089e-06–7.277e-05, mean 1.263e-05 ± 8.242e-06 |
| Zn_area | target | numeric | *Not specified.* | n=609, missing=5, range 2.297e-08–5.234e-06, mean 5.131e-07 ± 6.318e-07 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top 4c0bdc9f-a767-4b2b-be22-bdb10edb2a67 (×609) |
| site | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=609, missing=0, range -34.81–45.99, mean 36.64 ± 25.29 |
| longitude | metadata | numeric | *Not specified.* | n=609, missing=0, range -75.52–116.1, mean -52.65 ± 59.82 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top source-provided coordinates when available (×609) |
| year | metadata | numeric | *Not specified.* | n=609, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=609, missing=0, classes=66, top Populus tremuloides Michaux (×102) |
| genus | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=609, missing=609, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top Leaf (×609) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top leaf (×609) |
| instrument | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×609) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top Contact (×609) |
| signal_type | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top reflectance (×609) |
| axis_unit | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top nm (×609) |
| axis_min | metadata | numeric | *Not specified.* | n=609, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=609, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=609, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top 10.1111/2041-210X.13958 \| 10.21232/44vxHorW \| 10.21232/QfzAxZoM \| 10.21232/VYJzNBEy \| 10.21232/deP7jVyq \| 10.21232/dep7jvyq (×609) |
| citation | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top Shan Kothari, Rosalie Beauchamp-Rioux, Etienne Lalibert and Jeannine Cavender-Bares. 2022. Fresh-leaf CABO spectra from herbarium project v2. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/QfzAxZoM (×609) |
| license | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×609) |
| rights_status | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top explicit_open (×609) |
| usage_scope | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top public_reuse_possible (×609) |
| notes | metadata | categorical | *Not specified.* | n=609, missing=0, classes=1, top EcoSIS package fresh-leaf-cabo-spectra-from-herbarium-project-v2, no interpolation applied by project. (×609) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-leaf-cabo-spectra-from-herbarium-project-v2`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Reflectance spectroscopy allows rapid, accurate, and non-destructive estimates of functional traits from pressed leaves — [10.1111/2041-210X.13958](https://doi.org/10.1111/2041-210X.13958)
- Fresh-leaf CABO spectra from herbarium project v2 — [10.21232/QfzAxZoM](https://doi.org/10.21232/QfzAxZoM)
- *Not specified.* — [10.21232/44vxHorW](https://doi.org/10.21232/44vxHorW)
- *Not specified.* — [10.21232/VYJzNBEy](https://doi.org/10.21232/VYJzNBEy)
- *Not specified.* — [10.21232/deP7jVyq](https://doi.org/10.21232/deP7jVyq)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `541df22622999b47098b4b496609013e34bd01e9738d6e5a310dcf8610597b32`
- **Processing hash:** `e53e5765319817512a8828dd2d490f7af441bf7b65cd78c33ff839700901eb89` | **metadata hash:** `f15cfac22e02d35aef91034d771388fad2fcc0a8636afd5611ea0ffb3fac0043`
