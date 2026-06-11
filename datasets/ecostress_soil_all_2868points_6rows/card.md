# Datasheet — ECOSTRESS soil all axis d24e4e1f

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS soil all axis d24e4e1f. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 6 sample(s), 6 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | soil all | source instruments vary by sample | other | 0.4–14.98 none | 6 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=6, missing=0, classes=6, top Light yellowish brown loamy sand (×1) |
| class_label | target | categorical | *Not specified.* | n=6, missing=0, classes=2, top Aridisol (×4) |
| subclass | target | categorical | *Not specified.* | n=6, missing=0, classes=6, top Camborthid (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=6, missing=0, classes=6, top soil.aridisol.camborthid.none.all.89p1772.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top soil (×6) |
| material_type | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top soil (×6) |
| site | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=6, missing=0, classes=4, top Kit Carson Co., Co. via USDA Soil Conservation service. (×3) |
| country | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=6, missing=0, classes=6, top The parent material is alluvium material over eolian. Light yellowish brown loamy sand, (sandy, mixed, thermic typic camborthid). Original ASTER Spectral Library name was jhu.becknic.soil.aridisol.camborthid.coarse.89P1772.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top jhu.becknic (×6) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Directional (10 degree) hemispherical reflectance (×6) |
| signal_type | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Reflectance (percent) (×6) |
| axis_unit | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Wavelength (micrometers) (×6) |
| axis_min | metadata | numeric | *Not specified.* | n=6, missing=0, range 0.4–0.4, mean 0.4 ± 6.081e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=6, missing=0, range 14.98–14.98, mean 14.98 ± 1.946e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=6, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×6) |
| citation | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×6) |
| license | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×6) |
| rights_status | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top manual_review_needed (×6) |
| usage_scope | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top private_use_only (×6) |
| notes | metadata | categorical | *Not specified.* | n=6, missing=0, classes=6, top soil.aridisol.camborthid.none.all.89p1772.jhu.becknic.ancillary.txt (×1) |

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
- **Content hash:** `ac1a8eda9d86a68004ac92b1d7d303fc5af68d6075210bac515fdb962e7fc70a`
- **Processing hash:** `32ada4bcebc93a290cf49ffd74e498b8aaf544c05bbd0dd53808a3db44b4bff0` | **metadata hash:** `84b7353631465a38b832e9199643c02409bd645be3e188d398e042d93a40c0b5`
