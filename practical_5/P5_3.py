# A) Load and report (use SeqIO)

# - Read all records from `dna.fasta`.
# - For each record, print the record ID and the sequence length.
# - Also print the first 10 bases of the sequence.
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

records = list(SeqIO.parse('dna.fasta','fasta'))

for record in records:
    print(record.id, record.seq[:10])
    
# B) Reverse complements to a new FASTA (use Seq, SeqRecord, SeqIO)

# - For each original record, create the reverse complement of its sequence.
# - Make a new SeqRecord for the reverse complement.
# - Set the new ID to "<oldid>_rc" and the description to "reverse complement of <oldid>".
# - Write all reverse-complement records to a file named `dna_rc.fasta`.
unique = set()
revcomp_records = []

for record in records:
    seq_str = str(record.seq)
    # Only process unique sequences
    if seq_str not in unique:
        unique.add(seq_str)

        # Create reverse complement record immediately
        revcomp = record.seq.reverse_complement()
        new_id = f"{record.id}_rc"

        revcomp_record = SeqRecord(
            seq=revcomp,id=new_id,description=f'Reverse complement of {record.id}'
        )

        revcomp_records.append(revcomp_record)

# Save all reverse complements to a new FASTA
SeqIO.write(revcomp_records, "dna_rc.fasta", "fasta")

# C) GC% annotation to a new FASTA (use SeqRecord, SeqIO)

# - For each original record, calculate GC% = 100 * (count of 'G' + count of 'C') / length.
# - Round to 1 decimal place.
# - Create a copy of the record where the description includes "GC=<value>%".
# - Write these annotated records to `dna_with_gc.fasta`.
gc_records =[]

for record in records:
    g_count = record.seq.count("G")
    c_count = record.seq.count("C")

    seq_len = len(record.seq)
    GC_cont = round(100*(g_count + c_count)/seq_len, 1)

    gc_record = record

    gc_record.description = record.description + f" GC={GC_cont}%"
    gc_records.append(gc_record)

SeqIO.write(gc_records, "dna_with_gc.fasta", "fasta")


# D) Translation (Optional, do if you have extra time)

# - Translate each DNA sequence and print the first 10 amino acids.
# - Read `dna_rc.fasta` back in and confirm IDs/descriptions look correct.

for record in records:
    print(record.seq.translate()[:10])
