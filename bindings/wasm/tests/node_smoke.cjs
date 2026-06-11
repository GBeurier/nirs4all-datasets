// SPDX-License-Identifier: MIT
// Node smoke test for the WASM binding. Run after `wasm-pack build bindings/wasm
// --target nodejs --out-dir pkg-node`:  `node bindings/wasm/tests/node_smoke.cjs`.
const assert = require("node:assert");
const wasm = require("../pkg-node/nirs4all_datasets_wasm.js");

const index = JSON.stringify({
  schema: "1.0",
  n_datasets: 1,
  datasets: {
    demo: {
      tier: "public",
      dataverse: { instance: "https://dv.example", doi: "10.70112/ABC", dataset_version: "1.0" },
      files: [{ name: "X.parquet", relpath: "canonical/sources/X.parquet", directory_label: "canonical/sources", sha256: "aa", size: 9, file_id: 42 }],
      origins: [{ kind: "zenodo", mode: "canonical", locator: "10.5281/zenodo.5", access: "open" }],
      descriptor: { id: "demo" },
    },
  },
});

const resolved = JSON.parse(wasm.resolve(index, "demo"));
assert.strictEqual(resolved.id, "demo");
assert.strictEqual(resolved.tier, "public");
assert.strictEqual(resolved.files[0].file_id, 42);

// SHA-256("abc")
assert.strictEqual(
  wasm.sha256(Buffer.from("abc")),
  "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
);

assert.throws(() => wasm.resolve(index, "nope"));

assert.match(wasm.abiVersion(), /^\d/);
console.log("wasm node smoke OK");
