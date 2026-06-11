# Datasheet — ECOSTRESS mineral vswir axis 61f98690

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral vswir axis 61f98690. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 148 sample(s), 406 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–3 (mean 2.743).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral vswir | source instruments vary by sample | other | 0.4–2.5 none | 406 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=148, missing=0, classes=130, top Quartz SiO_2 (×5) |
| class_label | target | categorical | *Not specified.* | n=148, missing=0, classes=12, top Silicate (×76) |
| subclass | target | categorical | *Not specified.* | n=148, missing=66, classes=7, top Phyllosilicate (×29) |
| particle_size | target | categorical | *Not specified.* | n=148, missing=0, classes=2, top Coarse (×129) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=148, missing=0, classes=148, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.perkin.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top mineral (×148) |
| material_type | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Mineral (×148) |
| site | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=148, missing=0, classes=113, top Unknown. (×14) |
| country | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=148, missing=148, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=148, missing=0, classes=148, top Particle size was 125-500um.Collected by: JPL Original ASTER Spectral Library name was jpl.perkin.mineral.arsenate.none.coarse.a01a.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top jpl.perkin (×148) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Hemispherical reflectance (×148) |
| signal_type | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Reflectance (percent) (×148) |
| axis_unit | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Wavelength (micrometers) (×148) |
| axis_min | metadata | numeric | *Not specified.* | n=148, missing=0, range 0.4–0.4, mean 0.4 ± 1.114e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=148, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=148, missing=0, range 2101–2101, mean 2101 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×148) |
| citation | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×148) |
| license | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×148) |
| rights_status | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top manual_review_needed (×148) |
| usage_scope | metadata | categorical | *Not specified.* | n=148, missing=0, classes=1, top private_use_only (×148) |
| notes | metadata | categorical | *Not specified.* | n=148, missing=0, classes=148, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.perkin.ancillary.txt (×1) |

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
- **Content hash:** `b19bd74826c3bc1ff63ce2ea1ed34d1b54cd06c910a9ac0ba8c2fdc115224cf5`
- **Processing hash:** `ca8751e24cb863656c1fccb42f68201efce69f4069ba0ecd815fb1048b0f88b0` | **metadata hash:** `dd4cc50dba2dd3baf2072cf481f3dd8a851dc03bd679430d1bfbce84581c0074`
