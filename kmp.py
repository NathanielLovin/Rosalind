import rna

d = rna.FASTAreader("rosalind_kmp.txt")
dna = d[0]
failure = [0]

for i in range(1,len(dna)):
		fail = True
		for l in range(failure[-1]+1,-1,-1):
			j = i-l
			if dna[j+1:i+1] == dna[0:l]:
				failure.append(l)
				fail = False
				break;
		if fail:
			failure.append(0)

p = ""
for x in failure:
	p += str(x) + " "
f = open("rosalind_kmp_out.txt",'w')
f.write(p)
f.close()