import argparse, json
from pathlib import Path
import pandas as pd

from vep import annotate_variants
from clinvar import clinvar_query

def load_variants(path):
    df = pd.read_csv(path, sep="\t", dtype={"chrom": str})
    required = {"chrom", "pos", "ref", "alt"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if "id" not in df.columns:
        df["id"] = [f"variant_{i+1}" for i in range(len(df))]
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results/report.json")
    args = parser.parse_args()

    df = load_variants(args.input)
    variants = df.to_dict(orient="records")
    vep_results = annotate_variants(variants)
    clinvar_results = {
        v["id"]: clinvar_query(v["chrom"], v["pos"], v["ref"], v["alt"])
        for v in variants
    }

    report = {
        "input_variants": variants,
        "vep": vep_results,
        "clinvar": clinvar_results,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
