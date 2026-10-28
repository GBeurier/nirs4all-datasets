"""Original-source recipes for selected public datasets.

This module assembles tabular source fields into the standardized interchange
layout; it does not parse instrument/vendor formats.
"""
from __future__ import annotations

import io
import json
import re
import sqlite3
import zipfile
import zlib
from pathlib import Path

import numpy as np
import pandas as pd

_MALARIA = {"malaria_anopheles_gambiae_oocyst_nir", "malaria_anopheles_gambiae_sporozoite_nir"}
_CHEMBL_LIMIT = 50000
_PERTEN = {f"{crop}_{trait}_perten" for crop in ("barley", "corn", "wheat", "cereals_all") for trait in ("moisture", "protein")} | {"perten_cereals_nir"}
_ROD = json.loads(Path(__file__).with_name("other_recipes.json").read_text(encoding="utf-8"))
_UVA = {f"figshare_uva_illicit_drugs_{instrument}_avg_nir" for instrument in ("asd", "micronir", "neospectra", "nirone", "scio")}
_FLANAGAN = {"flanagan_api_compounds_raman", "drug_compound_flanagan_raman", "drug_common_application_flanagan_raman", "drug_solvent_reagent_flanagan_raman"}
_ZENODO = {
    "zenodo_milk_composition_transmittance_nir": ("8263430", "data_table.csv"),
    "zenodo_twinspectra_fieldspec_rdf_nir": ("18471662", "measurements_2151.csv"),
    "zenodo_twinspectra_micronir_rdf_nir": ("18471662", "measurements_125.csv"),
    "zenodo_neospectra_soil_nir_ccby": ("13122321", "1976_NSlibrary_withmetadata.csv"),
    "zenodo_western_highveld_soil_nir_mir": ("17510653", "NWU_NIR_MIR_Dataset.csv"),
}


def supports(dataset_id: str) -> bool:
    return dataset_id in _PERTEN or dataset_id in _ZENODO or dataset_id in _FLANAGAN or dataset_id in _UVA or dataset_id in _ROD or dataset_id in _MALARIA or dataset_id == "chembl_ir_raman_multiblock" or dataset_id == "cartilage_spectroscopy_scientificdata_nir" or dataset_id == "data_in_brief_rice_amylose_transflection_nir_matio" or dataset_id == "zenodo_tomato_leaf_stress_visnir_matio"


def _ids(dataset_id: str, n: int) -> pd.Series:
    return pd.Series([f"{dataset_id}_{i:05d}" for i in range(1, n + 1)], name="observation_id")


def _write(context, dataset_id: str, raw: pd.DataFrame, blocks: dict[str, pd.DataFrame], targets: list[str], sample: pd.Series | None, url: str) -> Path:
    raw = raw.reset_index(drop=True)
    obs = _ids(dataset_id, len(raw))
    source_frames = {}
    for name, block in blocks.items():
        block = block.reset_index(drop=True).copy()
        block.insert(0, "observation_id", obs)
        source_frames[name] = block
    y = raw[targets].copy()
    y.insert(0, "observation_id", obs)
    m = raw.drop(columns=targets).copy()
    # Canonical reserves source_* columns; retain source metadata under visible names.
    aliases = {name: "origin_" + name.removeprefix("source_") for name in m.columns if name.startswith("source_")}
    if any(alias in m.columns for alias in aliases.values()):
        raise ValueError("source metadata names conflict with origin metadata names")
    m = m.rename(columns=aliases)
    m.insert(0, "sample_id", sample.reset_index(drop=True).astype(str) if sample is not None else obs)
    m.insert(0, "observation_id", obs)
    m.insert(0, "dataset_id", dataset_id)
    m["origin_url"] = url
    return Path(context.write_tables(source_frames, y, m))


