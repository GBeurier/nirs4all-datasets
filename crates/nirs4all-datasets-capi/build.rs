// SPDX-License-Identifier: MIT
//! Build script: regenerate the C ABI header into `include/nirs4all_datasets.h`.
//!
//! Re-runs whenever the crate source or the workspace-level `cbindgen.toml` changes.
//! The generated header is committed alongside the crate so downstream packagers
//! (R / MATLAB / C consumers) can pin a stable copy without invoking cargo.
//! Platform linker export controls restrict the cdylib to the `n4ds_*` ABI.

use std::path::PathBuf;

fn main() {
    let crate_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let workspace_dir = crate_dir
        .parent()
        .and_then(|p| p.parent())
        .expect("workspace root is two levels above the crate manifest");
    let config_path = workspace_dir.join("cbindgen.toml");
    let output_path = crate_dir.join("include").join("nirs4all_datasets.h");

    println!("cargo:rerun-if-changed=src/lib.rs");
    println!("cargo:rerun-if-changed={}", config_path.display());

    let target_os = std::env::var("CARGO_CFG_TARGET_OS").unwrap_or_default();
    if target_os == "linux" {
        let version_script = crate_dir.join("abi").join("version_script.map");
        println!("cargo:rerun-if-changed={}", version_script.display());
        println!(
            "cargo:rustc-cdylib-link-arg=-Wl,--version-script={}",
            version_script.display()
        );
        println!("cargo:rustc-cdylib-link-arg=-Wl,--exclude-libs,ALL");
    } else if target_os == "macos" {
        let exports = crate_dir.join("abi").join("exported_symbols_macos.txt");
        println!("cargo:rerun-if-changed={}", exports.display());
        println!(
            "cargo:rustc-cdylib-link-arg=-Wl,-exported_symbols_list,{}",
            exports.display()
        );
    }

    if !config_path.exists() {
        eprintln!(
            "warning: cbindgen.toml not found at {}; skipping header regeneration",
            config_path.display()
        );
        return;
    }
    let config = match cbindgen::Config::from_file(&config_path) {
        Ok(config) => config,
        Err(err) => {
            eprintln!("warning: failed to load cbindgen.toml: {err}; skipping header regeneration");
            return;
        }
    };
    match cbindgen::Builder::new()
        .with_crate(&crate_dir)
        .with_config(config)
        .generate()
    {
        Ok(bindings) => {
            std::fs::create_dir_all(output_path.parent().expect("include dir parent"))
                .expect("create include directory");
            // Normalize to exactly one trailing newline (cbindgen emits a blank line
            // before EOF, which trips `git diff --check` whitespace lint).
            let mut buf: Vec<u8> = Vec::new();
            bindings.write(&mut buf);
            let text = format!("{}\n", String::from_utf8_lossy(&buf).trim_end());
            std::fs::write(&output_path, text).expect("write header");
        }
        Err(err) => eprintln!("warning: cbindgen failed to generate header: {err}"),
    }
}
