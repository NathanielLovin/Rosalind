f = open('rosalind_2sum.txt', 'r')
head = f.readline().strip().split()
arrays = []
for line in f:
	array = line.strip().split()
	for i in range(len(array)):
		array[i] = int(array[i])
	arrays.append(array)

for x in arrays:
	i = 0
	found = False
	while i < len(x):
		j = i+1
		while j < len(x):
			if x[i] == -x[j]:
				print(str(i+1) + " " + str(j+1))
				found = True
				i = len(x)
				j = len(x)
			j += 1
		i += 1
	if found == False:
		print(-1)