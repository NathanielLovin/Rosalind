import math

rna = "AUGUUAUGACGAAGGUUUUAGUCUCCACAUCGCACGCAGGUGUGCAUGCGAAGCACUCAAUCUAGCGAUGAAGAGGGCCCUGACCAAUUCGGGUA"
a = 0
g = 0
c = 0
u = 0
for x in rna:
	if x == 'A':
		a += 1
	if x == 'G':
		g += 1
	if x == 'U':
		u += 1
	if x == 'C':
		c += 1
au = math.factorial(max(a, u))//math.factorial(max(a, u) - min(a,u))
gc = math.factorial(max(g, c))//math.factorial(max(g, c) - min(g,c))
print(au * gc)