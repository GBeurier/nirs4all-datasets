// SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
//! Raw-resource retrieval engine.
//!
//! This is deliberately narrower than canonical [`crate::fetch`]: it retrieves raw
//! origin resources into a cache and reports what happened. It does not claim that
//! the resulting dataset is byte-identical to the canonical manifest; callers must
//! run a canonicalization layer (`nirs4all-io`, `nirs4all-formats`, or a recipe)
//! before exposing a dataset object.

use std::fs;
use std::io::{self, Write};
use std::path::{Path, PathBuf};

use serde::{Deserialize, Serialize};

use crate::cache::{default_cache_dir, part_path, safe_join};
use crate::error::{Error, Result};
use crate::hash::{sha256_hex_file, HashingWriter};
use crate::http::HttpClient;
use crate::origins::{ckan, dataverse, figshare, zenodo};

const DEFAULT_MAX_TOTAL_BYTES: u64 = 1_000_000_000;

/// Raw-retrieval request accepted by the C/Python ABI.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RetrieveRequest {
    /// Dataset id; used only to namespace the cache.
    pub dataset_id: String,
    /// Retrieval route, usually copied from `descriptor.retrieval.routes[]`.
    pub route: RetrievalRoute,
}

/// Options for raw-resource retrieval.
#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct RetrieveOptions {
    /// Cache root. Defaults to the same OS cache root as canonical fetch.
    #[serde(default)]
    pub cache_dir: Option<String>,
    /// Per-request timeout, interpreted by the concrete HTTP client.
    #[serde(default)]
    pub timeout_secs: Option<u64>,
    /// Safety cap for the total downloaded bytes in this call.
    #[serde(default)]
    pub max_total_bytes: Option<u64>,
}

impl RetrieveOptions {
    /// Parse options from JSON; empty/null means defaults.
    pub fn from_json(s: &str) -> Result<RetrieveOptions> {
        if s.trim().is_empty() {
            Ok(RetrieveOptions::default())
        } else {
            Ok(serde_json::from_str(s)?)
        }
    }
}

/// One retrieval route.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RetrievalRoute {
    pub id: String,
    #[serde(default)]
    pub access: String,
    #[serde(default)]
    pub method: String,
    #[serde(default)]
    pub provider: String,
    pub locator: String,
    #[serde(default)]
    pub landing_url: Option<String>,
    #[serde(default)]
    pub api_url: Option<String>,
    #[serde(default)]
    pub max_total_bytes: Option<u64>,
    #[serde(default)]
    pub resources: Vec<RetrievalResource>,
}

/// One retrievable resource.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RetrievalResource {
    pub id: String,
    #[serde(default)]
    pub role: String,
    #[serde(default = "default_true")]
    pub required: bool,
    pub selector: RetrievalSelector,
    #[serde(default)]
    pub file_name: Option<String>,
    #[serde(default)]
    pub format: Option<String>,
    #[serde(default)]
    pub sha256: Option<String>,
    #[serde(default)]
    pub size: Option<u64>,
    #[serde(default)]
    pub unpack: RetrievalUnpack,
}

/// Provider-specific selector.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RetrievalSelector {
    pub kind: String,
    pub value: String,
}

/// Archive extraction instruction.
#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct RetrievalUnpack {
    #[serde(default)]
    pub archive: bool,
    #[serde(default)]
    pub members: Vec<String>,
}

/// Result returned by raw retrieval.
#[derive(Debug, Clone, Serialize)]
pub struct RetrieveResult {
    pub dir: String,
    pub ok: bool,
    pub verified: bool,
    pub route_id: String,
    pub resources: Vec<ResourceStatus>,
}

/// One resource's status.
#[derive(Debug, Clone, Serialize)]
pub struct ResourceStatus {
    pub id: String,
    pub path: Option<String>,
    pub status: String,
    pub verified: bool,
    pub sha256: Option<String>,
    pub bytes: Option<u64>,
    pub extracted: Vec<String>,
    pub reason: Option<String>,
}

