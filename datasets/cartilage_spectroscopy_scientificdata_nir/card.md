# Datasheet — Cartilage spectroscopy Scientific Data NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cartilage
- **Description:** Cartilage spectroscopy Scientific Data NIR. v2.0 standardized NIRS package: 1 spectral source(s), 12 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cartilage
- **Contributor:** Nature Scientific Data supplementary data

## Composition

- **Alignment:** sample level; 869 sample(s), 2605 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 2–3 (mean 2.998).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | cartilage_spectra | source_export | NIR | 700–1150 none | 2605 | 812 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| joint_id | target | categorical | *Not specified.* | n=869, missing=0, classes=5, top 2.0 (×206) |
| bone_type | target | categorical | *Not specified.* | n=869, missing=0, classes=2, top proximal_phalanx (×525) |
| cartilage_thickness | target | numeric | *Not specified.* | n=869, missing=0, range 0.32–1.81, mean 0.8878 ± 0.2384 |
| instantaneous_modulus | target | numeric | *Not specified.* | n=869, missing=0, range 1.158e+05–2.089e+07, mean 4.759e+06 ± 3.453e+06 |
| equilibrium_modulus | target | numeric | *Not specified.* | n=869, missing=652, range 3.68e+04–5.382e+06, mean 2.047e+06 ± 1.523e+06 |
| dynamic_modulus_at_01_hz | target | numeric | *Not specified.* | n=869, missing=652, range 3.625e+05–2.298e+07, mean 8.496e+06 ± 6.223e+06 |
| dynamic_modulus_at_025_hz | target | numeric | *Not specified.* | n=869, missing=652, range 2.347e+05–2.317e+07, mean 8.958e+06 ± 6.444e+06 |
| dynamic_modulus_at_05_hz | target | numeric | *Not specified.* | n=869, missing=652, range 2.414e+05–2.324e+07, mean 9.231e+06 ± 6.566e+06 |
| dynamic_modulus_at_0625_hz | target | numeric | *Not specified.* | n=869, missing=652, range 2.243e+05–2.326e+07, mean 9.292e+06 ± 6.592e+06 |
| dynamic_modulus_at_0833_hz | target | numeric | *Not specified.* | n=869, missing=652, range 2.135e+05–2.334e+07, mean 9.374e+06 ± 6.627e+06 |
| dynamic_modulus_at_1_hz | target | numeric | *Not specified.* | n=869, missing=652, range 2.426e+05–2.338e+07, mean 9.436e+06 ± 6.659e+06 |
| dynamic_modulus_at_2_hz | target | numeric | *Not specified.* | n=869, missing=652, range 3.539e+05–4.03e+07, mean 1.069e+07 ± 7.98e+06 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): historical_splits_documented_not_applied: 869

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://static-content.springer.com/esm/art%3A10.1038%2Fs41597-019-0170-y/MediaObjects/41597_2019_170_MOESM1_ESM.zip`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
- **Curated views:** M: 0 fields, Y: 12 fields, passport: 7 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *Not specified.* — [10.1038/s41597-019-0170-y](https://doi.org/10.1038/s41597-019-0170-y)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `7a682029ad5b6289693b114d3292e2062a0d34f46725443664df75bb3fed9d23`
- **Processing hash:** `9251b427b06509c455fcbf482bad926fff49078adb103b28600d7a8f182720b7` | **metadata hash:** `c231809f18d612a3540f6c4c740eff60a2077083dcdf56571884bb7b7049780c`
