# Datasheet — FLOPP FTIR polymer classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** plastic
- **Description:** FLOPP FTIR polymer classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, plastic
- **Contributor:** ATR-FTIR Spectral Libraries of Plastic Particles, FLOPP and FLOPP-e

## Composition

- **Alignment:** sample level; 186 sample(s), 186 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | FLOPP FTIR spectra | ATR-FTIR instruments as represented in source library | MIR | 399.2–4002 cm-1 | 186 | 1869 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| polymer_name | target | categorical | *Not specified.* | n=186, missing=0, classes=17, top PP (×19) |
| library_name | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top FLOPP (×186) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top FTIR (×186) |
| sample_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top plastic particle (×186) |
| sample_description | metadata | categorical | *Not specified.* | n=186, missing=1, classes=162, top White Fiber (×6) |
| axis_unit | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top cm^-1 (×186) |
| axis_min | metadata | numeric | *Not specified.* | n=186, missing=0, range 399.2–399.2, mean 399.2 ± 5.7e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=186, missing=0, range 4002–4002, mean 4002 ± 9.119e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=186, missing=0, range 1869–1869, mean 1869 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top ATR-FTIR intensity (×186) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): not_provided: 186

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://acs.figshare.com/articles/dataset/_ATR-FTIR_Spectral_Libraries_of_Plastic_Particles_FLOPP_and_FLOPP-e_for_the_Analysis_of_Microplastics/17070059`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/17070059`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://figshare.com/ndownloader/articles/17070059/versions/1`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.17070059`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 17 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.1021/acs.analchem.1c02549](https://doi.org/10.1021/acs.analchem.1c02549)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights are not cleared for public redistribution, internal/private use only by default.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `3bbcf2ca5612692229f87f5880bf53a49081392b4f958c3d85dc9dbb9fc6384c`
- **Processing hash:** `b1408bf92178b8330dcae093f9ac05f186c9ce2c4ffd4176c8468f618ca71333` | **metadata hash:** `6cca15983f10ca9e4aa0dbe2921f541c772d1222e3f96a5884fd893aac91756c`
