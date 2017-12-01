f = open('rosalind_bfs.txt', 'r')
head = f.readline().strip().split()
size = int(head[0])
graph = [[0 for x in range(size)] for y in range(size)]
for line in f:
    edge = line.strip().split()
    edge[0] = int(edge[0])-1
    edge[1] = int(edge[1])-1
    graph[edge[0]][edge[1]] = 1

Q = [0]
D = [-1 for y in range(size)]
D[0] = 0
while len(Q) != 0:
    z = Q.pop(0)
    for n in range(size):
        if D[n] == -1 and graph[z][n] == 1:
            D[n] = D[z] + 1
            Q.append(n)
print(len(D))
s = ''
for d in D:
	s += str(d) + ' '
print(s)
