# Retrieval Audit and Schema Proposal

Date: 2026-06-29
Catalog status refreshed: 2026-07-06

## Scope

This audit covers the current `nirs4all-datasets` acquisition path, the 164
`NIRS DB/v2.0/*/source_to_standard.py` scripts, `catalog/datasets/*.yaml`, and
the Rust acquisition core. The goal is to determine how many datasets can be
retrieved from public origins without hosting a copy, and what retrieval schema
is needed to make that safe and cross-language.

The key distinction is:

- **Retrieval**: download raw or canonical bytes from the authoritative origin.
- **Canonicalization**: turn retrieved raw bytes into the local v2/canonical
  dataset layout.

The current code mostly supports canonical retrieval, while the NIRS DB scripts
mostly describe raw retrieval plus dataset-specific canonicalization.

## Implementation Status

This audit has been partially implemented in the Rust acquisition layer:

- `catalog/index.json` now carries the retrieval schema and sanitized routes.
- `retrieve_raw` downloads open raw resources in Rust for direct URLs and
  provider-backed routes.
- `prepare_raw` stages retrieved resources in Rust: native spectra are decoded
  through `nirs4all-formats`; simple tabular resources are summarized through
  `nirs4all-io`; ECOSTRESS spectrum text files are parsed and assembled into a
  dataset-level canonical payload by the Rust recipe
  `jpl_ecostress_spectrum_txt_v1`.
- As of the 2026-07-06 catalog status, all 164 datasets have descriptors,
  generated cards, and local canonical artifacts. The distributable index
  status is 157 `raw_reproducible`, 7 `token_required` private Dataverse
  uploads, and 0 `missing_delegate`. ECOSTRESS uses direct public raw retrieval
  via `https://speclib.jpl.nasa.gov/ecospeclibdata/<file>.spectrum.txt`.

## Current Repository State

`catalog/datasets` contains 164 descriptors, with matching generated cards and
local canonical artifacts for all 164 datasets:

| Metric | Count |
|---|---:|
| Public datasets | 42 |
| Private datasets | 122 |
| Anonymized datasets | 0 |
| Generated dataset cards | 164 |
| Materialized local canonical datasets | 164 |
| Datasets with raw-only origins | 164 |
| Datasets with canonical origins | 0 |
| Datasets with open origins | 157 |
| Retrieval status `raw_reproducible` | 157 |
| Retrieval status `token_required` | 7 |
| Retrieval status `missing_delegate` | 0 |

Origin entries total 460:

| Field | Counts |
|---|---|
| `mode` | `raw`: 460, `canonical`: 0 |
| `access` | `open`: 287, `manual`: 173, `token`: 0 |
| `kind` | `url`: 282, `script`: 164, `figshare`: 7, `zenodo`: 5, `dataverse`: 2 |

Manifest/index state:

| Metric | Count |
|---|---:|
| Manifests | 164 |
| Canonical file contracts in manifests | 537 |
| Raw file records in manifests | 3,846 |
| Canonical files with Dataverse `file_id` | 0 / 537 |
| Descriptor Dataverse DOIs | 0 |
| Manifest DOIs / dataset versions | 0 |
| Local `datasets/*/canonical/dataset.json` | 164 |

Local `get()` can resolve the materialized canonical artifacts in this
workspace. Remote canonical fetch is still pending where local bytes are absent:
there is no published canonical DOI, no Dataverse file IDs, and no open
canonical DOI origin. The only datasets actually blocked for remote retrieval
are the seven private `token_required` Dataverse uploads listed in
[DATAVERSE_PENDING.md](DATAVERSE_PENDING.md); their local canonical artifacts
exist, but DOI/version/file IDs must be minted by a private Dataverse upload.

## Current Acquisition Behavior

The Python and Rust code already have a good canonical acquisition boundary:

- `access.py` prefers local `datasets/<id>/canonical/dataset.json`, then a
  descriptor/manifest Dataverse DOI, then open canonical origins.
- `_has_fetchable_origin()` only accepts origins that are `open`, `canonical`,
  DOI-like, and one of Dataverse, Zenodo, or Figshare.
- The Rust core downloads manifest-declared canonical files, verifies SHA-256,
  writes atomically through a `.part` file, and caches under the OS cache.
- `retrieve_raw` accepts synthesized direct URL resources, provider-backed
  routes, and size/hash metadata when available; it does not execute scripts.
- `reproduce.py` is opt-in and Python-only. It tries open Zenodo/Figshare/URL
  raw origins, unpacks simple archives, and delegates assembly to
  `nirs4all-io`. It does not execute the NIRS DB scripts and is not
  byte-pinned.

This means the native acquisition core is already appropriate for canonical
fetches, but not yet for public raw repatriation.

