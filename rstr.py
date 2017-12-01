import math

n = 85958
gc = 0.495989
d = "TACCGGCACC"
prob = 0
for x in d:
	if x == 'A' or x == 'T':
		prob += math.log((1-gc)/2, 10)
	else:
		prob += math.log(gc/2, 10)
prob = 10**prob
ans = 1-(1-prob)**n
print(ans)