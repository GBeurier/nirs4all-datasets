# Datasheet — ECOSTRESS mineral tir axis d3032c60

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis d3032c60. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 10 sample(s), 14 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.4).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 14 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=10, missing=0, classes=10, top Hornblende Ca2(Fe2+,Mg)4Al(Si7,Al)O22(OH,F)2 (×1) |
| class_label | target | categorical | *Not specified.* | n=10, missing=0, classes=2, top Silicate (×9) |
| subclass | target | categorical | *Not specified.* | n=10, missing=1, classes=4, top Inosilicate (×4) |
| particle_size | target | categorical | *Not specified.* | n=10, missing=0, classes=2, top Coarse (×7) |
| measurement | target | categorical | *Not specified.* | n=10, missing=0, classes=2, top Bidirectional reflectance (×9) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top mineral.silicate.inosilicate.coarse.tir.hornblen_2.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top mineral (×10) |
| material_type | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Mineral (×10) |
| site | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Kragero, Norway via the Smithsonian (sample no. NMNH117329). (×1) |
| country | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Sample was a fragment of a black crystal, contaminated on one end with a clay coating and surficial quartz crystals, this surficial contamination was scraped off. There appeared to be a small amount of internal contamination by a fibrous mineral. Very few grains showed mild alteration, there was about 1% contamination by a low refractive index mineral with low birefringence. Particle size was 74-250 micrometers.(Amphibole Group) Original ASTER Spectral Library name was jhu.nicolet.mineral.silicate.inosilicate.coarse.hornbl2.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top jhu.nicolet (×10) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=10, missing=0, classes=2, top Bidirectional reflectance (×9) |
| signal_type | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Reflectance (percent) (×10) |
| axis_unit | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Wavelength (micrometers) (×10) |
| axis_min | metadata | numeric | *Not specified.* | n=10, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=10, missing=0, range 25.04–25.04, mean 25.04 ± 3.745e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=10, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×10) |
| citation | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×10) |
| license | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×10) |
| rights_status | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top manual_review_needed (×10) |
| usage_scope | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top private_use_only (×10) |
| notes | metadata | categorical | *Not specified.* | n=10, missing=1, classes=9, top mineral.silicate.inosilicate.coarse.tir.hornblen_2.jhu.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `5e9d58a30a827a436233f13f6c55cc3d6a2c7db7b50b065631344e8a7d9da99c`
- **Processing hash:** `fd91c764ae7fd9971d357435aceac3ea6f35b05e2716ffd5af3bae0ee7230a43` | **metadata hash:** `b8fa20fc5778170c11d78de60d27e32a78b675b72c68cf3c49588284c580f6d4`
