# Feasibility — a cross-language dataset acquisition core (Rust + C ABI + bindings)

**Question.** Move the *download* of datasets (from Dataverse / Zenodo / figshare / URL) into a Rust (or
C++) core with a stable **C ABI** and **WASM / Python / R / Octave-Matlab / Rust** bindings — published
like the other ecosystem libraries — while keeping the **identity-card analysis / report generation in
Python** on the clients. Is it feasible, Dataverse-API-compatible, and credible?

**Verdict: feasible and credible — recommended, in phases.** The boundary (acquisition in Rust, analysis
in Python) is clean and *already the ecosystem's design*. The only genuinely hard binding is **WASM**
(browser CORS + no filesystem + dataset size); every native binding is low-risk. A small prerequisite —
a **distributable catalog index** — must land first (and it independently fixes standalone `pip` use).

---

## 1. Why it fits the ecosystem (credibility)

This is not a novel architecture; it is the **established nirs4all pattern**:

| Project | Core | ABI | Bindings | Publish |
|---|---|---|---|---|
| `nirs4all-formats` | Rust (`crates/`) | `cbindgen.toml` | `python, r, wasm` | `release-{crates,npm,r,source}.yml`, `conformance.yml` |
| `nirs4all-io` | Rust (rewrite) | C ABI `n4io_` + pyo3 | `python, r, wasm, matlab` | full `release-*` + `abi-check` + `cross-binding` |
| `nirs4all-methods` | C++17 (`libn4m`) | stable C ABI | `python, r, matlab, octave, js` | `release-{python,r,matlab,npm}` + `parity-gate`, `sanitizers` |
| `dag-ml` / `dag-ml-data` | Rust | C ABI | (host vtable) | — |

A dataset-acquisition core would be a direct sibling of **`nirs4all-io`** (which is *also* an IO/Rust
rewrite with the same binding set and an `n4io_` C ABI). Reusing its
[`bindings/SPEC.md`](../nirs4all-io/bindings/SPEC.md) discipline verbatim — *raw C-ABI layer + idiomatic
per-language layer, JSON canonical on the wire, generated header committed, conformance/parity gated* —
makes the marginal cost per binding small and the result consistent with the rest of nirs4all.

## 2. The boundary (what moves, what stays)

The split is natural because acquisition and analysis have very different dependency profiles.

**Moves to the Rust core (`nirs4all-datasets-core`)** — pure I/O + integrity, no scientific stack:
- resolve a dataset name → its pinned origin/DOI + per-file SHA-256 + Dataverse file-ids (read the
  catalog index + the dataset manifest, both JSON);
- per-repository **DOI → file-URL** resolution (Dataverse Native API, Zenodo API, figshare API, raw URL);
- **download** with token auth, redirect-safe (token never follows a cross-host S3 redirect);
- **SHA-256 verify** against the manifest; **atomic write + pooch-style cache**;
- return the local **canonical directory path** + a JSON status (per file: cached / downloaded / verified).

**Stays in Python (host-side, maintainer + Python clients)** — the heavy scientific layer, unportable and
not worth porting:
- `qualify/` (per-source/per-variable metrics, PCA, plots, Croissant, datasheet), `anonymize`, the card
  builder, the catalog assembler, `health.py`, the site generator. These depend on numpy/scipy/sklearn/
  matplotlib + **nirs4all** and produce the artifacts that ship in git — they run *once*, on the
  maintainer's machine, not on every consumer.

**Consumers read the data natively.** The core returns *paths to verified Parquet*; each language reads
it with its own reader (`pyarrow`, R `arrow`, MATLAB `parquetread`, `parquet-wasm`). **No materialized
arrays cross the C ABI** — exactly the nirs4all-io v0 rule (`D-R7`). The ABI carries **JSON strings +
file paths**, never multi-MB spectra. This keeps the ABI tiny, stable, and binding-cheap.

