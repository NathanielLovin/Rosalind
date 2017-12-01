import rna

d=rna.FASTAreader("rosalind_splc.txt")
s = d[0]
introns = d[1:]

for i in range(len(s)):
	for x in introns:
		if (s[i:i+len(x)] == x):
			s = s[0:i] + s[i+len(x):]
			break;

print(rna.protein(rna.transcribe(s)))