"""Generate the complete, source-bound diagnostic migration inventory (no kernels run)."""
from __future__ import annotations

import ast
import hashlib
import json
from contextlib import suppress
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUALIFY = ROOT / "src/nirs4all_datasets/qualify"

# (family, implementation, output-key constant, scope, transition action, target owner)
FAMILIES = [
    ("integrity", "spectral_integrity", "_INTEGRITY_KEYS", "source", "migrate", "Preflight"),
    ("amplitude", "spectral_amplitude", "_AMPLITUDE_KEYS", "source", "delegate", "Methods via Preflight"),
    ("noise", "spectral_noise", "_NOISE_KEYS", "source", "delegate", "Methods with Datasets adapter"),
    ("artefacts", "spectral_artefacts", "_ARTEFACT_KEYS", "source", "migrate", "Preflight"),
    ("shape", "spectral_shape_metrics", "_SHAPE_SPECTRAL_KEYS", "source", "migrate", "Preflight"),
    ("outliers", "pca_outlier_metrics", "_PCA_OUTLIER_KEYS", "source", "migrate", "Preflight"),
    ("reference", "reference_similarity", "_REFERENCE_KEYS", "source", "migrate", "Preflight"),
    ("repeatability", "repeatability_metrics", "_REPEATABILITY_KEYS", "source", "migrate", "Preflight"),
    ("structure", "dataset_structure_metrics", "_STRUCTURE_KEYS", "source", "migrate", "Preflight"),
    ("profile_scores", "_profile_scores", "_PROFILE_SCORE_KEYS", "source", "keep metadata", "Datasets"),
    ("aggregate_profile_scores", "aggregate_profile_scores", "_PROFILE_SCORE_KEYS", "dataset", "keep metadata", "Datasets"),
    ("quality", "spectral_quality", "_QUALITY_KEYS", "source", "migrate", "Preflight"),
    ("spacing", "wavelength_spacing", "_SPACING_KEYS", "source", "keep metadata", "Datasets"),
    ("class_balance", "class_balance", "_CLASS_KEYS", "variable", "delegate", "Methods"),
    ("distribution_shape", "distribution_shape", "_SHAPE_KEYS", "variable", "delegate", "Methods"),
    ("target_shift", "target_shift", "_TARGET_SHIFT_KEYS", "task/split", "migrate", "Domains"),
    ("class_shift", "class_shift", "_CLASS_SHIFT_KEYS", "task/split", "migrate", "Domains"),
    ("source_target_correlation", "spectral_target_correlation", None, "task/split", "migrate", "Domains"),
    ("curve", "spectral_curve", None, "display", "keep metadata", "Datasets"),
    ("histogram", "histogram_bins", None, "display", "keep metadata", "Datasets"),
    ("pca_projection", "pca_score_plot", None, "source", "delegate", "Methods via Preflight"),
    ("imputation", "impute_columns", None, "source", "deprecated", "Preflight"),
    ("effective_rank", "effective_rank", (), "source", "delegate", "Methods via Preflight"),
]
REGISTRY_FAMILIES = [
    ("value_range", "_source_value_range", "source", "delegate", "Methods via Preflight"),
    ("numeric_stats", "_variable_numeric_stats", "variable", "keep metadata", "Datasets"),
    ("categorical_stats", "_variable_categorical_stats", "variable", "keep metadata", "Datasets"),
    ("observations_per_unit", "_dataset_reps_per_sample", "dataset", "keep metadata", "Datasets"),
]


def parse_module(name: str):
    text = (QUALIFY / (name + ".py")).read_text()
    tree = ast.parse(text)
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    constants = {}
    for node in tree.body:
        target = node.targets[0] if isinstance(node, ast.Assign) else node.target if isinstance(node, ast.AnnAssign) else None
        if isinstance(target, ast.Name):
            with suppress(ValueError, TypeError, AttributeError):
                constants[target.id] = ast.literal_eval(node.value)
    return text, functions, constants


def dictionary_fields(node):
    """Only returned fields, not dictionaries used for arguments or intermediate configuration."""
    fields = {}
    for item in ast.walk(node):
        if not isinstance(item, ast.Return):
            continue
        values = list(item.value.elts) if isinstance(item.value, ast.Tuple) else [item.value]
        for value in values:
            if isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == "_proxy_fields":
                value = value.args[1]
            if not isinstance(value, ast.Dict):
                continue
            for key, expression in zip(value.keys, value.values, strict=True):
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    text = ast.unparse(expression)
                    if text != "None" or key.value not in fields:
                        fields[key.value] = text
    return fields


