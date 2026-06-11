# Datasheet — ECOSTRESS mineral tir axis 02866850

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 02866850. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 125 sample(s), 207 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–4 (mean 1.656).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 207 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=125, missing=0, classes=100, top Topaz Al2SiO4(F,OH)2 (×4) |
| class_label | target | categorical | *Not specified.* | n=125, missing=0, classes=7, top Silicate (×101) |
| subclass | target | categorical | *Not specified.* | n=125, missing=24, classes=7, top Nesosilicate (×27) |
| particle_size | target | categorical | *Not specified.* | n=125, missing=0, classes=2, top Coarse (×120) |
| measurement | target | categorical | *Not specified.* | n=125, missing=0, classes=3, top Bidirectional reflectance (×119) |
| owner | target | categorical | *Not specified.* | n=125, missing=0, classes=2, top JHU (×124) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=125, missing=0, classes=125, top mineral.carbonate.none.coarse.tir.aragonite_1.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top mineral (×125) |
| material_type | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top Mineral (×125) |
| site | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=125, missing=0, classes=124, top Ilmen Mountains, Urals, USSR via the Smithsonian (sample no.NMNH 96189) (×2) |
| country | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=125, missing=125, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=125, missing=0, classes=125, top The sample was composed of two transparent, colorless pieces: one prismatic, 1.8 cm x 1.8 cm x 2 cm, and weighing about 2 g, the other a 5 mm x 5 mm x 5 mm cleavage fragment weighing 0.65 g. No impurities were detected in hand sample or microscopically. Particle size was 74-250 Micrometers. Original ASTER Spectral Library name was jhu.nicolet.mineral.carbonate.none.coarse.aragon1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top jhu.nicolet (×125) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=125, missing=0, classes=3, top Bidirectional reflectance (×119) |
| signal_type | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top Reflectance (percent) (×125) |
| axis_unit | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top Wavelength (micrometers) (×125) |
| axis_min | metadata | numeric | *Not specified.* | n=125, missing=0, range 2.079–2.079, mean 2.079 ± 4.459e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=125, missing=0, range 25.04–25.04, mean 25.04 ± 1.427e-14 |
| n_points_original | metadata | numeric | *Not specified.* | n=125, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×125) |
| citation | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×125) |
| license | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×125) |
| rights_status | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top manual_review_needed (×125) |
| usage_scope | metadata | categorical | *Not specified.* | n=125, missing=0, classes=1, top private_use_only (×125) |
| notes | metadata | categorical | *Not specified.* | n=125, missing=21, classes=90, top none (×15) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `cb2ce0952d6b460cfd922d7a42e321bcf7755e6f6e9bf26c88dbf8c66a9c06d0`
- **Processing hash:** `1c77e388be66eba83251d0c1e7d3f8651b3b80805e3f8665eae164fa60e91fa1` | **metadata hash:** `1585d62466871de6a92d46cff2cfe77460d827db0c8d7b91b341a0ef4a9837ee`
