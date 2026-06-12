// SPDX-License-Identifier: MIT
// Node smoke test for the WASM binding. Run after `wasm-pack build bindings/wasm
// --target nodejs --out-dir pkg-node`:  `node bindings/wasm/tests/node_smoke.cjs`.
const assert = require("node:assert");
const { execFileSync } = require("node:child_process");
const { mkdtempSync, rmSync, writeFileSync } = require("node:fs");
const { tmpdir } = require("node:os");
const path = require("node:path");
const wasm = require("../pkg-node/nirs4all_datasets_wasm.js");

const indexObject = {
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
};
const index = JSON.stringify(indexObject);

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

const repoRoot = path.resolve(__dirname, "../../..");
const tmp = mkdtempSync(path.join(tmpdir(), "n4ds-wasm-"));
try {
  const indexPath = path.join(tmp, "index.json");
  writeFileSync(indexPath, JSON.stringify(indexObject, null, 2) + "\n");
  const cliOut = execFileSync(
    "cargo",
    ["run", "--quiet", "-p", "nirs4all-datasets-cli", "--", "resolve", "--index", indexPath, "demo"],
    { cwd: repoRoot, encoding: "utf8" },
  );
  assert.deepStrictEqual(JSON.parse(cliOut), resolved);
} finally {
  rmSync(tmp, { recursive: true, force: true });
}

assert.match(wasm.abiVersion(), /^\d/);
console.log("wasm node smoke OK");
