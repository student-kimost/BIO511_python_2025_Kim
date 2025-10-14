# A) Load and report (use SeqIO)

# - Read all records from `dna.fasta`.
# - For each record, print the record ID and the sequence length.
# - Also print the first 10 bases of the sequence.
from Bio import SeqIO

records = list(SeqIO.parse('dna.fasta','fasta'))

for record in records:
    print(record.id, record.seq[:10])
    
# B) Reverse complements to a new FASTA (use Seq, SeqRecord, SeqIO)

# - For each original record, create the reverse complement of its sequence.
# - Make a new SeqRecord for the reverse complement.
# - Set the new ID to "<oldid>_rc" and the description to "reverse complement of <oldid>".
# - Write all reverse-complement records to a file named `dna_rc.fasta`.



# C) GC% annotation to a new FASTA (use SeqRecord, SeqIO)

# - For each original record, calculate GC% = 100 * (count of 'G' + count of 'C') / length.
# - Round to 1 decimal place.
# - Create a copy of the record where the description includes "GC=<value>%".
# - Write these annotated records to `dna_with_gc.fasta`.



# D) Translation (Optional, do if you have extra time)

# - Translate each DNA sequence and print the first 10 amino acids.
# - Read `dna_rc.fasta` back in and confirm IDs/descriptions look correct.