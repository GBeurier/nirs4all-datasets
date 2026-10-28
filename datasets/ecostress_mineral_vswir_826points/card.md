# Datasheet — ECOSTRESS mineral vswir axis 158dfad5

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral vswir axis 158dfad5. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 430 sample(s), 430 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral vswir | source instruments vary by sample | other | 0.4–2.5 none | 430 | 826 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=430, missing=0, classes=143, top Quartz SiO_2 (×15) |
| class_label | target | categorical | *Not specified.* | n=430, missing=0, classes=12, top Silicate (×216) |
| subclass | target | categorical | *Not specified.* | n=430, missing=214, classes=6, top Phyllosilicate (×70) |
| particle_size | target | categorical | *Not specified.* | n=430, missing=0, classes=3, top Fine (×160) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=430, missing=0, classes=430, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.beckman.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top mineral (×430) |
| material_type | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Mineral (×430) |
| site | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=430, missing=57, classes=116, top USA, California, Kern County, Boron (×15) |
| country | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=430, missing=430, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=430, missing=0, classes=430, top Particle size was 125-500um.Collected by JPL Original ASTER Spectral Library name was jpl.beckman.mineral.arsenate.none.coarse.a01.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top jpl.beckman (×430) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Hemispherical reflectance (×430) |
| signal_type | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Reflectance (percent) (×430) |
| axis_unit | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Wavelength (micrometers) (×430) |
| axis_min | metadata | numeric | *Not specified.* | n=430, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=430, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=430, missing=0, range 826–826, mean 826 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×430) |
| citation | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×430) |
| license | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×430) |
| rights_status | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top manual_review_needed (×430) |
| usage_scope | metadata | categorical | *Not specified.* | n=430, missing=0, classes=1, top private_use_only (×430) |
| notes | metadata | categorical | *Not specified.* | n=430, missing=9, classes=421, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.beckman.ancillary.txt (×1) |
| original_sample_id | metadata | categorical | *Not specified.* | n=430, missing=0, classes=160, top A-1A (×3) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Observation identity is used as the canonical join key because source sample_id has differing per-observation values in ecostress_resource_id, sample_description, notes, material_name, particle_size. The original physical-sample key is preserved as metadata 'original_sample_id'; sample grouping must use that field.

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
- **Content hash:** `468ee75052cb92f0abdd0a5f76614392bec0fad26721c05972f098096ae7db69`
- **Processing hash:** `3857be766c2d0c3608fc962c026e692441027c11836d95cbf2d26ed597156747` | **metadata hash:** `b12899284a1821888ef72d63621f387db314e33578933c3bbbdb7c1abdf885d4`