def _perten(dataset_id: str, context) -> Path:
    url = "https://zenodo.org/api/records/15838136/files/sensAIfood_Perten.zip/content"
    archive = context.download(url, filename="sensAIfood_Perten.zip")
    crops = ("Barley", "Corn", "Wheat") if dataset_id.startswith(("cereals_all", "perten_cereals")) else (dataset_id.split("_")[0].title(),)
    frames = []
    with zipfile.ZipFile(archive) as z:
        for crop in crops:
            name = f"{crop}_sensAIfood_Perten.csv"
            with z.open(name) as f:
                frame = pd.read_csv(f)
            values = {"source_file": name}
            # Each workbook documents the measurement and laboratory protocol.
            with z.open(f"{crop}_sensAIfood_Perten_metadata.xlsx") as f:
                metadata = pd.read_excel(f, header=None)
            for _, row in metadata.iterrows():
                if len(row) >= 2 and row.iloc[0] != "Field" and pd.notna(row.iloc[0]) and pd.notna(row.iloc[1]):
                    key = "meta_" + re.sub(r"[^A-Za-z0-9]+", "_", str(row.iloc[0])).strip("_")
                    values[key] = str(row.iloc[1])
            frames.append(pd.concat([frame, pd.DataFrame([values] * len(frame))], axis=1))
    data = pd.concat(frames, ignore_index=True)
    xcols = [c for c in data if str(c).isdigit()]
    block = data[xcols].copy()
    meta = data.drop(columns=xcols).copy()
    meta["cereal_type"] = meta["Cereal"]
    if dataset_id == "perten_cereals_nir":
        targets = ["Moisture", "Protein"]
        meta["crop"] = meta["Cereal"]
        meta["instrument"] = meta["Spectrometer"]
        meta["country"] = meta["Country"]
        meta["year"] = meta["Year"]
        meta["variety"] = meta["Variety"]
    else:
        target = "moisture" if "moisture" in dataset_id else "protein"
        original = target.title()
        meta[target] = meta.pop(original)
        targets = [target]
    return _write(context, dataset_id, meta, {"X": block}, targets, data["ID"], url)


def _zenodo(dataset_id: str, context) -> Path:
    record, filename = _ZENODO[dataset_id]
    url = f"https://zenodo.org/api/records/{record}/files/{filename}/content"
    data = pd.read_csv(context.download(url, filename=filename), sep=";" if record == "17510653" else ",")
    sample = None
    if record == "8263430":
        cols = [f"Trans_Tot_{i}" for i in range(1, 257)]
        block = data[cols].copy()
        block.columns = [f"{x:.10g}" for x in np.linspace(960, 1690, 256)]
        raw = data.iloc[:, :14].copy()
        # Preserve the source's auxiliary detector readings alongside Trans_Tot.
        for channel in ("Dark", "Sample", "White"):
            readings = data[[f"Trans_{channel}_{i}" for i in range(1, 257)]]
            raw[f"Trans_{channel}"] = [json.dumps(row.tolist()) for row in readings.to_numpy()]
        targets = ["Fat", "Prot", "Lact", "SCC", "Urea", "Milk_yield"]
        blocks = {"X": block}
    elif record == "18471662":
        blocks = {"X": data.iloc[:, 4:].copy()}
        raw = data.iloc[:, :4].copy()
        targets = ["group"]
        sample = raw["sample"]
    elif record == "13122321":
        blocks = {"X": data.iloc[:, 13:].copy()}
        raw = data.iloc[:, :13].copy()
        raw.columns = [re.sub(r"[^A-Za-z0-9_]+", "_", c).strip("_") for c in raw.columns]
        targets = raw.columns[3:].tolist()
        sample = None  # Multiple scans share a layer UUID; preserve every scan as a distinct sample.
    else:
        cols = [c for c in data.columns if c.startswith("spec.")]
        nir, mir = cols[:251], cols[251:]
        blocks = {"X1": data[nir].copy(), "X2": data[mir].copy()}
        for b in blocks.values():
            b.columns = [c.removeprefix("spec.") for c in b.columns]
        raw = data.drop(columns=cols)
        sample = raw["Sample Name"]
        targets = ["pH(KCl)", "P(Bray 1)", "K", "Ca", "Mg", "Na"]
    return _write(context, dataset_id, raw, blocks, targets, sample, url)



