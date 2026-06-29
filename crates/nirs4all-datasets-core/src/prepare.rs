// SPDX-License-Identifier: MIT
//! Rust-side preparation of retrieved raw resources.
//!
//! `retrieve_raw` only acquires bytes. This module performs the next portable
//! step: decode what can be decoded with the Rust nirs4all stack and write
//! stable JSON artifacts next to the raw cache. Per-resource decoding always runs;
//! for ECOSTRESS spectral libraries it then assembles the per-file records into a
//! single dataset-level canonical payload (shared spectral axis + X matrix + the
//! per-observation header targets/metadata), so every binding can inspect the same
//! prepared payloads without shelling out to Python/R scripts.

use std::collections::BTreeSet;
use std::fs;
use std::path::{Path, PathBuf};

use serde::{Deserialize, Serialize};
use serde_json::json;

use crate::cache::{default_cache_dir, safe_join};
use crate::error::{Error, Result};
use crate::retrieve::{RetrievalResource, RetrievalRoute, RetrieveRequest};

/// Options for preparing already-retrieved raw resources.
#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct PrepareOptions {
    /// Cache root. Defaults to the same OS cache root as retrieval/fetch.
    #[serde(default)]
    pub cache_dir: Option<String>,
}

impl PrepareOptions {
    /// Parse options from JSON; empty/null means defaults.
    pub fn from_json(s: &str) -> Result<PrepareOptions> {
        if s.trim().is_empty() {
            Ok(PrepareOptions::default())
        } else {
            Ok(serde_json::from_str(s)?)
        }
    }
}

/// Result returned by raw preparation.
#[derive(Debug, Clone, Serialize)]
pub struct PrepareResult {
    pub dir: String,
    pub ok: bool,
    pub route_id: String,
    pub resources: Vec<PreparedResource>,
    /// Dataset-level canonical assembly, when the route's resources form a
    /// recognized multi-file dataset (currently ECOSTRESS spectrum libraries).
    /// Absent for routes that only yield independent per-resource records.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub dataset: Option<PreparedDataset>,
}

/// Summary of a dataset-level canonical assembly written next to the per-resource
/// records. The full payload (shared axis + `x_matrix` + per-observation headers)
/// is written to `output_path`; this struct is only the status the ABI returns.
#[derive(Debug, Clone, Serialize)]
pub struct PreparedDataset {
    /// Schema id of the canonical payload at `output_path`.
    pub schema: String,
    /// Recipe id that produced it.
    pub recipe_id: String,
    /// Engine label (always `rust_recipe`).
    pub engine: String,
    /// Whether a usable X matrix (at least one aligned spectrum) was assembled.
    pub ok: bool,
    /// Where the full canonical JSON was written, or `None` if nothing was written.
    pub output_path: Option<String>,
    /// Number of observations (rows of the X matrix) that aligned to the axis.
    pub n_observations: usize,
    /// Number of spectral points (columns of the X matrix / axis length).
    pub n_variables: usize,
    /// Number of distinct header metadata/target columns across the observations.
    pub n_metadata_columns: usize,
    /// Best-effort canonical axis unit (e.g. `micrometers`) from the `X Units` header.
    pub axis_unit: Option<String>,
    /// Minimum spectral-axis value.
    pub axis_min: Option<f64>,
    /// Maximum spectral-axis value.
    pub axis_max: Option<f64>,
    /// Non-fatal assembly notes (parse failures, axis mismatches excluded, …).
    pub warnings: Vec<String>,
}

/// One prepared resource status.
#[derive(Debug, Clone, Serialize)]
pub struct PreparedResource {
    pub id: String,
    pub input_path: Option<String>,
    pub status: String,
    pub engine: Option<String>,
    pub format: Option<String>,
    pub output_path: Option<String>,
    pub n_records: Option<usize>,
    pub n_rows: Option<usize>,
    pub n_columns: Option<usize>,
    pub reason: Option<String>,
}

#[derive(Debug, Clone)]
struct Candidate {
    id: String,
    path: PathBuf,
    format: Option<String>,
}

/// Prepare resources that are already present in the raw cache.
pub fn prepare_raw(request: &RetrieveRequest, opts: &PrepareOptions) -> Result<PrepareResult> {
    if request.dataset_id.trim().is_empty() {
        return Err(Error::InvalidArgument(
            "prepare request dataset_id must be non-empty".into(),
        ));
    }
    let route = &request.route;
    if route.method != "raw_retrieve" {
        return Err(Error::NotFetchable(format!(
            "route {:?} has method {:?}; expected 'raw_retrieve'",
            route.id, route.method
        )));
    }

    let cache_root = match &opts.cache_dir {
        Some(p) => PathBuf::from(p),
        None => default_cache_dir()?,
    };
    let route_dir = route_cache_dir(&cache_root, &request.dataset_id, &route.id);
    let prepared_dir = route_dir.join("prepared");
    fs::create_dir_all(&prepared_dir)?;

    let candidates = candidates(&route_dir, route)?;
    let mut resources = Vec::new();
    let mut ok = true;
    for candidate in &candidates {
        let status = prepare_one(&prepared_dir, candidate);
        ok &= status.status == "prepared" || status.status == "skipped";
        resources.push(status);
    }

    let dataset = assemble_ecostress_dataset(&prepared_dir, &request.dataset_id, &candidates);
    if let Some(dataset) = &dataset {
        ok &= dataset.ok;
    }

    Ok(PrepareResult {
        dir: prepared_dir.to_string_lossy().into_owned(),
        ok,
        route_id: route.id.clone(),
        resources,
        dataset,
    })
}

