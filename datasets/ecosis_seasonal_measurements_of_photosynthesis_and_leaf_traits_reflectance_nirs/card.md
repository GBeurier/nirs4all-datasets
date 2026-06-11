# Datasheet — EcoSIS Seasonal measurements of photosynthesis and leaf traits in scarlet oak (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Seasonal measurements of photosynthesis and leaf traits in scarlet oak (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 19 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Seasonal measurements of photosynthesis and leaf traits in scarlet oak

## Composition

- **Alignment:** observation level; 48 sample(s), 48 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | leaf_spectra.csv | Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i | NIR | 350–2500 nm | 48 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Tree_ID | target | categorical | *Not specified.* | n=48, missing=0, classes=6, top 1 (×8) |
| LMA | target | numeric | *Not specified.* | n=48, missing=0, range 57.8–135.3, mean 102.4 ± 16.88 |
| RWC | target | numeric | *Not specified.* | n=48, missing=6, range 43.33–63.65, mean 50.62 ± 5.401 |
| Nmass | target | numeric | *Not specified.* | n=48, missing=0, range 9.3–19, mean 15.45 ± 2.376 |
| Narea | target | numeric | *Not specified.* | n=48, missing=0, range 0.8091–2.336, mean 1.585 ± 0.3712 |
| ChlNDI | target | numeric | *Not specified.* | n=48, missing=0, range 0.2412–0.5833, mean 0.484 ± 0.07471 |
| PRI | target | numeric | *Not specified.* | n=48, missing=0, range -0.07352–0.07825, mean 0.03807 ± 0.03268 |
| Asat | target | numeric | *Not specified.* | n=48, missing=7, range 2.718–13.75, mean 7.475 ± 2.981 |
| gs | target | numeric | *Not specified.* | n=48, missing=7, range 0.02536–0.2139, mean 0.0911 ± 0.04436 |
| WUEi | target | numeric | *Not specified.* | n=48, missing=7, range 34.28–137.6, mean 89.86 ± 25.63 |
| CiCa | target | numeric | *Not specified.* | n=48, missing=13, range 0.4118–0.8392, mean 0.6119 ± 0.103 |
| Tleaf | target | numeric | *Not specified.* | n=48, missing=7, range 22–29.04, mean 25.47 ± 2.294 |
| VcmaxT | target | numeric | *Not specified.* | n=48, missing=7, range 12.13–93.78, mean 43.47 ± 16.39 |
| JmaxT | target | numeric | *Not specified.* | n=48, missing=10, range 33.48–139.6, mean 85.71 ± 23.54 |
| Vcmax25 | target | numeric | *Not specified.* | n=48, missing=7, range 14.59–69.89, mean 41.1 ± 14.04 |
| Jmax25 | target | numeric | *Not specified.* | n=48, missing=10, range 37.91–137.9, mean 83.61 ± 23.23 |
| NUE | target | numeric | *Not specified.* | n=48, missing=7, range 15.41–58.88, mean 27.52 ± 9.063 |
| Modelled_A | target | numeric | *Not specified.* | n=48, missing=10, range 2.577–15.87, mean 8.726 ± 3.57 |
| g1 | target | numeric | *Not specified.* | n=48, missing=7, range 2.485–5.458, mean 3.366 ± 0.9328 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top 944364af-9869-44ee-b857-377e397e89dc (×48) |
| site | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Brookhaven National Laboratory (×48) |
| country | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top source-provided coordinates when available (×48) |
| year | metadata | numeric | *Not specified.* | n=48, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=48, missing=0, classes=8, top 20190529 (×6) |
| species | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top QUCO2 (×48) |
| genus | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Leaf (×48) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top leaf (×48) |
| instrument | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Spectral Evolution, Spectra Vista Corporation PSR+, HR-1024i (×48) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Proximal (×48) |
| signal_type | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top reflectance (×48) |
| axis_unit | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top nm (×48) |
| axis_min | metadata | numeric | *Not specified.* | n=48, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=48, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=48, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top 10.1093/treephys/tpab015 \| 10.21232/ujBYNxhm (×48) |
| citation | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Angela C Burnett Shawn P Serbin Julien Lamour Jeremiah Anderson Kenneth J Davidson Dedi Yang Alistair Rogers. 2019. Seasonal measurements of photosynthesis and leaf traits in scarlet oak. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/ujBYNxhm (×48) |
| license | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Creative Commons Attribution (×48) |
| rights_status | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top explicit_open (×48) |
| usage_scope | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top public_reuse_possible (×48) |
| notes | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top EcoSIS package seasonal-measurements-of-photosynthesis-and-leaf-traits-in-scarlet-oak, no interpolation applied by project. (×48) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/seasonal-measurements-of-photosynthesis-and-leaf-traits-in-scarlet-oak`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Seasonal trends in photosynthesis and leaf traits in scarlet oak — [10.1093/treephys/tpab015](https://doi.org/10.1093/treephys/tpab015)
- Seasonal measurements of photosynthesis and leaf traits in scarlet oak — [10.21232/ujBYNxhm](https://doi.org/10.21232/ujBYNxhm)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `1d21750ad05dabddc861935af745a0f2f10dc0564b739cd44d9bd1795ef8136a`
- **Processing hash:** `88d2e4a6317f5dc402587de50647bdd87ae6b60688255c22852ccc49aafa5e27` | **metadata hash:** `2032193bc486b4751be9a5a36dd0dbc293bc7bc77d27617b6a794df6cee8ddb2`