def _flanagan(dataset_id: str, context) -> Path:
    files = {item["name"]: item["url"] for item in context.provider_files("figshare", "10.6084/m9.figshare.27931131")}
    spectral_name = "raman_spectra_api_compounds.csv"
    spectral = pd.read_csv(context.download(files[spectral_name], filename=spectral_name))
    information = pd.read_excel(context.download(files["API_Product_Information.xlsx"], filename="API_Product_Information.xlsx"))
    information = information.rename(columns={"Compound": "compound", "Solvent / Reagent": "solvent_reagent", "Common Application": "common_application"})
    raw = pd.DataFrame({"compound": spectral["label"]})
    raw = raw.merge(information, on="compound", how="left", validate="many_to_one", sort=False)
    raw["label"] = raw["compound"]
    raw["compound_rep_index"] = raw.groupby("compound", dropna=False).cumcount() + 1
    raw = raw.rename(columns={"Organic": "organic", "Formula": "formula", "Supplier - Product": "supplier_product", "Assay %": "assay_pct", "Exposure (secs)": "exposure_secs", "Pixel Fill %": "pixel_fill_pct", "Samples": "compound_source_sample_count", "Approx. Raman bands (deviation of 2 cm-1 per external sources)": "approx_raman_bands_source"})
    if dataset_id != "flanagan_api_compounds_raman":
        aliases = {"organic": "Organic", "formula": "Formula", "solvent_reagent": "Solvent_Reagent", "common_application": "Common_Application", "supplier_product": "Supplier_Product", "assay_pct": "Assay_pct", "exposure_secs": "Exposure_secs", "pixel_fill_pct": "Pixel_Fill_pct", "compound_source_sample_count": "Samples", "approx_raman_bands_source": "Approx_Raman_bands_deviation_of_2_cm_1_per_external_sources"}
        for source, alias in aliases.items():
            raw[alias] = raw[source]
    # The single-target derivative cards classify the remaining source fields as metadata.
    if dataset_id == "flanagan_api_compounds_raman":
        targets = ["compound", "common_application", "solvent_reagent"]
    else:
        targets = [dataset_id.removeprefix("drug_").removesuffix("_flanagan_raman")]
    return _write(context, dataset_id, raw, {"X": spectral.drop(columns="label")}, targets, None, files[spectral_name])


def _uva(dataset_id: str, context) -> Path:
    files = {item["name"]: item["url"] for item in context.provider_files("figshare", "10.6084/m9.figshare.21252300")}
    url = files["dataset.zip"]
    instrument = {"asd": "ASD", "micronir": "MicroNIR", "neospectra": "NeoSpectra", "nirone": "NIRONE", "scio": "Scio"}[dataset_id.removeprefix("figshare_uva_illicit_drugs_").removesuffix("_avg_nir")]
    with zipfile.ZipFile(context.download(url, filename="uva_dataset.zip")) as z:
        metadata = pd.read_excel(z.open("metadata.xlsx")).rename(columns={"salt form": "salt_form"})
        blocks, names = [], []
        for name in sorted(z.namelist()):
            if name.startswith("datafiles averaged per sample/") and name.endswith(f"_Avg_{instrument}.xlsx"):
                frame = pd.read_excel(z.open(name))
                names.extend([Path(name).name] * len(frame))
                blocks.append(frame)
    if not blocks:
        raise ValueError(f"No averaged {instrument} workbooks in original archive")
    source = pd.concat(blocks, ignore_index=True)
    source = source.rename(columns={source.columns[0]: "code"})
    raw = pd.DataFrame({"code": source["code"], "source_file": names})
    raw = raw.merge(metadata, on="code", how="left", validate="many_to_one", sort=False)
    return _write(context, dataset_id, raw, {"X": source.drop(columns="code")}, ["component", "set", "salt_form", "matrix", "color"], raw["code"], url)


