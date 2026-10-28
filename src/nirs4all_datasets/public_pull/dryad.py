"""Reproduce audited Dryad datasets from public version archives."""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

import pandas as pd

from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import DatasetDescriptor

_BEETLE = {
    "dryad_beetle_reflectance_manual": "1_Reflectancedata.csv",
    "dryad_scarab_reflectance_firstbatch_manual": "2_Reflectance_FirstBatch.csv",
    "dryad_beetle_transmittance_top_manual": "2_Transmittancetopdata.csv",
    "dryad_beetle_transmittance_ventral_manual": "3_Transmittanceventraldata.csv",
}


def supports(dataset_id: str) -> bool:
    """Whether the dataset has an audited source conversion."""
    return dataset_id in _BEETLE or dataset_id in {"dryad_grassland_hyspex_species_manual", "dryad_beech_leaf_second_derivative_nir_manual", "dryad_frogs_spectraldata_reflectance_manual", "dryad_avocado_oo_benchtop_snv_nir_manual", "dryad_avocado_felix_handheld_nir_manual", "dryad_walnut_moisture_nir_manual", "dryad_guava_leaf_infestation_visnir_manual", "dryad_bird_nh_reflectance_manual", "dryad_bird_nn_reflectance_manual", "dryad_drosophila_spc_nir_manual", "dryad_gastropods_reflectance_manual", "dryad_dragon_lizard_reflectance_manual", "dryad_tree_leaf_girdling_visnir_manual", "dryad_herbarium_resurvey_nirs_manual", "dryad_tree_tissue_nsc_nir_manual", "dryad_rice_leaf_reflectance_manual", "dryad_sea_cucumber_representative_nir_manual"}


def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    """Download and transpose the published beetle spectral table."""
    if descriptor.id == "dryad_rice_leaf_reflectance_manual":
        return _build_rice(context)
    if descriptor.id == "dryad_sea_cucumber_representative_nir_manual":
        return _build_sea_cucumber(context)
    if descriptor.id == "dryad_tree_tissue_nsc_nir_manual":
        return _build_tree_tissue(context)
    if descriptor.id == "dryad_herbarium_resurvey_nirs_manual":
        return _build_herbarium(context)
    if descriptor.id == "dryad_tree_leaf_girdling_visnir_manual":
        return _build_tree_leaf(context)
    if descriptor.id == "dryad_dragon_lizard_reflectance_manual":
        return _build_lizard(context)
    if descriptor.id == "dryad_gastropods_reflectance_manual":
        return _build_gastropods(context)
    if descriptor.id == "dryad_drosophila_spc_nir_manual":
        return _build_drosophila(context)
    if descriptor.id in {"dryad_bird_nh_reflectance_manual", "dryad_bird_nn_reflectance_manual"}:
        return _build_bird(descriptor, context)
    if descriptor.id == "dryad_grassland_hyspex_species_manual":
        return _build_grassland(context)
    if descriptor.id == "dryad_beech_leaf_second_derivative_nir_manual":
        return _build_beech(context)
    if descriptor.id == "dryad_frogs_spectraldata_reflectance_manual":
        return _build_frogs(context)
    if descriptor.id.startswith("dryad_avocado_"):
        return _build_avocado(descriptor, context)
    if descriptor.id == "dryad_walnut_moisture_nir_manual":
        return _build_walnut(descriptor, context)
    if descriptor.id == "dryad_guava_leaf_infestation_visnir_manual":
        return _build_guava(context)
    filename = _BEETLE[descriptor.id]
    version = "331103" if descriptor.id == "dryad_scarab_reflectance_firstbatch_manual" else "196843"
    url = f"https://datadryad.org/api/v2/versions/{version}/download"
    archive = context.download(url, f"dryad_{version}.zip")
    extracted = context.extract(archive)
    matches = list(extracted.rglob(filename))
    if len(matches) != 1:
        raise ValueError(f"Expected one Dryad file named {filename!r}, found {len(matches)}")
    table = pd.read_csv(matches[0])
    if table.columns[0] != "wl" or table.shape[1] < 2:
        raise ValueError(f"Unexpected source table shape or axis in {filename}: {table.shape}")
    axis = table.iloc[:, 0].astype(str).tolist()
    labels = table.columns[1:].tolist()
    ids = [f"{descriptor.id}_{label}" for label in labels]
    x = table.iloc[:, 1:].T.reset_index(drop=True)
    x.columns = axis
    x.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": labels})
    return context.write_tables({"X": x}, metadata=metadata)


