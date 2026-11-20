// SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
//! Filesystem-free origin recipes. The host transports declared original bytes;
//! IO reads tables and materializes the declared roles, identity and masks.

use std::collections::HashSet;
use std::sync::OnceLock;

use nirs4all_io_core::materialize::frame::Cell;
use nirs4all_io_core::materialize::loaders::read_table_bytes;
use nirs4all_io_core::spec::dataset_spec::LoadingParams;
use serde::{Deserialize, Serialize};
use serde_json::{json, Map, Value};

use crate::error::{Error, Result};
use crate::hash::sha256_hex_bytes;

const METADATA: &str = include_str!("browser_origin_metadata.json");
const PROFILE: &str = "public-single-table-v1";

/// Named original or prepared bytes, with no filesystem or network authority.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BrowserFile {
    pub name: String,
    pub bytes: Vec<u8>,
}

/// Inputs to the existing IO in-memory assembler; no inferred dataset policy.
#[derive(Debug, Serialize)]
pub struct BrowserPrepared {
    pub files: Vec<BrowserFile>,
    pub record_sets: Vec<Value>,
    pub spec: Value,
    pub provenance: Value,
}

fn metadata() -> &'static Value {
    static VALUE: OnceLock<Value> = OnceLock::new();
    VALUE.get_or_init(|| serde_json::from_str(METADATA).expect("generated public origin metadata"))
}

fn refuse(message: impl Into<String>) -> Error {
    Error::NotFetchable(message.into())
}

fn provenance(descriptor: &Value) -> Value {
    json!({"owner_version": env!("CARGO_PKG_VERSION"), "profile": PROFILE,
           "index_sha256": metadata()["index_sha256"], "recipes_sha256": metadata()["recipes_sha256"],
           "ids": descriptor["ids"], "alignment_level": descriptor["alignment_level"],
           "representation": "original-source-tables", "canonical_identity_claimed": false})
}

fn reason(entry: &Value, recipe: Option<&Value>) -> Option<String> {
    let descriptor = &entry["descriptor"];
    let routes = entry["retrieval"]["routes"].as_array();
    if !routes.is_some_and(|routes| {
        routes.iter().any(|route| {
            route["id"] == "public_origin_recipe"
                && route["access"] == "open"
                && route["automated_download_allowed"] == true
        })
    }) {
        return Some(
            "The declared retrieval policy does not admit automatic public-origin acquisition"
                .into(),
        );
    }
    let Some(recipe) = recipe else {
        let delegate = routes
            .and_then(|r| r.first())
            .and_then(|r| r["locator"].as_str())
            .unwrap_or("unknown");
        return Some(format!(
            "The declared recipe {delegate} is not implemented by browser profile {PROFILE}"
        ));
    };
    if descriptor["sources"].as_array().map_or(0, Vec::len) != 1 {
        return Some(format!("{PROFILE} requires one declared spectral source; multimodal recipes retain their native path"));
    }
    if descriptor["splits"]
        .as_array()
        .is_some_and(|rows| !rows.is_empty())
    {
        return Some(format!(
            "{PROFILE} does not yet project the declared native partition metadata"
        ));
    }
    let allowed = [
        "url",
        "filename",
        "resource_id",
        "sample_column",
        "metadata_columns",
        "target_columns",
        "target_maps",
        "axis_columns",
        "child",
        "metadata_constants",
        "metadata_prefix_count",
        "generated_observation_identity",
        "observation_id_width",
    ];
    if let Some(key) = recipe
        .as_object()
        .unwrap()
        .keys()
        .find(|key| !allowed.contains(&key.as_str()))
    {
        return Some(format!(
            "{PROFILE} does not implement the declared recipe operation {key:?}"
        ));
    }
    let source = &descriptor["sources"][0];
    if source["axis_min"].as_f64().is_none() || source["axis_max"].as_f64().is_none() {
        return Some("The recipe needs an explicit original spectral axis range".into());
    }
    if !matches!(source["axis_unit"].as_str(), Some("nm" | "cm-1" | "index")) {
        return Some("The declared axis unit is not supported by this browser profile".into());
    }
    if descriptor["ids"]["sample_id_available"] == true
        && recipe["sample_column"].as_str().is_none()
        && recipe["generated_observation_identity"] != true
    {
        return Some("The descriptor declares sample identity but the recipe names no original sample column".into());
    }
    let mut output_names = HashSet::from(["observation_id", "sample_id"]);
    let target_names = descriptor["variables"]
        .as_array()
        .unwrap()
        .iter()
        .filter(|variable| variable["role"] == "target")
        .filter_map(|variable| variable["name"].as_str());
    for name in target_names
        .chain(
            recipe["metadata_columns"]
                .as_object()
                .unwrap()
                .keys()
                .map(String::as_str),
        )
        .chain(
            recipe["metadata_constants"]
                .as_object()
                .unwrap()
                .keys()
                .map(String::as_str),
        )
    {
        if !output_names.insert(name) {
            return Some(format!("{PROFILE} cannot represent the declared target/metadata output-name collision {name:?} in one table"));
        }
    }
    None
}

