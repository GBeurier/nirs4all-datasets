<!-- SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later -->
# @nirs4all/datasets-wasm

WASM binding over the `nirs4all-datasets` acquisition core. **Scoped to metadata +
small public datasets**: it resolves the descriptor+download contract from the distributable
`catalog/index.json` and computes SHA-256, but does not itself download large files —
in the browser, Dataverse CORS is per-instance, there is no real filesystem, and
dataset size is bounded (see `migration_ABI_C.md` §4). The native bindings (Python / R
/ Octave-MATLAB) do the byte download + caching.

```js
const wasm = require("@nirs4all/datasets-wasm"); // or `import` for the web target
const index = await (await fetch(INDEX_URL)).text();       // catalog/index.json
const contract = JSON.parse(wasm.resolve(index, "corn_eigenvector_nir"));
// contract.descriptor.sources / variables -> neutral dataset metadata
// contract.files[i].sha256  -> verify a blob you fetched yourself:
const ok = wasm.sha256(new Uint8Array(buf)) === contract.files[0].sha256;
```

## Public original-source acquisition

The separate additive public-origin API does not require hosted dataset assets.
`browserCatalog()` returns embedded public descriptor metadata with explicit
per-source applicability. `resolveBrowserPlan(id, sourceId)` names the original
resources for a supported source. The host downloads only those resources, then
passes `{name, bytes: Uint8Array}` inputs to `prepareBrowserDataset(planJson, files)`.
Pass its `files`, `record_sets` and unchanged `spec` to IO's `assembleDataset`.
No network, filesystem, inference, numerical method or upload is executed here.

The initial `public-single-table-v1` profile uses the existing owner recipes and
IO's table reader. It preserves axis aliases, target maps, sample/observation
identity, missing cells and original metadata. Other recipes, joins, filters,
archives and native partition projections carry explicit unsupported reasons;
they are never replaced by generic inference. CORS and provider reachability
remain properties of each actual origin, not a universal refusal.

Supported routes include the selected EcoSIS single-table recipes and the
existing Zenodo NeoSpectra soil CSV recipe. Soil keeps the native recipe's
per-scan observation identities; the repeated layer UUID remains metadata,
not an inferred specimen group. Its profile descriptor declares this generated
identity explicitly and provenance retains the original catalog declaration.
The index and existing `resolve()` results are not rewritten. Declared numeric
targets with unsupported nonnumeric/censored content are refused, never
silently recast as categories.

Origin hashes are not supplied by these existing recipes. The actual downloaded
SHA-256 is retained as `observed-unpinned`; historical canonical checksums are
never reused as origin pins. `canonical_identity_claimed` remains false. This
fresh original-source profile does not claim equality to historical canonical
file bytes. Original `resolve()` and SHA-256 contracts remain unchanged.

Regenerate/check only the public metadata projection with
`python3 scripts/generate_browser_origin_metadata.py [--check]` from the root.
After building, `python3 scripts/stage_wasm_package.py bindings/wasm/pkg-web`
stages the exact locked Rust license closure. The release workflow does the same
for `pkg-node` before packing; generated legal files are part of the distribution.

Build the browser package used by `nirs4all-web`:

```bash
wasm-pack build bindings/wasm --release --target web --out-dir pkg --scope nirs4all
```

Build and test the Node package:

```bash
wasm-pack build bindings/wasm --release --target nodejs --out-dir pkg-node --scope nirs4all
node bindings/wasm/tests/node_smoke.cjs
```

`wasm-pack` derives the local generated package name from the crate
(`@nirs4all/nirs4all-datasets-wasm`). The release workflow rewrites it to the
published npm package name shown above.
