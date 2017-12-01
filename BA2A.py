def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def immediateNeighbors(pattern):
	neighborhood = [pattern]
	for i in range(len(pattern)):
		symbol = pattern[i]
		if symbol != 'A':
			neighborhood.append(pattern[0:i] + 'A' + pattern[i+1:])
		if symbol != 'C':
			neighborhood.append(pattern[0:i] + 'C' + pattern[i+1:])
		if symbol != 'G':
			neighborhood.append(pattern[0:i] + 'G' + pattern[i+1:])
		if symbol != 'T':
			neighborhood.append(pattern[0:i] + 'T' + pattern[i+1:])
	return neighborhood

def neighbors(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	neighborhood = []
	sufneigh = neighbors(pattern[1:],d)
	for x in sufneigh:
		if hammingDistance(pattern[1:],x) < d:
			for y in ['A', 'C', 'G', 'T']:
				 neighborhood.append(y + x)
		else:
			neighborhood.append(pattern[0] + x)
	return neighborhood

def patternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])

def symbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def motifEnumeration(dna, k, d):
	patterns = [0] * 4**k
	for x in  dna:
		for i in range(len(x)-k+1):
			neighborhood = neighbors(x[i:i+k], d)
			for n in neighborhood:
				inAll = True
				for y in dna:
					inY = False
					for j in range(len(y)-k+1):
						if hammingDistance(n, y[j:j+k]) <= d:
							inY = True
					if not inY:
						inAll = False
				if inAll:
					patterns[patternToNumber(n)] = 1
	finalPatterns = []
	for i in range(4**k):
		if patterns[i] == 1:	
			finalPatterns.append(numberToPattern(i, k))
	return finalPatterns

dna = ["CGTGCATCATCTTATGCCCTGAACT",
"CTTTGCTATTATCAGGAACTATCAT",
"CTTAGGCCTCTAATTAAGCAATCAT",
"ACAGATCACGATCGTTAAAAAACAA",
"CCGGTGCGCGCCGTAATCTTTCGGT",
"CGCAGATCCTATGCTTCAATTCCCA",
"GTCGTCAAGTCGCCCCATTGATCGT",
"ACTAAGGGGATACGCATCCTTGGAG",
"AAGCACCAACACGCTGATCGATCCT",
"TTAATATCTTAGCCCGTAACGGTCG"]
k = 5
d = 1
patterns = motifEnumeration(dna, k, d)
p = ""
for x in patterns:
	p += x + " "
print(p)