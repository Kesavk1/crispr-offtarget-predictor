import argparse
import pandas as pd
from crispr_offtarget.aligner import find_offtargets

def main():
    parser = argparse.ArgumentParser(description="CRISPR sgRNA off-target predictor")
    parser.add_argument("-s", "--sgRNA", required=True, help="sgRNA sequence")
    parser.add_argument("-g", "--genome", required=True, help="FASTA genome file")
    parser.add_argument("-o", "--output", default="results/offtargets.csv", help="Output CSV path")
    args = parser.parse_args()

    results = find_offtargets(args.sgRNA, args.genome)
    df = pd.DataFrame(results)
    df.to_csv(args.output, index=False)
    print(f"Saved {len(df)} off-target hits to {args.output}")

if __name__ == "__main__":
    main()
