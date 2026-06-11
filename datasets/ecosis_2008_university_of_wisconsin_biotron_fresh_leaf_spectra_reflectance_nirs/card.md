# Datasheet — EcoSIS 2008 University of Wisconsin Biotron Fresh Leaf Spectra and Gas Exchange Leaf Traits (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 2008 University of Wisconsin Biotron Fresh Leaf Spectra and Gas Exchange Leaf Traits (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 2008 University of Wisconsin Biotron Fresh Leaf Spectra and Gas Exchange Leaf Traits

## Composition

- **Alignment:** observation level; 87 sample(s), 87 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW_Biotron_2008_Compiled_Refl_Spectra.csv | Analytical Spectral Devices ASD FieldSpec 3 | NIR | 350–2500 nm | 87 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| USDA_Species_Code | target | categorical | *Not specified.* | n=87, missing=0, classes=2, top PODE3 (×50) |
| Geo_Species_Info | target | categorical | *Not specified.* | n=87, missing=0, classes=5, top WCW (×45) |
| House_Num | target | numeric | *Not specified.* | n=87, missing=0, range 1–6, mean 3.586 ± 1.702 |
| Plant_Number | target | categorical | *Not specified.* | n=87, missing=0, classes=46, top 32 (×5) |
| LI6400_Measurement_Temperature_degC | target | numeric | *Not specified.* | n=87, missing=33, range 20.39–30.95, mean 25.86 ± 3.842 |
| PLSR_Leaf_Temp_degC | target | numeric | *Not specified.* | n=87, missing=0, range 17.47–32.47, mean 24.54 ± 3.701 |
| Ev | target | numeric | *Not specified.* | n=87, missing=0, range 49.43–61.33, mean 54.49 ± 5.917 |
| Nmass_percent | target | numeric | *Not specified.* | n=87, missing=33, range 2.031–4.864, mean 3.74 ± 0.6633 |
| SLA | target | numeric | *Not specified.* | n=87, missing=33, range 13.13–42.14, mean 22.52 ± 5.87 |
| LMA_gDW_m2 | target | numeric | *Not specified.* | n=87, missing=33, range 23.73–76.14, mean 47.19 ± 11.63 |
| Narea | target | numeric | *Not specified.* | n=87, missing=33, range 0.8434–2.903, mean 1.767 ± 0.5612 |
| Vcmax_LI6400_Temperature | target | numeric | *Not specified.* | n=87, missing=37, range 38.88–169.2, mean 102.3 ± 36.18 |
| Vcmax_PLSR_Temperature | target | numeric | *Not specified.* | n=87, missing=37, range 44.6–163.5, mean 92.28 ± 26.14 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top 022f5676-004a-40ca-9494-2296d06b4c51 (×87) |
| site | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top source-provided coordinates when available (×87) |
| year | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=87, missing=0, classes=4, top 9/29/08 (×26) |
| species | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=87, missing=87, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top Leaf (×87) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top leaf (×87) |
| instrument | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top Analytical Spectral Devices ASD FieldSpec 3 (×87) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top Contact (×87) |
| signal_type | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top reflectance (×87) |
| axis_unit | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top nm (×87) |
| axis_min | metadata | numeric | *Not specified.* | n=87, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=87, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=87, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top 10.1016/j.rse.2023.113926 \| 10.1093/jxb/err294 \| 10.1186/s13007-021-00816-4 \| 10.21232/44vxhorw \| 10.21232/C22M27 \| 10.21232/c22m27 \| 10.21232/dep7jvyq (×87) |
| citation | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top Shawn P Serbin Dylan N Dillaway Eric L Kruger Philip A Townsend. 2008 University of Wisconsin Biotron Fresh Leaf Spectra and Gas Exchange Leaf Traits. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). doi:10.21232/C22M27 (×87) |
| license | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×87) |
| rights_status | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top explicit_open (×87) |
| usage_scope | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top public_reuse_possible (×87) |
| notes | metadata | categorical | *Not specified.* | n=87, missing=0, classes=1, top EcoSIS package 2008-university-of-wisconsin-biotron-fresh-leaf-spectra-and-gas-exchange-leaf-traits, no interpolation applied by project. (×87) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2008-university-of-wisconsin-biotron-fresh-leaf-spectra-and-gas-exchange-leaf-traits`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Serbin et al (2012) — [10.1093/jxb/err294](https://doi.org/10.1093/jxb/err294)
- 2008 University of Wisconsin Biotron Fresh Leaf Spectra and Gas Exchange Leaf Traits — [10.21232/C22M27](https://doi.org/10.21232/C22M27)
- *Not specified.* — [10.1016/j.rse.2023.113926](https://doi.org/10.1016/j.rse.2023.113926)
- *Not specified.* — [10.1186/s13007-021-00816-4](https://doi.org/10.1186/s13007-021-00816-4)
- *Not specified.* — [10.21232/44vxhorw](https://doi.org/10.21232/44vxhorw)
- *Not specified.* — [10.21232/c22m27](https://doi.org/10.21232/c22m27)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** ODbL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `bde3277a25b22e3c9355aeb7252e445b008975119674abcab97358ed9b8ccf87`
- **Processing hash:** `081276bfd0d650100e8090c7cfe5a7f63e424ec4da90420c01ddd874321b8a8c` | **metadata hash:** `6203418a359eb53395d6f78c2b95ff855ea66c6f76c92d37ea346762557d7dbd`