fn prepare_one(prepared_dir: &Path, candidate: &Candidate) -> PreparedResource {
    let format = resolved_format(candidate);
    let Some(format) = format else {
        return skipped(candidate, None, "unsupported or unknown file extension");
    };
    if format == "ecostress_spectrum_txt" {
        return match prepare_with_ecostress_spectrum_txt(prepared_dir, candidate, &format) {
            Ok(status) => status,
            Err(err) => failed(candidate, "rust_recipe", &format, err),
        };
    }
    match engine_for_format(&format) {
        Some("nirs4all_formats") => match prepare_with_formats(prepared_dir, candidate, &format) {
            Ok(status) => status,
            Err(err) => failed(candidate, "nirs4all_formats", &format, err),
        },
        Some("nirs4all_io") => match prepare_with_io(prepared_dir, candidate, &format) {
            Ok(status) => status,
            Err(err) => failed(candidate, "nirs4all_io", &format, err),
        },
        _ => skipped(
            candidate,
            Some(format),
            "no Rust preparation engine for this format",
        ),
    }
}

fn prepare_with_formats(
    prepared_dir: &Path,
    candidate: &Candidate,
    format: &str,
) -> std::result::Result<PreparedResource, String> {
    let records = nirs4all_formats::open_path(&candidate.path).map_err(|e| e.to_string())?;
    let value = serde_json::to_value(&records).map_err(|e| e.to_string())?;
    let out = safe_join(
        &prepared_dir.join("records"),
        &format!("{}.records.json", safe_segment(&candidate.id)),
    )
    .map_err(|e| e.to_string())?;
    if let Some(parent) = out.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    let text = nirs4all_io::canonical_json(&value).map_err(|e| e.to_string())?;
    fs::write(&out, text).map_err(|e| e.to_string())?;
    Ok(PreparedResource {
        id: candidate.id.clone(),
        input_path: Some(candidate.path.to_string_lossy().into_owned()),
        status: "prepared".into(),
        engine: Some("nirs4all_formats".into()),
        format: Some(format.into()),
        output_path: Some(out.to_string_lossy().into_owned()),
        n_records: Some(records.len()),
        n_rows: None,
        n_columns: None,
        reason: None,
    })
}

fn prepare_with_io(
    prepared_dir: &Path,
    candidate: &Candidate,
    format: &str,
) -> std::result::Result<PreparedResource, String> {
    use nirs4all_io::core::spec::dataset_spec::LoadingParams;
    use nirs4all_io::materialize::loaders::read_table;

    let frame =
        read_table(&candidate.path, &LoadingParams::default()).map_err(|e| e.to_string())?;
    let summary = json!({
        "schema": "nirs4all-datasets.raw_table_summary.v1",
        "input_path": candidate.path.to_string_lossy(),
        "format": format,
        "n_rows": frame.n_rows,
        "n_columns": frame.columns.len(),
        "columns": frame.column_names(),
        "dtypes": frame.dtype_labels(),
        "header_unit": frame.header_unit,
    });
    let out = safe_join(
        &prepared_dir.join("tables"),
        &format!("{}.table.json", safe_segment(&candidate.id)),
    )
    .map_err(|e| e.to_string())?;
    if let Some(parent) = out.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    let text = nirs4all_io::canonical_json(&summary).map_err(|e| e.to_string())?;
    fs::write(&out, text).map_err(|e| e.to_string())?;
    Ok(PreparedResource {
        id: candidate.id.clone(),
        input_path: Some(candidate.path.to_string_lossy().into_owned()),
        status: "prepared".into(),
        engine: Some("nirs4all_io".into()),
        format: Some(format.into()),
        output_path: Some(out.to_string_lossy().into_owned()),
        n_records: None,
        n_rows: Some(frame.n_rows),
        n_columns: Some(frame.columns.len()),
        reason: None,
    })
}

