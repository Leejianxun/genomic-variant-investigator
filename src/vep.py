import requests

ENSEMBL_VEP_URL = "https://rest.ensembl.org/vep/homo_sapiens/region"

def annotate_variants(variants):
    payload = {
        "variants": [
            f"{v['chrom']} {v['pos']} {v.get('id', '.')} {v['ref']} {v['alt']} . . ."
            for v in variants
        ]
    }
    r = requests.post(
        ENSEMBL_VEP_URL,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        json=payload,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()
