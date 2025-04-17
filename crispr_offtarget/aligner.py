from Bio import SeqIO
from Bio.Seq import Seq

def find_offtargets(sgRNA, genome_fasta, max_mismatches=2):
    sgRNA = sgRNA.upper().replace("U", "T")
    results = []

    for record in SeqIO.parse(genome_fasta, "fasta"):
        seq = str(record.seq).upper()
        for i in range(len(seq) - len(sgRNA)):
            window = seq[i:i+len(sgRNA)]
            mismatches = sum(1 for a, b in zip(sgRNA, window) if a != b)

            if mismatches <= max_mismatches:
                results.append({
                    "chr": record.id,
                    "start": i,
                    "sequence": window,
                    "mismatches": mismatches
                })
    return results
