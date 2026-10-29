# Datasheet — EcoSIS FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 138 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | spectra.csv | Spectral Evolution PSR+ 3500 | NIR | 350–2500 nm | 138 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| SpeciesCode | target | categorical | *Not specified.* | n=138, missing=0, classes=8, top QUMA (×18) |
| Genus | target | categorical | *Not specified.* | n=138, missing=0, classes=4, top Quercus (×72) |
| Species | target | categorical | *Not specified.* | n=138, missing=0, classes=8, top macrocarpa (×18) |
| Treatment | target | categorical | *Not specified.* | n=138, missing=0, classes=3, top Monoculture (×48) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top a3b4c504-c975-423c-9abb-0a8075cefc85 (×138) |
| site | metadata | numeric | *Not specified.* | n=138, missing=0, range 7–147, mean 71.07 ± 43.8 |
| location | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Cedar Creek LTER (×138) |
| country | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top source-provided coordinates when available (×138) |
| year | metadata | numeric | *Not specified.* | n=138, missing=0, range 2018–2018, mean 2018 ± 0 |
| date | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=138, missing=0, classes=8, top macrocarpa (×18) |
| genus | metadata | categorical | *Not specified.* | n=138, missing=0, classes=4, top Quercus (×72) |
| family | metadata | categorical | *Not specified.* | n=138, missing=138, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Leaf (×138) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top leaf (×138) |
| instrument | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×138) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Contact (×138) |
| signal_type | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top reflectance (×138) |
| axis_unit | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top nm (×138) |
| axis_min | metadata | numeric | *Not specified.* | n=138, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=138, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=138, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top 10.1101/845701 \| 10.21232/FR7US97g (×138) |
| citation | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Shan Kothari, Rebecca Montgomery and Jeannine Cavender-Bares. 2018. FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/FR7US97g (×138) |
| license | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top Creative Commons Attribution (×138) |
| rights_status | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top explicit_open (×138) |
| usage_scope | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top public_reuse_possible (×138) |
| notes | metadata | categorical | *Not specified.* | n=138, missing=0, classes=1, top EcoSIS package fab-leaf-spectra-across-a-light-gradient-at-cedar-creek-lter, no interpolation applied by project. (×138) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fab-leaf-spectra-across-a-light-gradient-at-cedar-creek-lter`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 5 fields, Y: 4 fields, measurements: 0 fields, passport: 30 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Physiological responses to light explain competition and facilitation in a tree diversity experiment — [10.1101/845701](https://doi.org/10.1101/845701)
- FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER — [10.21232/FR7US97g](https://doi.org/10.21232/FR7US97g)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f231b2c4cff7bd73d521875833cc71f1f82c62362cc34178feeb8c936cff776d`
- **Processing hash:** `2d079f5eb0af8c3431c4a106b2252b0fad710a4bbdaa49b7759069fcc396d9b8` | **metadata hash:** `5a79e2d352b04c02a807bcd7be164b7039f167320a1edf81d25daa3fef80f202`
