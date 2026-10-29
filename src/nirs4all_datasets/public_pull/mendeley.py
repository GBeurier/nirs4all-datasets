"""Reproduce supported Mendeley datasets from their public source files."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import DatasetDescriptor

_CHICKEN = "mendeley_chicken_meat_authenticity_handheld_nir"
_FEED = "mendeley_animal_feed_quality_nir"


def supports(dataset_id: str) -> bool:
    """Whether a dataset has an audited source conversion."""
    return dataset_id in {_CHICKEN, _FEED, *_TABLES, "mendeley_coffee_drying_ftnir_moisture", "mendeley_black_pmma_transmissivity_uvvisnir", "mendeley_specialty_coffee_green_roasted_ftnir", "mendeley_human_arm_muscle_vis_swir_reflectance", "mendeley_eliquid_alpha_mid_opus_manual", "mendeley_eliquid_invenio_fir_mid_nir_opus_manual", "mendeley_tobacco_leaf_chemical_nir_manual", "mendeley_diesel_biodiesel_ftmir_opus"}


def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    """Download the public Mendeley source and produce standardized tables."""
    if descriptor.id == "mendeley_diesel_biodiesel_ftmir_opus":
        return _build_diesel(descriptor, context)
    if descriptor.id == "mendeley_tobacco_leaf_chemical_nir_manual":
        return _build_tobacco(context)
    if descriptor.id.startswith("mendeley_eliquid_"):
        return _build_eliquid(descriptor, context)
    if descriptor.id == "mendeley_human_arm_muscle_vis_swir_reflectance":
        return _build_human_arm(descriptor, context)
    if descriptor.id == "mendeley_specialty_coffee_green_roasted_ftnir":
        return _build_specialty_coffee(descriptor, context)
    if descriptor.id == "mendeley_black_pmma_transmissivity_uvvisnir":
        return _build_pmma(descriptor, context)
    if descriptor.id == "mendeley_coffee_drying_ftnir_moisture":
        return _build_coffee_drying(descriptor, context)
    if descriptor.id in _TABLES:
        return _build_table(descriptor, context)
    if descriptor.id == _FEED:
        return _build_feed(descriptor, context)
    if descriptor.id != _CHICKEN:
        raise ValueError(f"Unsupported Mendeley dataset: {descriptor.id}")
    locator = "https://data.mendeley.com/datasets/cp2hdhkys3/6"
    filename = "Data-Parastar et al 2020 Food Control v2.csv"
    matches = [item for item in context.provider_files("mendeley", locator) if item["name"] == filename]
    if len(matches) != 1:
        raise ValueError(f"Expected one Mendeley source file named {filename!r}, found {len(matches)}")
    item = matches[0]
    path = context.download(item["url"], filename, sha256=item.get("sha256"), size=item.get("size"))
    data = pd.read_csv(path, sep=";")
    spectral_columns = [col for col in data.columns if col.startswith("X")]
    if len(spectral_columns) != 125:
        raise ValueError(f"Expected 125 spectral columns in {filename}, found {len(spectral_columns)}")
    ids = pd.Series([f"{descriptor.id}_{i:05d}" for i in range(1, len(data) + 1)], name="observation_id")
    x = data[spectral_columns].rename(columns=lambda col: col[1:]).copy()
    x.insert(0, "observation_id", ids)
    targets = data[["Production_system", "Scan_type", "Freshness"]].copy()
    targets.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": data["Sample_number"]})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_feed(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    locator = "https://data.mendeley.com/datasets/r6fjtx943d/1"
    filename = "Dataset NIR Spectrum of Animal Feed.xlsx"
    matches = [item for item in context.provider_files("mendeley", locator) if item["name"] == filename]
    if len(matches) != 1:
        raise ValueError(f"Expected one Mendeley source file named {filename!r}, found {len(matches)}")
    item = matches[0]
    path = context.download(item["url"], filename, sha256=item.get("sha256"), size=item.get("size"))
    table = pd.read_excel(path, sheet_name="RAW spectrum", header=3)
    table = table[pd.to_numeric(table.iloc[:, 0], errors="coerce").notna()].copy()
    if len(table) != 25 or len(table.columns) != 1562:
        raise ValueError(f"Unexpected source table shape: {table.shape}")
    ids = pd.Series([f"{descriptor.id}_{i:05d}" for i in range(1, len(table) + 1)], name="observation_id")
    table = table.reset_index(drop=True)
    x = table.iloc[:, 1:1558].copy()
    x.columns = [str(c) for c in x.columns]
    x.insert(0, "observation_id", ids)
    targets = table[["IVOMD", "IVDMD", "NDF", "ADF"]].copy()
    targets.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


_TABLES = {
    "mendeley_intact_mango_raw_nir": ("b9d6s7hr33", "Dataset_RawSpectrum_NIRS_for_Intact_Mangoes.xlsx", "RawData"),
    "mendeley_intact_mango_ta_vitc_raw_nir": ("ph57ynng46", "Spectra datasets NIRS_intact_mangos.xlsx", "Raw Spectra data"),
    "mendeley_agricultural_soil_fertility_nir": ("h8mht3jsbz", "NIR spectra Data of Soil samples and fertility properties as matrix X and Y.xlsx", "Data X (spectra data)"),
    "mendeley_homemade_soil_om_tc_nir": ("yt78nwnhbd", "Data research.xlsx", "Raw spectral + chemical"),
    "mendeley_cucurbitaceae_fruits_visnir": ("k55b8mvs84", "Dataset_RAW_Vis-NIR_Spectra_for_Intact_Cucurbitaceae_Fruits.xlsx", "Calibration Set"),
    "mendeley_cocoa_beans_moisture_fat_nir": ("7734j4fd98", "NIRS spectrum Cocoa Beans.xlsx", "Absorbance Spectrum"),
}


def _build_table(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    dataset, filename, sheet = _TABLES[descriptor.id]
    matches = [f for f in context.provider_files("mendeley", f"https://data.mendeley.com/datasets/{dataset}/1") if f["name"] == filename]
    if len(matches) != 1:
        raise ValueError(f"Expected one Mendeley file {filename!r}")
    item = matches[0]
    path = context.download(item["url"], filename, sha256=item.get("sha256"), size=item.get("size"))
    table = pd.read_excel(path, sheet_name=sheet, header=6 if dataset == "7734j4fd98" else 0)
    if dataset == "k55b8mvs84":
        a = table.copy()
        b = pd.read_excel(path, sheet_name="Prediction Set")
        a["original_split"] = "calibration"
        b["original_split"] = "prediction"
        table = pd.concat([a, b], ignore_index=True)
    table = table.reset_index(drop=True)
    targets_names = {
        "b9d6s7hr33": ([1, 2, 3, 4], ["Mango_Cultivar", "Vit_C_mg_100g", "TA_mg_100g", "SSC_oBrix"]),
        "h8mht3jsbz": (list(range(1, 7)), ["N_content_pct", "P_ppm", "K_cmol_kg", "pH_KCl", "Mg_cmol_kg", "Ca_cmol_kg"]),
        "7734j4fd98": ([-2, -1], ["Moisture_Content_pct", "Fat_Content_pct"]),
        "ph57ynng46": ([1, 2], ["TA_mg_100gr_FM", "Vit_C_mg_100gr_FM"]),
        "k55b8mvs84": ([1, 2], ["Water_Content_pct", "SSC_pct"]),
        "yt78nwnhbd": ([-2, -1], ["OM_pct", "TC_pct"]),
    }
    positions, names = targets_names[dataset]
    targets_source = table
    if dataset in {"h8mht3jsbz", "ph57ynng46"}:
        targets_source = pd.read_excel(path, sheet_name="Data Y (soil properties)" if dataset == "h8mht3jsbz" else "TA and Vit C")
        if not table.iloc[:, 0].equals(targets_source.iloc[:, 0]):
            raise ValueError("Spectra and targets have different sample identifiers")
    targets = targets_source.iloc[:, positions].copy()
    targets.columns = names
    excluded = {"b9d6s7hr33": (5, -1), "h8mht3jsbz": (1, None), "7734j4fd98": (1, -2), "ph57ynng46": (2, None), "k55b8mvs84": (3, -1), "yt78nwnhbd": (1, -2)}
    start, end = excluded[dataset]
    features = table.iloc[:, start:end].copy()
    features.columns = [str(c) for c in features.columns]
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(table) + 1)]
    features.insert(0, "observation_id", ids)
    targets.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": table.iloc[:, 0]})
    if dataset == "ph57ynng46":
        metadata["mango_variety"] = table.iloc[:, 1]
    if dataset == "b9d6s7hr33":
        metadata["original_label"] = table.iloc[:, -1]
    if dataset == "k55b8mvs84":
        metadata["original_split"] = table["original_split"]
        metadata["split_original"] = table["original_split"]
        metadata["commodity"] = table.iloc[:, 0].str.rsplit(" ", n=1).str[0]
    return context.write_tables({"X": features}, targets=targets, metadata=metadata)


def _build_coffee_drying(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/7c6gx7rr6d/1")
    def download(name: str) -> Path:
        matches = [f for f in files if f["name"] == name]
        if len(matches) != 1:
            raise ValueError(f"Expected one Mendeley file {name!r}")
        item = matches[0]
        return context.download(item["url"], name, sha256=item.get("sha256"), size=item.get("size"))
    spectra = pd.read_excel(download("FTNIR_Data.xlsx"), sheet_name="FTNIR_data ")
    moisture = pd.read_excel(download("Moisture_values.xlsx"), sheet_name="Hoja1").set_index("Sample")
    axis = spectra.iloc[:, 0].astype(str).tolist()
    labels = [str(c) for c in spectra.columns[1:]]
    groups = [label.rsplit("_", 1)[0] for label in labels]
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(labels) + 1)]
    x = spectra[labels].T.reset_index(drop=True)
    x.columns = axis
    x.insert(0, "observation_id", ids)
    targets = pd.DataFrame({"observation_id": ids, "Moisture_WB": moisture["Moisture W.B"].reindex(groups).to_numpy()})
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": labels, "sample_group": groups, "replicate": [label.rsplit("_", 1)[1] for label in labels]})
    metadata["moisture_standard_deviation"] = moisture["Standard deviation"].reindex(groups).to_numpy()
    metadata["moisture_coefficient_of_variation_pct"] = moisture["Coefficient of variation (%)"].reindex(groups).to_numpy()
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_pmma(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/8wpgzrp33s/1")
    frames = []
    for thickness in (50, 73):
        filename = f"Transmissivity_{thickness}µm_UV-Vis-NIR.xlsx"
        matches = [f for f in files if f["name"] == filename]
        if len(matches) != 1:
            raise ValueError(f"Expected one Mendeley file {filename!r}")
        item = matches[0]
        path = context.download(item["url"], filename, sha256=item.get("sha256"), size=item.get("size"))
        frame = pd.read_excel(path)
        if list(frame.columns) != ["Wavelength (µm)", "Transmissivity (%)"]:
            raise ValueError(f"Unexpected source columns in {filename}")
        frames.append(frame)
    if not frames[0].iloc[:, 0].equals(frames[1].iloc[:, 0]):
        raise ValueError("PMMA source spectra have different wavelength axes")
    ids = [f"{descriptor.id}_{n}um" for n in (50, 73)]
    x = pd.DataFrame([f.iloc[:, 1].to_numpy() for f in frames], columns=[str(w) for w in frames[0].iloc[:, 0]])
    x.insert(0, "observation_id", ids)
    targets = pd.DataFrame({"observation_id": ids, "film_thickness_um": [50, 73]})
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": ["black_PMMA_50um", "black_PMMA_73um"]})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_specialty_coffee(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/nz2fr76trm/3")
    def download(name: str) -> Path:
        matches = [f for f in files if f["name"] == name]
        if len(matches) != 1:
            raise ValueError(f"Expected one Mendeley file {name!r}")
        item = matches[0]
        return context.download(item["url"], name, sha256=item.get("sha256"), size=item.get("size"))
    green = pd.read_excel(download("RawSpectra_GreenCoffee.xlsx"), header=None)
    roasted = pd.read_excel(download("RawSpectra_RoastedCoffee.xlsx"), header=None)
    sensory = pd.read_excel(download("SensoryQuality_RoastedCoffee.xlsx"))
    sample = green.iloc[0, 1:].ffill().astype(int).tolist()
    replicate = green.iloc[1, 1:].astype(int).tolist()
    if sample != roasted.iloc[0, 1:].ffill().astype(int).tolist() or replicate != roasted.iloc[1, 1:].astype(int).tolist():
        raise ValueError("Green and roasted coffee samples do not align")
    if not green.iloc[3:, 0].equals(roasted.iloc[3:, 0]):
        raise ValueError("Green and roasted coffee axes differ")
    sensory.iloc[:, 0] = sensory.iloc[:, 0].ffill()
    by_key = sensory.set_index([sensory.columns[0], sensory.columns[1]])
    keys = list(zip(sample, replicate, strict=True))
    if not all(key in by_key.index for key in keys):
        raise ValueError("Coffee sensory values do not align with spectra")
    ids = [f"{descriptor.id}_{s:03d}_{r}" for s, r in keys]
    sources = {}
    for name, frame in (("X1", green), ("X2", roasted)):
        x = frame.iloc[3:, 1:].T.reset_index(drop=True)
        x.columns = [str(int(w)) if float(w).is_integer() else str(w) for w in frame.iloc[3:, 0]]
        x.insert(0, "observation_id", ids)
        sources[name] = x
    targets = pd.DataFrame({"observation_id": ids, "Cup_quality_points": [by_key.loc[key].iloc[0] for key in keys]})
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": sample, "replicate": replicate})
    return context.write_tables(sources, targets=targets, metadata=metadata)


def _build_human_arm(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/24pg3ywxs5/1")
    def download(name: str) -> Path:
        matches = [f for f in files if f["name"] == name]
        if len(matches) != 1:
            raise ValueError(f"Expected one Mendeley file {name!r}")
        item = matches[0]
        return context.download(item["url"], name, sha256=item.get("sha256"), size=item.get("size"))
    source = pd.read_csv(download("Reflectance_spectra.csv"), header=None, low_memory=False)
    demographics = pd.read_csv(download("Table.csv"), header=None)
    axis = pd.to_numeric(source.iloc[8, 4:], errors="raise")
    table = source.iloc[9:].reset_index(drop=True)
    labels = table.iloc[:, 1].astype(str).str.strip()
    parts = labels.str.extract(r"^(S\d+)\s+([BD])$")
    if parts.isna().any().any():
        raise ValueError("Unexpected subject/aspect labels in human arm source")
    subjects = demographics.iloc[10:, [1, 3, 4, 5, 6, 7]].copy()
    subjects.columns = ["subject_id", "age_years", "sex_code", "weight_kg", "height_cm", "bmi"]
    subjects = subjects.dropna(subset=["subject_id"]).set_index("subject_id")
    if not parts[0].isin(subjects.index).all():
        raise ValueError("Human arm spectra do not match demographics")
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(table) + 1)]
    x = table.iloc[:, 4:].apply(pd.to_numeric, errors="raise")
    x.columns = [str(int(v)) if float(v).is_integer() else str(v) for v in axis]
    x.insert(0, "observation_id", ids)
    classes = table.iloc[:, 3]
    targets = pd.DataFrame({"observation_id": ids, "muscle_class": classes, "arm_aspect": parts[1].map({"B": "ventral_arm", "D": "dorsal_arm"})})
    metadata = subjects.loc[parts[0]].reset_index()
    metadata.insert(0, "observation_id", ids)
    metadata["arm_aspect_code"] = parts[1]
    metadata["source_label"] = parts[0] + parts[1]
    metadata["sample_id"] = metadata["source_label"]
    metadata["replicate_index_within_subject_aspect"] = labels.groupby(labels).cumcount() + 1
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_eliquid(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    from nirs4all_datasets.public_pull import native as nirs4all_formats

    alpha = descriptor.id == "mendeley_eliquid_alpha_mid_opus_manual"
    dataset = "ddrzk7t5nt" if alpha else "2cwtxdtstn"
    prefix = "eliquid_alpha" if alpha else "eliquid_invenio"
    files = sorted(context.provider_files("mendeley", f"https://data.mendeley.com/datasets/{dataset}/1"), key=lambda f: f["name"])
    if not files:
        raise ValueError("No public OPUS files found")
    axes = None
    spectra = []
    labels = []
    for item in files:
        path = context.download(item["url"], item["name"], sha256=item.get("sha256"), size=item.get("size"))
        records = nirs4all_formats.open_records(path)
        if len(records) != 1 or "transmittance" not in records[0]["signals"]:
            raise ValueError(f"Missing single transmittance spectrum in {item['name']!r}")
        signal = records[0]["signals"]["transmittance"]
        axis = signal["axis"]["values"]
        if axes is None:
            axes = axis
        elif len(axis) != len(axes) or any(abs(a-b) > 1e-5 for a, b in zip(axis, axes, strict=True)):
            raise ValueError(f"Spectral axis differs in {item['name']!r}")
        labels.append(Path(item["name"]).stem)
        spectra.append(signal["values"])
    ids = [f"{prefix}_{label}" for label in labels]
    assert axes is not None
    x = pd.DataFrame(spectra, columns=[str(v) for v in axes])
    x.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": labels, "instrument_family": prefix, "format_reader": "nirs4all_formats::readers::bruker_opus", "format_name": "bruker-opus", "signal_name": "transmittance"})
    return context.write_tables({"X": x}, metadata=metadata)


def _build_tobacco(context: PullContext) -> Path:
    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/9z7dgdtggk/1")
    def download(name: str) -> Path:
        matches = [f for f in files if f["name"] == name]
        if len(matches) != 1:
            raise ValueError(f"Expected one Mendeley file {name!r}")
        item = matches[0]
        return context.download(item["url"], name, sha256=item.get("sha256"), size=item.get("size"))
    raw = pd.read_excel(download("Raw-nir-spectra-data-B9Y2sV.xlsx"))
    chemistry = pd.read_excel(download("13-Chemical-Components-data-auTyGX.xlsx"))
    if not raw.iloc[:, 0].equals(chemistry.iloc[:, 0]):
        raise ValueError("Tobacco spectral and chemical sample IDs do not align")
    ids = [f"tobacco_leaf_{int(n):03d}" for n in raw.iloc[:, 0]]
    x = raw.iloc[:, 4:].copy()
    x.columns = [str(c) for c in x.columns]
    x.insert(0, "observation_id", ids)
    targets = chemistry.iloc[:, 1:].copy()
    targets.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": raw.iloc[:, 0], "year": raw.iloc[:, 1], "origin_label": raw.iloc[:, 2], "original_row_number": raw.iloc[:, 3]})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_diesel(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    from nirs4all_datasets.public_pull import native as nirs4all_formats

    files = context.provider_files("mendeley", "https://data.mendeley.com/datasets/d7sx7bf2hk/1")
    labels = json.loads(Path(__file__).with_name("mendeley_diesel_recipes.json").read_text(encoding="utf-8"))["products"]
    by_lot = {entry["lot_number"]: entry for entry in labels}
    axes = None
    rows = []
    selected = []
    for item in sorted(files, key=lambda f: f["name"]):
        lot = Path(item["name"]).stem.replace("DO_", "D0_", 1)
        if lot not in by_lot:
            raise ValueError(f"No published product label for OPUS file {item['name']!r}")
        path = context.download(item["url"], item["name"], sha256=item.get("sha256"), size=item.get("size"))
        records = nirs4all_formats.open_records(path)
        if len(records) != 1 or "transmittance" not in records[0]["signals"]:
            raise ValueError(f"Missing single transmittance spectrum in {item['name']!r}")
        signal = records[0]["signals"]["transmittance"]
        axis = signal["axis"]["values"]
        if axes is None:
            axes = axis
        elif len(axis) != len(axes) or any(abs(a-b) > 1e-5 for a, b in zip(axis, axes, strict=True)):
            raise ValueError(f"Spectral axis differs in {item['name']!r}")
        rows.append(signal["values"])
        selected.append((lot, item, by_lot[lot]))
    if len(selected) != len(by_lot):
        raise ValueError("Published diesel product labels do not match source files")
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(rows) + 1)]
    assert axes is not None
    x = pd.DataFrame(rows, columns=[str(v) for v in axes])
    x.insert(0, "observation_id", ids)
    targets = pd.DataFrame({"observation_id": ids, "fuel_blend_class": ["B7" if lot.startswith("DE5_") else "B10" for lot, _, _ in selected], "product_name": [entry["product_name"] for _, _, entry in selected], "brand": [entry["brand"] for _, _, entry in selected]})
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": [Path(item["name"]).stem for _, item, _ in selected], "lot_number": [lot for lot, _, _ in selected]})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)
