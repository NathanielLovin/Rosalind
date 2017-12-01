f = open("rosalind_ba3c.txt", 'r')
dna = []
for line in f:
	dna.append(line.strip())
adj = [[0 for x in range(len(dna))] for y in range(len(dna))]
for i in range(len(dna)):
	for j in range(len(dna)):
		if i!=j:
			if dna[i][1:] == dna[j][:-1]:
				adj[i][j] = 1
for i in range(len(adj)):
	for j in range(len(adj[i])):
		if adj[i][j] == 1:
			print(dna[i] + " -> " + dna[j])