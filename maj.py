f = open('maj.txt', 'r')
head = f.readline().strip().split()
length = int(head[1])
arrays = []
for line in f:
	array = line.strip().split()
	for x in array:
		x = int(x)
	arrays.append(array)
print(arrays)
maj = []
for a in arrays:
	for y in range(len(a)):
		occ = 1
		if y > len(a)/2:
			maj.append(-1)
			break
		for x in range(y+1,len(a)):
			if a[y] == a[x]:
				occ +=1
		if occ > len(a)/2:
			maj.append(a[y])
			break
p = ''
for x in maj:
	p += str(x) + ' '
print(p)
