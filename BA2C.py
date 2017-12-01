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

def profileProbable(text, k, profile):
	probs = [0] * 4**k
	for i in range(len(text) - k +1):
		prob = 1
		pattern = text[i:i+k]
		for j in range(k):
			l = symbolToNumber(pattern[j])
			prob *= profile[l][j]
		probs[patternToNumber(pattern)] = prob
	m = max(probs)
	for x in range(4**k):
		if probs[x] == m:
			return numberToPattern(x, k)

text = "GCGTACATCAAGTCGTGCCGTAAACCAAGCCGTACACATGGTTATAGTTAGTAACTCTTATCCGGAGGATTTCATCACGCTTCTTGGTTGACGCCTCCTGACCATTTCATTAAATTCCGCTTTCCTATACTTGCAGGAGCGCAGGATGTGTAGCAACCGATCTGGAGTCACGCAGCATACCGATTCCCGATGACCGTTTG"
k = 6
profile = [[0.212, 0.333, 0.333, 0.242, 0.212, 0.242],
[0.242, 0.273, 0.212, 0.242, 0.273, 0.364],
[0.242, 0.242, 0.152, 0.333, 0.303, 0.152],
[0.303, 0.152, 0.303, 0.182, 0.212, 0.242]]

print(profileProbable(text, k, profile))
			
		

