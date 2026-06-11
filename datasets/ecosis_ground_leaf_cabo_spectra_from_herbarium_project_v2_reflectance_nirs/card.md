# Datasheet — EcoSIS Ground-leaf CABO spectra from herbarium project v2 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Ground-leaf CABO spectra from herbarium project v2 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 31 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Ground-leaf CABO spectra from herbarium project v2

## Composition

- **Alignment:** observation level; 607 sample(s), 607 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ground_spec_avg.csv | Spectral Evolution PSR+ 3500 | NIR | 400–2400 nm | 607 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=607, missing=0, classes=66, top Populus tremuloides Michaux (×100) |
| LatinGenus | target | categorical | *Not specified.* | n=607, missing=0, classes=46, top Acer (×136) |
| LatinSpecies | target | categorical | *Not specified.* | n=607, missing=0, classes=61, top tremuloides (×100) |
| Discoloration | target | numeric | *Not specified.* | n=607, missing=0, range 0–4, mean 0.5173 ± 0.8201 |
| GrowthForm | target | categorical | *Not specified.* | n=607, missing=0, classes=4, top tree (×498) |
| LMA | target | numeric | *Not specified.* | n=607, missing=5, range 0.02339–0.2179, mean 0.07732 ± 0.03668 |
| LDMC | target | numeric | *Not specified.* | n=607, missing=7, range 158.8–573, mean 403.1 ± 64.73 |
| EWT | target | numeric | *Not specified.* | n=607, missing=74, range 0.04433–0.2585, mean 0.0992 ± 0.0341 |
| EWT_rehydrated | target | numeric | *Not specified.* | n=607, missing=7, range 0.04878–0.2815, mean 0.1115 ± 0.03649 |
| N | target | numeric | *Not specified.* | n=607, missing=0, range 0.8833–5.618, mean 2.118 ± 0.5814 |
| C | target | numeric | *Not specified.* | n=607, missing=0, range 39.54–53.6, mean 48.13 ± 2.188 |
| NDF | target | numeric | *Not specified.* | n=607, missing=8, range 11.05–61.47, mean 29.98 ± 8.207 |
| ADF | target | numeric | *Not specified.* | n=607, missing=12, range 7.972–34.66, mean 19.43 ± 4.454 |
| ADL | target | numeric | *Not specified.* | n=607, missing=12, range 1.145–21.8, mean 9.038 ± 3.46 |
| solubles | target | numeric | *Not specified.* | n=607, missing=8, range 38.53–88.95, mean 70.03 ± 8.208 |
| hemicellulose | target | numeric | *Not specified.* | n=607, missing=12, range 2.773–34.1, mean 10.58 ± 4.892 |
| cellulose | target | numeric | *Not specified.* | n=607, missing=12, range 5.19–25.77, mean 10.4 ± 3.196 |
| lignin | target | numeric | *Not specified.* | n=607, missing=12, range 0.918–21.47, mean 8.72 ± 3.42 |
| chlA | target | numeric | *Not specified.* | n=607, missing=47, range 1.242–15.5, mean 5.991 ± 2.186 |
| chlB | target | numeric | *Not specified.* | n=607, missing=47, range 0.486–5.293, mean 2.035 ± 0.7612 |
| car | target | numeric | *Not specified.* | n=607, missing=47, range 0.193–3.048, mean 1.251 ± 0.4398 |
| Al | target | numeric | *Not specified.* | n=607, missing=1, range 0–0.379, mean 0.05697 ± 0.04643 |
| Ca | target | numeric | *Not specified.* | n=607, missing=0, range 1.639–36.54, mean 11.33 ± 6.05 |
| Cu | target | numeric | *Not specified.* | n=607, missing=1, range 0–0.052, mean 0.00784 ± 0.005908 |
| Fe | target | numeric | *Not specified.* | n=607, missing=1, range 0.01497–0.266, mean 0.0763 ± 0.04019 |
| K | target | numeric | *Not specified.* | n=607, missing=0, range 1.058–38.15, mean 7.167 ± 4.651 |
| Mg | target | numeric | *Not specified.* | n=607, missing=0, range 0.482–7.862, mean 2.495 ± 0.9311 |
| Mn | target | numeric | *Not specified.* | n=607, missing=0, range 0–1.023, mean 0.1721 ± 0.1895 |
| Na | target | numeric | *Not specified.* | n=607, missing=0, range 0–4.872, mean 0.8523 ± 0.6964 |
| P | target | numeric | *Not specified.* | n=607, missing=0, range 0.2228–7.178, mean 1.758 ± 1.015 |
| Zn | target | numeric | *Not specified.* | n=607, missing=0, range 0.001424–0.647, mean 0.07022 ± 0.08171 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top 2dcfc28e-d7f5-432b-a469-5d71e37384d8 (×607) |
| site | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=607, missing=0, range -34.81–45.99, mean 36.61 ± 25.33 |
| longitude | metadata | numeric | *Not specified.* | n=607, missing=0, range -75.52–116.1, mean -52.58 ± 59.9 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top source-provided coordinates when available (×607) |
| year | metadata | numeric | *Not specified.* | n=607, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=607, missing=0, classes=66, top Populus tremuloides Michaux (×100) |
| genus | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=607, missing=607, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top Leaf (×607) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top leaf (×607) |
| instrument | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×607) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top Contact (×607) |
| signal_type | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top reflectance (×607) |
| axis_unit | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top nm (×607) |
| axis_min | metadata | numeric | *Not specified.* | n=607, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=607, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=607, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top 10.1111/2041-210X.13958 \| 10.21232/DCpLBYke \| 10.21232/dcplbyke \| 10.21232/vj7AGhTC (×607) |
| citation | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top Shan Kothari, Rosalie Beauchamp-Rioux, Etienne Laliberté and Jeannine Cavender-Bares. 2022. Ground-leaf CABO spectra from herbarium project v2. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/vj7AGhTC (×607) |
| license | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×607) |
| rights_status | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top explicit_open (×607) |
| usage_scope | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top public_reuse_possible (×607) |
| notes | metadata | categorical | *Not specified.* | n=607, missing=0, classes=1, top EcoSIS package ground-leaf-cabo-spectra-from-herbarium-project-v2, no interpolation applied by project. (×607) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ground-leaf-cabo-spectra-from-herbarium-project-v2`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Reflectance spectroscopy allows rapid, accurate, and non-destructive estimates of functional traits from pressed leaves — [10.1111/2041-210X.13958](https://doi.org/10.1111/2041-210X.13958)
- Ground-leaf CABO spectra from herbarium project v2 — [10.21232/vj7AGhTC](https://doi.org/10.21232/vj7AGhTC)
- *Not specified.* — [10.21232/DCpLBYke](https://doi.org/10.21232/DCpLBYke)
- *Not specified.* — [10.21232/dcplbyke](https://doi.org/10.21232/dcplbyke)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `3448ae9748fb734d44a16294624e92c4f982204a876836d1c9cacd26a683a4a9`
- **Processing hash:** `72c40315dbbc6c457351f85aa01547030b533ce439599fc5843fd4612ae3c4b9` | **metadata hash:** `ea8a98b9ac43dfb3a3ef7b5eb46482af450f0dbdf12b543eea98ce38ce031fcb`