```
            ┌────────────────────────── Rust core: nirs4all-datasets-core ──────────────────────────┐
 name/DOI → │  catalog/manifest (serde) → DOI resolver (Dataverse/Zenodo/figshare/url) → reqwest     │ → cache dir path
   token  → │  download (X-Dataverse-key, redirect-safe) → sha2 verify → atomic write → cache         │ + JSON status
            └──────────────────────── C ABI  n4ds_*  (JSON in, path/JSON out) ─────────────────────────┘
                 │ pyo3 │ extendr │ wasm-bindgen │ C-ABI→mex/oct │ native Rust │   ← bindings (idiomatic)
   host reads the verified Parquet natively (pyarrow / R arrow / parquetread / parquet-wasm) → its own NIRS workflow
   ── Python ALSO keeps the analysis layer (qualify/card/site) for maintainer + report generation ──
```

## 3. Current download layer (the thing we port)

`src/nirs4all_datasets/access.py` + `dataverse.py` already isolate exactly this surface, which makes the
port mechanical to scope:
- `fetch_public(doi, registry, cache)` — pooch resolves a DOI to a repository base URL, fetches by
  basename, verifies `sha256:` from the registry.
- `fetch_private(file_ids, registry, cache, instance, token)` — Dataverse **Access API**
  `GET /api/access/datafile/<id>` with the `X-Dataverse-key` header and **`allow_redirects=False`** (the
  token is *not* replayed onto the signed S3 redirect — the redirect is followed manually without it),
  then SHA-256 verify + atomic write + cache.
- `canonical_registry` / `canonical_file_ids` — `filename → sha256` / `filename → Dataverse file-id` from
  the manifest (the pinned, frozen download contract).

This is ~150 lines of HTTP + crypto + cache, but it is **not** a 1:1 port: the *public* path delegates
DOI→URL **resolution and caching to `pooch`**, so the Rust core must *re-implement* that (the per-rep
resolver + an ETag/size cache), not just translate it; the *private* path is the only fully-explicit
Dataverse code today. Reproducibility must also pin the **Dataverse dataset version**, not only the DOI —
the schema already carries `dataverse.dataset_version` and the manifest records it, and Dataverse version
specifiers (`:latest-published`, a numeric `M.N`, `:draft`) must be honoured so a consumer re-fetches the
exact pinned bytes. The Rust toolbox is `reqwest` + `sha2` + `serde_json` + `directories` — well-trodden,
but the *design* (version-pinned resolver + streaming + cache) is where the real work is.

## 4. Dataverse / origin API compatibility (the crux)

The Dataverse **Native** API (dataset metadata, `GET /api/datasets/:persistentId/?persistentId=doi:…` →
`files[]` with file-ids + `storageIdentifier`) and **Access** API (`GET /api/access/datafile/<id>`) are
plain REST/JSON over HTTPS with the token in `X-Dataverse-key`. **All of it is language-agnostic and
trivially callable from Rust** (`reqwest`), and equally from any binding.

| Concern | Native HTTP (Rust + Python/R/Matlab/Octave) | WASM / browser |
|---|---|---|
| Native + Access API (JSON) | ✅ reqwest / curl | ⚠️ subject to **CORS** — Dataverse API CORS is not guaranteed for arbitrary origins |
| Token hygiene (`X-Dataverse-key`, never on S3 redirect) | ✅ `reqwest` redirect policy / manual no-redirect (mirrors the Python) | ✅ header on the API call only |
| Signed S3 / Swift redirect for file bytes | ✅ follow without the token | ✅ usually CORS-open for `GET`; large files OK only if streamed |
| Zenodo (`/api/records/<id>`), figshare (`/v2/articles/<id>`), raw URL | ✅ | ⚠️ per-host CORS; Zenodo/figshare CDNs are often CORS-friendly for file `GET` |
| SHA-256 verification (our canonical bytes, `tabIngest=false`) | ✅ `sha2` | ✅ `SubtleCrypto`/`sha2` |
| Cache | ✅ OS cache dir (`directories`) | ⚠️ no filesystem → IndexedDB/OPFS, bounded; impractical for OSSL-scale (320 MB) |

