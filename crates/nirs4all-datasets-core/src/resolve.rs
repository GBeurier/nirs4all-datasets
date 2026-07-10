// SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
//! Resolve a dataset id, via the distributable index, to its complete download
//! contract. Pure and offline — it only reads JSON.

use crate::error::{Error, Result};
use crate::model::{Index, Resolved};

/// Look up `dataset_id` in a parsed [`Index`] and return its [`Resolved`] contract.
pub fn resolve(index: &Index, dataset_id: &str) -> Result<Resolved> {
    index
        .datasets
        .get(dataset_id)
        .map(|entry| Resolved::from_entry(dataset_id, entry))
        .ok_or_else(|| Error::UnknownDataset(dataset_id.to_string()))
}

/// Parse an index JSON string and resolve `dataset_id`, returning the [`Resolved`]
/// contract serialized as JSON (the C ABI's `n4ds_resolve` payload).
pub fn resolve_json(index_json: &str, dataset_id: &str) -> Result<String> {
    let index: Index = serde_json::from_str(index_json)?;
    let resolved = resolve(&index, dataset_id)?;
    Ok(serde_json::to_string(&resolved)?)
}

#[cfg(test)]
mod tests {
    use super::*;

    const INDEX: &str = r#"{
      "schema": "1.0", "n_datasets": 1,
      "datasets": {
        "demo": {
          "tier": "public",
          "dataverse": {"instance": "https://dv.example", "doi": "10.70112/ABC", "dataset_version": "1.0"},
          "files": [{"name":"X.parquet","relpath":"canonical/sources/X.parquet","directory_label":"canonical/sources","sha256":"aa","size":9,"file_id":42}],
          "origins": [{"kind":"zenodo","mode":"canonical","locator":"10.5281/zenodo.5","access":"open"}],
          "retrieval": {"schema_version":"1.0","status":"raw_reproducible","routes":[{"id":"official","method":"raw_retrieve","provider":"url","locator":"https://example.test/raw.csv","resources":[{"id":"raw","selector":{"kind":"direct_url","value":"https://example.test/raw.csv"}}]}]},
          "descriptor": {"id":"demo","sources":[{"source_id":"X","modality":"NIR"}],"variables":[{"name":"target","role":"target","type":"numeric"}],"ids":{"sample_id":"sample_id"}}
        }
      }
    }"#;
    const BRIDGE_INDEX: &str = include_str!("../../../tests/goldens/nonpython_bridge/index.json");
    const BRIDGE_RESOLVED: &str =
        include_str!("../../../tests/goldens/nonpython_bridge/resolved_contract.json");

    #[test]
    fn resolves_known_dataset() {
        let r = resolve_json(INDEX, "demo").unwrap();
        let v: serde_json::Value = serde_json::from_str(&r).unwrap();
        assert_eq!(v["id"], "demo");
        assert_eq!(v["tier"], "public");
        assert_eq!(v["instance"], "https://dv.example");
        assert_eq!(v["doi"], "10.70112/ABC");
        assert_eq!(v["files"][0]["file_id"], 42);
        assert_eq!(v["retrieval"]["status"], "raw_reproducible");
        assert_eq!(
            v["retrieval"]["routes"][0]["resources"][0]["selector"]["kind"],
            "direct_url"
        );
        assert_eq!(v["descriptor"]["id"], "demo");
        assert_eq!(v["descriptor"]["sources"][0]["source_id"], "X");
        assert_eq!(v["descriptor"]["variables"][0]["role"], "target");
    }

    #[test]
    fn unknown_dataset_errors() {
        let err = resolve_json(INDEX, "nope").unwrap_err();
        assert!(matches!(err, Error::UnknownDataset(_)));
    }

    #[test]
    fn bridge_golden_preserves_descriptor_materialization_contract() {
        let r = resolve_json(BRIDGE_INDEX, "bridge_native").unwrap();
        let produced: serde_json::Value = serde_json::from_str(&r).unwrap();
        let expected: serde_json::Value = serde_json::from_str(BRIDGE_RESOLVED).unwrap();
        assert_eq!(produced, expected);
        assert_eq!(produced["descriptor"]["retrieval"], produced["retrieval"]);
        assert_eq!(produced["descriptor"]["sources"][0]["source_id"], "X1");
        assert_eq!(produced["descriptor"]["sources"][1]["source_id"], "X2");
        assert_eq!(produced["descriptor"]["variables"][0]["role"], "target");
        assert!(produced["files"]
            .as_array()
            .unwrap()
            .iter()
            .any(|file| file["relpath"] == "canonical/dataset.json"));
        assert!(produced["files"]
            .as_array()
            .unwrap()
            .iter()
            .any(|file| file["relpath"] == "canonical/splits/original.parquet"));
    }
}
