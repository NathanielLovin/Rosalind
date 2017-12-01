def transcribe(DNA):
	RNA = ''
	for x in DNA:
		if x == 'T':
			RNA += 'U'
		else:
			RNA += x
	return RNA

def reverseTranscribe(DNA):
	RNA = ''
	for x in DNA:
		if x == 'T':
			RNA = 'A' + RNA
		if x == 'A':
			RNA = 'U' + RNA
		if x == 'G':
			RNA = 'C' + RNA
		if x == 'C':
			RNA = 'G' + RNA
	return RNA

def Complement(DNA):
	RNA = ''
	for x in DNA:
		if x == 'T':
			RNA += 'A'
		if x == 'A':
			RNA += 'T'
		if x == 'G':
			RNA += 'C'
		if x == 'C':
			RNA += 'G'
	return RNA

def reverseComplement(DNA):
	RNA = ''
	for x in DNA:
		if x == 'T':
			RNA = 'A' + RNA
		if x == 'A':
			RNA = 'T' + RNA
		if x == 'G':
			RNA = 'C' + RNA
		if x == 'C':
			RNA = 'G' + RNA
	return RNA

def hamming(s1,s2):
	hamming = 0
	for x, y in zip(s1, s2):
		if x != y:
			hamming += 1
	return hamming

def protein(l):
    x = l[0:3]
    min = 0
    max = 3
    while x != 'AUG' and max+3 <= len(l):
        min += 3
        max += 3
        x = l[min:max]
        if codon(x) == 'STOP':
            return ""
    if max+3 > len(l):
        return ""
    y = codon(x)
    min += 3
    max += 3
    while(max <= len(l)):
        x = l[min:max]
        z = codon(x)
        if z == 'Stop':
            return y
        y = y + z
        min = min + 3
        max = max + 3
    return ""

def FASTAreader(file):
    f = open(file, 'r')
    label = ''
    d = []
    i = -1;
    for line in f:
        if line[0:1] == '>':
            label = line.strip()[1:]
            i+=1
            d.insert(i,'')
        else:
            x = d[i]
            x += line.strip()
            d[i] = x
    f.close()
    return d

def codon(z):
	d = {}
	d['UUU']='F'
	d['CUU']='L'
	d['AUU']='I'
	d['GUU']='V'
	d['UUC']='F'
	d['CUC']='L'
	d['AUC']='I'
	d['GUC']='V'
	d['UUA']='L'
	d['CUA']='L'
	d['AUA']='I'
	d['GUA']='V'
	d['UUG']='L'
	d['CUG']='L'
	d['AUG']='M'
	d['GUG']='V'
	d['UCU']='S'
	d['CCU']='P'
	d['ACU']='T'
	d['GCU']='A'
	d['UCC']='S'
	d['CCC']='P'
	d['ACC']='T'
	d['GCC']='A'
	d['UCA']='S'
	d['CCA']='P'
	d['ACA']='T'
	d['GCA']='A'
	d['UCG']='S'
	d['CCG']='P'
	d['ACG']='T'
	d['GCG']='A'
	d['UAU']='Y'
	d['CAU']='H'
	d['AAU']='N'
	d['GAU']='D'
	d['UAC']='Y'
	d['CAC']='H'
	d['AAC']='N'
	d['GAC']='D'
	d['UAA']='Stop'
	d['CAA']='Q'
	d['AAA']='K'
	d['GAA']='E'
	d['UAG']='Stop'
	d['CAG']='Q'
	d['AAG']='K'
	d['GAG']='E'
	d['UGU']='C'
	d['CGU']='R'
	d['AGU']='S'
	d['GGU']='G'
	d['UGC']='C'
	d['CGC']='R'
	d['AGC']='S'
	d['GGC']='G'
	d['UGA']='Stop'
	d['CGA']='R'
	d['AGA']='R'
	d['GGA']='G'
	d['UGG']='W'
	d['CGG']='R'
	d['AGG']='R'
	d['GGG']='G'
	return d[z]

def massOfProtein(z):
    d = {}
    d['A'] = 71.03711
    d['C'] = 103.00919
    d['D'] = 115.02694
    d['E'] = 129.04259
    d['F'] = 147.06841
    d['G'] = 57.02146
    d['H'] = 137.05891
    d['I'] = 113.08406
    d['K'] = 128.09496
    d['L'] = 113.08406
    d['M'] = 131.04049
    d['N'] = 114.04293
    d['P'] = 97.05276
    d['Q'] = 128.05858
    d['R'] = 156.10111
    d['S'] = 87.03203
    d['T'] = 101.04768
    d['V'] = 99.06841
    d['W'] = 186.07931
    d['Y'] = 163.06333
    return d[z]

def proteinOfMass(z):
    d = {}
    d['A'] = 71.03711
    d['C'] = 103.00919
    d['D'] = 115.02694
    d['E'] = 129.04259
    d['F'] = 147.06841
    d['G'] = 57.02146
    d['H'] = 137.05891
    d['I'] = 113.08406
    d['K'] = 128.09496
    d['L'] = 113.08406
    d['M'] = 131.04049
    d['N'] = 114.04293
    d['P'] = 97.05276
    d['Q'] = 128.05858
    d['R'] = 156.10111
    d['S'] = 87.03203
    d['T'] = 101.04768
    d['V'] = 99.06841
    d['W'] = 186.07931
    d['Y'] = 163.06333
    return d.keys()[d.values().index(z)]