def _build_grassland(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/235566/download", "dryad_cfxpnvx9w_20230517.zip")
    root = context.extract(archive)
    spectra = pd.read_csv(root / "Hyspex.csv")
    plants = pd.read_csv(root / "Plant_species_data.csv").set_index("Plot_ID")
    plots = pd.read_csv(root / "Plots_info.csv")
    plots["key"] = plots["Plot_ID"].str.replace("_", "", regex=False)
    plots = plots.set_index("key")
    keys = spectra.pop("Plot_ID")
    if not keys.is_unique or not keys.isin(plants.index).all() or not keys.isin(plots.index).all():
        raise ValueError("Grassland spectral plots do not uniquely match source metadata and targets")
    ids = [f"grassland_{key}" for key in keys]
    spectra.columns = [str(c).removeprefix("X") for c in spectra.columns]
    spectra.insert(0, "observation_id", ids)
    targets = plants.loc[keys].reset_index(drop=True)
    targets.insert(0, "observation_id", ids)
    metadata = plots.loc[keys].reset_index(drop=True).rename(columns={"Plot_ID": "plot_id_info", "Site": "site", "Age": "age", "SWE99TM_X": "swe99tm_x", "SWE99TM_Y": "swe99tm_y"})
    metadata.insert(0, "plot_id", keys.to_numpy())
    metadata.insert(0, "observation_id", ids)
    return context.write_tables({"X": spectra}, targets=targets, metadata=metadata)


def _build_beech(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/437733/download", "dryad_m37pvmdgv.zip")
    table = pd.read_csv(context.extract(archive) / "Second_derivative_ANF.csv")
    table.columns = [str(c).removeprefix("X") for c in table.columns]
    ids = [f"beech_leaf_{i:04d}" for i in range(1, len(table) + 1)]
    table.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "source_row_index": range(1, len(table) + 1)})
    return context.write_tables({"X": table}, metadata=metadata)


def _build_frogs(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/345375/download", "dryad_6t1g1jx4p.zip")
    table = pd.read_csv(context.extract(archive) / "spectraldata.csv")
    keys = ["species", "NIR", "type", "treatment"]
    matrix = table.pivot(index=keys, columns="wl", values="refl").reset_index()
    ids = ["frogs_" + "_".join(map(str, row)) for row in matrix[keys].itertuples(index=False, name=None)]
    metadata = matrix[keys].rename(columns={"NIR": "nir_class"}).copy()
    metadata.insert(0, "observation_id", ids)
    x = matrix.drop(columns=keys)
    x.columns = [str(col) for col in x.columns]
    x.insert(0, "observation_id", ids)
    return context.write_tables({"X": x}, metadata=metadata)


def _build_avocado(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/294315/download", "dryad_avocado.zip")
    root = context.extract(archive)
    felix = descriptor.id == "dryad_avocado_felix_handheld_nir_manual"
    table = pd.read_excel(root / ("Felix_2nd_ave.xlsx" if felix else "OO_All199_ave_SNV.xlsx"))
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(table) + 1)]
    features = table.iloc[:, 5 if felix else 2:].copy()
    features.columns = [str(c).removeprefix("W").removesuffix("nm") for c in features.columns]
    features.insert(0, "observation_id", ids)
    targets = table[["Variety", "Days in Room Temp"] if felix else ["Variety"]].copy()
    if felix:
        targets["Days in Room Temp"] = pd.to_numeric(targets["Days in Room Temp"], errors="coerce")
    targets.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": table["Sample ID"]})
    if not felix:
        metadata["sample_id"] = table["Sample ID"]
    if felix:
        metadata["harvest_date"] = table["Harvest Date"].astype(str)
        metadata["nir_date"] = table["NIR Date"].astype(str)
    else:
        metadata["variety"] = table["Variety"]
    return context.write_tables({"X": features}, targets=targets, metadata=metadata)


