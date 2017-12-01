f = open('/Users/Nat/Downloads/rosalind_fib (2).txt', 'r')
data = f.readline().strip().split()
n = int(data[0])
k = int(data[1])

fib = [1, 1]
for x in range(2, n):
	fib.append(k * fib[x-2] + fib[x-1])
print fib[n-1]
print fib