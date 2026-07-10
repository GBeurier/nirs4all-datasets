// SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
//! WASM binding (wasm-bindgen) over the pure, offline surface of the acquisition
//! core. Per `migration_ABI_C.md` §4 the browser is the sharp constraint (per-instance
//! Dataverse CORS, no real filesystem, dataset size), so the WASM surface is scoped to
//! what works there: **resolving the descriptor+download contract** from the distributable
//! `catalog/index.json`, and a streaming-free **SHA-256** a JS host can use to verify a
//! blob it fetched itself. The actual byte download + caching stays on the native
//! bindings (a `--no-default-features` core has no networking/filesystem).

use wasm_bindgen::prelude::*;

use nirs4all_datasets_core::hash::sha256_hex_bytes;
use nirs4all_datasets_core::resolve_json;

/// The core's version string.
#[wasm_bindgen(js_name = abiVersion)]
pub fn abi_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

/// Resolve a dataset id against an index JSON string; return the descriptor+download-contract JSON.
///
/// Throws (a JS `Error`) if the id is absent or the index is malformed.
#[wasm_bindgen]
pub fn resolve(index_json: &str, dataset_id: &str) -> Result<String, JsValue> {
    resolve_json(index_json, dataset_id).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Hex SHA-256 of a byte buffer (so a JS host can verify a file it fetched against the
/// contract's `sha256`).
#[wasm_bindgen]
pub fn sha256(bytes: &[u8]) -> String {
    sha256_hex_bytes(bytes)
}
