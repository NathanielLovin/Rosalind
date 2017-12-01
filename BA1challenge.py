import rna

def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def immediateNeighbors(pattern):
	neighborhood = [pattern]
	for i in range(len(pattern)):
		symbol = pattern[i]
		if symbol != 'A':
			neighborhood.append(pattern[0:i] + 'A' + pattern[i+1:])
		if symbol != 'C':
			neighborhood.append(pattern[0:i] + 'C' + pattern[i+1:])
		if symbol != 'G':
			neighborhood.append(pattern[0:i] + 'G' + pattern[i+1:])
		if symbol != 'T':
			neighborhood.append(pattern[0:i] + 'T' + pattern[i+1:])
	return neighborhood

def neighbors(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	neighborhood = []
	sufneigh = neighbors(pattern[1:],d)
	for x in sufneigh:
		if hammingDistance(pattern[1:],x) < d:
			for y in ['A', 'C', 'G', 'T']:
				 neighborhood.append(y + x)
		else:
			neighborhood.append(pattern[0] + x)
	return neighborhood

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

def approximatePatternCount(text, pattern, d):
	count = 0
	for i in range(len(text) - len(pattern) +1):
		test = text[i:i+len(pattern)]
		if hammingDistance(test, pattern) <= d:
			count = count+1
	return count

def frequencyArrayWithMismatches(text, k, d):
	frequencyArray = [0] * 4**k
	close = [0] * 4**k
	for i in range(len(text)-k):
		neighborhood = neighbors(text[i:i+k],d)
		for x in neighborhood:
			close[patternToNumber(x)] = 1
	for i in range(4**k):
		if close[i] == 1:
			pattern = numberToPattern(i,k)
			frequencyArray[i] = approximatePatternCount(text, pattern, d)
	return frequencyArray

def frequentWordsWithMismatches(text, k, d):
	frequentPatterns = []
	frequent = frequencyArrayWithMismatches(text, k, d)
	reverseFrequent = frequencyArrayWithMismatches(rna.reverseComplement(text), k, d)
	frequencyArray = [0] * 4**k
	for i in range(4**k):
		frequencyArray[i] = frequent[i] + reverseFrequent[i]
	maxCount = max(frequencyArray)
	for i in range(4**k):
		if frequencyArray[i] == maxCount:
			frequentPatterns.append(numberToPattern(i,k))
	return frequentPatterns

def minSkew(genome):
	skew = [0]
	for i in genome:
		if i == 'A' or i == 'T':
			skew.append(skew[-1])
		if i == 'C':
			skew.append(skew[-1]-1)
		if i == 'G':
			skew.append(skew[-1]+1)
	m = min(skew)
	minSkews = []
	for i in range(len(skew)):
		if skew[i] == m:
			minSkews.append(i)
	return minSkews

d = rna.FASTAreader("Salmonella enterica.txt")
salmonella = d[0]
turning = minSkew(salmonella)[0]
a = frequentWordsWithMismatches(salmonella[turning-500:turning+500],9,1)
p = ""
for x in a:
	p += x + " "
print(p)

/* TGTGGATAA TTATCCACA
Which is empirically correct! */ 