/// Retrieve raw resources for one route.
pub fn retrieve_raw(
    request: &RetrieveRequest,
    opts: &RetrieveOptions,
    http: &dyn HttpClient,
) -> Result<RetrieveResult> {
    if request.dataset_id.trim().is_empty() {
        return Err(Error::InvalidArgument(
            "retrieve request dataset_id must be non-empty".into(),
        ));
    }
    let route = &request.route;
    if route.method != "raw_retrieve" {
        return Err(Error::NotFetchable(format!(
            "route {:?} has method {:?}; expected 'raw_retrieve'",
            route.id, route.method
        )));
    }
    if route.access != "open" && !route.access.is_empty() {
        return Err(Error::NotFetchable(format!(
            "route {:?} is not open (access={:?})",
            route.id, route.access
        )));
    }

    let cache_root = match &opts.cache_dir {
        Some(p) => PathBuf::from(p),
        None => default_cache_dir()?,
    };
    let route_dir = cache_root
        .join(&request.dataset_id)
        .join("raw")
        .join(safe_segment(&route.id));
    fs::create_dir_all(&route_dir)?;

    let limit = opts
        .max_total_bytes
        .or(route.max_total_bytes)
        .unwrap_or(DEFAULT_MAX_TOTAL_BYTES);
    let mut total = 0_u64;
    let mut statuses = Vec::new();
    let mut all_ok = true;
    let mut all_verified = true;

    let resources = if route.resources.is_empty() {
        match resources_from_route(route, http) {
            Ok(resources) => resources,
            Err(err) => {
                return Ok(RetrieveResult {
                    dir: route_dir.to_string_lossy().into_owned(),
                    ok: false,
                    verified: false,
                    route_id: route.id.clone(),
                    resources: vec![ResourceStatus {
                        id: "resource".into(),
                        path: None,
                        status: "failed".into(),
                        verified: false,
                        sha256: None,
                        bytes: None,
                        extracted: Vec::new(),
                        reason: Some(err.to_string()),
                    }],
                });
            }
        }
    } else {
        route.resources.clone()
    };

    for resource in resources {
        match retrieve_one(&route_dir, route, &resource, http, limit, &mut total) {
            Ok(status) => {
                all_ok &= matches!(
                    status.status.as_str(),
                    "cached" | "cached_unverified" | "downloaded" | "downloaded_unverified"
                );
                all_verified &= status.verified;
                statuses.push(status);
            }
            Err(err) => {
                if resource.required {
                    all_ok = false;
                }
                all_verified = false;
                statuses.push(ResourceStatus {
                    id: resource.id,
                    path: None,
                    status: "failed".into(),
                    verified: false,
                    sha256: None,
                    bytes: None,
                    extracted: Vec::new(),
                    reason: Some(err.to_string()),
                });
            }
        }
    }

    Ok(RetrieveResult {
        dir: route_dir.to_string_lossy().into_owned(),
        ok: all_ok,
        verified: all_verified,
        route_id: route.id.clone(),
        resources: statuses,
    })
}

fn retrieve_one(
    route_dir: &Path,
    route: &RetrievalRoute,
    resource: &RetrievalResource,
    http: &dyn HttpClient,
    limit: u64,
    total: &mut u64,
) -> Result<ResourceStatus> {
    let url = resource_url(route, resource, http)?;
    let file_name = resource_file_name(resource, &url)?;
    let dest = safe_join(route_dir, &file_name)?;
    let expected = resource.sha256.as_ref().map(|s| s.to_lowercase());

    if dest.exists() {
        let actual = sha256_hex_file(&dest)?;
        let meta = fs::metadata(&dest)?;
        if expected.as_ref().map(|s| s == &actual).unwrap_or(true) {
            let extracted = extract_if_requested(route_dir, resource, &dest)?;
            return Ok(ResourceStatus {
                id: resource.id.clone(),
                path: Some(dest.to_string_lossy().into_owned()),
                status: if expected.is_some() {
                    "cached"
                } else {
                    "cached_unverified"
                }
                .into(),
                verified: expected.is_some(),
                sha256: Some(actual),
                bytes: Some(meta.len()),
                extracted,
                reason: None,
            });
        }
    }

    let tmp = part_path(&dest);
    if let Some(parent) = dest.parent() {
        fs::create_dir_all(parent)?;
    }
    let resp = http.get(&url, &[], true, None)?;
    if !resp.is_success() {
        return Err(Error::Http(format!(
            "raw retrieval {} failed: HTTP {}",
            resource.id, resp.status
        )));
    }

    let mut body = resp.body;
    let mut hw = HashingWriter::new(fs::File::create(&tmp)?);
    let bytes = match copy_limited(&mut body, &mut hw, limit, total) {
        Ok(n) => n,
        Err(e) => {
            let _ = fs::remove_file(&tmp);
            return Err(e);
        }
    };
    let (file, actual, _n) = hw.finish();
    file.sync_all().ok();

    if let Some(expected) = &expected {
        if actual != *expected {
            let _ = fs::remove_file(&tmp);
            return Err(Error::ChecksumMismatch {
                name: resource.id.clone(),
                expected: expected.clone(),
                actual,
            });
        }
    }
    if dest.exists() {
        let _ = fs::remove_file(&dest);
    }
    if let Err(e) = fs::rename(&tmp, &dest) {
        let _ = fs::remove_file(&tmp);
        return Err(e.into());
    }
    let extracted = extract_if_requested(route_dir, resource, &dest)?;
    Ok(ResourceStatus {
        id: resource.id.clone(),
        path: Some(dest.to_string_lossy().into_owned()),
        status: if expected.is_some() {
            "downloaded"
        } else {
            "downloaded_unverified"
        }
        .into(),
        verified: expected.is_some(),
        sha256: Some(actual),
        bytes: Some(bytes),
        extracted,
        reason: None,
    })
}

