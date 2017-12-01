f = open('/Users/Nat/Downloads/rosalind_hamm.txt', 'r')
s1 = f.readline().strip()
s2 = f.readline().strip()
distance = 0
for x in range(0, len(s1)):
	if s1[x:x+1] != s2[x:x+1]:
		distance += 1
print distance