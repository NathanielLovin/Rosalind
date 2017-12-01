import rna

dna = rna.FASTAreader("rosalind_revp.txt")[0]
dnac = rna.Complement(dna)

for x in range(len(dna)):
	for y in range(4,13):
		if x+y > len(dna):
			break;
		if dna[x:x+y] == dnac[x:x+y][::-1]:
			print(str(x+1) + " " + str(y))