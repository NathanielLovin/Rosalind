f = open('/Users/Nat/Downloads/rosalind_dna (1).txt', 'r')
dna = f.readline().strip()
a = 0
c = 0
g = 0
t = 0
print dna
for x in range(0, len(dna)):
	if dna[x:x+1] == 'A':
		a += 1
	if dna[x:x+1] == 'C':
		c += 1
	if dna[x:x+1] == 'G':
		g += 1
	if dna[x:x+1] == 'T':
		t += 1
output = str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)
print output