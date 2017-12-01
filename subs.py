f = open('/Users/Nat/Downloads/rosalind_subs.txt', 'r')
strand = f.readline().strip()
motif = f.readline().strip()
locations = []
motlen = len(motif)
for x in range(0,len(strand)-motlen):
	if strand[x:x+motlen] == motif:
		locations.append(x+1)

s = ''
for x in locations:
	s += str(x) + ' '

print s.strip()