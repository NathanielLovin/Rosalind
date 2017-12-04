def expand(list):
	peps = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	newlist = []
	for x in list:
		for z in peps:
			y = x.copy()
			y.append(z)
			newlist.append(y)
	return newlist

def cyclospectrum(peptide):
	spec = [0]
	for x in range(1,len(peptide)):
		for i in range(len(peptide)):
			if i+x >= len(peptide):
				y = i+x-len(peptide)
				spec.append(sum(peptide[i:])+sum(peptide[:y]))
			else:
				spec.append(sum(peptide[i:i+x]))
	spec.append(sum(peptide))
	spec.sort()
	return spec

def linospectrum(peptide):
	spec = [0]
	for x in range(1,len(peptide)):
		for i in range(len(peptide)):
			if i+x <= len(peptide):
				spec.append(sum(peptide[i:i+x]))
	spec.append(sum(peptide))
	spec.sort()
	return spec

def output(pep):
	p = ""
	for x in pep:
		p += str(x) + '-'
	print(p[:-1])

def score(peptide, spectrum):
	spec = linospectrum(peptide)
	score = 0
	i = 0
	for x in spectrum:
		for y in range(i,len(spec)):
			if x == spec[y]:
				score +=1
				i = y+1
				break
	return score

def circScore(peptide, spectrum):
	spec = cyclospectrum(peptide)
	score = 0
	i = 0
	for x in spectrum:
		for y in range(i,len(spec)):
			if x == spec[y]:
				score +=1
				i = y+1
				break
	return score

def cut(leaderboard, spectrum, n):
	if len(leaderboard) <= n:
		return leaderboard
	scores = []
	for x in leaderboard:
		scores.append(circScore(x, spectrum))
	scores.sort()
	scores.reverse()
	min = scores[n-1]
	new = []
	for x in leaderboard:
		if circScore(x, spectrum) >= min:
			new.append(x)
	return new

def leaderboardCyclopeptideSequencing(spectrum, n):
	leaderboard = [[]]
	leaderPeptide = []
	leaderScore = 0
	while leaderboard != []:
		leaderboard = expand(leaderboard)
		newleaderboard = []
		for pep in leaderboard:
			if sum(pep) == spectrum[-1]:
				if circScore(pep, spectrum) >= leaderScore:
					leaderPeptide = pep
					leaderScore = circScore(pep, spectrum)
			if sum(pep) <= spectrum[-1]:
				newleaderboard.append(pep)
		leaderboard = cut(newleaderboard,spectrum, n)
	return leaderPeptide



n = 364
spectrum = [0, 71, 71, 99, 101, 103, 113, 114, 115, 128, 131, 156, 172, 184, 186, 186, 186, 212, 217, 227, 231, 245, 257, 283, 287, 287, 287, 299, 330, 340, 342, 345, 348, 358, 358, 370, 398, 401, 411, 443, 443, 444, 469, 471, 473, 473, 476, 504, 514, 514, 526, 544, 557, 570, 574, 575, 587, 597, 628, 629, 629, 632, 645, 657, 688, 688, 690, 698, 700, 731, 743, 756, 759, 759, 760, 791, 801, 813, 814, 818, 831, 844, 862, 874, 874, 884, 912, 915, 915, 917, 919, 944, 945, 945, 977, 987, 990, 1018, 1030, 1030, 1040, 1043, 1046, 1048, 1058, 1089, 1101, 1101, 1101, 1105, 1131, 1143, 1157, 1161, 1171, 1176, 1202, 1202, 1202, 1204, 1216, 1232, 1257, 1260, 1273, 1274, 1275, 1285, 1287, 1289, 1317, 1317, 1388]
output(leaderboardCyclopeptideSequencing(spectrum, n))