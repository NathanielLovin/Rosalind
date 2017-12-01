def enum(alpha, n):
	if n == 0:
		return [""]
	current = []
	next = enum(alpha, n-1)
	for i in alpha:
		for j in next:
			if not (i == '' and j != ''):
				current.append(i + j)
	return current

alpha = ['', 'L', 'X', 'M', 'B', 'D', 'O', 'E', 'H', 'W', 'U', 'R']
n = 3

for i in enum(alpha, n):
	print(i)