f = open('/Users/Nat/Downloads/rosalind_ini5.txt', 'r')
odd = True
for line in f:
	if odd:
		odd = False
	else:
		print line.strip()
		odd = True