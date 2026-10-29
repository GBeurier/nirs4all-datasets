# Datasheet — UCPH marzipan multi-instrument spectroscopy

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH marzipan multi-instrument spectroscopy. v2.0 standardized NIRS package: 6 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** Data sets for multi-variate data analysis - Marzipan

## Composition

- **Alignment:** sample level; 32 sample(s), 192 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | Infratec 1255 NIT | Infratec 1255 NIT | NIR | 850–1048 nm | 32 | 100 |
| X2 | NIRSystems 6500 sample cup reflection | NIRSystems 6500 sample cup reflection | NIR | 450–2448 nm | 32 | 1000 |
| X3 | NIRSystems 6500 fibre probe reflection | NIRSystems 6500 fibre probe reflection | NIR | 850–2048 nm | 32 | 600 |
| X4 | Infraprover II FT-NIR | Infraprover II FT-NIR | NIR | 1051–2148 nm | 32 | 406 |
| X5 | Bomem MB160 Diffusir FT-NIR | Bomem MB160 Diffusir FT-NIR | NIR | 850–2443 nm | 32 | 664 |
| X6 | IR spectroscopy | IR spectroscopy | MIR | 651–3799 cm-1 | 32 | 950 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| ref_sugar | target | numeric | *Not specified.* | n=32, missing=0, range 32.7–68.7, mean 46.25 ± 12.88 |
| ref_moisture | target | numeric | *Not specified.* | n=32, missing=0, range 6.8–18.6, mean 13.57 ± 3.664 |
| license | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top NOASSERTION (×32) |
| rights_status | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top manual_review_needed (×32) |
| usage_scope | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top internal_benchmark_only_until_license_review (×32) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top False (×32) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top multi_instrument_NIR_IR (×32) |
| notes | metadata | categorical | *Not specified.* | n=32, missing=0, classes=1, top Public UCPH/ERDA dataset, local readme does not state explicit redistribution license. (×32) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/AY8wS3D8Kn/Marzipan.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/datasets/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 2 fields, measurements: 0 fields, passport: 11 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** No explicit redistribution license found on checked UCPH/ERDA source.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f34af256236f54bf7d826f56cd6f28eaa50aae64f23062db0baa0043e8905dd8`
- **Processing hash:** `95cd7fd13b4bcb4e9c355820cd1b82be141d402d6a944f95f915dbf22ca6daa6` | **metadata hash:** `aacf25d59dd86e77358a8bcb0cd5f0cbaa7d798945636d5991d17407a457db68`
