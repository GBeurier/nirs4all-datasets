# Datasheet — ECOSTRESS rock tir axis 16aa20e0

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock tir axis 16aa20e0. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 5 sample(s), 5 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock tir | source instruments vary by sample | other | 2.079–14.98 none | 5 | 2148 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=5, missing=0, classes=5, top Grey-green phyllite (×1) |
| class_label | target | categorical | *Not specified.* | n=5, missing=0, classes=2, top Sedimentary (×4) |
| subclass | target | categorical | *Not specified.* | n=5, missing=0, classes=4, top Arenaceou (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top rock.metamorphic.phyllite.solid.tir.fge4.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top rock (×5) |
| material_type | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top rock (×5) |
| site | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=5, missing=0, classes=4, top Nundooka Sandstone, Fowlers Gap, western New South Wales, AustraliaHewson(1998) PhD thesis (×2) |
| country | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top N/A (×5) |
| species | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top Chlorite/muscovite-rich phyllite Greenschist facies Physiography: Exposed in low relief valleys as abundant scree and weathered outcrops Original ASTER Spectral Library name was jpl.nicolet.rock.metamorphic.phyllite.solid.fge4.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top jpl.nicolet (×5) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Directional hemispherical reflectance (×5) |
| signal_type | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Reflectance (percent) (×5) |
| axis_unit | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Wavelength (micrometers) (×5) |
| axis_min | metadata | numeric | *Not specified.* | n=5, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=5, missing=0, range 14.98–14.98, mean 14.98 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=5, missing=0, range 2148–2148, mean 2148 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×5) |
| citation | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×5) |
| license | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×5) |
| rights_status | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top manual_review_needed (×5) |
| usage_scope | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top private_use_only (×5) |
| notes | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top rock.metamorphic.phyllite.solid.tir.fge4.jpl.nicolet.ancillary.txt (×1) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 1 fields, Y: 3 fields, passport: 49 fields, measurements: 4 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `f938cccab059e34380ca43cceeca35cb78b9dead579741071ba5e35c287d77f5`
- **Processing hash:** `748741a529801a744b3f4eec8e19f6297ae12ba1e0ca99cb9a5c95b640a9ef2d` | **metadata hash:** `9517f6bdba88efb7181206b84f49bcead3c4bc6841469376d30ae2d6e6a7d425`
