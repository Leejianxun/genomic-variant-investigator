# Genomic Variant Investigator

A small reproducible Python pipeline for annotating human genomic variants using public biological databases.

The project takes a simple tab-separated list of genomic variants, queries external annotation resources, and produces both a detailed JSON report and a concise summary table.

## Motivation

Interpreting genomic variants often requires combining information from multiple biological resources. This project is a learning-focused pipeline designed to explore how variant annotation can be automated in a reproducible way.

The current implementation focuses on GRCh38 variants and integrates:

- Ensembl Variant Effect Predictor (VEP) for functional consequences
- ClinVar for clinically reported variant evidence
- Python and pandas for data handling and reporting

## Pipeline

    Input variants
          |
          v
    Input validation
          |
          v
    Ensembl VEP annotation
          |
          v
    ClinVar query
          |
          v
    Structured JSON report
          +
    Human-readable TSV summary

## Input

Example input:

    chrom   pos       ref   alt   id
    17      43071077  G     A     variant_1
    13      32932018  G     A     variant_2

Genome assembly: **GRCh38**

## Example Output

The pipeline produces `results/summary.tsv`.

Example:

    variant_id   gene    consequence         impact    amino_acids   sift          polyphen             clinvar_matches
    variant_1    BRCA1   missense_variant    MODERATE  S/C           deleterious   possibly_damaging    0
    variant_2    NA      intergenic_variant  NA        NA            NA            NA                   0

For the BRCA1 example variant, Ensembl VEP identifies a missense consequence with an amino-acid change from serine to cysteine (`S/C`). The second example is annotated as an intergenic variant.

ClinVar results are queried using GRCh38-aware genomic coordinates. A value of `0` indicates that no matching ClinVar record was returned for the query.

## Project Structure

    .
    ├── data/
    │   └── example_variants.tsv
    ├── results/
    │   ├── report.json
    │   └── summary.tsv
    ├── src/
    │   ├── clinvar.py
    │   ├── pipeline.py
    │   ├── summary.py
    │   └── vep.py
    ├── tests/
    │   └── test_input.py
    ├── README.md
    └── requirements.txt

## Installation

Create and activate a Python virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Usage

Run the pipeline with:

    PYTHONPATH=src python src/pipeline.py \
      --input data/example_variants.tsv \
      --output results/report.json

Outputs:

    results/report.json
    results/summary.tsv

## Current Limitations

This is a learning-oriented mini-project and is not intended for clinical use.

Current limitations include:

- only simple SNV-style inputs are currently demonstrated
- genome assembly is currently fixed to GRCh38
- ClinVar querying is intentionally conservative
- transcript selection is currently simplified
- no pathogenicity classification is performed

## Next Steps

Planned improvements include:

- stronger ClinVar allele matching and validation
- support for additional variant formats
- clearer transcript-selection logic
- automated tests for annotation and reporting
- improved command-line configuration

## Purpose

I am developing this project as part of my transition from computer science into bioinformatics and computational genomics.

The goal is to build practical experience with genomic data, biological APIs, reproducible pipelines, and variant annotation while understanding the biological meaning behind each computational step.