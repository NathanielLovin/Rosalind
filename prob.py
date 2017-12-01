import math

f = open('rosalind_prob.txt', 'r')
s = f.readline().strip()
A = f.readline().strip().split()
A = list(map(float, A))
print(A)
prob = [0.0 for x in range(len(A))]
for x in s:
	if x == 'A' or x == 'T':
		for y in range(len(prob)):
			prob[y] += math.log((1-A[y])/2, 10)
	else:
		for y in range(len(prob)):
			prob[y] += math.log(A[y]/2, 10)

p = ''
for x in prob:
	p += str(x) + ' '
print(p)