# Datasheet — ECOSTRESS mineral vswir axis 158dfad5

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral vswir axis 158dfad5. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 160 sample(s), 430 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–3 (mean 2.688).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral vswir | source instruments vary by sample | other | 0.4–2.5 none | 430 | 826 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=160, missing=0, classes=142, top Quartz SiO_2 (×5) |
| class_label | target | categorical | *Not specified.* | n=160, missing=0, classes=12, top Silicate (×84) |
| subclass | target | categorical | *Not specified.* | n=160, missing=76, classes=6, top Phyllosilicate (×30) |
| particle_size | target | categorical | *Not specified.* | n=160, missing=0, classes=2, top Coarse (×135) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=160, missing=0, classes=160, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.beckman.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top mineral (×160) |
| material_type | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Mineral (×160) |
| site | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=160, missing=25, classes=116, top USA, California, Kern County, Boron (×5) |
| country | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=160, missing=160, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=160, missing=0, classes=160, top Particle size was 125-500um.Collected by JPL Original ASTER Spectral Library name was jpl.beckman.mineral.arsenate.none.coarse.a01.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top jpl.beckman (×160) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Hemispherical reflectance (×160) |
| signal_type | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Reflectance (percent) (×160) |
| axis_unit | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Wavelength (micrometers) (×160) |
| axis_min | metadata | numeric | *Not specified.* | n=160, missing=0, range 0.4–0.4, mean 0.4 ± 5.569e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=160, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=160, missing=0, range 826–826, mean 826 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×160) |
| citation | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×160) |
| license | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×160) |
| rights_status | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top manual_review_needed (×160) |
| usage_scope | metadata | categorical | *Not specified.* | n=160, missing=0, classes=1, top private_use_only (×160) |
| notes | metadata | categorical | *Not specified.* | n=160, missing=0, classes=160, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.beckman.ancillary.txt (×1) |

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
- **Content hash:** `7a76a97e5567091be0365043c80a1aae2beb4576ddce4a1f5eeb120b1ec9d17a`
- **Processing hash:** `a8d8ec8e0f3e136815eb663374e8023959ce5ab4d3ed6526d9c70605fc1da811` | **metadata hash:** `a991443a2f9c282063d844787edee133ef4124f2b1446df37dc7c2f27ade2ec5`