def generate():
    modules = {name: parse_module(name) for name in ["metrics", "registry", "profile"]}
    aliases = modules["metrics"][2]["LEGACY_METRIC_ALIASES"]
    formulas = modules["metrics"][2]["_METRIC_FORMULAS"]
    definitions = {}
    metrics = []

    def add(module, family, symbol, keys, scope, action, owner):
        text, functions, _ = modules[module]
        node = functions[symbol]
        body = ast.get_source_segment(text, node)
        assert body is not None
        # Bind the exact implementation, including every local helper it invokes.
        reachable = set()
        pending = [symbol]
        while pending:
            current = pending.pop()
            if current in reachable:
                continue
            reachable.add(current)
            pending.extend(call.func.id for call in ast.walk(functions[current]) if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id in functions)
        implementations = {name: ast.get_source_segment(text, functions[name]) for name in sorted(reachable)}
        definition_id = module + "." + symbol
        definitions[definition_id] = {
            "source_file": "src/nirs4all_datasets/qualify/" + module + ".py",
            "symbol": symbol,
            "arguments": ast.unparse(node.args),
            "definition": ast.get_docstring(node),
            "implementation_sha256": hashlib.sha256(body.encode()).hexdigest(),
            "local_helper_implementations": implementations,
            "missing_data_and_population_rules": "Exact executable preconditions, finite handling, imputation, sampling, grouping and denominators are retained in the source above; no native equivalence is inferred.",
        }
        fields = dictionary_fields(node)
        output_keys = (list(fields) or ["value"]) if keys is None else list(keys) if keys else ["value"]
        for key in output_keys:
            old_id = family + "." + key
            canonical_id = aliases.get(old_id, old_id)
            expression = fields.get(key)
            metrics.append({
                "metric_id": canonical_id,
                "legacy_key": old_id if canonical_id != old_id else None,
                "scope": scope,
                "definition_id": definition_id,
                "scientific_definition": formulas.get(old_id) or expression or "See exact implementation and its local helper closure, including dynamic field assembly.",
                "return_expression": expression,
                "current_owner": "Datasets legacy Python",
                "target_owner": owner,
                "transition": "replace" if canonical_id != old_id else action,
                "replacement_kind": "truthful name; same historical proxy definition, not a different algorithm" if canonical_id != old_id else None,
                "current_protocol": "7" if family == "repeatability" else "6 (unchanged raw definition; presentation7)",
                "population": "Explicit original split populations; never intrinsic/pre-training input" if scope == "task/split" else "Input source/variable population; observation count is not a claim of physical independence",
                "native_equivalence": "not_assumed",
            })
            if canonical_id != old_id:
                metrics.append({"metric_id": old_id, "scope": scope, "definition_id": definition_id, "scientific_definition": formulas.get(old_id) or expression, "current_owner": "Datasets compatibility reader", "target_owner": owner, "transition": "deprecated", "replaced_by": canonical_id, "native_equivalence": "alias_only_not_LOF_or_repeat_measured_SNR"})

    for family, symbol, constant, scope, action, owner in FAMILIES:
        keys = modules["metrics"][2][constant] if isinstance(constant, str) else constant
        add("metrics", family, symbol, keys, scope, action, owner)
    # Methods computes the roughness kernel; Datasets attaches axis coordinates,
    # producer identity and compatibility aliases. Quality remains an aggregate.
    native_binding = {
        "engine": "nirs4all-methods", "minimum_abi": "2.20",
        "operation": "diagnostics.spectral_noise_proxy",
        "c_abi_entrypoint": "n4m_procedure_run",
        "python_facade": "n4m.roles.SpectralNoiseProxy",
        "protocol_version": "spectral-second-difference-mad-index.v1",
        "producer_metadata": ["name", "engine_version", "abi_version", "operation", "protocol_version"],
    }
    definitions["metrics.spectral_noise"]["native_binding"] = native_binding
    definitions["metrics.spectral_noise"]["ownership"] = "Methods native roughness kernel; Datasets axis, provenance and compatibility alias adapter."
    for row in metrics:
        if row["definition_id"] == "metrics.spectral_noise":
            row["current_owner"] = "Methods native kernel; Datasets axis, provenance and aliases"
            row["native_binding"] = native_binding
            row["current_protocol"] = "Methods spectral-second-difference-mad-index.v1; Datasets presentation 7"
            if row.get("transition") != "deprecated":
                row["native_equivalence"] = "not_assumed"
                row["native_semantics"] = (
                    "Datasets axis coordinate for Methods worst-band index" if row["metric_id"] == "noise.worst_band_axis"
                    else "Methods second-difference MAD roughness; parity with the historical calculation must be verified, not Savitzky–Golay residual noise or measured SNR"
                )
    definitions["metrics.spectral_quality"]["noise_component"] = "Consumes Methods native second-difference MAD roughness through the Datasets adapter; quality remains a Datasets aggregate."

    for family, symbol, scope, action, owner in REGISTRY_FAMILIES:
        add("registry", family, symbol, None, scope, action, owner)
    add("profile", "legacy_pca", "_source_pca", None, "source", "migrate", "Preflight")
    add("profile", "legacy_x_outliers", "_x_outliers", None, "source", "migrate", "Preflight")
    # Hypotheses are interpretations, not additional measured defects or probabilities.
    add("metrics", "diagnostic_hypotheses", "diagnostic_hypotheses", (), "interpretation", "keep metadata", "Datasets")
    metrics.pop()  # Replace the list-valued wrapper with each actual interpretation rule.
    for call in ast.walk(modules["metrics"][1]["diagnostic_hypotheses"]):
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "_diagnostic_row":
            key = ast.literal_eval(call.args[0])
            metrics.append({
                "metric_id": "hypothesis." + key, "scope": "interpretation",
                "definition_id": "metrics.diagnostic_hypotheses",
                "scientific_definition": ast.unparse(call.args[2]),
                "current_owner": "Datasets heuristic presentation", "target_owner": "Datasets",
                "transition": "keep metadata", "native_equivalence": "not_a_measured_cause_or_probability",
                "domain_context_required": "VERA25" if key == "vera25_like" else None,
                "causal_validation": "unvalidated",
            })
    definitions["native.preflight.integrity.missing_cells"] = {
        "source_file": "https://github.com/GBeurier/nirs4all-preflight/blob/main/crates/nirs4all-preflight/src/lib.rs",
        "symbol": "integrity.missing_cells (native metric)",
        "implementation_sha256": None,
        "external_version_binding": "Owner engine/protocol identity in each attached report; executable/library SHA in the independent native integration receipt",
        "local_helper_implementations": {},
        "definition": "Count cells for which native valid_cell(source,row,column) is absent; denominator n_cells is the actual evaluated matrix cell count. x:null and valid_mask:false each invalidate a cell, counted once.",
    }
    metrics.append({
        "metric_id": "integrity.missing_cells", "scope": "source", "definition_id": "native.preflight.integrity.missing_cells",
        "scientific_definition": definitions["native.preflight.integrity.missing_cells"]["definition"],
        "current_owner": "Preflight", "target_owner": "Preflight", "transition": "delegate",
        "native_equivalence": "identity; native count retained with original denominator, not converted to a legacy ratio",
        "population": "The exact source/population/view/context named by the owner assessment",
    })
    ids = [row["metric_id"] for row in metrics]
    assert len(ids) == len(set(ids)), "Inventory metric IDs are ambiguous"
    return {
        "schema_version": 1,
        "purpose": "Complete migration inventory; no numerical kernels run during generation",
        "qualification_protocol": "7",
        "transition_policy": "Legacy Python generation remains optional and readable. Shared provider metrics are accepted only with explicit context/protocol; this inventory is not an assertion of native parity for every legacy metric.",
        "owners": {"Methods": "reusable numerical kernels", "Preflight": "intrinsic assessment/protocol and identity-aware aggregation", "Domains": "task/split/fit-reference assessment", "Datasets": "ingestion, provenance, card/cache/presentation metadata"},
        "actions": ["keep metadata", "delegate", "migrate", "replace", "deprecated"],
        "non_metric_public_helpers": {
            "spectral_profile": "composition of the inventoried source metrics",
            "profile_score_labels": "presentation labels",
            "metric_catalog": "presentation metadata",
            "technology_guidance": "qualitative guidance, not computed values",
            "bug_method_catalog": "qualitative guidance, not computed values",
            "with_metric_semantics": "additive aliases, no calculations",
            "migrate_profile_metadata": "explicit labels/signatures migration, no raw kernels",
            "metric_score_rows": "presentation joins over inventoried values and heuristic alerts",
            "diagnostic_presentation": "historical score preserved; current honest labels/domain filter",
        },
        "definitions": definitions,
        "metrics": sorted(metrics, key=lambda row: row["metric_id"]),
    }


if __name__ == "__main__":
    target = QUALIFY / "metric_inventory.json"
    target.write_text(json.dumps(generate(), indent=2, ensure_ascii=False) + "\n")
    print("Wrote", target.relative_to(ROOT))
