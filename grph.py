import rna

dna = rna.FASTAreader("rosalind_grph.txt")
names = []
f = open("rosalind_grph.txt", 'r')
label = ''
for line in f:
	if line[0:1] == '>':
		label = line.strip()[1:]
		names.append(label)
f.close()


for i in range(len(dna)):
	for j in range(len(dna)):
		x = len(dna[i])
		if i != j:
			if dna[i][x-3:] == dna[j][0:3]:
				print(names[i] + " " + names[j])