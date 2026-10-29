# Datasheet — ECOSTRESS mineral tir axis 02866850

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 02866850. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 125 sample(s), 207 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–4 (mean 1.656).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 207 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=207, missing=0, classes=101, top Olivine (Fo92) (Fe+2,Mg)2SiO4 (×7) |
| class_label | target | categorical | *Not specified.* | n=207, missing=0, classes=7, top Silicate (×165) |
| subclass | target | categorical | *Not specified.* | n=207, missing=0, classes=8, top None (×43) |
| particle_size | target | categorical | *Not specified.* | n=207, missing=0, classes=4, top Coarse (×121) |
| measurement | target | categorical | *Not specified.* | n=207, missing=0, classes=3, top Bidirectional reflectance (×199) |
| owner | target | categorical | *Not specified.* | n=207, missing=0, classes=2, top JHU (×205) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=207, missing=0, classes=207, top mineral.carbonate.none.coarse.tir.aragonite_1.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top mineral (×207) |
| material_type | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top Mineral (×207) |
| site | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=207, missing=0, classes=126, top Donated by Bruce Hemingway, Sample from Prince of WalesIsland, Alaska. (×3) |
| country | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top N/A (×207) |
| species | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=207, missing=207, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=207, missing=0, classes=207, top The sample was composed of two transparent, colorless pieces: one prismatic, 1.8 cm x 1.8 cm x 2 cm, and weighing about 2 g, the other a 5 mm x 5 mm x 5 mm cleavage fragment weighing 0.65 g. No impurities were detected in hand sample or microscopically. Particle size was 74-250 Micrometers. Original ASTER Spectral Library name was jhu.nicolet.mineral.carbonate.none.coarse.aragon1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top jhu.nicolet (×207) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=207, missing=0, classes=3, top Bidirectional reflectance (×199) |
| signal_type | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top Reflectance (percent) (×207) |
| axis_unit | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top Wavelength (micrometers) (×207) |
| axis_min | metadata | numeric | *Not specified.* | n=207, missing=0, range 2.079–2.079, mean 2.079 ± 4.452e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=207, missing=0, range 25.04–25.04, mean 25.04 ± 1.068e-14 |
| n_points_original | metadata | numeric | *Not specified.* | n=207, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×207) |
| citation | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×207) |
| license | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×207) |
| rights_status | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top manual_review_needed (×207) |
| usage_scope | metadata | categorical | *Not specified.* | n=207, missing=0, classes=1, top private_use_only (×207) |
| notes | metadata | categorical | *Not specified.* | n=207, missing=0, classes=160, top None (×31) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques. La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 2 fields, Y: 5 fields, passport: 50 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- The ECOSTRESS spectral library version 1.0 — [10.1016/j.rse.2019.05.015](https://doi.org/10.1016/j.rse.2019.05.015)
- The ASTER Spectral Library Version 2.0 — [10.1016/j.rse.2008.11.007](https://doi.org/10.1016/j.rse.2008.11.007)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Official ECOSTRESS page requests citation and states copyright/all rights reserved; converted matrices are private/internal until redistribution rights are clarified.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `6f3fc094c94c845ff867206a2e8d59813563f919ffdaa3012b757e119a8875d9`
- **Processing hash:** `954ecae2a4301945507d957fde7f0f06b7be62a72003e6b98e9b5c8748a4a488` | **metadata hash:** `b55557cd7ab3998b790a6f2da6188b2a1c51e5ec31caeddeebf45e0581b08028`
