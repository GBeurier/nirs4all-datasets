# Datasheet — PNNL/NIST Quantitative Infrared Database private-use subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** pnnl
- **Description:** PNNL/NIST Quantitative Infrared Database private-use subset. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, pnnl
- **Contributor:** NIST Chemistry WebBook Quantitative Infrared Database

## Composition

- **Alignment:** observation level; 20 sample(s), 20 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | PNNL/NIST Quant IR private-use subset | Bruker IFS66V where specified in JCAMP metadata | MIR | 574.7–3976 none | 20 | 3527 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| compound_name | target | categorical | *Not specified.* | n=20, missing=0, classes=20, top Ethylene (×1) |
| cas_number | target | categorical | *Not specified.* | n=20, missing=0, classes=20, top 74-85-1 (×1) |
| formula | target | categorical | *Not specified.* | n=20, missing=0, classes=20, top C H2: C H2 (×1) |
| class_label | target | categorical | *Not specified.* | n=20, missing=0, classes=20, top Ethylene (×1) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top IR (×20) |
| axis_unit | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top cm-1 (×20) |
| axis_min | metadata | numeric | *Not specified.* | n=20, missing=0, range 574.7–574.7, mean 574.7 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=20, missing=0, range 3976–3976, mean 3976 ± 9.331e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=20, missing=0, range 3527–3527, mean 3527 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top (micromol/mol)-1m-1 (base 10) (×20) |
| chemical_family | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top volatile_organic_compound_inferred (×20) |
| phase | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top gas (×20) |
| pressure | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top 101.3 kPa (×20) |
| temperature | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top 23 C (×20) |
| path_length | metadata | categorical | *Not specified.* | n=20, missing=20, classes=0, — |
| resolution | metadata | numeric | *Not specified.* | n=20, missing=0, range 1.929–1.929, mean 1.929 ± 2.278e-16 |
| instrument | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top IFS66V (Bruker) (×20) |
| acquisition_conditions | metadata | categorical | *Not specified.* | n=20, missing=0, classes=20, top KBr Beam splitter, MCT Detector, Multipass cell \| 1 L/min Flow \| Boxcar Apodization \| 2.1 % relative (B=1.1E-04,C=8.5E-10,D=2.7E-14) (×1) |
| data_source | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top QUANT-IR (×20) |
| citation | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top P.M. Chu, F.R. Guenther, G.C. Rhoderick, and W.J. Lafferty, The NIST Quantitative Infrared Database, J. Res. Natl. Inst. Stand. Technol. 104, 59 (1999), DOI 10.6028/jres.104.004. (×20) |
| rights_status | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top manual_review_needed (×20) |
| usage_scope | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top private_use_only (×20) |
| notes | metadata | categorical | *Not specified.* | n=20, missing=0, classes=1, top private_use_only, public redistribution not cleared, selected common-axis Quant IR subset, no interpolation (×20) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://webbook.nist.gov/chemistry/quant-ir/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://webbook.nist.gov/cgi/cbook.cgi?JCAMP=C74851&Index=1&Type=IR`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** NIST/SRD rights are not cleared for redistribution of derived X/Y/M exports. Conversion is private/internal only.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `252c9b3ddc5445e26571c5f80901cf2ddfae397d79a73618842913a1764cdd87`
- **Processing hash:** `4f6e427a4952beff8c1e2157db461641f8e0eac31e2cecd2b01569c02d913ba7` | **metadata hash:** `09cefe8a298a653a328b1ac921bd4995e8f0dedd3bcd2b6e988ce7005f2ff188`
