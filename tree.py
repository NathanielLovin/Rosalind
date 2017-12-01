f = open("rosalind_tree.txt", 'r')
n= int(f.readline())
edges = 0
for line in f:
	edges += 1
ans = n - edges - 1
print(ans)