fn prepare_with_ecostress_spectrum_txt(
    prepared_dir: &Path,
    candidate: &Candidate,
    format: &str,
) -> std::result::Result<PreparedResource, String> {
    let text = fs::read_to_string(&candidate.path).map_err(|e| e.to_string())?;
    let parsed = parse_ecostress_spectrum_txt(&text)?;
    let n_points = parsed.x.len();
    let value = json!({
        "schema": "nirs4all-datasets.ecostress_spectrum_txt.v1",
        "input_path": candidate.path.to_string_lossy(),
        "file_name": path_name(&candidate.path),
        "format": format,
        "metadata": parsed.metadata,
        "n_points": n_points,
        "x": parsed.x,
        "y": parsed.y,
    });
    let out = safe_join(
        &prepared_dir.join("records"),
        &format!("{}.ecostress.json", safe_segment(&candidate.id)),
    )
    .map_err(|e| e.to_string())?;
    if let Some(parent) = out.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    let text = nirs4all_io::canonical_json(&value).map_err(|e| e.to_string())?;
    fs::write(&out, text).map_err(|e| e.to_string())?;
    Ok(PreparedResource {
        id: candidate.id.clone(),
        input_path: Some(candidate.path.to_string_lossy().into_owned()),
        status: "prepared".into(),
        engine: Some("rust_recipe".into()),
        format: Some(format.into()),
        output_path: Some(out.to_string_lossy().into_owned()),
        n_records: Some(1),
        n_rows: Some(n_points),
        n_columns: Some(2),
        reason: None,
    })
}

struct EcostressSpectrum {
    metadata: serde_json::Map<String, serde_json::Value>,
    x: Vec<f64>,
    y: Vec<f64>,
}

fn parse_ecostress_spectrum_txt(text: &str) -> std::result::Result<EcostressSpectrum, String> {
    let mut metadata = serde_json::Map::new();
    let mut x = Vec::new();
    let mut y = Vec::new();
    for line in text.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }
        let mut fields = trimmed.split_whitespace();
        let first = fields.next();
        let second = fields.next();
        if let (Some(a), Some(b)) = (first, second) {
            if let (Ok(xv), Ok(yv)) = (a.parse::<f64>(), b.parse::<f64>()) {
                x.push(xv);
                y.push(yv);
                continue;
            }
        }
        if let Some((key, value)) = trimmed.split_once(':') {
            let key = key.trim().to_ascii_lowercase().replace([' ', '.'], "_");
            let value = value.trim();
            if !key.is_empty() {
                metadata.insert(key, serde_json::Value::String(value.to_string()));
            }
        }
    }
    if x.is_empty() {
        return Err("ECOSTRESS spectrum contained no numeric X/Y rows".into());
    }
    if let Some(expected) = metadata
        .get("number_of_x_values")
        .and_then(|v| v.as_str())
        .and_then(|s| s.parse::<usize>().ok())
    {
        if expected != x.len() {
            return Err(format!(
                "ECOSTRESS spectrum declared {expected} X values but parsed {}",
                x.len()
            ));
        }
    }
    Ok(EcostressSpectrum { metadata, x, y })
}

/// Recipe identity for the ECOSTRESS spectrum assembly (mirrors the
/// `canonicalization` block emitted in `catalog/index.json`).
const ECOSTRESS_RECIPE_ID: &str = "jpl_ecostress_spectrum_txt_v1";
const ECOSTRESS_RECIPE_VERSION: &str = "1.0.0";
const ECOSTRESS_DATASET_SCHEMA: &str = "nirs4all-datasets.ecostress_dataset.v1";

/// What is *not* derivable from the retrieved `.spectrum.txt` bytes alone, recorded in
/// the canonical payload so consumers know the boundary of this Rust-side assembly.
const ECOSTRESS_GAP: &str = "Targets/metadata are the raw ECOSTRESS spectrum header fields (e.g. name, type, class, subclass, owner, origin). The NIRS DB standardized column names (material_name<-name, subclass<-subclass, material_type<-type; axis_min/axis_max/n_points_original from the spectral axis), the per-dataset manifest constants (license, citation, instrument, acquisition_mode, publication_doi, rights_status, usage_scope), and the all-missing geographic/biological fields (site, country, latitude, longitude, year, date, species, genus, family) are applied by the upstream NIRS DB standardization (dataset_card.json / raw_manifest.csv) and are not present in the spectrum bytes.";

