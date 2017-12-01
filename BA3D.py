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

def deBruijn(text, k):
	graph = [[] for x in range(4**(k-1))]
	for i in range(len(text)-(k-1)):
		print(i)
		start = patternToNumber(text[i:i+k-1])
		end = text[i+1:i+k]
		graph[start].append(end)
	return graph

text = "TCGAGATCACGAGTATTGCGTTTACCTGTGACGCCATATAGTCTGGTTCTCATGAGGGACTTATCCTGGGTCAGCGCTTAGCTGGTAATATTCATGTCAGAGAGCCTATGTACCGCGCGGACGTAGCCGACAAAATCAACGGGAAAACGGGTGGAACTGCCGCATATCACGTGCATCTTGAGTAAGGTACTTCCGTCCTAAGCGTCCGTGCGCTTAATGTACCGCGCACCGAGACACCTCTTAGAATAGCAACCTGCTGAACGCTTAGCTCGACGATCCTAGATCCAGAGTAATAGTGGTGGCATACGCTCTTAGATGCCGTGACTGTAAGCAGGCAGCCCGGACGATTAGAATGGAGTGGGTTGAATTTCTATAAACGTCTACAAGCGGTCCCAATATTATTAGCATGCAGGGTTAATGTACCAGGCCCGTATTACGGGTGCCGTCCGCACAAGGCGTAACCATAAAATGACCCACGTTCATGAGAAGCTATGGCGCGCACTTTGCTTATACAAGTTCCCTTACGGAAATTAGAGTATTCTCTAGTGAGCACGTGATGCCTTGAATAGAGTAATGTCGCCCGTACGGGGCACATCGAGACTCAACTTGTATAATAATGCACGCAGGCGGATTGCCGCCGGCATTGCGGGCACTGCGAACCACCAACGCGCTATTAGCGGGTCCACAAGGTTCTATCCCCGTCACCGCAAGGCCATAGCTCATTGACACAGGCCCTGCCAATCAGGCCTAAGATTGCATGACTCCTACATTAGGCCGTGTGATGAGAAGCTGAGAATCAGAGCGTCAGCTGGTCACATATTTTAACCGAACGACCAGTAGATTACTTCTAGAAACATACAGTGCATACGCGAACACGTCATCCAGGGCCCGATGCGCCCTCCTCCCAACAAACAGCTCCGCCGATGCAGACCGCACTTAAGTTGGCTTCGCCCAGACAACGTTGCGCTGCGCGGTTCCTCATTATTAGTCTAAAAGGGCGACCGCAAGGAAGGGTCTCGTCCAATTAGTATATGCGTGAGCTAAGGGTTGCGACTCGCTGTGGAACTTGGGTCGAAGTGAAGAACTAATTAGAGGGGACGGTGACGCCTCCGTCGCATGCCCCGTATACAGCTTATACGAGGGACGTCGGTCTACTATCGGCAAGAAGACATAGATGATCGTTCTACGAAACTCTAGTACATTCGATATTACGTTGAGAGTTATCTGACCGAACGAGCCGTTGTTAACGTGTGAGACGCGGGGATATTCGAGCGTGCTATTCCCCCTAAAATGACGTTTCAAGCAGAGTTCACGTAGGTATCCTTTAAGTTCGCTCAATTAACCAAATCCAGAAAAACGATGTCGCTACACCCGATGTATAGTAGGTTTTGTGTGACAAAGGCACGACAGGTCGCCTGGTGAAGGCGATAAAGTCAAAGCCGGAGGCTGATGAGGATAGCGGGAACGATGTATGTTGACTCCAGATAGAGAATCGCACCGATAGGGCCGACAAACCGTCATACCAATATTTAGGGAATTGGATCTCGATGTCTAAGGTTGAGTATATCTTTCAAAGCCCAGATTGCGAGTACAGTGATAAATGGCGTACGCTCAGCGGGAAGCATGGGTGGCTTTGTCCATCACTTCCTGCACTCGCTTTAGATCCACTAGCTTCCCGCGTTCCTCAAGGTATCGCAGCAATAGCCTAGCTTGCATGCCCCCACTTCCCTAAGGGCATGAGTAGAGGGCGGATGTAGTATATTGAGTAACTGCTCACTTTCCACCATCCAGGCCTGAACCCGCTATGTCATCAATCAGAGGGGCCCATCCTACGCCTTGGCCCCTGGACATAATTCGATATTTCTTACAGTAAATGTCGGACCATGGACCGAAGGGAACCTGATGATGGAAAGGCAAAGGTCAAGACTGGGAAACGGCTGCTATATAGTCAACGTGGATTCACTTTCACAGGGCCTGACAAGACTTATAAAAATAGTCAC"
print(len(text))
k = 12
graph = deBruijn(text, k)
for i in range(len(graph)):
	out = numberToPattern(i,k-1) + " -> "
	outnodes = 0
	for j in graph[i]:
		if outnodes > 0:
			out += ","
		out += j
		outnodes += 1
	if outnodes > 0:
		print(out)