## Script Corpus Audit

There are 164 `source_to_standard.py` files. All datasets have one, but many
are not standalone retrieval scripts. The real diversity is much lower than 164.

| Family | Count | Examples | Current retrieval shape |
|---|---:|---|---|
| ECOSTRESS shared-converter stubs | 58 | `ecostress_lunar_tir_2124points`, `ecostress_rock_all_2868points` | Docstring only; raw retrieval is now synthesized from `raw_manifest.csv` to JPL `ecospeclibdata` files; dataset-level X assembly is handled by the Rust family recipe. Public `.spectrum.txt` headers do not contain every historical Y/M field. |
| EcoSIS shared-converter stubs | 57 | `ecosis_3d_leaf_level_spectra_reflectance_nirs` | Docstring only; says to run missing `convert_ecosis_nirs.py`. |
| OSSL / NeoSpectra CSV.gz | 16 | `ossl_jovic_visnir_soil_all_y`, `ossl_lucas_mir_soil_all_y` | Downloads Google Storage `.csv.gz` resources or uses cache. |
| Time-series ZIP verifier | 9 | `timeseries_boeuf_classe_adulteration_ts`, `timeseries_vin_cepage_type_ts` | Downloads public ZIPs, verifies raw availability, intentionally does not regenerate X/Y/M. |
| OpenSpecy RDS wrappers | 2 | `openspecy_ftir`, `openspecy_raman` | Raw retrieval is direct; Rust preparation now delegates the OpenSpecy `.rds` object to `nirs4all-formats`. Exact FTIR/RAMAN X/Y/M assembly remains a dataset recipe. |
| Private Dataverse pending uploads | 7 | `cgl_nir_grain_eigenvector`, `corn_eigenvector_nir`, `grapevine_leaftraits_multisensor_nir` | Local canonical bytes and cards exist. Retrieval status is `token_required`, not a missing delegate; remote fetch waits for Dataverse DOI/version/file IDs (see [DATAVERSE_PENDING.md](DATAVERSE_PENDING.md)). |
| Repository API downloads | 4 | `flanagan_api_compounds_raman`, `plastic_polymer_name_grouped_flopp_ftir` | Figshare or EcoSIS/CKAN API, select files by name, download CSV/XLSX/ZIP. |
| R/RDA route | 3 | `ohpl_beer_nir`, `ohpl_soil_nir`, `ohpl_wheat_nir` | Downloads GitHub `.rda`, writes temporary R script, calls `Rscript`. |
| Local/manual extracted bundles | 4 | `grapevine_leaftraits_multisensor_nir`, `manure21_nir_all_y`, `ucph_tablet_nir` | Requires pre-staged local raw files or extracted archives. |
| Local/native or blocked vendor formats | 3 | `chembl_ir_raman_multiblock`, malaria oocyst/sporozoite | SQLite/zlib or Dataverse SPC/DTA, blocked on parser/tooling. |
| Direct Eigenvector ZIP/MAT | 1 | `corn_eigenvector_nir` | Downloads ZIP, extracts `corn.mat`, parses MATLAB data. |
| EcoSIS urban direct XLSX | 1 | `ecosis_urban_materials_spectral_library_reflectance_nirs` | Direct EcoSIS URLs / XLSX resources. |

Common implementation signals:

| Signal | Count |
|---|---:|
| `urllib` | 36 |
| `requests` | 3 |
| `subprocess` | 15 |
| `zipfile` | 12 |
| `pandas` | 30 |
| `sqlite3` | 9 |
| `Rscript` / R route | 3 to 5 depending on signal |
| `RAW_SOURCE_MODE` | 40 |
| `RAW_DOWNLOAD_DIR` | 38 |
| `STANDARD_OUTPUT_DIR` | 24 |
| `RAW_FORCE_DOWNLOAD` | 15 |
| `OSSL_RAW_CACHE_DIR` | 16 |

The strongest consolidation opportunities are:

- one ECOSTRESS group recipe instead of 58 leaf stubs;
- one EcoSIS group recipe instead of 57 leaf stubs;
- one OSSL parameterized recipe instead of 16 copied scripts;
- one TimeSeries archive recipe plus a missing parser/assembler stage;
- explicit API selectors for Figshare, CKAN/EcoSIS, Dataverse, and Zenodo;
- private Dataverse upload metadata for the remaining `token_required` datasets
  (DOI, dataset version, and per-file IDs).

## Main Findings

1. **The current descriptor model records raw provenance, not retrieval.**
   `origin_sources` knows `kind`, `mode`, `locator`, and `access`, but not the
   remote file selectors, archive members, expected filenames, parser route,
   or whether automated retrieval is legally/technically allowed.

