# Datasheet — EcoSIS Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA) (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA) (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA)

## Composition

- **Alignment:** observation level; 962 sample(s), 962 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | all_data.csv | ASD FieldSpec 4 | NIR | 350–2500 nm | 962 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| spec_id | target | categorical | *Not specified.* | n=962, missing=0, classes=955, top 20250925_00000 (×3) |
| species_binom | target | categorical | *Not specified.* | n=962, missing=0, classes=13, top heteromeles arbutifolia (×202) |
| lwp_MPa | target | numeric | *Not specified.* | n=962, missing=0, range 0.05–5.33, mean 1.994 ± 1.13 |
| lwa_g/cm2 | target | numeric | *Not specified.* | n=962, missing=0, range 0.006364–0.02914, mean 0.01756 ± 0.005154 |
| lma_g/cm2 | target | numeric | *Not specified.* | n=962, missing=0, range 0.005555–0.03143, mean 0.01564 ± 0.006195 |
| tlp_MPa | target | numeric | *Not specified.* | n=962, missing=0, range -4.43–-1.827, mean -2.743 ± 0.7626 |
| capacitance_g/cm2/MPa | target | numeric | *Not specified.* | n=962, missing=0, range 0.0006894–0.003741, mean 0.002104 ± 0.0008595 |
| genus | target | categorical | *Not specified.* | n=962, missing=0, classes=10, top eucalyptus (×254) |
| species | target | categorical | *Not specified.* | n=962, missing=0, classes=13, top arbutifolia (×202) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top 558572a9-2fd0-40f2-b8e4-21215412931f (×962) |
| site | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top Santa Barbara CA (×962) |
| country | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top source-provided coordinates when available (×962) |
| year | metadata | numeric | *Not specified.* | n=962, missing=0, range 2025–2025, mean 2025 ± 0 |
| date | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=962, missing=962, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top Leaf (×962) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top leaf (×962) |
| instrument | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top ASD FieldSpec 4 (×962) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top Contact (×962) |
| signal_type | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top reflectance (×962) |
| axis_unit | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top nm (×962) |
| axis_min | metadata | numeric | *Not specified.* | n=962, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=962, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=962, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top 10.21232/egGyynzX (×962) |
| citation | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top Jean Allen, Leander D. L. Anderegg, Dar Roberts and Anna T. Trugman. 2025. Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA). Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/egGyynzX (×962) |
| license | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top Open Data Commons Public Domain Dedication and License (PDDL) (×962) |
| rights_status | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top explicit_open (×962) |
| usage_scope | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top public_reuse_possible (×962) |
| notes | metadata | categorical | *Not specified.* | n=962, missing=0, classes=1, top EcoSIS package tabletop-leaf-drydowns-to-relate-leaf-spectra-and-leaf-water--santa-barbara--ca-, no interpolation applied by project. (×962) |
| original_sample_id | metadata | categorical | *Not specified.* | n=962, missing=0, classes=48, top hear_10 (×37) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/tabletop-leaf-drydowns-to-relate-leaf-spectra-and-leaf-water--santa-barbara--ca-`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Observation identity is used as the canonical join key because source sample_id has differing per-observation values in spec_id, lwp_MPa, lwa_g/cm2. The original physical-sample key is preserved as metadata 'original_sample_id'; sample grouping must use that field.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA) — [10.21232/egGyynzX](https://doi.org/10.21232/egGyynzX)

## Distribution

- **License:** PDDL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `00a6b8d05b24004aa0903c81015126dfb422e7272d142cf9166a5cbc5fcd0def`
- **Processing hash:** `7bef4236ed01f1b6a02fa855dca6d1470617604d2c17bd10a03f517de6d2bc9f` | **metadata hash:** `d6824a124054ad8dc9fc9b18d516b00506b88257a588aaa9a8cba3a0dd966886`
