mass = {}
mass['G'] = 57
mass['A'] = 71
mass['S'] = 87
mass['P'] = 97
mass['V'] = 99
mass['T'] = 101
mass['C'] = 103
mass['I'] = 113
mass['L'] = 113
mass['N'] = 114
mass['D'] = 115
mass['K'] = 128
mass['Q'] = 128
mass['E'] = 129
mass['M'] = 131
mass['H'] = 137
mass['F'] = 147
mass['R'] = 156
mass['Y'] = 163
mass['W'] = 186

def proteinMass(pep):
	weight = 0
	for x in pep:
		weight += mass[x]
	return weight

peptide = "SVYQERFHWNIHSH"
spec = [0]
for x in range(1,len(peptide)):
	for i in range(len(peptide)):
		if i+x > len(peptide):
			y = i+x-len(peptide)
			spec.append(proteinMass(peptide[i:]+peptide[:y]))
		else:
			spec.append(proteinMass(peptide[i:i+x]))
spec.append(proteinMass(peptide))
spec.sort()
p = ""
for x in spec:
	p +=  str(x) + " "
print(p)
