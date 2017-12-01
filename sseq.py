import rna

d = rna.FASTAreader("rosalind_sseq.txt")
p = ""
j = 0
for i in range(len(d[0])):
	if j >= len(d[1]):
		break
	if d[0][i] == d[1][j]:
		p += str(i+1) + " "
		j += 1

print(p)
	