**Beyond the happy path**, a production resolver must also handle (these are *additions* to the current
Python, not regressions):
- **Versioned file listing.** Dataverse `…/versions/{version}` defaults to *excluding* files — list with
  `…/versions/{version}/files` or `?excludeFiles=false`, keyed by the pinned `dataset_version`, never the
  always-moving "latest". (`DataverseClient.get_version()` should pass `excludeFiles=false`.)
- **Restricted / gated access.** `restrict`ed files, embargo/retention windows, **access requests**,
  **guestbook** responses, and **preview/signed-URL tokens** are first-class Dataverse flows; the core
  must surface a clear "needs request/guestbook/embargoed" status rather than silently 403.
- **Large files.** Stream to disk with **incremental SHA-256**, support **Range resume**, **re-acquire a
  fresh signed S3/Swift URL on expiry**, and add **retry/backoff** for per-instance rate limits (Dataverse
  supports single-range reads + configurable rate limiting). OSSL-scale (320 MB) makes this mandatory.
- **Filename vs layout.** Match files by Dataverse **directory label + name** (not bare basename) to avoid
  `raw/` vs `canonical/` collisions, and honour `Content-Disposition`.

**Bottom line:** for every **native** target the Dataverse/Zenodo/figshare APIs are tractable — the
current Python proves the core request shapes — but the resolver is "version-pinned + streaming +
gated-access aware", not a thin wrapper. **WASM is the sharp constraint**: Dataverse emits CORS headers
**only when the instance is configured to**, and the S3/CDN that actually serves the bytes needs its own
bucket/CDN CORS; combined with no real filesystem (→ OPFS/IndexedDB, bounded) and in-browser token
handling, the WASM binding is realistic only for **metadata + small public datasets**, or behind a
first-party app/proxy that controls CORS + storage. Known and documentable, not a blocker for the native
bindings.

## 5. C ABI surface (sketch, JSON-on-the-wire, `n4ds_` prefix)

```c
// All strings are UTF-8 canonical JSON owned by the core; free with n4ds_string_free.
const char* n4ds_version(void);
// Resolve from the catalog index -> JSON {id, tier, instance, doi, dataset_version,
//   files:[{name, relpath, sha256, size, file_id, directory_label}], origins:[...]}
int32_t n4ds_resolve(const char* index_json, const char* dataset_id, char** out_json);
// Download + verify into cache; opts_json = {cache_dir, token?, instance?, source?, retry?}.
//   Returns JSON {dir, files:[{name, relpath, path, status}]} -- relpath includes canonical/dataset.json
//   so the host can load() the dataset without re-deriving paths.
int32_t n4ds_fetch(const char* resolved_json, const char* opts_json, char** out_status_json);
// Offline integrity re-check of an already-cached dir (no network).
int32_t n4ds_verify_cached(const char* resolved_json, const char* dir, char** out_json);
void    n4ds_string_free(char* s);
```
No arrays, no opaque scientific handles — only JSON + filesystem paths, and the returned paths are
**relative canonical paths** (including `canonical/dataset.json`). Origin *health probing* and the health
*report* stay in Python (`health.py`) — they are catalog-maintenance, not consumer acquisition; a
liveness probe can be promoted to a core symbol later if a binding needs it. The header is generated by
`cbindgen` and committed; an `abi-check` workflow diffs the snapshot (the `nirs4all-io`/`methods` pattern).

## 6. Per-binding feasibility + publication

| Binding | Tooling (ecosystem-proven) | Difficulty | Publish to |
|---|---|---|---|
| **Rust** | native crate | trivial | crates.io (`release-crates.yml`) |
| **Python** | `pyo3` + `maturin` (as formats/io) | low | PyPI (`release-python/wheels`) |
| **R** | `extendr` over the C ABI (as io/methods) | **med** (native-lib packaging, TLS/cert store, CRAN policy) | r-universe / CRAN (`release-r.yml`) |
| **Octave/MATLAB** | C-ABI `mex`/`oct` (as methods) | **med** (binary distribution per platform) | File Exchange / Add-On (`release-matlab.yml`) |
| **WASM/JS** | `wasm-bindgen` (as formats/io) | **high** (CORS, no-fs→OPFS, size, in-browser token) | npm (`release-npm.yml`) |

