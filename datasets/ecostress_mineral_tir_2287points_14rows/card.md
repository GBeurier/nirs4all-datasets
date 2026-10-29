# Datasheet — ECOSTRESS mineral tir axis d3032c60

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis d3032c60. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 10 sample(s), 14 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.4).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 14 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=14, missing=0, classes=10, top Hornblende Ca2(Fe+2,Mg)4Al(Si7Al)O22(OH,F)2 (×2) |
| class_label | target | categorical | *Not specified.* | n=14, missing=0, classes=2, top Silicate (×13) |
| subclass | target | categorical | *Not specified.* | n=14, missing=0, classes=5, top Inosilicate (×5) |
| particle_size | target | categorical | *Not specified.* | n=14, missing=0, classes=3, top Coarse (×7) |
| measurement | target | categorical | *Not specified.* | n=14, missing=0, classes=2, top Bidirectional reflectance (×13) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=14, missing=0, classes=14, top mineral.silicate.inosilicate.coarse.tir.hornblen_2.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top mineral (×14) |
| material_type | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Mineral (×14) |
| site | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=14, missing=0, classes=10, top Calumet Island, Ottowa River, Canada via the Smithsaonian(sample no. NMNH 78662) (×2) |
| country | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top N/A (×14) |
| species | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=14, missing=0, classes=14, top Sample was a fragment of a black crystal, contaminated on one end with a clay coating and surficial quartz crystals, this surficial contamination was scraped off. There appeared to be a small amount of internal contamination by a fibrous mineral. Very few grains showed mild alteration, there was about 1% contamination by a low refractive index mineral with low birefringence. Particle size was 74-250 micrometers.(Amphibole Group) Original ASTER Spectral Library name was jhu.nicolet.mineral.silicate.inosilicate.coarse.hornbl2.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top jhu.nicolet (×14) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=14, missing=0, classes=2, top Bidirectional reflectance (×13) |
| signal_type | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Reflectance (percent) (×14) |
| axis_unit | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Wavelength (micrometers) (×14) |
| axis_min | metadata | numeric | *Not specified.* | n=14, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=14, missing=0, range 25.04–25.04, mean 25.04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=14, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×14) |
| citation | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×14) |
| license | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×14) |
| rights_status | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top manual_review_needed (×14) |
| usage_scope | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top private_use_only (×14) |
| notes | metadata | categorical | *Not specified.* | n=14, missing=0, classes=13, top None (×2) |

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
- **Curated views:** M: 2 fields, Y: 5 fields, measurements: 3 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `ba6c0c112abc4fa0f00fb055c9ba982f3870c6c694ed6659d2ecc0f16fc28fd4`
- **Processing hash:** `4b131d5a131b36a761687358a1ccab365331589676cdde402f2d33b6bb98c961` | **metadata hash:** `e5bae7458c862795f700b74ea7a717560e474046b7a17bdaae81831b6b8ce7bb`
