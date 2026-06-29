// SPDX-License-Identifier: MIT
//! pyo3 native module (`nirs4all_datasets_core._n4ds`) over the acquisition core.
//!
//! JSON-string in / JSON-string out — the idiomatic Python layer
//! (`nirs4all_datasets_core/__init__.py`) parses to/from dicts. Errors map to the
//! Python exception the legacy `access.py` raised (`KeyError` for an unknown id,
//! `RuntimeError` for a missing token, `ValueError` for a not-fetchable contract).

use pyo3::exceptions::{PyKeyError, PyRuntimeError, PyValueError};
use pyo3::prelude::*;

use nirs4all_datasets_core::fetch::FetchOptions;
use nirs4all_datasets_core::model::Resolved;
use nirs4all_datasets_core::prepare::{prepare_raw as core_prepare_raw, PrepareOptions};
use nirs4all_datasets_core::retrieve::{RetrieveOptions, RetrieveRequest};
use nirs4all_datasets_core::{fetch as core_fetch, resolve_json, retrieve_raw as core_retrieve_raw, verify_cached as core_verify, Error, UreqClient};

fn to_pyerr(err: Error) -> PyErr {
    match err {
        Error::UnknownDataset(_) => PyKeyError::new_err(err.to_string()),
        Error::TokenRequired(_) => PyRuntimeError::new_err(err.to_string()),
        Error::NotFetchable(_) | Error::InvalidArgument(_) | Error::Json(_) => PyValueError::new_err(err.to_string()),
        _ => PyRuntimeError::new_err(err.to_string()),
    }
}

/// The ABI version of the underlying core.
#[pyfunction]
fn abi_version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

/// Resolve a dataset id against an index JSON; return the resolved contract JSON.
#[pyfunction]
fn resolve(index_json: &str, dataset_id: &str) -> PyResult<String> {
    resolve_json(index_json, dataset_id).map_err(to_pyerr)
}

/// Download + verify a resolved dataset; return the fetch-status JSON. Releases the
/// GIL for the (blocking, network) duration.
#[pyfunction]
fn fetch(py: Python<'_>, resolved_json: &str, opts_json: &str) -> PyResult<String> {
    let resolved: Resolved = serde_json::from_str(resolved_json).map_err(|e| PyValueError::new_err(e.to_string()))?;
    let opts = FetchOptions::from_json(opts_json).map_err(to_pyerr)?;
    py.allow_threads(|| {
        let client = UreqClient::new(opts.timeout_secs.unwrap_or(300));
        let result = core_fetch(&resolved, &opts, &client).map_err(to_pyerr)?;
        serde_json::to_string(&result).map_err(|e| PyRuntimeError::new_err(e.to_string()))
    })
}

/// Retrieve raw origin resources; return retrieval-status JSON. Releases the GIL for
/// the blocking network/filesystem work.
#[pyfunction]
fn retrieve_raw(py: Python<'_>, request_json: &str, opts_json: &str) -> PyResult<String> {
    let request: RetrieveRequest = serde_json::from_str(request_json).map_err(|e| PyValueError::new_err(e.to_string()))?;
    let opts = RetrieveOptions::from_json(opts_json).map_err(to_pyerr)?;
    py.allow_threads(|| {
        let client = UreqClient::new(opts.timeout_secs.unwrap_or(300));
        let result = core_retrieve_raw(&request, &opts, &client).map_err(to_pyerr)?;
        serde_json::to_string(&result).map_err(|e| PyRuntimeError::new_err(e.to_string()))
    })
}

/// Prepare already-retrieved raw resources with the Rust reader stack.
#[pyfunction]
fn prepare_raw(py: Python<'_>, request_json: &str, opts_json: &str) -> PyResult<String> {
    let request: RetrieveRequest = serde_json::from_str(request_json).map_err(|e| PyValueError::new_err(e.to_string()))?;
    let opts = PrepareOptions::from_json(opts_json).map_err(to_pyerr)?;
    py.allow_threads(|| {
        let result = core_prepare_raw(&request, &opts).map_err(to_pyerr)?;
        serde_json::to_string(&result).map_err(|e| PyRuntimeError::new_err(e.to_string()))
    })
}

/// Offline re-verify of a cached dataset directory; return the report JSON.
#[pyfunction]
fn verify_cached(resolved_json: &str, dir: &str) -> PyResult<String> {
    let resolved: Resolved = serde_json::from_str(resolved_json).map_err(|e| PyValueError::new_err(e.to_string()))?;
    let report = core_verify(&resolved, std::path::Path::new(dir)).map_err(to_pyerr)?;
    serde_json::to_string(&report).map_err(|e| PyRuntimeError::new_err(e.to_string()))
}

#[pymodule]
fn _n4ds(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(abi_version, m)?)?;
    m.add_function(wrap_pyfunction!(resolve, m)?)?;
    m.add_function(wrap_pyfunction!(fetch, m)?)?;
    m.add_function(wrap_pyfunction!(retrieve_raw, m)?)?;
    m.add_function(wrap_pyfunction!(prepare_raw, m)?)?;
    m.add_function(wrap_pyfunction!(verify_cached, m)?)?;
    Ok(())
}
