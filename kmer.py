import rna

def enum(alpha, n):
	if n == 0:
		return [""]
	current = []
	next = enum(alpha, n-1)
	for i in alpha:
		for j in next:
			current.append(i + j)
	return current

def patternCount(text, pattern):
	count = 0
	for i in range(len(text) - len(pattern)+1):
		if (text[i:i+len(pattern)] == pattern):
			count += 1
	return count

k = 4
kmers = enum(['A', 'C', 'G', 'T'], k)
s = rna.FASTAreader("rosalind_kmer.txt")[0]
d = []
for x in kmers:
	d.append(patternCount(s, x))
p = ""
for x in d:
	p += str(x) + " "
print(p)