2. **The public/private split is not the same as retrievable/not retrievable.**
   Some datasets are private because redistribution is not cleared, but their
   raw bytes may still be publicly reachable. The schema needs independent
   fields for `public_retrievable`, `public_redistributable`, and
   `canonical_hosted`.

3. **Most hard cases are not HTTP hard cases.**
   Downloading can usually be made generic. The harder part is expressing the
   post-download route: select files, unpack archives, choose modality, parse
   native formats, join metadata, or delegate to a family converter.

4. **A full Rust rewrite is feasible for retrieval, not for every conversion.**
   Rust should own safe network/cache/unpack/provider logic. Canonicalization
   should call either declarative Rust recipes, `nirs4all-formats`,
   `nirs4all-io`, or a compatibility delegate for legacy cases.

## Proposed Retrieval Schema

Add first-class retrieval metadata, preferably next to each descriptor and then
export a sanitized form in `catalog/index.json`. The schema should not overload
`origin_sources` further.

```yaml
retrieval:
  schema_version: "1.0"
  status: raw_reproducible        # canonical_verified | raw_reproducible |
                                  # verifier_only | documented_only |
                                  # manual_only | token_required |
                                  # blocked_parser
  routes:
    - id: official_raw
      priority: 10
      access: open                # open | token | manual
      method: raw_retrieve         # canonical_fetch | raw_retrieve |
                                  # delegate | manual
      provider: figshare           # url | dataverse | zenodo | figshare |
                                  # ckan | google_storage | github |
                                  # timeseriesclassification | jpl_ecostress
      locator: "10.xxxx/yyyy"      # DOI, URL, API endpoint, or provider id
      landing_url: "https://..."
      api_url: "https://..."
      automated_download_allowed: true
      redistribution_allowed: false
      terms_url: "https://..."
      citation: "..."
      max_total_bytes: 1000000000
      resources:
        - id: spectra
          role: spectra            # spectra | targets | metadata | archive |
                                  # split | license | readme
          required: true
          selector:
            kind: api_file_name    # direct_url | api_file_name |
                                  # dataverse_file_id | zenodo_key |
                                  # figshare_file_id | archive_member |
                                  # local_path
            value: "X.csv"
          file_name: "X.csv"
          format: csv              # csv | csv_gz | xlsx | zip | mat |
                                  # rda | sqlite | spc | parquet | unknown
          compression: gzip
          sha256: null
          size: null
          unpack:
            archive: false
      canonicalization:
        engine: nirs4all_io        # rust_recipe | nirs4all_io |
                                  # nirs4all_formats | python_compat |
                                  # rscript_compat | delegate | manual
        recipe_id: ossl_soil_v1
        recipe_version: "1.0.0"
        parameters:
          dataset_code: "SERBIA.SSL"
          spectral_kind: visnir
        expected_outputs:
          layout: v2_standard      # v2_standard | canonical
          files: ["X.csv", "Y.csv", "M.csv"]
      health:
        probe: true
        expected_status: [200, 302]
```

### Route Types

| Route type | Purpose | Rust responsibility | Canonicalization responsibility |
|---|---|---|---|
| `canonical_fetch` | Existing verified canonical download | resolve, download, cache, SHA-256 verify | none |
| `raw_retrieve` | Public raw repatriation without hosting copy | provider API, direct HTTP, cache, size guard, checksums, unpack | recipe / `nirs4all-io` / `nirs4all-formats` |
| `delegate` | Legacy family converter or compatibility script | validate delegate fingerprint, prepare inputs, report unsupported on non-Python bindings | delegate process or host language |
| `manual` | Public but not safely automatable | structured instructions and blockers | manual user action |

### Status Semantics

The 2026-07-06 catalog uses `raw_reproducible` for 157 datasets and
`token_required` for the 7 private Dataverse uploads. Historical
`missing_delegate` cases have been resolved; the current count is 0.

| Status | Meaning |
|---|---|
| `canonical_verified` | `get()` can return byte-verified canonical data. |
| `raw_reproducible` | Raw bytes can be retrieved automatically; canonicalization is supported. |
| `verifier_only` | Raw bytes can be retrieved, but current script does not regenerate X/Y/M. |
| `documented_only` | Source is documented, but recipe/helper is missing. |
| `manual_only` | Requires click-through, local bundle, or human action. |
| `token_required` | Needs a credential or token for retrieval. |
| `blocked_parser` | Retrieval is possible, parser route is not available yet. |

## Family-Specific Schema Mapping

