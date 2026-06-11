# Datasheet — EcoSIS Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD) (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD) (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD)

## Composition

- **Alignment:** observation level; 190 sample(s), 190 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra.csv | spectral evolution SR-3500 | NIR | 400–2500 nm | 190 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| group | target | categorical | *Not specified.* | n=190, missing=0, classes=3, top Hydr (×80) |
| group_aux | target | categorical | *Not specified.* | n=190, missing=0, classes=3, top Hydr (×80) |
| Chl-a | target | numeric | *Not specified.* | n=190, missing=2, range 13.72–61.19, mean 30.63 ± 8.959 |
| Chl-b | target | numeric | *Not specified.* | n=190, missing=2, range 3.41–16.62, mean 7.588 ± 2.254 |
| Car | target | numeric | *Not specified.* | n=190, missing=2, range 3.78–14.43, mean 8.565 ± 2.155 |
| Chl-a_Chl-b | target | numeric | *Not specified.* | n=190, missing=3, range 2.75–6.1, mean 4.073 ± 0.5654 |
| Chl_Car | target | numeric | *Not specified.* | n=190, missing=4, range 2.42–6.24, mean 4.504 ± 0.7939 |
| Thickness | target | numeric | *Not specified.* | n=190, missing=2, range 123.5–1234, mean 338.1 ± 240.4 |
| EWT | target | numeric | *Not specified.* | n=190, missing=0, range 24.33–529, mean 171.9 ± 100.5 |
| LMA | target | numeric | *Not specified.* | n=190, missing=0, range 14.53–118.7, mean 62.47 ± 21.06 |
| DMC | target | numeric | *Not specified.* | n=190, missing=0, range 0.1391–0.7529, mean 0.297 ± 0.115 |
| LNC | target | numeric | *Not specified.* | n=190, missing=0, range 0.0139–0.0492, mean 0.03269 ± 0.009057 |
| LCC | target | numeric | *Not specified.* | n=190, missing=0, range 0.4136–0.5315, mean 0.4571 ± 0.02545 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top 9dc85ee2-8596-4b62-bce3-be02224028e6 (×190) |
| site | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top source-provided coordinates when available (×190) |
| year | metadata | numeric | *Not specified.* | n=190, missing=0, range 2021–2021, mean 2021 ± 0 |
| date | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=190, missing=190, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Leaf (×190) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top leaf (×190) |
| instrument | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top spectral evolution SR-3500 (×190) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Contact (×190) |
| signal_type | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top reflectance (×190) |
| axis_unit | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top nm (×190) |
| axis_min | metadata | numeric | *Not specified.* | n=190, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=190, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=190, missing=0, range 2101–2101, mean 2101 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top 10.1016/j.rse.2023.113926 \| 10.21232/xYgn5GKv (×190) |
| citation | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Villa P., Dalla Vecchia A., Piaser E. and Bolpagni R.. 2020-2024. Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD). Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/xYgn5GKv (×190) |
| license | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top Creative Commons Non-Commercial (Any) (×190) |
| rights_status | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top explicit_restricted (×190) |
| usage_scope | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top private_use_only (×190) |
| notes | metadata | categorical | *Not specified.* | n=190, missing=0, classes=1, top EcoSIS package leaf-reflectance-and-traits-of-plants-sampled-along-a-water-affinity-gradient--aqgrad-, no interpolation applied by project. (×190) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-reflectance-and-traits-of-plants-sampled-along-a-water-affinity-gradient--aqgrad-`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Assessing PROSPECT performance on aquatic plant leaves — [10.1016/j.rse.2023.113926](https://doi.org/10.1016/j.rse.2023.113926)
- Leaf reflectance and traits of plants sampled along a water affinity gradient (AQGRAD) — [10.21232/xYgn5GKv](https://doi.org/10.21232/xYgn5GKv)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is restricted or non-commercial; public redistribution of derived X/Y/M is not cleared in this pass.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `4e72904f827f2fd8bdca4a595bf2e2b40a1f500a37792aacfbcfb8832e97394d`
- **Processing hash:** `a4a867673f2bcf2142bdf23d31c9c78716d8fd89c545b84997dce7b3938e478a` | **metadata hash:** `74cd785e3cf210b16c8620744a11c910e9cb6748bd39dce5ab4a425adde9949d`
