from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pipeline import load_variants

def test_load_variants(tmp_path):
    p = tmp_path / "variants.tsv"
    p.write_text("chrom\tpos\tref\talt\n1\t100\tA\tG\n")
    df = load_variants(p)
    assert df.iloc[0]["id"] == "variant_1"
