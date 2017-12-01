import rna
strings = rna.FASTAreader("rosalind_cons.txt")
mat = [[0 for x in range(len(strings[0]))] for y in range(0,4)]
for i in strings:
	for x in range(len(i)):
		if i[x] == 'A':
			mat[0][x] +=1
		if i[x] == 'C':
			mat[1][x] +=1
		if i[x] == 'G':
			mat[2][x] +=1
		if i[x] == 'T':
			mat[3][x] +=1

trans = zip(*mat)
cons = ""
alist = ''
clist = ''
glist = ''
tlist = ''
for z in trans:
	a = z.index(max(z))
	if a == 0:
		cons += 'A'
	if a == 1:
		cons += 'C'
	if a == 2:
		cons += 'G'
	if a == 3:
		cons += 'T'
	alist+=str(z[0]) + ' '
	clist+=str(z[1]) + ' '
	glist+=str(z[2]) + ' '
	tlist+=str(z[3]) + ' '
print(cons)
print('A:' + " " + alist)
print('C:' + " " + clist)
print('G:' + " " + glist)
print('T:' + " " + tlist)
