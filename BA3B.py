f = open("rosalind_ba3b.txt", 'r')
dna = []
for line in f:
	dna.append(line.strip())
str = dna[0][0:-1]
for x in dna:
	str += x[-1]

print(str)