fn copy_limited<R: io::Read, W: Write>(
    reader: &mut R,
    writer: &mut W,
    limit: u64,
    total: &mut u64,
) -> Result<u64> {
    let mut buf = vec![0_u8; 1 << 20];
    let mut written = 0_u64;
    loop {
        let n = reader.read(&mut buf)?;
        if n == 0 {
            break;
        }
        *total += n as u64;
        written += n as u64;
        if *total > limit {
            return Err(Error::NotFetchable(format!(
                "raw retrieval exceeds the configured {:.3} GB limit",
                limit as f64 / 1_000_000_000.0
            )));
        }
        writer.write_all(&buf[..n])?;
    }
    Ok(written)
}

fn resource_url(
    route: &RetrievalRoute,
    resource: &RetrievalResource,
    http: &dyn HttpClient,
) -> Result<String> {
    match resource.selector.kind.as_str() {
        "direct_url" => Ok(resource.selector.value.clone()),
        "api_file_name" => lookup_named_resource(route, resource, http, &resource.selector.value),
        "zenodo_key" if route.provider == "zenodo" => {
            lookup_named_resource(route, resource, http, &resource.selector.value)
        }
        "figshare_file_id" if route.provider == "figshare" => {
            let id = resource.selector.value.parse::<i64>().map_err(|_| {
                Error::InvalidArgument(format!(
                    "figshare_file_id selector for resource {:?} must be an integer",
                    resource.id
                ))
            })?;
            figshare::list_file_records(http, &route.locator)?
                .into_iter()
                .find(|f| f.id == id)
                .map(|f| f.url)
                .ok_or_else(|| {
                    Error::NotFetchable(format!(
                        "figshare article {:?} has no file id {} for resource {:?}",
                        route.locator, id, resource.id
                    ))
                })
        }
        "dataverse_file_id" if route.provider == "dataverse" => {
            let id = resource.selector.value.parse::<i64>().map_err(|_| {
                Error::InvalidArgument(format!(
                    "dataverse_file_id selector for resource {:?} must be an integer",
                    resource.id
                ))
            })?;
            Ok(dataverse::access_url(&dataverse_instance(route, http)?, id))
        }
        "archive_member" | "doi" => Err(Error::NotFetchable(format!(
            "selector kind {:?} for resource {:?} needs a higher-level archive/DOI route",
            resource.selector.kind, resource.id
        ))),
        _ if route.provider == "url" && route.locator.starts_with("http") => {
            Ok(route.locator.clone())
        }
        _ => Err(Error::NotFetchable(format!(
            "unsupported selector kind {:?} for resource {:?}",
            resource.selector.kind, resource.id
        ))),
    }
}

fn lookup_named_resource(
    route: &RetrievalRoute,
    resource: &RetrievalResource,
    http: &dyn HttpClient,
    name: &str,
) -> Result<String> {
    let by_name = match route.provider.as_str() {
        "zenodo" => zenodo::list_files(http, &route.locator),
        "figshare" => figshare::list_files(http, &route.locator),
        "dataverse" => dataverse::list_files_by_doi(http, &route.locator),
        "ckan" => ckan::list_files(http, &route.locator),
        provider => Err(Error::NotFetchable(format!(
            "provider {provider:?} does not support named resource lookup"
        ))),
    }?;
    by_name.get(name).cloned().ok_or_else(|| {
        Error::NotFetchable(format!(
            "provider {:?} locator {:?} has no resource named {:?} for {:?}",
            route.provider, route.locator, name, resource.id
        ))
    })
}

