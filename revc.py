f = open('/Users/Nat/Downloads/rosalind_revc.txt', 'r')
dna = f.readline().strip()
comp = ''
for x in dna:
	if x == 'A':
		comp = 'T' + comp
	if x == 'G':
		comp = 'C' + comp
	if x == 'C':
		comp = 'G' + comp
	if x == 'T':
		comp = 'A' + comp
print comp