/// Assemble all ECOSTRESS spectrum resources of a route into one dataset-level
/// canonical payload: a shared spectral axis, the per-observation X matrix, and the
/// per-observation header targets/metadata. Returns `None` when the route has no
/// ECOSTRESS spectrum resource (so non-ECOSTRESS routes are untouched).
fn assemble_ecostress_dataset(
    prepared_dir: &Path,
    dataset_id: &str,
    candidates: &[Candidate],
) -> Option<PreparedDataset> {
    let mut eco: Vec<&Candidate> = candidates
        .iter()
        .filter(|c| resolved_format(c).as_deref() == Some("ecostress_spectrum_txt"))
        .collect();
    if eco.is_empty() {
        return None;
    }
    // Sort by resource id for a deterministic row order that does not depend on how the
    // candidates were collected (explicit resource list vs. cache directory scan).
    eco.sort_by(|a, b| a.id.cmp(&b.id));

    let mut warnings = Vec::new();
    let mut parsed: Vec<(&Candidate, EcostressSpectrum)> = Vec::new();
    for candidate in eco {
        match fs::read_to_string(&candidate.path)
            .map_err(|e| e.to_string())
            .and_then(|text| parse_ecostress_spectrum_txt(&text))
        {
            Ok(spectrum) => parsed.push((candidate, spectrum)),
            Err(reason) => warnings.push(format!(
                "{}: failed to parse spectrum ({reason})",
                candidate.id
            )),
        }
    }
    if parsed.is_empty() {
        return Some(empty_dataset(warnings));
    }

    // The first parsed spectrum fixes the reference axis; any spectrum whose axis does
    // not match (length or values) is excluded from the matrix and reported, never
    // silently resampled — the dataset grouping already guarantees a shared grid.
    let axis = parsed[0].1.x.clone();
    let mut x_matrix: Vec<&Vec<f64>> = Vec::new();
    let mut rows: Vec<&(&Candidate, EcostressSpectrum)> = Vec::new();
    let mut metadata_columns: BTreeSet<String> = BTreeSet::new();
    for entry in &parsed {
        let (candidate, spectrum) = entry;
        if !axis_matches(&axis, &spectrum.x) {
            warnings.push(format!(
                "{}: spectral axis ({} points) does not match the dataset axis ({} points); excluded from the X matrix.",
                candidate.id,
                spectrum.x.len(),
                axis.len()
            ));
            continue;
        }
        x_matrix.push(&spectrum.y);
        for key in spectrum.metadata.keys() {
            metadata_columns.insert(key.clone());
        }
        rows.push(entry);
    }
    if x_matrix.is_empty() {
        return Some(empty_dataset(warnings));
    }

    let axis_min = axis.iter().copied().fold(f64::INFINITY, f64::min);
    let axis_max = axis.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let first_header = &rows[0].1.metadata;
    let x_units = header_str(first_header, "x_units");
    let y_units = header_str(first_header, "y_units");
    let axis_unit = axis_unit_from_x_units(x_units.as_deref());

    let observations: Vec<serde_json::Value> = rows
        .iter()
        .map(|(candidate, spectrum)| {
            json!({
                "observation_id": candidate.id,
                "sample_id": candidate.id,
                "file_name": path_name(&candidate.path),
                "header": spectrum.metadata,
            })
        })
        .collect();
    let metadata_columns: Vec<String> = metadata_columns.into_iter().collect();

    let payload = json!({
        "schema": ECOSTRESS_DATASET_SCHEMA,
        "id": dataset_id,
        "engine": "rust_recipe",
        "recipe_id": ECOSTRESS_RECIPE_ID,
        "recipe_version": ECOSTRESS_RECIPE_VERSION,
        "format_version": "1.0",
        "join_key": "sample_id",
        "alignment_level": "observation",
        "n_observations": x_matrix.len(),
        "n_variables": axis.len(),
        "spectral_axis": axis,
        "axis_unit": axis_unit,
        "axis_min": axis_min,
        "axis_max": axis_max,
        "x_units": x_units,
        "y_units": y_units,
        "sources": [{
            "source_id": "X",
            "path": "x_matrix",
            "n_observations": x_matrix.len(),
            "n_variables": axis.len(),
            "axis_unit": axis_unit,
            "axis_min": axis_min,
            "axis_max": axis_max,
        }],
        "x_matrix": x_matrix,
        "observations": observations,
        "metadata_columns": metadata_columns,
        "gap": ECOSTRESS_GAP,
        "warnings": warnings,
    });

    let output_path = match write_dataset_payload(prepared_dir, &payload) {
        Ok(path) => Some(path),
        Err(reason) => {
            warnings.push(format!(
                "could not write the dataset canonical payload: {reason}"
            ));
            None
        }
    };

    Some(PreparedDataset {
        schema: ECOSTRESS_DATASET_SCHEMA.into(),
        recipe_id: ECOSTRESS_RECIPE_ID.into(),
        engine: "rust_recipe".into(),
        ok: output_path.is_some(),
        output_path,
        n_observations: x_matrix.len(),
        n_variables: axis.len(),
        n_metadata_columns: metadata_columns.len(),
        axis_unit,
        axis_min: Some(axis_min),
        axis_max: Some(axis_max),
        warnings,
    })
}

/// A failed-assembly status (no usable matrix). Keeps the warnings that explain why.
fn empty_dataset(warnings: Vec<String>) -> PreparedDataset {
    PreparedDataset {
        schema: ECOSTRESS_DATASET_SCHEMA.into(),
        recipe_id: ECOSTRESS_RECIPE_ID.into(),
        engine: "rust_recipe".into(),
        ok: false,
        output_path: None,
        n_observations: 0,
        n_variables: 0,
        n_metadata_columns: 0,
        axis_unit: None,
        axis_min: None,
        axis_max: None,
        warnings,
    }
}

