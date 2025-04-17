# CRISPR Off-Target Predictor 🔬

This is a simple bioinformatics pipeline that predicts potential off-target binding sites of CRISPR sgRNAs in a DNA sequence (e.g., human genome), allowing for mismatch tolerance.

## Features
- Customizable mismatch threshold
- FASTA genome input
- CSV output of off-target sites
- Easy to extend or integrate into larger pipelines

## Usage

```bash
python crispr_offtarget/main.py \
  --sgRNA GACGTACGTAGCTAGCTAGC \
  --genome data/example_genome.fa \
  --output results/output.csv
