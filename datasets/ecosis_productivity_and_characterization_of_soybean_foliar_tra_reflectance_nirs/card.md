# Datasheet — Soybean leaves — aphid pressure, reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Productivity and Characterization of Soybean Foliar Traits Under Aphid Pressure (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Productivity and Characterization of Soybean Foliar Traits Under Aphid Pressure

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 1131 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | UW_Greenhouse_Soy_Spectra_noWAVE-2.csv | Analytical Spectral Devices FieldSpec4 | NIR | 350–2500 nm | 1131 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| SAMP_ID | target | categorical | *Not specified.* | n=1131, missing=0, classes=1131, top 1 (×1) |
| pct_CARBON | target | numeric | *Not specified.* | n=1131, missing=0, range 41.66–45.68, mean 43.72 ± 0.6674 |
| pct_CELLULOSE | target | numeric | *Not specified.* | n=1131, missing=0, range 7.345–19.77, mean 13.64 ± 2.098 |
| pct_NITROGEN | target | numeric | *Not specified.* | n=1131, missing=0, range 2.035–5.718, mean 3.594 ± 0.628 |
| pct_FIBER | target | numeric | *Not specified.* | n=1131, missing=0, range 30.79–60.24, mean 43.27 ± 5.429 |
| gmm2_LMA | target | numeric | *Not specified.* | n=1131, missing=0, range -9.172–74.1, mean 31.54 ± 16.33 |
| pct_LIGNIN | target | numeric | *Not specified.* | n=1131, missing=0, range 15.31–42.51, mean 27.06 ± 4.972 |
| CHL_a | target | numeric | *Not specified.* | n=1131, missing=0, range 3.411–34.22, mean 16.31 ± 7.488 |
| CHL_b | target | numeric | *Not specified.* | n=1131, missing=0, range 4.639–18.53, mean 7.905 ± 1.54 |
| CAROTENOIDS | target | numeric | *Not specified.* | n=1131, missing=0, range 1.528–11.06, mean 7.582 ± 1.24 |
| MM | target | numeric | *Not specified.* | n=1131, missing=0, range 7–8, mean 7.429 ± 0.4951 |
| DD | target | numeric | *Not specified.* | n=1131, missing=0, range 2–31, mean 14.72 ± 7.846 |
| PLANT | target | numeric | *Not specified.* | n=1131, missing=0, range 1–42, mean 20.91 ± 12.65 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top 45af66fa-7a19-4c29-b52d-733b8fc433ff (×1131) |
| site | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Walnut Street Greenhouses (×1131) |
| country | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1131, missing=0, range 43.08–43.08, mean 43.08 ± 7.109e-15 |
| longitude | metadata | numeric | *Not specified.* | n=1131, missing=0, range -89.42–-89.42, mean -89.42 ± 1.422e-14 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top source-provided coordinates when available (×1131) |
| year | metadata | numeric | *Not specified.* | n=1131, missing=0, range 2013–2013, mean 2013 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=22, top 7082013 (×82) |
| species | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Glycine max (×1131) |
| genus | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Leaf (×1131) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Analytical Spectral Devices FieldSpec4 (×1131) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Contact (×1131) |
| signal_type | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top reflectance (×1131) |
| axis_unit | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top nm (×1131) |
| axis_min | metadata | numeric | *Not specified.* | n=1131, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1131, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1131, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1131, missing=1131, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Aditya Singh. 2013. Productivity and Characterization of Soybean Foliar Traits Under Aphid Pressure. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1131) |
| license | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Creative Commons Attribution (×1131) |
| rights_status | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top explicit_open (×1131) |
| usage_scope | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top public_reuse_possible (×1131) |
| notes | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top EcoSIS package productivity-and-characterization-of-soybean-foliar-traits-under-aphid-pressure, no interpolation applied by project. (×1131) |
| source_SPECIES | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Glycine max (×1131) |
| source_DATAFROM | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Greenhouse (×1131) |
| source_INSTRUMENT | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top ASD FieldSpec 4 (×1131) |
| source_LATITUDE | metadata | numeric | *Not specified.* | n=1131, missing=0, range 43.08–43.08, mean 43.08 ± 7.109e-15 |
| source_LONGITUDE | metadata | numeric | *Not specified.* | n=1131, missing=0, range -89.42–-89.42, mean -89.42 ± 1.422e-14 |
| source_CITY | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Madison (×1131) |
| source_STATE | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=1, top Wisconsin (×1131) |
| source_DATE | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=22, top 7082013 (×82) |
| source_YYYY | metadata | numeric | *Not specified.* | n=1131, missing=0, range 2013–2013, mean 2013 ± 0 |
| source_TREAT | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=5, top H (×288) |
| source_STAGE | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=2, top R (×572) |
| source_REP | metadata | numeric | *Not specified.* | n=1131, missing=0, range 1–6, mean 3.057 ± 1.443 |
| source_LEAF_HEIGHT | metadata | categorical | *Not specified.* | n=1131, missing=0, classes=2, top U (×570) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/productivity-and-characterization-of-soybean-foliar-traits-under-aphid-pressure`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M. Index fields examined: source_REP. The number of levels of a Rep factor is not used as the number of spectra per sample.
- **Curated views:** M: 4 fields, Y: 12 fields, measurements: 0 fields, passport: 36 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `ced215a74dd21bd182e866caa2289c87cb49cf05052872704bf6119e934b2bf4`
- **Processing hash:** `ac68f57ab9b5982c0a424956d32fabac6ac0ddb7fe91ce1b019cb04432f231a8` | **metadata hash:** `5d6e1932654dafc7585350b72f3fa430b3b023aa8ee71f119e5b152d25dca918`