/// Write the full canonical payload to `prepared/dataset/canonical.json` and return it.
fn write_dataset_payload(
    prepared_dir: &Path,
    payload: &serde_json::Value,
) -> std::result::Result<String, String> {
    let out =
        safe_join(&prepared_dir.join("dataset"), "canonical.json").map_err(|e| e.to_string())?;
    if let Some(parent) = out.parent() {
        fs::create_dir_all(parent).map_err(|e| e.to_string())?;
    }
    let text = nirs4all_io::canonical_json(payload).map_err(|e| e.to_string())?;
    fs::write(&out, text).map_err(|e| e.to_string())?;
    Ok(out.to_string_lossy().into_owned())
}

/// Two spectral axes match when they have the same length and element-wise values
/// within a small relative tolerance (identical text grids parse bit-for-bit equal;
/// the tolerance only guards against trailing-zero formatting differences).
fn axis_matches(reference: &[f64], other: &[f64]) -> bool {
    reference.len() == other.len()
        && reference
            .iter()
            .zip(other)
            .all(|(a, b)| (a - b).abs() <= 1e-6 * a.abs().max(1.0))
}

/// Best-effort canonical axis unit from an ECOSTRESS `X Units` header value such as
/// `Wavelength (micrometers)`; `None` when the unit is not recognized.
fn axis_unit_from_x_units(x_units: Option<&str>) -> Option<String> {
    let lower = x_units?.to_ascii_lowercase();
    if lower.contains("micromet") || lower.contains("micron") {
        Some("micrometers".into())
    } else if lower.contains("nanomet") {
        Some("nanometers".into())
    } else if lower.contains("wavenumber") || lower.contains("1/cm") || lower.contains("cm-1") {
        Some("wavenumber_cm-1".into())
    } else {
        None
    }
}

/// Read a header field as an owned trimmed string, if present and a string.
fn header_str(metadata: &serde_json::Map<String, serde_json::Value>, key: &str) -> Option<String> {
    metadata
        .get(key)
        .and_then(|v| v.as_str())
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty())
}

fn skipped(candidate: &Candidate, format: Option<String>, reason: &str) -> PreparedResource {
    PreparedResource {
        id: candidate.id.clone(),
        input_path: Some(candidate.path.to_string_lossy().into_owned()),
        status: "skipped".into(),
        engine: None,
        format,
        output_path: None,
        n_records: None,
        n_rows: None,
        n_columns: None,
        reason: Some(reason.into()),
    }
}

fn failed(candidate: &Candidate, engine: &str, format: &str, reason: String) -> PreparedResource {
    PreparedResource {
        id: candidate.id.clone(),
        input_path: Some(candidate.path.to_string_lossy().into_owned()),
        status: "failed".into(),
        engine: Some(engine.into()),
        format: Some(format.into()),
        output_path: None,
        n_records: None,
        n_rows: None,
        n_columns: None,
        reason: Some(reason),
    }
}

fn candidates(route_dir: &Path, route: &RetrievalRoute) -> Result<Vec<Candidate>> {
    let mut out = Vec::new();
    if route.resources.is_empty() {
        collect_cache_files(route_dir, &mut out)?;
        return Ok(out);
    }
    for resource in &route.resources {
        let path = route_dir.join(resource_file_name(resource, &route.locator));
        if path.exists() {
            out.push(Candidate {
                id: resource.id.clone(),
                path,
                format: resource.format.clone(),
            });
        }
        let extracted = route_dir.join("extracted").join(safe_segment(&resource.id));
        if extracted.exists() {
            collect_cache_files(&extracted, &mut out)?;
        }
    }
    Ok(out)
}

fn collect_cache_files(dir: &Path, out: &mut Vec<Candidate>) -> Result<()> {
    if !dir.exists() {
        return Ok(());
    }
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        let name = entry.file_name();
        let name = name.to_string_lossy();
        if name == "prepared" || name.ends_with(".part") {
            continue;
        }
        if path.is_dir() {
            collect_cache_files(&path, out)?;
        } else if path.is_file() {
            out.push(Candidate {
                id: resource_id_for_path(&path),
                format: format_from_name(path_name(&path)).map(str::to_string),
                path,
            });
        }
    }
    Ok(())
}

fn resource_file_name(resource: &RetrievalResource, route_locator: &str) -> String {
    if let Some(name) = &resource.file_name {
        if !name.trim().is_empty() {
            return name.trim().to_string();
        }
    }
    let value = if resource.selector.kind == "direct_url" {
        resource.selector.value.as_str()
    } else {
        route_locator
    };
    path_name(Path::new(value.split(['?', '#']).next().unwrap_or(value))).to_string()
}

fn route_cache_dir(cache_root: &Path, dataset_id: &str, route_id: &str) -> PathBuf {
    cache_root
        .join(dataset_id)
        .join("raw")
        .join(safe_segment(route_id))
}

