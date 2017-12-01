import rna

d = rna.FASTAreader("rosalind_rvco.txt")
count = 0
for x in d:
	b = rna.reverseComplement(x)
	if b == x:
		count += 1

print(count)