def _tomato(dataset_id: str, context) -> Path:
    import matio

    files = context.provider_files("zenodo", "https://zenodo.org/records/12800065")
    arrays: dict[str, list[pd.DataFrame]] = {"X_reflectance": [], "X_transmittance": [], "X_absorbance": []}
    rows = []
    axis = None
    url = "https://zenodo.org/records/12800065"
    for day in (0, 2, 4, 7):
        name = f"2023_d{day}_Leaf_Spec_Tomato_Stress.mat"
        matches = [f for f in files if f["name"] == name]
        if len(matches) != 1:
            raise ValueError(f"Missing original Zenodo file {name}")
        doc = matio.load_from_mat(str(context.download(matches[0]["url"], filename=name)), raw_data=False)
        for condition in ("PAR1000", "PAR300"):
            source = doc[condition][0, 0]
            wavelengths = np.asarray(source["wvl"])
            current = wavelengths[0]
            if axis is None:
                axis = current
            if not np.allclose(wavelengths, axis, rtol=0, atol=1e-7):
                raise ValueError(f"Incompatible tomato wavelength axes in {name}")
            for out, field in (("X_reflectance", "refl_real"), ("X_transmittance", "trans_real"), ("X_absorbance", "abs_real")):
                arrays[out].append(pd.DataFrame(source[field], columns=[str(v) for v in axis]))
            treatment = source["treatment"].reshape(-1)
            replicate = source["repli"].reshape(-1)
            sample = source["sample"].reshape(-1)
            for index, (t, r, leaf) in enumerate(zip(treatment, replicate, sample, strict=True)):
                row = {"treatment": str(t), "par_condition": condition, "day_after_stress": day, "replicate": str(r), "leaf_sample": str(leaf), "source_file": name}
                for field in ("PAR", "PARf", "Fup", "Fdw", "refl_real_smooth", "trans_real_smooth", "abs_real_smooth"):
                    row[field] = json.dumps(np.asarray(source[field])[index].tolist(), allow_nan=True)
                rows.append(row)
    raw = pd.DataFrame(rows)
    sample = raw["treatment"] + "_" + raw["replicate"] + "_" + raw["leaf_sample"] + "_" + raw["par_condition"] + "_d" + raw["day_after_stress"].astype(str)
    return _write(context, dataset_id, raw, {k: pd.concat(v, ignore_index=True) for k, v in arrays.items()}, ["treatment", "par_condition", "day_after_stress"], sample, url)


def _rod(dataset_id: str, context) -> Path:
    from nirs4all_datasets.public_pull.native import open_records

    rows, spectra = [], []
    axis = None
    for code in _ROD[dataset_id]["codes"]:
        url = f"https://solsa.crystallography.net/rod/{code}.rod"
        records = open_records(context.download(url, filename=f"{code}.rod"))
        if len(records) != 1:
            raise ValueError(f"Expected one ROD record for {code}")
        record = records[0]
        signal = record["signals"]["intensity"]
        current = np.asarray(signal["axis"]["values"])
        if axis is None:
            axis = current
        if current.shape != axis.shape or not np.array_equal(current, axis):
            raise ValueError(f"ROD {code} no longer has the declared common axis")
        spectra.append(signal["values"])
        info = record["metadata"].copy()
        info["mineral_name"] = info.get("chemical_name_mineral")
        info["compound_source"] = info.get("chemical_compound_source")
        info["rod_database_code"] = code
        rows.append(info)
    raw = pd.DataFrame(rows)
    assert axis is not None
    return _write(context, dataset_id, raw, {"X": pd.DataFrame(spectra, columns=[str(v) for v in axis])}, ["mineral_name", "chemical_formula_sum", "compound_source", "rod_database_code"], raw["rod_database_code"], "https://solsa.crystallography.net/rod/")


