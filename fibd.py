n = 88
m = 18

a = []
for x in range(m-1):
	a.append(0)
a.append(1)
for i in range(n-1):
	new = 0
	for x in range(m-1):
		new = new+a[x]
	for x in range(m-1):
		a[x] = a[x+1]
	a[m-1] = new
	print(a)

print(sum(a))