fn dataverse_instance(route: &RetrievalRoute, http: &dyn HttpClient) -> Result<String> {
    for value in [&route.api_url, &route.landing_url] {
        if let Some(url) = value.as_deref().filter(|u| u.starts_with("http")) {
            if let Some(instance) = scheme_host(url) {
                return Ok(instance);
            }
        }
    }
    if route.locator.starts_with("http") {
        if let Some(instance) = scheme_host(&route.locator) {
            return Ok(instance);
        }
    }
    dataverse::instance_from_doi(http, &route.locator)
}

fn scheme_host(url: &str) -> Option<String> {
    let (scheme, rest) = url.split_once("://")?;
    let host = rest.split('/').next()?;
    if host.is_empty() {
        None
    } else {
        Some(format!("{scheme}://{host}"))
    }
}

fn resource_file_name(resource: &RetrievalResource, url: &str) -> Result<String> {
    if let Some(name) = &resource.file_name {
        if !name.trim().is_empty() {
            return Ok(name.trim().to_string());
        }
    }
    let clean_url = url.split(['?', '#']).next().unwrap_or(url);
    let name = clean_url.rsplit('/').next().unwrap_or("").trim();
    if !name.is_empty() {
        Ok(name.to_string())
    } else {
        Ok(resource.id.clone())
    }
}

fn resources_from_route(
    route: &RetrievalRoute,
    http: &dyn HttpClient,
) -> Result<Vec<RetrievalResource>> {
    if route.provider == "url" {
        return Ok(vec![resource_from_url(
            "resource".into(),
            route.locator.clone(),
            None,
        )]);
    }

    let by_name = match route.provider.as_str() {
        "zenodo" => zenodo::list_files(http, &route.locator),
        "figshare" => figshare::list_files(http, &route.locator),
        "dataverse" => dataverse::list_files_by_doi(http, &route.locator),
        "ckan" => ckan::list_files(http, &route.locator),
        provider => Err(Error::NotFetchable(format!(
            "provider {provider:?} cannot enumerate route resources"
        ))),
    }?;
    if by_name.is_empty() {
        return Err(Error::NotFetchable(format!(
            "provider {:?} locator {:?} exposed no files",
            route.provider, route.locator
        )));
    }
    Ok(by_name
        .into_iter()
        .enumerate()
        .map(|(i, (name, url))| {
            resource_from_url(format!("resource_{:03}", i + 1), url, Some(name))
        })
        .collect())
}

fn resource_from_url(id: String, url: String, file_name: Option<String>) -> RetrievalResource {
    let format = file_name
        .as_deref()
        .and_then(format_from_name)
        .unwrap_or("unknown")
        .to_string();
    RetrievalResource {
        id,
        role: "raw".into(),
        required: true,
        selector: RetrievalSelector {
            kind: "direct_url".into(),
            value: url,
        },
        file_name,
        format: Some(format),
        sha256: None,
        size: None,
        unpack: RetrievalUnpack::default(),
    }
}

fn format_from_name(name: &str) -> Option<&'static str> {
    let lower = name.to_ascii_lowercase();
    for (suffix, format) in [
        (".csv.gz", "csv_gz"),
        (".csv", "csv"),
        (".xlsx", "xlsx"),
        (".xls", "xlsx"),
        (".zip", "zip"),
        (".mat", "mat"),
        (".rda", "rda"),
        (".sqlite", "sqlite"),
        (".db", "sqlite"),
        (".spc", "spc"),
        (".parquet", "parquet"),
        (".json", "json"),
        (".txt", "txt"),
    ] {
        if lower.ends_with(suffix) {
            return Some(format);
        }
    }
    None
}

fn default_true() -> bool {
    true
}