def _rice(dataset_id: str, context) -> Path:
    from scipy.io import loadmat

    url = "https://ars.els-cdn.com/content/image/1-s2.0-S2352340917305176-mmc3.zip"
    with zipfile.ZipFile(context.download(url, filename="rice_mmc3.zip")) as z:
        doc = loadmat(io.BytesIO(z.read("mmc3.mat")))
    axis = doc["xaxis"].reshape(-1)
    matrix = np.vstack([doc["Xcal"], doc["Xtest"]])
    labels = np.concatenate([doc["ycal"].reshape(-1), doc["ytest"].reshape(-1)])
    ncal, ntest = len(doc["Xcal"]), len(doc["Xtest"])
    raw = pd.DataFrame({"amylose_percent": labels, "source_split": ["calibration"] * ncal + ["test"] * ntest, "source_split_index": list(range(1, ncal + 1)) + list(range(1, ntest + 1)), "split_original": ["calibration"] * ncal + ["test"] * ntest})
    sample = "rice_amylose_" + raw["source_split"] + "_" + raw["source_split_index"].astype(str).str.zfill(3)
    return _write(context, dataset_id, raw, {"X": pd.DataFrame(matrix, columns=[str(v) for v in axis])}, ["amylose_percent"], sample, url)


def _cartilage(dataset_id: str, context) -> Path:
    from scipy.io import loadmat

    files = {item["name"]: item["url"] for item in context.provider_files("figshare", "10.6084/m9.figshare.7803845")}
    name = "nirs_and_references_revised.mat"
    doc = loadmat(context.download(files[name], filename=name), simplify_cells=True)["dataset"]
    spectra, rows, samples = [], [], []
    axis = None
    for item in doc:
        wavelength = np.asarray(item["wavelength"])
        if axis is None:
            axis = wavelength
        if not np.array_equal(axis, wavelength):
            raise ValueError("Cartilage source contains differing wavelength axes")
        block = np.atleast_2d(item["raw_spectra"])
        row = {}
        for key, value in item.items():
            if key in ("wavelength", "raw_spectra", "sample_id"):
                continue
            key = re.sub(r"(dynamic_modulus_at_[0-9]+)hz$", r"\1_hz", key)
            if isinstance(value, np.ndarray):
                value = None if value.size == 0 else json.dumps(value.tolist(), allow_nan=True)
            row[key] = value
        for values in block:
            spectra.append(values)
            rows.append(row.copy())
            samples.append(item["sample_id"])
    raw = pd.DataFrame(rows)
    assert axis is not None
    targets = ["joint_id", "bone_type", "cartilage_thickness", "instantaneous_modulus", "equilibrium_modulus"] + [f"dynamic_modulus_at_{n}_hz" for n in ("01", "025", "05", "0625", "0833", "1", "2")]
    return _write(context, dataset_id, raw, {"X": pd.DataFrame(spectra, columns=[str(v) for v in axis])}, targets, pd.Series(samples), files[name])


