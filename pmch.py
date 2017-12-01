import math

rna = "GCUCGCAUGGAUACGUUACCUAGUAUCAAACGGCCGCUCAGAGUUAGGUCGCAUACAUAUGGUCGCGAUGGCCGCC"
a = 0
g = 0
for x in rna:
	if x == 'A':
		a += 1
	if x == 'G':
		g += 1
matches = math.factorial(a) * math.factorial(g)
print(matches)