fn resource_id_for_path(path: &Path) -> String {
    let stem = path
        .file_stem()
        .and_then(|s| s.to_str())
        .unwrap_or("resource");
    safe_segment(stem)
}

fn path_name(path: &Path) -> &str {
    path.file_name()
        .and_then(|s| s.to_str())
        .unwrap_or("resource")
}

fn engine_for_format(format: &str) -> Option<&'static str> {
    match format {
        "jcamp_dx" | "spc" | "mat" | "rda" | "rds" | "openspecy_rds" => Some("nirs4all_formats"),
        "csv" | "csv_gz" | "txt" => Some("nirs4all_io"),
        "ecostress_spectrum_txt" => Some("rust_recipe"),
        _ => None,
    }
}

fn format_from_name(name: &str) -> Option<&'static str> {
    let lower = name.to_ascii_lowercase();
    for (suffix, format) in [
        (".csv.gz", "csv_gz"),
        (".csv", "csv"),
        (".jcamp", "jcamp_dx"),
        (".jcm", "jcamp_dx"),
        (".jdx", "jcamp_dx"),
        (".dx", "jcamp_dx"),
        (".spc", "spc"),
        (".mat", "mat"),
        (".rdata", "rda"),
        (".rda", "rda"),
        (".rds", "rds"),
        // `.spectrum.txt` must precede the generic `.txt` so JPL ECOSTRESS files are
        // routed to the spectrum recipe instead of the generic table reader.
        (".spectrum.txt", "ecostress_spectrum_txt"),
        (".txt", "txt"),
    ] {
        if lower.ends_with(suffix) {
            return Some(format);
        }
    }
    None
}

/// The format used to decode a candidate: the explicit resource format if present,
/// else inferred from the file name. Shared by per-resource prep and dataset assembly
/// so both agree on what an ECOSTRESS spectrum file is.
fn resolved_format(candidate: &Candidate) -> Option<String> {
    candidate
        .format
        .clone()
        .or_else(|| format_from_name(path_name(&candidate.path)).map(str::to_string))
}