fn resource(recipe: &Value) -> Value {
    // Existing recipes do not pin origin bytes. Never reuse historical canonical
    // hashes or label the observed hash as an expected origin checksum.
    json!({"id": recipe["resource_id"], "name": recipe["filename"], "url": recipe["url"],
           "sha256": null, "size_bytes": null})
}

/// Public metadata and explicit per-source applicability, embedded by the owner.
pub fn browser_catalog() -> Value {
    let datasets = metadata()["datasets"].as_object().unwrap().iter().map(|(id, entry)| {
        let descriptor = &entry["descriptor"];
        let recipe = metadata()["table_recipes"].get(id);
        let reason = reason(entry, recipe);
        let sources = descriptor["sources"].as_array().unwrap().iter().map(|source| {
            let mut value = json!({"id": source["source_id"], "name": source["name"],
                "status": if reason.is_none() {"supported"} else {"unsupported"},
                "resources": if reason.is_none() {vec![resource(recipe.unwrap())]} else {vec![]}});
            if let Some(reason) = &reason { value["reason"] = Value::String(reason.clone()); }
            value
        }).collect::<Vec<_>>();
        json!({"id": id, "name": descriptor["name"], "tier": "public",
               "license": descriptor["governance"]["license"], "description": descriptor["description"], "sources": sources})
    }).collect::<Vec<_>>();
    json!({"schema": "nirs4all.datasets.public-origin-catalog.v1", "datasets": datasets,
           "provenance": provenance(&Value::Null)})
}

/// Resolve one declared source to original resources and the exact owner recipe.
pub fn resolve_browser_plan(dataset_id: &str, source_id: &str) -> Result<Value> {
    let entry = metadata()["datasets"]
        .get(dataset_id)
        .ok_or_else(|| Error::UnknownDataset(dataset_id.into()))?;
    let descriptor = &entry["descriptor"];
    if !descriptor["sources"]
        .as_array()
        .unwrap()
        .iter()
        .any(|source| source["source_id"] == source_id)
    {
        return Err(refuse(format!(
            "{dataset_id}: unknown source {source_id:?}"
        )));
    }
    let recipe = metadata()["table_recipes"].get(dataset_id);
    if let Some(reason) = reason(entry, recipe) {
        return Err(refuse(format!("{dataset_id}/{source_id}: {reason}")));
    }
    let mut descriptor = descriptor.clone();
    if recipe.unwrap()["generated_observation_identity"] == true {
        // The existing native recipe deliberately uses one observation per scan,
        // not the repeated upstream layer UUID. This is a profile descriptor;
        // the distributable index and existing resolve output are unchanged.
        descriptor["ids"]["sample_id_available"] = json!(false);
        descriptor["alignment_level"] = json!("observation");
    }
    let mut proof = provenance(&descriptor);
    if recipe.unwrap()["generated_observation_identity"] == true {
        proof["identity_policy"] = json!("owner-recipe-generated-observation");
        proof["catalog_declared_ids"] = entry["descriptor"]["ids"].clone();
        proof["catalog_declared_alignment_level"] = entry["descriptor"]["alignment_level"].clone();
    } else if descriptor["ids"]["sample_id_available"] == false {
        proof["identity_policy"] = json!("descriptor-declares-no-sample-identity");
        proof["recipe_sample_column"] = recipe.unwrap()["sample_column"].clone();
    }
    Ok(
        json!({"schema": "nirs4all.datasets.public-origin-plan.v1", "dataset_id": dataset_id,
              "source_id": source_id, "descriptor": descriptor, "resources": [resource(recipe.unwrap())],
              "provenance": proof}),
    )
}

