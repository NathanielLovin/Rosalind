f = open('rosalind_dij.txt', 'r')
head = f.readline().strip()
size = head[0]
graph = [[0 for y in range(size)] for x in range(size)]
D = [-1 for y in range(size)]
for line in f:
	edge = line.split()
	graph[int(edge[0])-1][int(edge[1])-1] = int(edge[2])

D[0] = 0
Q = []
for x in len(graph[0]):
	if graph[0][x] !=  0:
		Q.append([x, graph[0]])

while len(Q) != 0:
