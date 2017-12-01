def enum(alpha, n):
	if n == 0:
		return [""]
	current = []
	next = enum(alpha, n-1)
	for i in alpha:
		for j in next:
			current.append(i + j)
	return current

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
n = 3

for i in enum(alpha, n):
	print(i)