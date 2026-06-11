# Datasheet — ECOSTRESS mineral all axis adc9f614

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral all axis adc9f614. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 17 sample(s), 17 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral all | source instruments vary by sample | other | 0.4–13.9 none | 17 | 2752 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top Gaylussite Na2Ca(CO3)2 * 5H2O (×1) |
| class_label | target | categorical | *Not specified.* | n=17, missing=0, classes=4, top Borate (×8) |
| owner | target | categorical | *Not specified.* | n=17, missing=0, classes=2, top Smithsonian Institute, National Museum of Nat. History (×10) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top mineral.borate.none.coarse.all.nmnh102876-2.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top mineral (×17) |
| material_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Mineral (×17) |
| site | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=17, missing=0, classes=16, top Boron, California (×2) |
| country | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top Gaylussite powder from Searles Lake, CASample was Unsieved coarse powder. Original ASTER Spectral Library name was usgs.perknic.mineral.borate.none.coarse.gaylusc.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top usgs.perknic (×17) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Directional Hemispherical Reflectance (×17) |
| signal_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Reflectance (percent) (×17) |
| axis_unit | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Wavelength (micrometers) (×17) |
| axis_min | metadata | numeric | *Not specified.* | n=17, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=17, missing=0, range 13.9–13.9, mean 13.9 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=17, missing=0, range 2752–2752, mean 2752 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×17) |
| citation | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×17) |
| license | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×17) |
| rights_status | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top manual_review_needed (×17) |
| usage_scope | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top private_use_only (×17) |
| notes | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top none (×17) |

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
- **Content hash:** `8b0f2c9c705d1d8d74298c7c78f08e6a5fb6895544a2b406e5048b31faf572df`
- **Processing hash:** `0f15b7c3a56b7854631994a340bcbc8283bfcd9429e35721fc9814cf5debc704` | **metadata hash:** `d6d1ff28ca0b0410fc62cae8d87f9806f502f93dfc4fcfbdc12382f84af75b8b`