| Family | Best schema mapping |
|---|---|
| ECOSTRESS | `raw_retrieve` via direct JPL `ecospeclibdata/*.spectrum.txt` resources plus Rust recipe `jpl_ecostress_spectrum_txt_v1`; `prepare_raw` writes a dataset-level canonical JSON with the shared axis, X matrix, and per-observation headers. Exact historical Y/M parity depends on manifest/card metadata that is not present in the public spectrum text files. |
| EcoSIS | `raw_retrieve` via CKAN/EcoSIS package/resource IDs; one group recipe with dataset-specific selectors. |
| OSSL | `raw_retrieve` with three Google Storage `.csv.gz` resources and OSSL parameters such as `dataset_code`, `spectral_kind`, and join keys. |
| TimeSeries | `raw_retrieve` ZIP resources; current catalog entries are `raw_reproducible`. |
| Figshare datasets | `raw_retrieve` with `api_file_name` or file-id selectors, not positional assumptions. |
| OHPL | `raw_retrieve` GitHub `.rda`; canonicalization is `rscript_compat` initially, later replace with native RDA support if needed. |
| Malaria | `raw_retrieve` Dataverse SPC/DTA with native preparation support; current catalog entries are `raw_reproducible`. |
| Private Dataverse pending uploads | `token_required` until the canonical files are uploaded and Dataverse DOI/version/file IDs are recorded; local canonical artifacts already exist for the 7 listed in [DATAVERSE_PENDING.md](DATAVERSE_PENDING.md). |

## Rust / C ABI Feasibility

The native core is already well placed for retrieval:

- provider resolution and HTTP are centralized behind a Rust `HttpClient`;
- cache paths are guarded;
- canonical files are SHA-256 verified;
- Dataverse token handling avoids leaking the token on redirects;
- bindings already call the core through a C ABI.

Recommended Rust expansion:

1. Add `n4ds_retrieve_raw` or extend `n4ds_fetch` with route type
   `raw_retrieve`.
2. Implement provider adapters for direct URL, Dataverse, Zenodo, Figshare,
   CKAN/EcoSIS, Google Storage, GitHub raw, and TimeSeries archive URLs.
3. Add generic resource cache, checksum validation when known, size limits,
   archive extraction, and path traversal protection.
4. Return a structured retrieval result containing raw file paths, verification
   status, route status, skipped/manual blockers, and provenance.
5. Let host bindings call `nirs4all-io` / `nirs4all-formats` or a recipe engine
   for canonicalization.

Do not initially move every converter into Rust. Start by moving retrieval and
unpack into Rust, then migrate family recipes in order of leverage.

## Risks and Design Constraints

- **Raw retrieval is not canonical verification.** The result must report
  `verified: false` unless canonical SHA-256 outputs are verified.
- **Index drift risk.** `index.py` and Rust `model.rs` mirror each other by
  convention. Add golden JSON tests for schema changes.
- **`:latest-published` is not a reproducibility pin.** Prefer concrete
  Dataverse versions and stable provider file IDs.
- **Bare filename matching can collide.** Remote selectors should include
  provider file IDs or archive paths, not only basenames.
- **Automated download permission is separate from reachability.** Store
  terms/click-through/redistribution flags explicitly.
- **Delegates need fingerprints.** Compatibility scripts must be identified by
  hash, engine, required tools, and support status.

## Recommended Implementation Plan

1. Generate a machine-readable audit table:
   `dataset_id`, current tier, current origins, script family, retrieval status,
   blocker reasons, and proposed route type.
2. Add `retrieval` to the Python schema and export a sanitized version into
   `catalog/index.json`.
3. Implement Rust raw-resource retrieval without canonicalization: provider
   adapters, cache, checksums, archive extraction, and health probing.
4. Convert high-leverage families first: OSSL, Figshare API datasets,
   EcoSIS, TimeSeries, and remaining non-ECOSTRESS family assemblers.
5. Add `nirs4all-io` / `nirs4all-formats` canonicalization hooks for native
   formats and simple tabular layouts. Initial Rust `prepare_raw` hooks are now
   present; ECOSTRESS has a family recipe, and other dataset-specific Rust
   recipes remain to be curated.
6. Keep `delegate` and `manual` as explicit statuses, not hidden failures.
7. Recompute tiers separately from retrievability. A dataset can be public
   retrievable but not redistributable.

## Bottom Line

The suggestion is sound if it is framed as **safe public raw repatriation**, not
as executing the current scripts unchanged. The repository already has the right
Rust/C ABI foundation for canonical fetches. The next layer should be a Rust
retrieval engine plus a declarative retrieval schema, with canonicalization
handled by recipes, `nirs4all-io`, `nirs4all-formats`, or compatibility
delegates.

This should substantially reduce the number of datasets treated as private only
because no hosted canonical copy exists, while preserving the rule that this
library does not redistribute source datasets.
