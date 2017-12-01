import rna

d = rna.FASTAreader("rosalind_tran.txt")
transition = 0
transversions = 0
for x,y in zip(d[0],d[1]):
	if (x == y):
		z =0
	else:
		if (x == 'A' and y == 'G') or (x == 'G' and y == 'A') or (x == 'C' and y == 'T') or (x == 'T' and y == 'C'):
			transition +=1
		else:
			transversions+= 1

print(transition/transversions)