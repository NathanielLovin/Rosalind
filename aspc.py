import math

def nCk(n,k):
	return math.factorial(n)//(math.factorial(k) * math.factorial(n-k))

n = 1981
m = 1269
sum = 0
for k in range(m,n+1):
	sum = (sum + nCk(n,k)) % 1000000

print(sum)