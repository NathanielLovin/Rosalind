f = open('rosalind_ddeg.txt', 'r')
head = f.readline().strip().split()
size = int(head[0])
graph = [[0 for x in range(size)] for y in range(size)]
for line in f:
	edge = line.strip().split()
	edge[0] = int(edge[0])-1
	edge[1] = int(edge[1])-1
	graph[edge[0]][edge[1]] = 1
	graph[edge[1]][edge[0]] = 1

deg = []
for node in graph:
	sum = 0
	for x in node:
		sum += x
	deg.append(sum)

ddeg = []
for node in graph:
	sum = 0
	for x in range(size):
		if node[x] != 0:
			sum += deg[x]
	ddeg.append(sum)

p = ''
for x in ddeg:
	p += str(x) + ' '
print(p)