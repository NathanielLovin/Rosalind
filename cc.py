def dfs(node):
	visited[node] = True
	for i in range(size):
		if graph[node][i] == 1 and visited[i] == False:
			dfs(i)


f = open('rosalind_cc.txt', 'r')
head = f.readline().strip().split()
size = int(head[0])
graph = [[0 for x in range(size)] for y in range(size)]
for line in f:
	edge = line.strip().split()
	edge[0] = int(edge[0])-1
	edge[1] = int(edge[1])-1
	graph[edge[0]][edge[1]] = 1
	graph[edge[1]][edge[0]] = 1

visited = [False for x in range(size)]
count = 0
for node in range(size):
	if visited[node] == False:
		count += 1
		dfs(node)

print(count)