fn extract_if_requested(
    route_dir: &Path,
    resource: &RetrievalResource,
    archive_path: &Path,
) -> Result<Vec<String>> {
    let wants_archive = resource.unpack.archive || resource.format.as_deref() == Some("zip");
    if !wants_archive {
        return Ok(Vec::new());
    }
    let file = fs::File::open(archive_path)?;
    let mut archive = zip::ZipArchive::new(file).map_err(|e| {
        Error::InvalidArgument(format!(
            "could not read ZIP archive {}: {e}",
            archive_path.display()
        ))
    })?;
    let extract_dir = route_dir.join("extracted").join(safe_segment(&resource.id));
    fs::create_dir_all(&extract_dir)?;
    let wanted: std::collections::BTreeSet<&str> =
        resource.unpack.members.iter().map(String::as_str).collect();
    let mut out = Vec::new();
    for i in 0..archive.len() {
        let mut file = archive.by_index(i).map_err(|e| {
            Error::InvalidArgument(format!("could not inspect ZIP member {i}: {e}"))
        })?;
        if file.is_dir() {
            continue;
        }
        let name = file.name().to_string();
        if !wanted.is_empty() && !wanted.contains(name.as_str()) {
            continue;
        }
        let dest = safe_join(&extract_dir, &name)?;
        if let Some(parent) = dest.parent() {
            fs::create_dir_all(parent)?;
        }
        let mut writer = fs::File::create(&dest)?;
        io::copy(&mut file, &mut writer)?;
        out.push(dest.to_string_lossy().into_owned());
    }
    Ok(out)
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
        "route".into()
    } else {
        out
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::hash::sha256_hex_bytes;
    use crate::http::testing::{MockHttp, MockResponse};

    #[test]
    fn retrieves_direct_url_with_checksum() {
        let body = b"raw bytes";
        let sha = sha256_hex_bytes(body);
        let dir = tempfile::tempdir().unwrap();
        let req = RetrieveRequest {
            dataset_id: "demo".into(),
            route: RetrievalRoute {
                id: "official".into(),
                access: "open".into(),
                method: "raw_retrieve".into(),
                provider: "url".into(),
                locator: "https://example.test/raw.csv".into(),
                landing_url: None,
                api_url: None,
                max_total_bytes: None,
                resources: vec![RetrievalResource {
                    id: "spectra".into(),
                    role: "spectra".into(),
                    required: true,
                    selector: RetrievalSelector {
                        kind: "direct_url".into(),
                        value: "https://example.test/raw.csv".into(),
                    },
                    file_name: Some("raw.csv".into()),
                    format: Some("csv".into()),
                    sha256: Some(sha.clone()),
                    size: None,
                    unpack: RetrievalUnpack::default(),
                }],
            },
        };
        let http = MockHttp::new(move |_| MockResponse::ok(body.to_vec()));
        let res = retrieve_raw(
            &req,
            &RetrieveOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
                timeout_secs: None,
                max_total_bytes: None,
            },
            &http,
        )
        .unwrap();
        assert!(res.ok);
        assert!(res.verified);
        assert_eq!(res.resources[0].status, "downloaded");
        assert_eq!(res.resources[0].sha256.as_deref(), Some(sha.as_str()));
    }

    #[test]
    fn resolves_zenodo_key_before_download() {
        let dir = tempfile::tempdir().unwrap();
        let req = RetrieveRequest {
            dataset_id: "demo".into(),
            route: RetrievalRoute {
                id: "zenodo_raw".into(),
                access: "open".into(),
                method: "raw_retrieve".into(),
                provider: "zenodo".into(),
                locator: "10.5281/zenodo.123".into(),
                landing_url: None,
                api_url: None,
                max_total_bytes: None,
                resources: vec![RetrievalResource {
                    id: "archive".into(),
                    role: "archive".into(),
                    required: true,
                    selector: RetrievalSelector {
                        kind: "zenodo_key".into(),
                        value: "demo.zip".into(),
                    },
                    file_name: Some("demo.zip".into()),
                    format: Some("unknown".into()),
                    sha256: None,
                    size: None,
                    unpack: RetrievalUnpack::default(),
                }],
            },
        };
        let http = MockHttp::new(|call| {
            if call.url.contains("/api/records/123") {
                MockResponse::ok(
                    br#"{"files":[{"key":"demo.zip","links":{"self":"https://zenodo.example/files/demo.zip"}}]}"#.to_vec(),
                )
            } else {
                MockResponse::ok(b"zip bytes".to_vec())
            }
        });
        let res = retrieve_raw(
            &req,
            &RetrieveOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
                timeout_secs: None,
                max_total_bytes: None,
            },
            &http,
        )
        .unwrap();
        assert!(res.ok);
        assert!(!res.verified);
        assert_eq!(res.resources[0].status, "downloaded_unverified");
        assert_eq!(http.call_count(), 2);
    }

    #[test]
    fn enumerates_provider_route_when_resources_are_empty() {
        let dir = tempfile::tempdir().unwrap();
        let req = RetrieveRequest {
            dataset_id: "demo".into(),
            route: RetrievalRoute {
                id: "zenodo_all".into(),
                access: "open".into(),
                method: "raw_retrieve".into(),
                provider: "zenodo".into(),
                locator: "https://zenodo.org/records/123".into(),
                landing_url: None,
                api_url: None,
                max_total_bytes: None,
                resources: Vec::new(),
            },
        };
        let http = MockHttp::new(|call| {
            if call.url.contains("/api/records/123") {
                MockResponse::ok(
                    br#"{"files":[{"key":"demo.csv","links":{"self":"https://zenodo.example/files/demo.csv"}}]}"#.to_vec(),
                )
            } else {
                MockResponse::ok(b"a,b\n1,2\n".to_vec())
            }
        });
        let res = retrieve_raw(
            &req,
            &RetrieveOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
                timeout_secs: None,
                max_total_bytes: None,
            },
            &http,
        )
        .unwrap();
        assert!(res.ok);
        assert_eq!(res.resources[0].id, "resource_001");
        assert!(res.resources[0]
            .path
            .as_deref()
            .unwrap()
            .ends_with("demo.csv"));
    }

    #[test]
    fn retrieves_ckan_route_by_enumerating_package_show() {
        let dir = tempfile::tempdir().unwrap();
        let req = RetrieveRequest {
            dataset_id: "ecosis_demo".into(),
            route: RetrievalRoute {
                id: "origin_001".into(),
                access: "open".into(),
                method: "raw_retrieve".into(),
                provider: "ckan".into(),
                locator: "https://data.ecosis.org/dataset/3d-lma-leaf-level-spectra".into(),
                landing_url: Some(
                    "https://data.ecosis.org/dataset/3d-lma-leaf-level-spectra".into(),
                ),
                api_url: Some(
                    "https://data.ecosis.org/api/3/action/package_show?id=3d-lma-leaf-level-spectra"
                        .into(),
                ),
                max_total_bytes: None,
                resources: Vec::new(),
            },
        };
        let http = MockHttp::new(|call| {
            if call.url.contains("/api/3/action/package_show") {
                MockResponse::ok(
                    br#"{"success":true,"result":{"resources":[
                        {"name":"spectra.csv","url":"https://data.ecosis.org/dataset/p/resource/a/download/spectra.csv"}
                    ]}}"#
                        .to_vec(),
                )
            } else {
                MockResponse::ok(b"wave,refl\n400,0.1\n".to_vec())
            }
        });
        let res = retrieve_raw(
            &req,
            &RetrieveOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
                timeout_secs: None,
                max_total_bytes: None,
            },
            &http,
        )
        .unwrap();
        assert!(res.ok);
        assert!(!res.verified); // raw retrieval: no canonical SHA-256 to check against
        assert_eq!(res.resources.len(), 1);
        assert!(res.resources[0]
            .path
            .as_deref()
            .unwrap()
            .ends_with("spectra.csv"));
        assert_eq!(http.call_count(), 2); // package_show + one download
    }

    #[test]
    fn rejects_size_guard_and_removes_part() {
        let dir = tempfile::tempdir().unwrap();
        let req = RetrieveRequest {
            dataset_id: "demo".into(),
            route: RetrievalRoute {
                id: "official".into(),
                access: "open".into(),
                method: "raw_retrieve".into(),
                provider: "url".into(),
                locator: "https://example.test/raw.csv".into(),
                landing_url: None,
                api_url: None,
                max_total_bytes: Some(2),
                resources: Vec::new(),
            },
        };
        let http = MockHttp::new(|_| MockResponse::ok(b"too large".to_vec()));
        let res = retrieve_raw(
            &req,
            &RetrieveOptions {
                cache_dir: Some(dir.path().to_string_lossy().into_owned()),
                timeout_secs: None,
                max_total_bytes: None,
            },
            &http,
        )
        .unwrap();
        assert!(!res.ok);
        assert_eq!(res.resources[0].status, "failed");
        assert!(!dir.path().join("demo/raw/official/raw.csv.part").exists());
    }
}
