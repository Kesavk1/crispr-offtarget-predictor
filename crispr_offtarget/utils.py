from Bio import SeqIO

def count_fasta_sequences(file_path):
    return sum(1 for _ in SeqIO.parse(file_path, "fasta"))