def _chembl(dataset_id: str, context) -> Path:
    """Expose source stick spectra by mode, retaining each row's actual frequencies.

    These are molecular normal modes, not spectra sampled on a shared cm-1 grid.
    No linewidth or continuous spectrum is inferred.
    """
    entries = context.provider_files("figshare", "10.6084/m9.figshare.28593698")
    matches = [item for item in entries if item["name"] == "Raman-ChEMBL-part1.db"]
    if len(matches) != 1:
        raise ValueError("Original ChEMBL part 1 SQLite file is not listed by Figshare")
    entry = matches[0]
    if hasattr(context, "timeout"):
        context.timeout = max(context.timeout, 3600)  # The original SQLite is approximately 5 GB.
    path = context.download(entry["url"], filename=entry["name"], size=entry.get("size"))
    spectra_ir, spectra_raman, rows, samples = [], [], [], []
    with sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True) as db:
        query = "SELECT id, SMILES, sdf_name, database_tag, Eg, Homo, Lumo, Dtotal, isotropic_pol, electronic_ext, heat_capacity, Rx, Ry, Rz, Dx, Dy, Dz, xyz_name, blob_data FROM molecule WHERE id BETWEEN 1 AND ? ORDER BY id"
        for molecule_id, smiles, sdf_name, tag, gap, homo, lumo, dipole, polar, electronic, heat, rx, ry, rz, dx, dy, dz, xyz_name, compressed in db.execute(query, (_CHEMBL_LIMIT,)):
            payload = json.loads(zlib.decompress(compressed))
            frequencies, ir, raman = payload["freq"], payload["IR Inten"], payload["Raman Activ"]
            if not (len(frequencies) == len(ir) == len(raman)):
                raise ValueError(f"ChEMBL molecule {molecule_id} has mismatched mode counts")
            chembl_id = str(sdf_name).split(".", 1)[0] if sdf_name else str(molecule_id)
            row = {"chembl_id": chembl_id, "compound_name": None, "molecular_formula": None, "smiles": smiles, "inchi": None, "inchikey": None, "compound_class": None, "band_gap": gap, "dipole_moment_total": dipole, "isotropic_polarizability": polar, "homo": homo, "lumo": lumo, "electronic_ext": electronic, "heat_capacity": heat, "molecule_id": molecule_id, "sdf_name": sdf_name, "database_tag": tag, "xyz_name": xyz_name, "Rx": rx, "Ry": ry, "Rz": rz, "Dx": dx, "Dy": dy, "Dz": dz, "n_atoms": len(payload.get("atoms", [])), "n_modes_total": len(frequencies), "n_modes_positive": sum(value > 0 for value in frequencies), "has_negative_freq": any(value < 0 for value in frequencies), "mode_frequencies_cm1": json.dumps(frequencies)}
            rows.append(row)
            spectra_ir.append(ir)
            spectra_raman.append(raman)
            samples.append(chembl_id)
    if len(rows) != _CHEMBL_LIMIT:
        raise ValueError(f"ChEMBL original database has {len(rows)} of the expected first {_CHEMBL_LIMIT} molecule IDs")
    width = max(map(len, spectra_ir))
    def padded(values):
        matrix = np.full((len(values), width), np.nan, dtype=np.float32)
        for i, row in enumerate(values):
            matrix[i, :len(row)] = row
        return pd.DataFrame(matrix, columns=[str(i + 1) for i in range(width)])
    raw = pd.DataFrame(rows)
    targets = ["chembl_id", "compound_name", "molecular_formula", "smiles", "inchi", "inchikey", "compound_class", "band_gap", "dipole_moment_total", "isotropic_polarizability", "homo", "lumo", "electronic_ext", "heat_capacity"]
    leaf = _write(context, dataset_id, raw, {"X1": padded(spectra_ir), "X2": padded(spectra_raman)}, targets, pd.Series(samples), entry["url"])
    layout = {"representation": "native_peak_lists", "sources": {"X1": {"axis_unit": "index"}, "X2": {"axis_unit": "index"}}, "warnings": ["Original IR intensities and Raman activities are indexed by vibrational mode; per-sample frequencies in cm-1 are stored in mode_frequencies_cm1. No Lorentz broadening or common-grid reconstruction was applied. The complete molecular record remains in the cached original SQLite database, addressable by molecule_id."]}
    (leaf / "pull-layout.json").write_text(json.dumps(layout, indent=2), encoding="utf-8")
    return leaf



def _malaria_id(value: str) -> tuple[str, str, int]:
    """Normalize the publisher's sample and SPC naming conventions."""
    value = re.sub(r"[^A-Z0-9]", "", value.upper())
    value = re.sub(r"^[SM]", "", value)
    # Some oocyst SPC names place C/G before the third collection digit.
    value = re.sub(r"^(\d\d)([CG])(\d)", r"\1\3\2", value)
    match = re.fullmatch(r"(\d{3})([CG]?)(\d+)", value)
    if not match:
        raise ValueError(f"Unrecognized malaria sample identifier {value!r}")
    return match[1], match[2], int(match[3])

