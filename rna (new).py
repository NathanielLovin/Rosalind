f = open('/Users/Nat/Downloads/rosalind_rna.txt', 'r')
dna = f.readline().strip()
rna = ''
for x in dna:
	if x == 'T':
		rna = rna + 'U'
	else:
		rna = rna + x
print rna