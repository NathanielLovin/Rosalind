permutations = [[1]]

for x in range(2,8):
	newpermutations = []
	for y in permutations:
		for z in range(0, len(y)+1):
			newpermutations.append(y[0:z] + [x] + y[z:])
	permutations = newpermutations

print len(permutations)
for a in permutations:
	s = ''
	for b in a:
		s += str(b) + ' '
	print s