fn cell_value(cell: &Cell) -> Value {
    match cell {
        Cell::Bool(value) => Value::Bool(*value),
        Cell::Int(value) => Value::from(*value),
        Cell::Float(value) => Value::from(*value),
        Cell::Str(value) => Value::from(value.clone()),
        Cell::Na => Value::Null,
    }
}

fn csv_cell(value: &Value) -> String {
    match value {
        Value::Null => String::new(),
        Value::String(value) => value.clone(),
        other => other.to_string(),
    }
}

fn metadata_alias(name: &str) -> String {
    // Other._zenodo: re.sub(r"[^A-Za-z0-9_]+", "_", name).strip("_").
    let mut value = String::new();
    let mut invalid_run = false;
    for character in name.chars() {
        if character.is_ascii_alphanumeric() || character == '_' {
            value.push(character);
            invalid_run = false;
        } else if !invalid_run {
            value.push('_');
            invalid_run = true;
        }
    }
    value.trim_matches('_').to_string()
}

/// Prepare a supported origin table in memory, retaining every original row.
///
/// IO owns CSV parsing and the subsequent materialization. This owner projects
/// the existing source recipe's names, target maps and identity declarations.
pub fn prepare_browser_dataset(plan: &Value, files: &[BrowserFile]) -> Result<BrowserPrepared> {
    let dataset_id = plan["dataset_id"]
        .as_str()
        .ok_or_else(|| refuse("Plan needs dataset_id"))?;
    let source_id = plan["source_id"]
        .as_str()
        .ok_or_else(|| refuse("Plan needs source_id"))?;
    if *plan != resolve_browser_plan(dataset_id, source_id)? {
        return Err(refuse(format!(
            "{dataset_id}: the owner acquisition plan was modified"
        )));
    }
    let recipe = &metadata()["table_recipes"][dataset_id];
    let filename = recipe["filename"].as_str().unwrap();
    if files.len() != 1 || files[0].name != filename {
        return Err(refuse(format!(
            "{dataset_id}: expected exactly the declared resource {filename:?}"
        )));
    }
    let params = LoadingParams::from_value(Some(
        &json!({"delimiter": ",", "has_header": true, "na": {"policy": "ignore"}}),
    ))
    .map_err(|error| refuse(error.to_string()))?;
    let frame = read_table_bytes(&files[0].bytes, &params).map_err(|error| {
        refuse(format!(
            "{dataset_id}: IO could not read the original table: {error}"
        ))
    })?;
    for column in &frame.columns {
        if column
            .values
            .iter()
            .any(|cell| matches!(cell, Cell::Float(value) if value.is_infinite()))
        {
            return Err(refuse(format!(
                "{dataset_id}: nonfinite observed value in original column {:?}",
                column.name
            )));
        }
    }
    let descriptor = &plan["descriptor"];
    let source = &descriptor["sources"][0];
    let axis_min = source["axis_min"].as_f64().unwrap();
    let axis_max = source["axis_max"].as_f64().unwrap();
    let aliases = recipe["axis_columns"].as_object();
    let mut axis = Vec::new();
    for column in &frame.columns {
        let label = aliases
            .and_then(|aliases| {
                aliases
                    .iter()
                    .find(|(_, raw)| raw.as_str() == Some(&column.name))
                    .map(|(name, _)| name.as_str())
            })
            .unwrap_or(&column.name);
        if label
            .parse::<f64>()
            .is_ok_and(|value| value >= axis_min && value <= axis_max)
        {
            axis.push((label.to_string(), column.name.clone()));
        }
    }
    if axis.len() != source["n_variables"].as_u64().unwrap() as usize {
        return Err(refuse(format!(
            "{dataset_id}: original table has {} declared-axis columns, expected {}",
            axis.len(),
            source["n_variables"]
        )));
    }
    let mut metadata_columns = recipe["metadata_columns"].as_object().unwrap().clone();
    let mut prefix_aliases = Map::new();
    for column in frame
        .columns
        .iter()
        .take(recipe["metadata_prefix_count"].as_u64().unwrap_or(0) as usize)
    {
        let alias = metadata_alias(&column.name);
        if prefix_aliases
            .insert(alias.clone(), Value::String(column.name.clone()))
            .is_some()
        {
            return Err(refuse(format!(
                "{dataset_id}: original metadata header aliases collide at {alias:?}"
            )));
        }
        if !descriptor["variables"]
            .as_array()
            .unwrap()
            .iter()
            .any(|variable| variable["role"] == "target" && variable["name"] == alias)
        {
            metadata_columns.insert(alias, Value::String(column.name.clone()));
        }
    }
    let mut targets = Map::new();
    let numeric_targets = descriptor["variables"]
        .as_array()
        .unwrap()
        .iter()
        .filter(|variable| variable["role"] == "target" && variable["type"] == "numeric")
        .filter_map(|variable| variable["name"].as_str())
        .collect::<HashSet<_>>();
    for variable in descriptor["variables"].as_array().unwrap() {
        if variable["role"] == "target" {
            let name = variable["name"].as_str().unwrap();
            let original = recipe["target_columns"]
                .get(name)
                .and_then(Value::as_str)
                .or_else(|| prefix_aliases.get(name).and_then(Value::as_str))
                .unwrap_or(name);
            targets.insert(name.to_string(), Value::String(original.to_string()));
        }
    }
    for original in targets
        .values()
        .chain(metadata_columns.values())
        .filter_map(Value::as_str)
    {
        if !frame.has_column(original) {
            return Err(refuse(format!(
                "{dataset_id}: original table is missing declared column {original:?}"
            )));
        }
    }
    let sample_column = recipe["sample_column"].as_str();
    if let Some(name) = sample_column {
        if !frame.has_column(name) {
            return Err(refuse(format!(
                "{dataset_id}: original table is missing sample column {name:?}"
            )));
        }
    }
    let mut metadata_names = vec!["observation_id".to_string(), "sample_id".to_string()];
    metadata_names.extend(metadata_columns.keys().cloned());
    let constants = recipe["metadata_constants"].as_object().unwrap();
    metadata_names.extend(constants.keys().cloned());
    let mut extra = Vec::new();
    for column in &frame.columns {
        // The native soil recipe already projected these to aliased Y/M.
        // Re-emitting them would leak unmarked copies of targets into metadata.
        if prefix_aliases
            .values()
            .any(|original| original.as_str() == Some(&column.name))
        {
            continue;
        }
        if axis.iter().any(|(_, original)| original == &column.name) {
            continue;
        }
        if targets.contains_key(&column.name) && recipe["target_maps"].get(&column.name).is_none() {
            continue;
        }
        let output = if metadata_names.contains(&column.name)
            || targets.contains_key(&column.name)
            || ["dataset_id", "observation_id", "sample_id"].contains(&column.name.as_str())
        {
            format!("raw_{}", column.name)
        } else {
            column.name.clone()
        };
        metadata_names.push(output.clone());
        extra.push((output, column.name.clone()));
    }
    let mut names = axis
        .iter()
        .map(|(label, _)| label.clone())
        .collect::<Vec<_>>();
    names.extend(targets.keys().cloned());
    names.extend(metadata_names.clone());
    if names.iter().collect::<HashSet<_>>().len() != names.len() {
        return Err(refuse(format!(
            "{dataset_id}: source declarations produce conflicting output column names"
        )));
    }
    let mut writer = csv::Writer::from_writer(Vec::new());
    writer
        .write_record(&names)
        .map_err(|error| refuse(error.to_string()))?;
    for row in 0..frame.n_rows {
        let value = |name: &str| cell_value(&frame.column(name).unwrap().values[row]);
        let width = recipe["observation_id_width"].as_u64().unwrap_or(6) as usize;
        let observation = format!("{dataset_id}_{:0width$}", row + 1);
        let sample = if descriptor["ids"]["sample_id_available"] == true {
            let cell = &frame.column(sample_column.unwrap()).unwrap().values[row];
            if cell_value(cell).is_null() {
                return Err(refuse(format!(
                    "{dataset_id}: missing original sample identity at row {}",
                    row + 1
                )));
            }
            cell.to_str_scalar()
        } else {
            observation.clone()
        };
        let mut values = Vec::new();
        for (_, original) in &axis {
            let cell = &frame.column(original).unwrap().values[row];
            let raw = cell_value(cell);
            if !raw.is_null() {
                let number = cell.to_numeric();
                if !number.is_finite() {
                    return Err(refuse(format!("{dataset_id}: nonnumeric or nonfinite observed spectrum at row {}, column {original:?}", row + 1)));
                }
            }
            values.push(csv_cell(&raw));
        }
        for (name, original) in &targets {
            let raw = value(original.as_str().unwrap());
            let mapped = if raw.is_null() {
                Value::Null
            } else if let Some(map) = recipe["target_maps"].get(name) {
                map.get(csv_cell(&raw)).cloned().ok_or_else(|| {
                    refuse(format!(
                        "{dataset_id}: unknown original category in target {name:?} at row {}",
                        row + 1
                    ))
                })?
            } else {
                raw
            };
            if numeric_targets.contains(name.as_str()) && !mapped.is_null() {
                let numeric = match &mapped {
                    Value::Number(value) => value.as_f64().is_some_and(f64::is_finite),
                    Value::Bool(_) => true,
                    Value::String(value) => Cell::Str(value.clone()).to_numeric().is_finite(),
                    _ => false,
                };
                if !numeric {
                    return Err(refuse(format!("{dataset_id}: declared numeric target {name:?} has unsupported nonnumeric or censored content at row {}", row + 1)));
                }
            }
            values.push(csv_cell(&mapped));
        }
        values.extend([observation, sample]);
        values.extend(
            metadata_columns
                .values()
                .map(|name| csv_cell(&value(name.as_str().unwrap()))),
        );
        values.extend(constants.values().map(csv_cell));
        values.extend(extra.iter().map(|(_, name)| csv_cell(&value(name))));
        writer
            .write_record(&values)
            .map_err(|error| refuse(error.to_string()))?;
    }
    let bytes = writer
        .into_inner()
        .map_err(|error| refuse(error.to_string()))?;
    let prepared_name = format!("{dataset_id}-{source_id}-origin.csv");
    let spec = json!({"name": dataset_id, "signal_type": source["signal_type"],
        "sample_index": {"by": "id", "key": "sample_id", "observation_id": "observation_id"},
        "params": {"delimiter": ",", "has_header": true, "header_unit": source["axis_unit"], "na": {"policy": "ignore"}},
        "sources": [{"id": source_id, "role": "mixed", "input": prepared_name,
            "columns": [{"role": "features", "select": axis.iter().map(|(label, _)| label).collect::<Vec<_>>()},
                        {"role": "targets", "select": targets.keys().collect::<Vec<_>>()},
                        {"role": "metadata", "select": metadata_names}]}]});
    nirs4all_io_core::spec::dataset_spec::DatasetSpec::from_value(&spec).map_err(|error| {
        refuse(format!(
            "{dataset_id}: invalid owner IO declaration: {error}"
        ))
    })?;
    let mut provenance = plan["provenance"].clone();
    provenance["downloads"] = json!([{"name": filename, "url": recipe["url"], "sha256": sha256_hex_bytes(&files[0].bytes), "size_bytes": files[0].bytes.len(), "expected_sha256": null, "integrity": "observed-unpinned"}]);
    provenance["n_observations"] = json!(frame.n_rows);
    provenance["target_maps"] = recipe["target_maps"].clone();
    Ok(BrowserPrepared {
        files: vec![BrowserFile {
            name: prepared_name,
            bytes,
        }],
        record_sets: vec![],
        spec,
        provenance,
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use nirs4all_io_core::materialize::assemble::{
        assemble_in_memory, InMemorySource, SourcePayload,
    };
    use nirs4all_io_core::spec::dataset_spec::DatasetSpec;
    use std::collections::HashMap;

    const CANOPY: &str = "canopy_treatment_2009_2016_to_cedar_ecosis";
    const CSV: &str = "Experiment,Treatment, 485 (nm) wavelength ,560 (nm) wavelength ,660 (nm) wavelength,830 (nm) wavelength,1650 (nm) wavelength ,PLOT,Note\ne244,Control,-0.0,0.2,,0.4,0.5,1,first\ne244,Insecticide,0.6,0.7,0.8,0.9,1.0,2,second\n";

    fn prepare(bytes: &[u8]) -> Result<BrowserPrepared> {
        prepare_browser_dataset(
            &resolve_browser_plan(CANOPY, "X")?,
            &[BrowserFile {
                name: "e244_multispec_raw_data.csv".into(),
                bytes: bytes.to_vec(),
            }],
        )
    }

    #[test]
    fn catalogue_is_public_and_every_refusal_is_explicit() {
        for dataset in browser_catalog()["datasets"].as_array().unwrap() {
            assert_eq!(dataset["tier"], "public");
            for source in dataset["sources"].as_array().unwrap() {
                if source["status"] == "unsupported" {
                    assert!(!source["reason"].as_str().unwrap().is_empty());
                }
            }
        }
        assert!(resolve_browser_plan("corn_eigenvector_nir", "X1").is_err());
        for id in [
            "ecosis_dessain_project_reflectance_spectra_reflectance_nirs",
            "ecosis_intact_and_ground_leaf_litter_spectra_from_cedar_creek_reflectance_nirs",
        ] {
            assert!(resolve_browser_plan(id, "X")
                .unwrap_err()
                .to_string()
                .contains("output-name collision"));
            let catalogue = browser_catalog();
            let source = &catalogue["datasets"]
                .as_array()
                .unwrap()
                .iter()
                .find(|entry| entry["id"] == id)
                .unwrap()["sources"][0];
            assert_eq!(source["status"], "unsupported");
            assert!(source["reason"]
                .as_str()
                .unwrap()
                .contains("output-name collision"));
        }
    }

    #[test]
    fn canopy_preserves_declared_axes_treatment_identity_masks_and_metadata_through_io() {
        let prepared = prepare(CSV.as_bytes()).unwrap();
        let spec = DatasetSpec::from_value(&prepared.spec).unwrap();
        let files = prepared
            .files
            .iter()
            .map(|file| InMemorySource {
                name: file.name.clone(),
                payload: SourcePayload::Bytes(file.bytes.clone()),
            })
            .collect::<Vec<_>>();
        let assembled = assemble_in_memory(&spec, &files, &HashMap::new(), None).unwrap();
        let block = &assembled.blocks["train"];
        assert_eq!(block.x[0].n_rows, 2);
        assert_eq!(
            block.feature_headers[0],
            ["485", "560", "660", "830", "1650"]
        );
        assert_eq!(block.x[0].data[0].to_bits(), (-0.0_f64).to_bits());
        assert!(block.x[0].data[2].is_nan());
        assert_eq!(block.y.as_ref().unwrap().data, [1.0, 3.0]);
        let metadata = block.metadata.as_ref().unwrap();
        assert_eq!(
            metadata.str_column("sample_id"),
            [format!("{CANOPY}_000001"), format!("{CANOPY}_000002")]
        );
        assert_eq!(metadata.str_column("Experiment"), ["e244", "e244"]);
        assert_eq!(
            metadata.str_column("raw_Treatment"),
            ["Control", "Insecticide"]
        );
        assert_eq!(metadata.numeric_column_f64("PLOT"), [1.0, 2.0]);
        assert_eq!(prepared.provenance["ids"]["sample_id_available"], false);
        assert_eq!(prepared.provenance["alignment_level"], "observation");
        assert_eq!(
            prepared.provenance["identity_policy"],
            "descriptor-declares-no-sample-identity"
        );
        assert_eq!(prepared.provenance["recipe_sample_column"], "Experiment");
        assert_eq!(
            prepared.provenance["downloads"][0]["integrity"],
            "observed-unpinned"
        );
    }

    #[test]
    fn modified_plan_wrong_resource_and_unknown_treatment_fail_closed() {
        let mut plan = resolve_browser_plan(CANOPY, "X").unwrap();
        plan["resources"][0]["url"] = json!("https://invalid.example/other.csv");
        assert!(prepare_browser_dataset(&plan, &[])
            .unwrap_err()
            .to_string()
            .contains("modified"));
        assert!(
            prepare_browser_dataset(&resolve_browser_plan(CANOPY, "X").unwrap(), &[])
                .unwrap_err()
                .to_string()
                .contains("exactly")
        );
        assert!(prepare(CSV.replace("Control", "Unexpected").as_bytes())
            .unwrap_err()
            .to_string()
            .contains("unknown original category"));
        assert!(prepare(CSV.replace("0.2", "not-a-number").as_bytes())
            .unwrap_err()
            .to_string()
            .contains("nonnumeric"));
        assert!(prepare(CSV.replace("0.2", "inf").as_bytes())
            .unwrap_err()
            .to_string()
            .contains("nonfinite"));
    }

    #[test]
    fn zenodo_soil_recipe_keeps_all_scans_and_declared_traits_without_grouping_layer_uuid() {
        let id = "zenodo_neospectra_soil_nir_ccby";
        let original_metadata = [
            "id.layer_uuid_txt",
            "dataset.code_ascii_txt",
            "id.scan_local_c",
            "oc_usda.c729_w.pct",
            "c.tot_usda.a622_w.pct",
            "n.tot_usda.a623_w.pct",
            "clay.tot_usda.a334_w.pct",
            "sand.tot_usda.c60_w.pct",
            "silt.tot_usda.c62_w.pct",
            "bd_usda.a4_g.cm3",
            "ph.h2o_usda.a268_index",
            "caco3_usda.a54_w.pct",
            "k.ext_usda.a725_cmolc.kg",
        ];
        let mut headers = original_metadata
            .iter()
            .map(|value| value.to_string())
            .collect::<Vec<_>>();
        headers.extend((0..601).map(|column| (1350 + column * 2).to_string()));
        let mut input = csv::Writer::from_writer(Vec::new());
        input.write_record(&headers).unwrap();
        for scan in 1..=2 {
            let mut row = vec![
                "same-layer".to_string(),
                "source".to_string(),
                scan.to_string(),
            ];
            row.extend((0..10).map(|target| (target + scan).to_string()));
            row.extend((0..601).map(|column| {
                if column == 2 {
                    String::new()
                } else {
                    (column + scan).to_string()
                }
            }));
            input.write_record(&row).unwrap();
        }
        let original = input.into_inner().unwrap();
        let prepared = prepare_browser_dataset(
            &resolve_browser_plan(id, "X").unwrap(),
            &[BrowserFile {
                name: "1976_NSlibrary_withmetadata.csv".into(),
                bytes: original.clone(),
            }],
        )
        .unwrap();
        let spec = DatasetSpec::from_value(&prepared.spec).unwrap();
        let sources = prepared
            .files
            .iter()
            .map(|file| InMemorySource {
                name: file.name.clone(),
                payload: SourcePayload::Bytes(file.bytes.clone()),
            })
            .collect::<Vec<_>>();
        let assembled = assemble_in_memory(&spec, &sources, &HashMap::new(), None).unwrap();
        let block = &assembled.blocks["train"];
        assert_eq!((block.x[0].n_rows, block.x[0].n_cols), (2, 601));
        assert_eq!(block.feature_headers[0].first().unwrap(), "1350");
        assert_eq!(block.feature_headers[0].last().unwrap(), "2550");
        assert!(block.x[0].data[2].is_nan());
        assert_eq!(block.y.as_ref().unwrap().data.len(), 20);
        assert_eq!(block.y.as_ref().unwrap().data[0], 1.0);
        let metadata = block.metadata.as_ref().unwrap();
        assert_eq!(
            metadata.str_column("sample_id"),
            [format!("{id}_00001"), format!("{id}_00002")]
        );
        assert_eq!(
            metadata.str_column("id_layer_uuid_txt"),
            ["same-layer", "same-layer"]
        );
        assert_eq!(
            metadata.column_names().into_iter().collect::<HashSet<_>>(),
            [
                "dataset_id",
                "observation_id",
                "sample_id",
                "id_layer_uuid_txt",
                "dataset_code_ascii_txt",
                "id_scan_local_c",
                "origin_url"
            ]
            .into_iter()
            .map(str::to_string)
            .collect()
        );
        assert_eq!(prepared.provenance["ids"]["sample_id_available"], false);
        assert_eq!(
            prepared.provenance["identity_policy"],
            "owner-recipe-generated-observation"
        );
        assert_eq!(
            prepared.provenance["catalog_declared_alignment_level"],
            "sample"
        );
        let censored = String::from_utf8(original).unwrap().replacen(
            "same-layer,source,1,1,",
            "same-layer,source,1,<LOD,",
            1,
        );
        let error = prepare_browser_dataset(
            &resolve_browser_plan(id, "X").unwrap(),
            &[BrowserFile {
                name: "1976_NSlibrary_withmetadata.csv".into(),
                bytes: censored.into_bytes(),
            }],
        )
        .unwrap_err();
        assert!(error.to_string().contains("declared numeric target"));
    }
}
