import math

n = 981211
s = "CCGGTCCCT"
A = [0.000, 0.071, 0.116, 0.157, 0.214, 0.268, 0.318, 0.380, 0.409, 0.488, 0.524, 0.592, 0.641, 0.676, 0.745, 0.755, 0.821, 0.863, 0.929, 1.000]
prob = [1.0 for x in range(len(A))]
for x in s:
	if x == 'A' or x == 'T':
		for y in range(len(prob)):
			prob[y] *= (1-A[y])/2
	else:
		for y in range(len(prob)):
			prob[y] *= A[y]/2

p = ''
for x in prob:
	p += str((n-len(s)+1)*x) + ' '
print(p)