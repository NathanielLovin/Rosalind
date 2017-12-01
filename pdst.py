import rna

d = rna.FASTAreader("rosalind_pdst.txt")
a = [[0 for y in range(len(d))] for x in range(len(d))]

for i in range(len(d)):
	for j in range(i+1,len(d)):
		x = rna.hamming(d[i], d[j])/len(d[i])
		a[i][j] = x
		a[j][i] = x

for x in a:
	p = ""
	for y in x:
		p += str(y) + " "
	print(p)