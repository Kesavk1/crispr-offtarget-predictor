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

## 🪴 Git Branching Strategy

To organize development and keep the project clean, we follow these branch guidelines:

- **`main`**: This is the **stable, production-ready branch**. Only tested and working code should go here.
  
- **`dev`**: This is where **new features** are developed and tested before being merged into `main`. For example:
    - PAM recognition
    - Score weighting for CRISPR predictions
  
- **`docs`**: If you want to add or update **documentation**, create this branch to keep it separate from the code development.
  
- **`gui`**: If you're adding a **web/Streamlit interface**, create this branch to keep the GUI-related changes isolated.
  
---

### Example of a typical workflow:
1. Start a new feature by creating a `dev` branch.
2. Once it’s ready and tested, merge it back into `dev` and finally into `main`.
3. For docs, work in a `docs` branch and merge it to `main` when updates are ready.