R and Octave/MATLAB are *medium* (not low): shipping a native Rust/C-ABI library through their packaging,
TLS/certificate behaviour, and CRAN/MathWorks distribution constraints are real work, even with the
sibling templates. WASM is scoped to **metadata + small public datasets** unless a first-party app owns
CORS, OPFS/IndexedDB storage, streaming, and token handling.

Publication mirrors `nirs4all-io` / `nirs4all-formats` exactly — the workflows already exist to copy:
`release-{crates,python,r,matlab,npm,source}.yml` + `version-sync.yml` + `abi-check.yml` +
`cross-binding(-parity).yml` (a golden-vector parity gate so every binding fetches+verifies identically).

## 7. Prerequisite — a distributable catalog index (Phase 0)

The core needs the catalog to turn a name into a *complete download contract*. Today that information is
spread across `catalog/datasets.yaml` (no download details) + per-dataset `manifest.json` (sha256, file
ids) + the descriptor (tier, DOI, version, origins). Phase 0 generates **one distributable
`catalog/index.json`** — derivable from the existing manifests/descriptors — that is the cross-language
contract, with **everything a resolver needs** (this is what makes it more than today's `datasets.yaml`):

```jsonc
{ "schema": "1.0",
  "datasets": { "<id>": {
    "tier": "public|private|anonymized",
    "dataverse": { "instance": "https://…", "doi": "10.x/y", "dataset_version": "1.0" },
    "files": [ { "name": "X1.parquet", "relpath": "canonical/sources/X1.parquet",
                 "sha256": "…", "size": 12345, "file_id": 678, "directory_label": "canonical/sources" } ],
    "origins": [ { "kind": "zenodo", "mode": "canonical", "locator": "10.5281/…", "access": "open" } ],
    "descriptor": { /* the PUBLIC (tier-sanitized) descriptor: anonymized fields already masked */ } } } }
```

Ship it (a) bundled into each binding's package and/or (b) fetched from the GitHub raw URL on demand
(pooch-style, **ETag-cached**). It is small (JSON), and it **independently solves the Python
`get()`-from-PyPI gap** in `docs/RELEASING.md`. Two cautions: the embedded descriptor MUST be the
**public/anonymized-sanitized** one (no leak via the bundled index), and the index is **version-pinned**
so an old release fetches the exact old bytes. It is the natural first step.

## 8. Effort / risk

| Item | Effort | Risk |
|---|---|---|
| Phase 0 — `index.json` generator + loader (Rust + Python) | S | low |
| Phase 1 — Rust core (version-pinned resolvers + streaming download + verify + cache) + sandbox tests | **M–L** | **med** |
| Phase 2 — C ABI (`cbindgen`) + Python (`pyo3`) binding; parity vs current `access.py` | M | low |
| Phase 3 — R + Octave/MATLAB bindings | M | **med** (native packaging/TLS/CRAN/MathWorks) |
| Phase 4 — WASM binding | M–L | **high** (CORS, no-fs, size, token) |
| Cross-binding parity + `abi-check` CI | S | low (copy from io/methods) |

Phase 1 is **medium**, not low: it replaces `pooch`, implements per-repository **version-pinned** APIs,
streams large files, and handles restricted/gated Dataverse edges. The risk surface to plan for:
per-repository resolver drift (Dataverse versioning, Zenodo/figshare API changes), **Dataverse instance +
version differences**, **signed-URL expiry** mid-download, **CORS per instance *and* per S3/CDN bucket**,
**basename vs directory-label collisions**, **old-version reproducibility** (a tagged release must re-fetch
the exact bytes), **rate limits** (retry/backoff), **proxy/TLS/cert-store** behaviour across platforms,
**cache locking** (concurrent fetchers), and **privacy leakage in the bundled index** (ship only the
sanitized public descriptor). Mitigations: golden fixtures + a `network`-gated conformance job against the
RDG/CIRAD **sandbox**, and the cross-binding parity oracle — exactly as the Python tests already isolate
the network with an injected session.

## 9. What stays in Python — and the IO/formats future

- **Analysis stays Python.** `qualify`/card/`anonymize`/site/`health` are maintainer-side, depend on
  nirs4all + the scientific stack, and run once to produce the git-tracked cards. Porting them is neither
  necessary nor sensible.
- **Proprietary file formats (future).** Today the v2.0 packages are **CSV**, so the *canonical builder*
  needs no instrument-format reader. When datasets arrive as vendor formats (OPUS/JCAMP/SPC/ASD/…), the
  decoding belongs to **`nirs4all-formats`** (the Rust reader registry) consumed via **`nirs4all-io`** —
  *not* re-implemented here. The acquisition core would then optionally call the formats core to
  materialize canonical Parquet at fetch time. We defer this until it is real; the boundary already
  reserves the slot.

## 10. Recommendation

**Go**, phased and incremental, reusing `nirs4all-io` as the template:

1. **Phase 0 (now-ish):** generate + ship `catalog/index.json`; have Python `get()` consume it (fixes
   standalone pip). Low cost, immediate value, and the cross-language contract.
2. **Phase 1:** a `nirs4all-datasets-core` Rust crate (could live in this repo under `crates/`), tested
   against the RDG/CIRAD **sandbox**. Wrap the Python `access.py` download path to call it (parity gate).
3. **Phases 2–4:** C ABI + Python, then R + Octave/MATLAB, then WASM (caveated), each mirroring the io
   release matrix + the cross-binding parity oracle.

This delivers the user's goal (download datasets from any language, published like the rest of nirs4all),
keeps the analysis where it belongs (Python), is fully Dataverse-API-compatible for native targets, and
isolates the one hard problem (WASM/CORS) behind a clearly-scoped, last phase.

---

## 11. Codex review

Reviewed by Codex (read-only, against the actual `access.py`/`dataverse.py` + the `nirs4all-io`/`formats`
precedents + the Dataverse guides). **Verdict: CREDIBLE; the phased recommendation is sound** — with
accuracy fixes required before treating it as implementation-ready. The fixes below have been **folded
into §§2–8 above**:

- **Boundary (correct).** Acquisition-in-Rust / analysis-in-Python matches the nirs4all-io rule that only
  JSON/strings cross the C ABI. *Fixed:* removed `health` from the v0 ABI (it stays Python); the fetch
  status now returns relative canonical paths including `canonical/dataset.json`; softened "mechanical
  port" (the public path delegates resolve+cache to `pooch`, which the core must re-implement).
- **Dataverse API (mostly correct; sharpened).** Token/Access/no-redirect/checksum confirmed against the
  code + Dataverse guides. *Fixed:* pin by **dataset version** (not just DOI; use the versioned `…/files`
  endpoint with `excludeFiles=false`); added the restricted/embargo/access-request/guestbook/preview-token
  flows; added large-file **streaming + incremental SHA-256 + Range resume + signed-URL-expiry re-acquire +
  rate-limit retry**; directory-label vs basename matching; sharper WASM/CORS (Dataverse emits CORS only
  when configured, and the S3/CDN needs its own bucket CORS).
- **Bindings.** *Fixed:* R and Octave/MATLAB re-rated **medium** (native-lib packaging, TLS/cert, CRAN /
  MathWorks distribution); WASM explicitly scoped to metadata + small public datasets.
- **Phase 0 (correct + completed).** The distributable index is the right prerequisite and does fix
  standalone `pip get()`. *Fixed:* §7 now specifies the full `index.json` download contract (instance, DOI,
  **dataset_version**, relpaths, sha256, sizes, file ids, directory labels, tier, origin mode, and the
  **sanitized public** descriptor).
- **Effort/risk.** *Fixed:* Phase 1 re-rated **M–L / medium**; added instance/version differences,
  signed-URL expiry, per-instance+bucket CORS, basename/label collisions, old-version reproducibility,
  rate limits, proxy/TLS/cert stores, cache locking, and bundled-index privacy to the risk list.

Codex's five headline improvements — version-pinned resolver, the `index.json` contract, streaming/resume/
retry, tightened WASM constraints, and upward risk re-rating — are all reflected above.

_Status: feasibility report (no code committed); Codex-reviewed and revised._
