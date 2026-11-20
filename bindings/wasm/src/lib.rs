// SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
//! WASM binding (wasm-bindgen) over the pure, offline surface of the acquisition
//! core. Per `migration_ABI_C.md` §4 the browser is the sharp constraint (per-instance
//! Dataverse CORS, no real filesystem, dataset size), so the WASM surface is scoped to
//! what works there: **resolving the descriptor+download contract** from the distributable
//! `catalog/index.json`, and a streaming-free **SHA-256** a JS host can use to verify a
//! blob it fetched itself. The actual byte download + caching stays on the native
//! bindings (a `--no-default-features` core has no networking/filesystem).

use wasm_bindgen::prelude::*;

use nirs4all_datasets_core::browser::{
    browser_catalog, prepare_browser_dataset, resolve_browser_plan, BrowserFile,
};
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

/// Embedded public metadata with explicit supported/unsupported origin profiles.
#[wasm_bindgen(js_name = browserCatalog)]
pub fn browser_catalog_json() -> String {
    browser_catalog().to_string()
}

/// Resolve one source to its owner plan; no network request is made.
#[wasm_bindgen(js_name = resolveBrowserPlan)]
pub fn browser_plan(dataset_id: &str, source_id: &str) -> Result<String, JsValue> {
    resolve_browser_plan(dataset_id, source_id)
        .map(|value| value.to_string())
        .map_err(|error| JsValue::from_str(&error.to_string()))
}

/// Apply the declared origin recipe, then return IO's exact in-memory inputs.
#[wasm_bindgen(js_name = prepareBrowserDataset)]
pub fn prepare_browser(plan_json: &str, files: JsValue) -> Result<JsValue, JsValue> {
    let plan =
        serde_json::from_str(plan_json).map_err(|error| JsValue::from_str(&error.to_string()))?;
    let files: Vec<BrowserFile> = serde_wasm_bindgen::from_value(files)
        .map_err(|error| JsValue::from_str(&error.to_string()))?;
    let prepared = prepare_browser_dataset(&plan, &files)
        .map_err(|error| JsValue::from_str(&error.to_string()))?;
    let output = js_sys::Object::new();
    let files = js_sys::Array::new();
    for file in prepared.files {
        let value = js_sys::Object::new();
        js_sys::Reflect::set(&value, &"name".into(), &file.name.into())?;
        js_sys::Reflect::set(
            &value,
            &"bytes".into(),
            &js_sys::Uint8Array::from(file.bytes.as_slice()),
        )?;
        files.push(&value);
    }
    js_sys::Reflect::set(&output, &"files".into(), &files)?;
    js_sys::Reflect::set(&output, &"record_sets".into(), &js_sys::Array::new())?;
    js_sys::Reflect::set(
        &output,
        &"spec".into(),
        &js_sys::JSON::parse(&prepared.spec.to_string())?,
    )?;
    js_sys::Reflect::set(
        &output,
        &"provenance".into(),
        &js_sys::JSON::parse(&prepared.provenance.to_string())?,
    )?;
    Ok(output.into())
}