def _malaria(dataset_id: str, context) -> Path:
    """Load the publisher's spectra after an explicitly supplied guestbook response."""
    from nirs4all_datasets.public_pull.native import open_bytes

    spectra_archive = context.dataverse_file(3326596, "NIRS spectra P falciparum infection.zip", guestbook_id=293)
    frames = []
    for label, split, file_id in (("Calibration dataset", "train", 3326589), ("Validation dataset", "test", 3330651)):
        path = context.dataverse_file(file_id, f"{label}.dta", guestbook_id=293)
        table = pd.read_stata(path, convert_categoricals=False)
        table["split_original"] = split
        table["parasite_load"] = table.get("parasite_load", table.get("parasiteload"))
        frames.append(table)
    data = pd.concat(frames, ignore_index=True)
    stage = 2 if "oocyst" in dataset_id else 1
    data = data[pd.to_numeric(data["Stage"], errors="coerce") == stage].reset_index(drop=True)
    data["sampleid"] = data["sampleid"].astype(str).str.strip()
    if data["sampleid"].duplicated().any():
        raise ValueError("Original malaria sample IDs are not unique")
    data["join_key"] = [_malaria_id(value) for value in data["sampleid"]]
    if data.duplicated(["split_original", "join_key"]).any():
        raise ValueError("Original malaria table has ambiguous normalized sample IDs")
    sample_ids = set(zip(data["split_original"], data["join_key"], strict=True))
    spectral_rows = {}
    spectral_names = {}
    axis = None
    expected_stage = "oocyst" if stage == 2 else "sporozoite"
    with zipfile.ZipFile(spectra_archive) as spectra:
        for member in spectra.namelist():
            lower = member.casefold()
            if not lower.endswith(".spc") or expected_stage not in lower:
                continue
            member_split = "train" if "training dataset" in lower else "test" if "test dataset" in lower else None
            if member_split is None:
                raise ValueError(f"Malaria spectrum {member} has no native partition")
            key = (member_split, _malaria_id(Path(member).stem))
            if key not in sample_ids:
                continue
            records = open_bytes(Path(member).name, spectra.read(member))
            if len(records) != 1 or len(records[0]["signals"]) != 1:
                raise ValueError(f"Malaria spectrum {member} does not contain one signal")
            signal = next(iter(records[0]["signals"].values()))
            current = np.asarray(signal["axis"]["values"])
            if axis is None:
                axis = current
            if not np.array_equal(axis, current):
                raise ValueError(f"Malaria spectrum {member} uses a different axis")
            if key in spectral_rows:
                raise ValueError(f"Duplicate original malaria spectrum ID {member}")
            spectral_rows[key] = signal["values"]
            spectral_names[key] = member
    keys = list(zip(data["split_original"], data["join_key"], strict=True))
    missing = [key for key in keys if key not in spectral_rows]
    if missing or axis is None:
        raise ValueError(f"Original malaria spectra do not match {len(missing)} sample IDs; inspect publisher file naming and do not substitute local exports")
    block = pd.DataFrame([spectral_rows[key] for key in keys], columns=[str(x) for x in axis])
    data["spectrum_file"] = [spectral_names[key] for key in keys]
    data = data.drop(columns="join_key")
    data["x"] = data["parasite_load"]
    return _write(context, dataset_id, data, {"X": block}, ["x"], data["sampleid"], "https://doi.org/10.7910/DVN/YD34OX")

def build(descriptor, context) -> Path:
    """Download the declared original source and construct a standardized leaf."""
    dataset_id = descriptor.id
    if dataset_id in _MALARIA:
        return _malaria(dataset_id, context)
    if dataset_id == "chembl_ir_raman_multiblock":
        return _chembl(dataset_id, context)
    if dataset_id == "cartilage_spectroscopy_scientificdata_nir":
        return _cartilage(dataset_id, context)
    if dataset_id == "data_in_brief_rice_amylose_transflection_nir_matio":
        return _rice(dataset_id, context)
    if dataset_id in _ROD:
        return _rod(dataset_id, context)
    if dataset_id == "zenodo_tomato_leaf_stress_visnir_matio":
        return _tomato(dataset_id, context)
    if dataset_id in _UVA:
        return _uva(dataset_id, context)
    if dataset_id in _FLANAGAN:
        return _flanagan(dataset_id, context)
    if dataset_id in _PERTEN:
        return _perten(dataset_id, context)
    if dataset_id in _ZENODO:
        return _zenodo(dataset_id, context)
    raise ValueError(f"No tabular origin recipe for {dataset_id!r}")
