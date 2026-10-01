#!/bin/bash
PYTHONPATH=src python src/pipeline.py \
  --input data/example_variants.tsv \
  --output results/report.json