fn safe_segment(value: &str) -> String {
    let mut out = String::with_capacity(value.len());
    for ch in value.chars() {
        if ch.is_ascii_alphanumeric() || matches!(ch, '-' | '_' | '.') {
            out.push(ch);
        } else {
            out.push('_');
        }
    }
    if out.is_empty() {
        "resource".into()
    } else {
        out
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::retrieve::{RetrievalSelector, RetrievalUnpack};

    fn route(resource: RetrievalResource) -> RetrievalRoute {
        RetrievalRoute {
            id: "official".into(),
            access: "open".into(),
            method: "raw_retrieve".into(),
            provider: "url".into(),
            locator: "https://example.test".into(),
            landing_url: None,
            api_url: None,
            max_total_bytes: None,
            resources: vec![resource],
        }
    }

    #[test]
    fn prepares_jcamp_with_nirs4all_formats() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        fs::write(
            raw_dir.join("sample.jdx"),
            b"##TITLE=TEST\n##JCAMP-DX=5.00\n##DATA TYPE=INFRARED SPECTRUM\n##XUNITS=1/CM\n##YUNITS=ABSORBANCE\n##XFACTOR=1\n##YFACTOR=1\n##FIRSTX=1000\n##LASTX=1002\n##DELTAX=1\n##NPOINTS=3\n##XYDATA=(X++(Y..Y))\n1000 1 2 3\n##END=\n",
        )
        .unwrap();
        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: route(RetrievalResource {
                id: "sample".into(),
                role: "raw".into(),
                required: true,
                selector: RetrievalSelector {
                    kind: "direct_url".into(),
                    value: "https://example.test/sample.jdx".into(),
                },
                file_name: Some("sample.jdx".into()),
                format: Some("jcamp_dx".into()),
                sha256: None,
                size: None,
                unpack: RetrievalUnpack::default(),
            }),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();
        assert!(result.ok);
        assert_eq!(
            result.resources[0].engine.as_deref(),
            Some("nirs4all_formats")
        );
        assert_eq!(result.resources[0].n_records, Some(1));
        assert!(Path::new(result.resources[0].output_path.as_deref().unwrap()).exists());
    }

    #[test]
    fn prepares_csv_summary_with_nirs4all_io() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        fs::write(raw_dir.join("table.csv"), b"a;b\n1;2\n3;4\n").unwrap();
        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: route(RetrievalResource {
                id: "table".into(),
                role: "raw".into(),
                required: true,
                selector: RetrievalSelector {
                    kind: "direct_url".into(),
                    value: "https://example.test/table.csv".into(),
                },
                file_name: Some("table.csv".into()),
                format: Some("csv".into()),
                sha256: None,
                size: None,
                unpack: RetrievalUnpack::default(),
            }),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();
        assert!(result.ok);
        assert_eq!(result.resources[0].engine.as_deref(), Some("nirs4all_io"));
        assert_eq!(result.resources[0].n_rows, Some(2));
        assert_eq!(result.resources[0].n_columns, Some(2));
    }

    #[test]
    fn prepares_ecostress_spectrum_txt_with_rust_recipe() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        fs::write(
            raw_dir.join("soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt"),
            b"Name: 12070.405\nType: Soil\nWavelength Range: TIR\nFirst Column: X\nSecond Column: Y\nX Units: Wavelength (micrometers)\nY Units: Reflectance (percent)\nNumber of X Values: 3\n\n14.0110\t1.3461\n13.9730\t1.3695\n13.9360\t1.2991\n",
        )
        .unwrap();
        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: route(RetrievalResource {
                id: "lunar_sample".into(),
                role: "spectra".into(),
                required: true,
                selector: RetrievalSelector {
                    kind: "direct_url".into(),
                    value: "https://speclib.jpl.nasa.gov/ecospeclibdata/soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt".into(),
                },
                file_name: Some(
                    "soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt".into(),
                ),
                format: Some("ecostress_spectrum_txt".into()),
                sha256: None,
                size: None,
                unpack: RetrievalUnpack::default(),
            }),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();
        assert!(result.ok);
        assert_eq!(result.resources[0].engine.as_deref(), Some("rust_recipe"));
        assert_eq!(result.resources[0].n_records, Some(1));
        assert_eq!(result.resources[0].n_rows, Some(3));
        assert_eq!(result.resources[0].n_columns, Some(2));
        let output = result.resources[0].output_path.as_deref().unwrap();
        let json = fs::read_to_string(output).unwrap();
        let value: serde_json::Value = serde_json::from_str(&json).unwrap();
        assert_eq!(
            value["schema"],
            "nirs4all-datasets.ecostress_spectrum_txt.v1"
        );
        assert_eq!(value["metadata"]["wavelength_range"], "TIR");
        // A single spectrum still assembles a one-row dataset-level canonical payload.
        let dataset = result
            .dataset
            .expect("single spectrum should assemble a dataset");
        assert!(dataset.ok);
        assert_eq!(dataset.n_observations, 1);
        assert_eq!(dataset.n_variables, 3);
        assert_eq!(dataset.axis_unit.as_deref(), Some("micrometers"));
    }

    fn multi_route(resources: Vec<RetrievalResource>) -> RetrievalRoute {
        RetrievalRoute {
            id: "official".into(),
            access: "open".into(),
            method: "raw_retrieve".into(),
            provider: "url".into(),
            locator: "https://example.test".into(),
            landing_url: None,
            api_url: None,
            max_total_bytes: None,
            resources,
        }
    }

    fn eco_resource(id: &str, file_name: &str) -> RetrievalResource {
        RetrievalResource {
            id: id.into(),
            role: "spectra".into(),
            required: true,
            selector: RetrievalSelector {
                kind: "direct_url".into(),
                value: format!("https://speclib.jpl.nasa.gov/ecospeclibdata/{file_name}"),
            },
            file_name: Some(file_name.into()),
            format: Some("ecostress_spectrum_txt".into()),
            sha256: None,
            size: None,
            unpack: RetrievalUnpack::default(),
        }
    }

    fn eco_spectrum(name: &str, subclass: &str, rows: &[(&str, &str)]) -> String {
        let mut text = format!(
            "Name: {name}\nType: Soil\nClass: Lunar\nSubclass: {subclass}\n\
             Wavelength Range: TIR\nFirst Column: X\nSecond Column: Y\n\
             X Units: Wavelength (micrometers)\nY Units: Reflectance (percent)\n\
             Number of X Values: {}\n\n",
            rows.len()
        );
        for (x, y) in rows {
            text.push_str(&format!("{x}\t{y}\n"));
        }
        text
    }

    #[test]
    fn assembles_ecostress_dataset_from_multiple_spectra() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        // Three spectra on the SAME 3-point axis, with distinct names/subclasses/values.
        let axis = [("14.0110", "1.0"), ("13.9730", "2.0"), ("13.9360", "3.0")];
        let b = [("14.0110", "4.0"), ("13.9730", "5.0"), ("13.9360", "6.0")];
        let c = [("14.0110", "7.0"), ("13.9730", "8.0"), ("13.9360", "9.0")];
        fs::write(
            raw_dir.join("a.spectrum.txt"),
            eco_spectrum("alpha", "Highland", &axis),
        )
        .unwrap();
        fs::write(
            raw_dir.join("b.spectrum.txt"),
            eco_spectrum("beta", "Maria", &b),
        )
        .unwrap();
        fs::write(
            raw_dir.join("c.spectrum.txt"),
            eco_spectrum("gamma", "Transitional", &c),
        )
        .unwrap();

        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: multi_route(vec![
                eco_resource("obs_a", "a.spectrum.txt"),
                eco_resource("obs_b", "b.spectrum.txt"),
                eco_resource("obs_c", "c.spectrum.txt"),
            ]),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();

        assert!(result.ok);
        // Per-resource records are still produced for every spectrum (behavior preserved).
        assert_eq!(result.resources.len(), 3);
        assert!(result
            .resources
            .iter()
            .all(|r| r.engine.as_deref() == Some("rust_recipe")));

        let dataset = result
            .dataset
            .expect("multi-spectrum route must assemble a dataset");
        assert!(dataset.ok);
        assert_eq!(dataset.n_observations, 3);
        assert_eq!(dataset.n_variables, 3);
        assert_eq!(dataset.axis_unit.as_deref(), Some("micrometers"));
        assert!(dataset.warnings.is_empty());

        let output = dataset.output_path.as_deref().unwrap();
        assert!(Path::new(output).exists());
        let value: serde_json::Value =
            serde_json::from_str(&fs::read_to_string(output).unwrap()).unwrap();
        assert_eq!(value["schema"], ECOSTRESS_DATASET_SCHEMA);
        assert_eq!(value["id"], "demo");
        assert_eq!(value["alignment_level"], "observation");
        assert_eq!(value["n_observations"], 3);
        assert_eq!(value["n_variables"], 3);
        // Shared axis is preserved in file order (descending wavelength).
        assert_eq!(
            value["spectral_axis"],
            serde_json::json!([14.011, 13.973, 13.936])
        );
        // X matrix rows align to the sorted observation order (obs_a, obs_b, obs_c).
        assert_eq!(
            value["x_matrix"],
            serde_json::json!([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        );
        assert_eq!(value["observations"][0]["observation_id"], "obs_a");
        assert_eq!(value["observations"][0]["header"]["name"], "alpha");
        assert_eq!(value["observations"][0]["header"]["subclass"], "Highland");
        assert_eq!(value["observations"][2]["header"]["name"], "gamma");
        // The metadata/target columns are the raw spectrum header keys.
        let columns = value["metadata_columns"].as_array().unwrap();
        for key in ["name", "type", "class", "subclass", "wavelength_range"] {
            assert!(
                columns.iter().any(|c| c == key),
                "missing metadata column {key}"
            );
        }
        assert!(value["gap"].as_str().unwrap().contains("material_name"));
    }

    #[test]
    fn excludes_misaligned_ecostress_spectrum_with_warning() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        let three = [("14.0110", "1.0"), ("13.9730", "2.0"), ("13.9360", "3.0")];
        let two = [("14.0110", "1.0"), ("13.9730", "2.0")];
        // Ids sort so the 3-point spectra come first and fix the reference axis.
        fs::write(
            raw_dir.join("a.spectrum.txt"),
            eco_spectrum("alpha", "Highland", &three),
        )
        .unwrap();
        fs::write(
            raw_dir.join("b.spectrum.txt"),
            eco_spectrum("beta", "Maria", &three),
        )
        .unwrap();
        fs::write(
            raw_dir.join("z.spectrum.txt"),
            eco_spectrum("zeta", "Other", &two),
        )
        .unwrap();

        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: multi_route(vec![
                eco_resource("obs_a", "a.spectrum.txt"),
                eco_resource("obs_b", "b.spectrum.txt"),
                eco_resource("obs_z", "z.spectrum.txt"),
            ]),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();

        let dataset = result.dataset.expect("dataset should still assemble");
        assert!(dataset.ok);
        assert_eq!(
            dataset.n_observations, 2,
            "the misaligned spectrum must be excluded"
        );
        assert_eq!(dataset.n_variables, 3);
        assert!(
            dataset
                .warnings
                .iter()
                .any(|w| w.contains("obs_z") && w.contains("excluded")),
            "expected an exclusion warning for obs_z, got {:?}",
            dataset.warnings
        );
    }

    #[test]
    fn non_ecostress_route_has_no_dataset_assembly() {
        let dir = tempfile::tempdir().unwrap();
        let raw_dir = dir.path().join("demo/raw/official");
        fs::create_dir_all(&raw_dir).unwrap();
        fs::write(raw_dir.join("table.csv"), b"a;b\n1;2\n3;4\n").unwrap();
        let request = RetrieveRequest {
            dataset_id: "demo".into(),
            route: route(RetrievalResource {
                id: "table".into(),
                role: "raw".into(),
                required: true,
                selector: RetrievalSelector {
                    kind: "direct_url".into(),
                    value: "https://example.test/table.csv".into(),
                },
                file_name: Some("table.csv".into()),
                format: Some("csv".into()),
                sha256: None,
                size: None,
                unpack: RetrievalUnpack::default(),
            }),
        };
        let result = prepare_raw(
            &request,
            &PrepareOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
            },
        )
        .unwrap();
        assert!(result.ok);
        assert!(
            result.dataset.is_none(),
            "non-ECOSTRESS routes must not assemble a dataset"
        );
    }
}
