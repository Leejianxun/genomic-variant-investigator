def build_summary(variants, vep_results, clinvar_results):
    rows = []

    for variant, vep in zip(variants, vep_results):
        row = {
            "variant_id": variant["id"],
            "chrom": variant["chrom"],
            "pos": variant["pos"],
            "ref": variant["ref"],
            "alt": variant["alt"],
            "gene": None,
            "consequence": vep.get("most_severe_consequence"),
            "impact": None,
            "amino_acids": None,
            "sift": None,
            "polyphen": None,
            "clinvar_matches": len(
                clinvar_results[variant["id"]]["matches"]
            ),
        }

        for tc in vep.get("transcript_consequences", []):
            if tc.get("biotype") == "protein_coding":
                row["gene"] = tc.get("gene_symbol")
                row["impact"] = tc.get("impact")
                row["amino_acids"] = tc.get("amino_acids")
                row["sift"] = tc.get("sift_prediction")
                row["polyphen"] = tc.get("polyphen_prediction")
                break

        rows.append(row)

    return rows
