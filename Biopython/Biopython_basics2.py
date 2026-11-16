from Bio.Seq import Seq
dna = Seq("ATGAAACCCGGGTTT")
print(dna)
gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print(gc)
at = (dna.count("A") + dna.count("T")) / len(dna) * 100
print(at)
from Bio.SeqUtils import gc_fraction
gc = gc_fraction(dna) * 100
print(gc)

from Bio.Seq import Seq
dna = Seq("ATGAAACCCGGGTTT")
print(len(dna))
print(dna.count("A"))
print(dna.count("T"))
print(dna.count("G"))
print(dna.count("C"))


