import requests

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def clinvar_query(chrom, pos, ref, alt, assembly="GRCh38"):
    term = f"{chrom}:{pos}:{ref}:{alt}({assembly})"
    r = requests.get(ESEARCH, params={
        "db": "clinvar", "term": term, "retmode": "json"
    }, timeout=30)
    r.raise_for_status()
    ids = r.json()["esearchresult"].get("idlist", [])
    if not ids:
        return {"query": term, "matches": []}

    s = requests.get(ESUMMARY, params={
        "db": "clinvar", "id": ",".join(ids[:10]), "retmode": "json"
    }, timeout=30)
    s.raise_for_status()
    data = s.json()["result"]
    return {
        "query": term,
        "matches": [data[i] for i in ids[:10] if i in data]
    }
