import rna

f = open('/Users/Nat/Downloads/rosalind_prot (1).txt', 'r')
strand = f.readline().strip()
print rna.protein(strand)