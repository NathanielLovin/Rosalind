f = open('/Users/Nat/Downloads/rosalind_ini6.txt', 'r')
words = f.readline().strip().split()
d ={}
for x in words:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

for key, value in d.items():
	print key
	print value