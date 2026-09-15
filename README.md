# Genomic Variant Investigation and Prioritisation Pipeline

A small, reproducible computational genomics project for investigating candidate human genetic variants.

## Current MVP
1. Parse a small variant list
2. Query Ensembl VEP for functional consequences
3. Query ClinVar through NCBI E-utilities
4. Save a structured JSON evidence report

## Research question
Can public genomic annotation resources be integrated into a reproducible workflow that organises evidence for candidate variants and helps prioritise variants for further investigation?

## Planned extensions
- clean evidence table
- population-frequency evidence
- rule-based prioritisation
- pathogenic-vs-benign sanity check
- regulatory-variant analysis for enhancer-focused work
- long-read vs short-read comparison

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python src/pipeline.py --input data/example_variants.tsv
```

## Important limitation
This project organises computational evidence. It does not provide clinical diagnoses.
