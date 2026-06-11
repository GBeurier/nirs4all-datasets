# Datasheet — EcoSIS Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA) (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA) (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA)

## Composition

- **Alignment:** observation level; 48 sample(s), 962 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 12–37 (mean 20.04).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | all_data.csv | ASD FieldSpec 4 | NIR | 350–2500 nm | 962 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| spec_id | target | categorical | *Not specified.* | n=48, missing=0, classes=48, top 20250710_00000 (×1) |
| species_binom | target | categorical | *Not specified.* | n=48, missing=0, classes=13, top eucalyptus sideroxylon (×6) |
| lwp_MPa | target | numeric | *Not specified.* | n=48, missing=0, range 0.05–1.35, mean 0.3617 ± 0.293 |
| lwa_g/cm2 | target | numeric | *Not specified.* | n=48, missing=0, range 0.008297–0.02914, mean 0.01844 ± 0.005433 |
| lma_g/cm2 | target | numeric | *Not specified.* | n=48, missing=0, range 0.005555–0.03143, mean 0.0145 ± 0.005674 |
| tlp_MPa | target | numeric | *Not specified.* | n=48, missing=0, range -4.43–-1.827, mean -2.615 ± 0.6716 |
| capacitance_g/cm2/MPa | target | numeric | *Not specified.* | n=48, missing=0, range 0.0006894–0.003741, mean 0.001979 ± 0.0008349 |
| genus | target | categorical | *Not specified.* | n=48, missing=0, classes=10, top eucalyptus (×12) |
| species | target | categorical | *Not specified.* | n=48, missing=0, classes=13, top sideroxylon (×6) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top 558572a9-2fd0-40f2-b8e4-21215412931f (×48) |
| site | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Santa Barbara CA (×48) |
| country | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top source-provided coordinates when available (×48) |
| year | metadata | numeric | *Not specified.* | n=48, missing=0, range 2025–2025, mean 2025 ± 0 |
| date | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Leaf (×48) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top leaf (×48) |
| instrument | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top ASD FieldSpec 4 (×48) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Contact (×48) |
| signal_type | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top reflectance (×48) |
| axis_unit | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top nm (×48) |
| axis_min | metadata | numeric | *Not specified.* | n=48, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=48, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=48, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top 10.21232/egGyynzX (×48) |
| citation | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Jean Allen, Leander D. L. Anderegg, Dar Roberts and Anna T. Trugman. 2025. Tabletop leaf drydowns to relate leaf spectra and leaf water (Santa Barbara, CA). Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/egGyynzX (×48) |
| license | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Open Data Commons Public Domain Dedication and License (PDDL) (×48) |
| rights_status | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top explicit_open (×48) |
| usage_scope | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top public_reuse_possible (×48) |
| notes | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top EcoSIS package tabletop-leaf-drydowns-to-relate-leaf-spectra-and-leaf-water--santa-barbara--ca-, no interpolation applied by project. (×48) |

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

- **Conversion warnings:** *Not specified.*

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
- **Content hash:** `5ea82aa69477f56fa908f71c596b57aff44f4e99fd9aa8240768c37909779e4a`
- **Processing hash:** `f9819df85fe47ef75464e3ba15c57bcc8def6c228f060231bb9689b51c707a90` | **metadata hash:** `d5678147ffb1be4ee5d638b93b509e30ef6602ca52923afb4aeaa8ba45d7744e`
