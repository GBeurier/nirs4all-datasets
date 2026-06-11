<!-- SPDX-License-Identifier: MIT -->
# @nirs4all/datasets-wasm

WASM binding over the `nirs4all-datasets` acquisition core. **Scoped to metadata +
small public datasets**: it resolves the download contract from the distributable
`catalog/index.json` and computes SHA-256, but does not itself download large files —
in the browser, Dataverse CORS is per-instance, there is no real filesystem, and
dataset size is bounded (see `migration_ABI_C.md` §4). The native bindings (Python / R
/ Octave-MATLAB) do the byte download + caching.

```js
const wasm = require("@nirs4all/datasets-wasm");          // or `import` for the web target
const index = await (await fetch(INDEX_URL)).text();       // catalog/index.json
const contract = JSON.parse(wasm.resolve(index, "corn_eigenvector_nir"));
// contract.files[i].sha256  -> verify a blob you fetched yourself:
const ok = wasm.sha256(new Uint8Array(buf)) === contract.files[0].sha256;
```

Build: `wasm-pack build bindings/wasm --release --target nodejs --out-dir pkg-node --scope nirs4all`,
then `node bindings/wasm/tests/node_smoke.cjs`.