def _build_walnut(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/110168/download", "dryad_walnut.zip")
    workbook = context.extract(archive) / "Measured_value+Raw_spectral_data.xlsx"
    table = pd.read_excel(workbook, sheet_name="Measured value+ spectral data", header=None)
    axis = [str(int(x)) if float(x).is_integer() else str(x) for x in table.iloc[2:, 0]]
    values = table.iloc[2:, 1:].T.reset_index(drop=True)
    values.columns = axis
    ids = [f"{descriptor.id}_{i:05d}" for i in range(1, len(values) + 1)]
    values.insert(0, "observation_id", ids)
    targets = pd.DataFrame({"observation_id": ids, "moisture_content_percent": pd.to_numeric(table.iloc[1, 1:]).to_numpy()})
    calibration = pd.read_excel(workbook, sheet_name="Calibration set", header=None)
    prediction = pd.read_excel(workbook, sheet_name="Prediction set", header=None)
    def signatures(frame: pd.DataFrame) -> set[tuple[float, ...]]:
        return {tuple(round(float(x), 9) for x in frame.iloc[2:10, j]) for j in range(1, frame.shape[1])}
    cal_keys, pred_keys = signatures(calibration), signatures(prediction)
    keys = [tuple(round(float(x), 9) for x in table.iloc[2:10, j]) for j in range(1, table.shape[1])]
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": [f"walnut_kernel_{i:05d}" for i in range(1, len(ids) + 1)], "split": ["calibration" if key in cal_keys and key not in pred_keys else "prediction" if key in pred_keys and key not in cal_keys else "unknown" for key in keys]})
    metadata["split_original"] = metadata["split"].replace("unknown", pd.NA)
    return context.write_tables({"X": values}, targets=targets, metadata=metadata)


def _build_guava(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/429117/download", "dryad_guava.zip")
    root = context.extract(archive)
    nested = context.extract(root / "Dataset-Spectral.zip")
    table = pd.read_csv(nested / "Dataset" / "Data-global.csv", sep=";", decimal=",")
    labels = [c for c in table.columns if (c.startswith("Infested L") or c.startswith("Uninfested L")) and "-R" in c]
    if len(labels) != 15:
        raise ValueError(f"Expected 15 guava replicate spectra, found {len(labels)}")
    ids = ["guava_leaf_" + label.replace(" ", "_").replace("-", "_") for label in labels]
    x = table[labels].T.reset_index(drop=True)
    x.columns = table["Wavelength"].astype(str)
    x.insert(0, "observation_id", ids)
    classes = ["uninfested" if label.startswith("Uninfested") else label.split("-")[0].lower().replace(" ", "_") for label in labels]
    targets = pd.DataFrame({"observation_id": ids, "infestation_status": classes})
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": labels})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_bird(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/444775/download", "dryad_bird.zip")
    workbook = context.extract(archive) / "Final.BirdData.xlsx"
    sheet = "NHReflectance" if descriptor.id == "dryad_bird_nh_reflectance_manual" else "NNReflectance"
    table = pd.read_excel(workbook, sheet_name=sheet)
    axis = pd.to_numeric(table.iloc[:, 0], errors="raise") * 1000
    labels = [str(c) for c in table.columns[1:]]
    ids = [f"bird_{sheet.lower()}_{label}" for label in labels]
    x = table.iloc[:, 1:].T.reset_index(drop=True)
    x.columns = [format(v, ".12g") for v in axis]
    x.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": labels, "measurement_sheet": sheet})
    return context.write_tables({"X": x}, metadata=metadata)


def _build_drosophila(context: PullContext) -> Path:
    from nirs4all_datasets.public_pull import native as nirs4all_formats

    archive = context.download("https://datadryad.org/api/v2/versions/22999/download", "dryad_drosophila.zip")
    nested = context.extract(context.extract(archive) / "NIRS.zip")
    files = sorted(p for p in nested.rglob("*.spc") if "__MACOSX" not in p.parts)
    if not files:
        raise ValueError("No Drosophila SPC spectra in source archive")
    axes = None
    rows = []
    for path in files:
        records = nirs4all_formats.open_records(path)
        if len(records) != 1 or "absorbance" not in records[0]["signals"]:
            raise ValueError(f"Expected one absorbance spectrum in {path.name}")
        signal = records[0]["signals"]["absorbance"]
        axis = signal["axis"]["values"]
        if axes is None:
            axes = axis
        elif len(axis) != len(axes) or any(abs(a-b) > 1e-5 for a, b in zip(axis, axes, strict=True)):
            raise ValueError(f"Drosophila axis differs in {path.name}")
        rows.append(signal["values"])
    assert axes is not None
    labels = [p.stem for p in files]
    if len(set(labels)) != len(labels):
        raise ValueError("Drosophila source file identifiers are not unique")
    ids = [f"drosophila_{label}" for label in labels]
    x = pd.DataFrame(rows, columns=[format(v, ".12g") for v in axes])
    x.insert(0, "observation_id", ids)
    groups = [re.sub(r"\d+$", "", label) for label in labels]
    targets = pd.DataFrame({"observation_id": ids, "sample_group_code": groups})
    metadata = pd.DataFrame({"observation_id": ids, "dataset_subset": [p.parent.name for p in files], "format_reader": "nirs4all_formats::readers::galactic_spc", "format_name": "galactic-spc"})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_gastropods(context: PullContext) -> Path:
    from nirs4all_datasets.public_pull import native as nirs4all_formats

    archive = context.download("https://datadryad.org/api/v2/versions/209701/download", "dryad_gastropods.zip")
    root = context.extract(context.extract(archive) / "Spec_RealDat.zip")
    files = sorted(p for p in root.rglob("*.txt") if "__MACOSX" not in p.parts)
    if not files:
        raise ValueError("No gastropod spectra in source archive")
    spectra = []
    all_axes: set[float] = set()
    for path in files:
        records = nirs4all_formats.open_records(path)
        if len(records) != 1 or "processed" not in records[0]["signals"]:
            raise ValueError(f"Expected one processed spectrum in {path.name}")
        signal = records[0]["signals"]["processed"]
        axis = signal["axis"]["values"]
        if len(set(axis)) != len(axis):
            raise ValueError(f"Duplicate gastropod wavelengths in {path.name}")
        all_axes.update(axis)
        spectra.append(dict(zip(axis, signal["values"], strict=True)))
    axes = sorted(all_axes)
    labels = [p.stem for p in files]
    if len(set(labels)) != len(labels):
        raise ValueError("Gastropod source file identifiers are not unique")
    ids = [f"gastropod_{label}" for label in labels]
    x = pd.DataFrame(spectra, columns=axes)
    x.columns = [format(v, ".12g") for v in axes]
    x.insert(0, "observation_id", ids)
    codes = [label.split("_") for label in labels]
    if any(len(c) < 5 for c in codes):
        raise ValueError("Unexpected gastropod sample label")
    metadata = pd.DataFrame({"observation_id": ids, "species_code": [c[0] for c in codes], "individual_id": [c[1] for c in codes], "state": [c[2] for c in codes], "body_region": [c[3] for c in codes], "size_code": [c[4] for c in codes]})
    return context.write_tables({"X": x}, metadata=metadata)


def _build_lizard(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/20537/download", "dryad_dragon_lizard.zip")
    root = context.extract(archive)
    sources = [("Raw beard reflectance values for temperature-independent experiments_Smith et al. 2016.xls", "temperature_independent"), ("Raw Reflectance Values Temperature-Dependent Experiments_Smith et al 2016.xls", "temperature_dependent")]
    axis = None
    rows = []
    records = []
    for filename, experiment in sources:
        workbook = pd.ExcelFile(root / filename)
        for sheet in workbook.sheet_names:
            table = pd.read_excel(workbook, sheet_name=sheet, header=3)
            current_axis = pd.to_numeric(table.iloc[:, 0], errors="raise").tolist()
            if axis is None:
                axis = current_axis
            elif current_axis != axis:
                raise ValueError(f"Different wavelength axis in {filename}: {sheet}")
            for name in table.columns[1:]:
                animal, condition = str(name).split("-", 1)
                identity = f"dragon_lizard_{sheet.replace(' ', '_')}_{animal}_{condition}_{experiment}"
                rows.append(table[name].tolist())
                records.append((identity, animal, sheet, condition, experiment, filename))
    assert axis is not None
    metadata = pd.DataFrame(records, columns=["observation_id", "animal_id", "body_region", "condition", "experiment", "origin_file"])
    x = pd.DataFrame(rows, columns=[str(v) for v in axis])
    x.insert(0, "observation_id", metadata["observation_id"])
    targets = metadata[["observation_id", "condition"]].copy()
    metadata = metadata.drop(columns="condition")
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_tree_leaf(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/89384/download", "dryad_tree_leaf.zip")
    root = context.extract(archive)
    files = sorted(root.glob("Cam??_*_spectra.xlsx"))
    if len(files) != 10:
        raise ValueError(f"Expected ten tree leaf spectral tables, found {len(files)}")
    features = []
    info = []
    axis = None
    for path in files:
        camera, kind, _ = path.stem.split("_")
        treatment = {"con": "control", "grd": "girdled"}[kind]
        table = pd.read_excel(path)
        current_axis = [str(c) for c in table.columns[1:]]
        if axis is None:
            axis = current_axis
        elif axis != current_axis:
            raise ValueError(f"Tree leaf spectral axis differs in {path.name}")
        for row, label in enumerate(table.iloc[:, 0].astype(str)):
            safe = re.sub(r"[^A-Za-z0-9]+", "_", label).strip("_")
            info.append((f"tree_leaf_{camera}_{treatment}_{row}_{safe}", label, camera, treatment))
        features.append(table.iloc[:, 1:])
    x = pd.concat(features, ignore_index=True)
    assert axis is not None
    x.columns = axis
    metadata = pd.DataFrame(info, columns=["observation_id", "leaf_code", "camera", "treatment"])
    x.insert(0, "observation_id", metadata["observation_id"])
    targets = metadata[["observation_id", "treatment"]].copy()
    return context.write_tables({"X": x}, targets=targets, metadata=metadata.drop(columns="treatment"))


def _build_herbarium(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/334916/download", "dryad_herbarium.zip")
    nested = context.extract(context.extract(archive) / "Kuehn_et_al._Resurvey_-_JEcol_Open_Data.zip")
    files = sorted(p for p in nested.rglob("*.dpt") if "__MACOSX" not in p.parts)
    if not files:
        raise ValueError("No tabular herbarium spectra in source archive")
    axes = None
    spectra = []
    ids = []
    subsets = []
    for path in files:
        table = pd.read_csv(path, sep="\t", header=None)
        if table.shape[1] != 2:
            raise ValueError(f"Expected wavelength and spectral value in {path.name}")
        axis = table.iloc[:, 0].tolist()
        if axes is None:
            axes = axis
        elif axis != axes:
            raise ValueError(f"Herbarium spectral axis differs in {path.name}")
        spectra.append(table.iloc[:, 1].tolist())
        subsets.append(path.parent.name)
        ids.append(f"herbarium_{path.parent.name}_{path.stem}")
    if len(set(ids)) != len(ids):
        raise ValueError("Herbarium source identifiers are not unique")
    assert axes is not None
    x = pd.DataFrame(spectra, columns=[str(v) for v in axes])
    x.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "dataset_subset": subsets, "original_sample_id": [p.stem for p in files]})
    return context.write_tables({"X": x}, metadata=metadata)


def _build_tree_tissue(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/25511/download", "dryad_tree_tissue.zip")
    root = context.extract(archive)
    spectra = pd.read_csv(root / "spectra_data.csv", encoding="latin1")
    info = pd.read_csv(root / "info_samples.csv", encoding="latin1")
    chemistry = pd.read_csv(root / "NSC_data.csv", encoding="latin1")
    sample = spectra.iloc[:, 0].astype(str)
    if sample.duplicated().any() or chemistry["Probe name"].duplicated().any() or info["sample"].duplicated().any():
        raise ValueError("Tree tissue source contains duplicate sample identifiers")
    ids = [f"tree_tissue_{label}" for label in sample]
    x = spectra.iloc[:, 1:].copy()
    x.columns = [str(i) for i in range(1, x.shape[1] + 1)]
    x.insert(0, "observation_id", ids)
    values = chemistry.set_index("Probe name").reindex(sample)[["TG*10", "Sugars", "Starch", "NSC"]].reset_index(drop=True)
    values.insert(0, "observation_id", ids)
    metadata = info.set_index("sample").reindex(sample).reset_index(drop=True).rename(columns={"analysis date": "analysis_date"})
    source_chemistry = chemistry.set_index("Probe name").reindex(sample).reset_index(drop=True)
    metadata["nsc_probe"] = source_chemistry["Probe"]
    metadata["nsc_tissue"] = source_chemistry["tissue"]
    metadata["nsc_place"] = source_chemistry["place"]
    metadata.insert(0, "sample_id", sample.to_numpy())
    metadata.insert(0, "original_sample_id", sample.to_numpy())
    metadata.insert(0, "observation_id", ids)
    return context.write_tables({"X": x}, targets=values, metadata=metadata)


def _extract_rar(context: PullContext, path: Path, suffix: str) -> Path:
    from py7zz import SevenZipFile

    output = context.directory / f"rar-{path.stem}"
    output.mkdir(exist_ok=True)
    with SevenZipFile(path) as archive:
        members = [name for name in archive.namelist() if name.lower().endswith(suffix)]
        if not members:
            raise ValueError(f"No {suffix} source files in {path.name}")
        if any(PurePosixPath(name.replace("\\", "/")).is_absolute() or ".." in PurePosixPath(name.replace("\\", "/")).parts or re.match(r"^[A-Za-z]:", name) for name in members):
            raise ValueError("Unsafe source archive member")
        archive.extractall(output, members=members)
    return output


def _build_sea_cucumber(context: PullContext) -> Path:
    from nirs4all_datasets.public_pull import native as nirs4all_formats

    archive = context.download("https://datadryad.org/api/v2/versions/21634/download", "dryad_sea_cucumber.zip")
    root = context.extract(archive)
    files = sorted(_extract_rar(context, root / "representative original spectra.rar", ".dpt").rglob("*.dpt"))
    axes = None
    rows = []
    for path in files:
        try:
            table = pd.read_csv(path, header=None)
            if table.shape[1] != 2:
                raise ValueError(f"Expected two tabular spectral columns in {path.name}")
            axis, values = table.iloc[:, 0].tolist(), table.iloc[:, 1].tolist()
        except UnicodeDecodeError:
            records = nirs4all_formats.open_records(path)
            if len(records) != 1 or "absorbance" not in records[0]["signals"]:
                raise ValueError(f"Unsupported binary spectrum in {path.name}") from None
            signal = records[0]["signals"]["absorbance"]
            axis, values = signal["axis"]["values"], signal["values"]
        if axes is None:
            axes = axis
        elif len(axis) != len(axes) or any(abs(a-b) > 1e-5 for a, b in zip(axis, axes, strict=True)):
            raise ValueError(f"Sea cucumber axis differs in {path.name}")
        rows.append(values)
    assert axes is not None
    ids = [f"sea_cucumber_{p.parent.name}_{p.stem}" for p in files]
    x = pd.DataFrame(rows, columns=[format(v, ".12g") for v in axes])
    x.insert(0, "observation_id", ids)
    targets = pd.DataFrame({"observation_id": ids, "class": [p.parent.name for p in files]})
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": [p.stem for p in files]})
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)


def _build_rice(context: PullContext) -> Path:
    archive = context.download("https://datadryad.org/api/v2/versions/48743/download", "dryad_rice.zip")
    root = context.extract(archive)
    files = sorted(_extract_rar(context, root / "data for publish.rar", "_reflectance_flag leaf.xlsx").rglob("*.xlsx"))
    if not files:
        raise ValueError("No rice leaf spectral workbooks")
    axes = None
    rows = []
    identities = []
    varieties = []
    for path in files:
        variety = path.name.split("_Reflectance_flag leaf.xlsx")[0]
        table = pd.read_excel(path)
        raw_axis = table.iloc[:, 0]
        axis = pd.to_numeric(raw_axis, errors="coerce").tolist()
        if axes is None:
            if any(pd.isna(v) for v in axis):
                raise ValueError(f"Missing numeric rice axis in {path.name}")
            axes = axis
        else:
            if len(axis) != len(axes):
                raise ValueError(f"Rice spectral axis length differs in {path.name}")
            for index, value in enumerate(axis):
                if pd.isna(value) and raw_axis.iloc[index] == "475.99S24942364":
                    axis[index] = axes[index]  # Source typo, verified against the other five workbooks.
            if axis != axes:
                raise ValueError(f"Rice spectral axis differs in {path.name}")
        for column in table.columns[1:]:
            identities.append(f"rice_leaf_{variety}_{column}")
            varieties.append(variety)
            rows.append(table[column].tolist())
    if len(identities) != len(set(identities)):
        raise ValueError("Rice source observation identifiers are not unique")
    assert axes is not None
    x = pd.DataFrame(rows, columns=[format(v, ".12g") for v in axes])
    x.insert(0, "observation_id", identities)
    metadata = pd.DataFrame({"observation_id": identities, "variety": varieties})
    return context.write_tables({"X": x}, metadata=metadata)
