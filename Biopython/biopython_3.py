from Bio.Seq import Seq
dna = Seq("ATGAAACCCGGGTTT")
print(dna)
print(len(dna))
print(dna.count("T"))
print(dna.count("G"))
print(dna.count("C"))
print(dna.count("A"))
print(dna.complement())
print(dna.reverse_complement())
print(dna.transcribe())
print(dna.translate())
gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print(gc)
print(dna.find("ATG"))
print(dna[4:9])
dna1 = Seq("ATGAAACCCGGGTTT")
dna2 = Seq("ATGAAATTTGGGTTT")
print(dna1 == dna2)
from Bio.SeqUtils import gc_fraction
gc = gc_fraction(dna1) * 100
print(gc)
from Bio.Seq import Seq
dna1 = Seq("ATGAAACCCGGGTTT")
dna2 = Seq("ATGCGCGCGGATTT")
dna3 = Seq("ATATATATATATAT")
sequences=[dna1,dna2,dna3]
print(sequences)
highest_gc = 0
highest_sequence = None
for dna in sequences:
    print("Sequence:", dna)
    print("length:", len(dna))
    gc = gc_fraction(dna) * 100
    print("GC Percentage:", gc)
    if gc > highest_gc:
        highest_gc = gc
        highest_sequence = dna
print("Highest GC Percentage:", highest_gc)
print("Highest Sequence:", highest_sequence)
