# Datasheet — Perten cereals NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** perten
- **Description:** Perten cereals NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, perten
- **Contributor:** 1) sensAIfood cereal NIR data (wheat, corn, barley) and reference protein and moisture (Perten set)

## Composition

- **Alignment:** sample level; 450 sample(s), 450 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Perten NIR spectra | Perten DA7200/DA72xx/DA7440/DA7250/DA7300, as available by sample | NIR | 950–1650 nm | 450 | 141 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Moisture | target | numeric | *Not specified.* | n=450, missing=0, range 6.37–31.82, mean 13.07 ± 3.481 |
| Protein | target | numeric | *Not specified.* | n=450, missing=0, range 6.397–20.29, mean 11.58 ± 2.54 |
| cereal_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=3, top barley (×150) |
| crop | metadata | categorical | *Not specified.* | n=450, missing=0, classes=3, top barley (×150) |
| product_type | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top whole grain (×450) |
| target_set | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top moisture_and_protein (×450) |
| original_row_id | metadata | categorical | *Not specified.* | n=450, missing=0, classes=150, top 1 (×3) |
| instrument | metadata | categorical | *Not specified.* | n=450, missing=9, classes=5, top Perten_DA7200 (×396) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top diffuse reflectance (post-dispersive) (×450) |
| wavelength_unit | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top nm (×450) |
| country | metadata | categorical | *Not specified.* | n=450, missing=51, classes=12, top US (×98) |
| year | metadata | numeric | *Not specified.* | n=450, missing=57, range 2002–2017, mean 2008 ± 3.037 |
| variety | metadata | categorical | *Not specified.* | n=450, missing=300, classes=3, top Wheat (×99) |
| notes | metadata | categorical | *Not specified.* | n=450, missing=0, classes=1, top 0 values in source metadata treated as unknown/missing where applicable (×450) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/15838136`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/15838136/files/sensAIfood_Perten.zip/content`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `10.5281/zenodo.15838136`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 6 fields, Y: 2 fields, measurements: 0 fields, passport: 11 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Zenodo API metadata license id cc-by-4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `95e42a1e6cc14978ddc50d30e3fd6ea8b1ef159d6e0fe1b317ac4110056875cb`
- **Processing hash:** `b466d3f05a14daea8fef7eda4d7eb845a12d291e79c193b95cbad55cdb24b80e` | **metadata hash:** `8ef246692d4f8ff0c6b0f3c1a08d4793a14b05a366b32173ff9ac8871904dc0b`
