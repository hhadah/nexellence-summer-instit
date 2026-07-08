"""Download the Human vs LLM text corpus from Kaggle and save a 10% sample to ~/Downloads."""

from pathlib import Path

import kagglehub
import pandas as pd

SAMPLE_FRAC = 0.10
SEED = 42

# Download latest version
path = Path(kagglehub.dataset_download("starblasters8/human-vs-llm-text-corpus"))
print("Path to dataset files:", path)

downloads = Path.home() / "Downloads"

# Sample every data file in the dataset (this one ships as parquet, but handle csv too)
data_files = sorted(list(path.rglob("*.parquet")) + list(path.rglob("*.csv")))
if not data_files:
    raise FileNotFoundError(f"No parquet or csv files found in {path}")

for file in data_files:
    print(f"\nReading {file.name} ...")
    if file.suffix == ".parquet":
        df = pd.read_parquet(file)
    else:
        df = pd.read_csv(file)

    sample = df.sample(frac=SAMPLE_FRAC, random_state=SEED)

    out_path = downloads / f"{file.stem}_10pct_sample{file.suffix}"
    if file.suffix == ".parquet":
        sample.to_parquet(out_path, index=False)
    else:
        sample.to_csv(out_path, index=False)

    print(f"  Full data: {len(df):,} rows -> Sample: {len(sample):,} rows")
    print(f"  Saved to {out_path}")
