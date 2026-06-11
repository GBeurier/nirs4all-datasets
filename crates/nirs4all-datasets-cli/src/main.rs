// SPDX-License-Identifier: MIT
//! `n4ds` — a thin CLI over the acquisition core. It reads the distributable
//! `catalog/index.json` and resolves / fetches / verifies a dataset, printing JSON.
//! It doubles as the cross-binding parity oracle (every binding must agree with it).

use std::path::PathBuf;
use std::process::ExitCode;

use clap::{Parser, Subcommand};
use nirs4all_datasets_core::fetch::FetchOptions;
use nirs4all_datasets_core::model::{Index, Resolved};
use nirs4all_datasets_core::{fetch, resolve, verify_cached, UreqClient};

#[derive(Parser)]
#[command(
    name = "n4ds",
    version,
    about = "Resolve / fetch / verify nirs4all-datasets from catalog/index.json"
)]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    /// Print a dataset's resolved download contract (JSON).
    Resolve {
        /// Path to catalog/index.json.
        #[arg(long)]
        index: PathBuf,
        /// Dataset id.
        id: String,
    },
    /// Download + verify a dataset into the cache and print the fetch status (JSON).
    Fetch {
        /// Path to catalog/index.json.
        #[arg(long)]
        index: PathBuf,
        /// Dataset id.
        id: String,
        /// Cache root (defaults to the OS cache dir).
        #[arg(long)]
        cache_dir: Option<String>,
        /// Dataverse token for a private/anonymized dataset.
        #[arg(long)]
        token: Option<String>,
        /// Override the Dataverse instance.
        #[arg(long)]
        instance: Option<String>,
    },
    /// Re-verify an already-cached dataset directory offline and print the report (JSON).
    Verify {
        /// Path to catalog/index.json.
        #[arg(long)]
        index: PathBuf,
        /// Dataset id.
        id: String,
        /// The cached dataset directory (`<cache>/<id>`).
        #[arg(long)]
        dir: PathBuf,
    },
}

fn load_index(path: &PathBuf) -> Result<Index, String> {
    let text =
        std::fs::read_to_string(path).map_err(|e| format!("read {}: {e}", path.display()))?;
    serde_json::from_str(&text).map_err(|e| format!("parse index: {e}"))
}

fn run() -> Result<String, String> {
    match Cli::parse().command {
        Command::Resolve { index, id } => {
            let index = load_index(&index)?;
            let resolved = resolve(&index, &id).map_err(|e| e.to_string())?;
            serde_json::to_string_pretty(&resolved).map_err(|e| e.to_string())
        }
        Command::Fetch {
            index,
            id,
            cache_dir,
            token,
            instance,
        } => {
            let index = load_index(&index)?;
            let resolved = resolve(&index, &id).map_err(|e| e.to_string())?;
            let opts = FetchOptions {
                cache_dir,
                token,
                instance,
                timeout_secs: None,
            };
            let client = UreqClient::default();
            let result = fetch(&resolved, &opts, &client).map_err(|e| e.to_string())?;
            serde_json::to_string_pretty(&result).map_err(|e| e.to_string())
        }
        Command::Verify { index, id, dir } => {
            let index = load_index(&index)?;
            let resolved: Resolved = resolve(&index, &id).map_err(|e| e.to_string())?;
            let report = verify_cached(&resolved, &dir).map_err(|e| e.to_string())?;
            serde_json::to_string_pretty(&report).map_err(|e| e.to_string())
        }
    }
}

fn main() -> ExitCode {
    match run() {
        Ok(out) => {
            println!("{out}");
            ExitCode::SUCCESS
        }
        Err(e) => {
            eprintln!("n4ds: {e}");
            ExitCode::FAILURE
        }
    }
}
