import rna

def func(a, b):
    c=0
    for j in range(32,41):
        for i in range(len(a)-j):
            c1=0
            for k in range(len(b)-j):
                if hamming(a[i:i+j], b[k:k+j])<=3:
                    c1+=1
                    if c1>c:
                        c=c1
    return c

def hamming(s1, s2):
	hammingnum = 0
	for x, y in zip(s1, s2):
		if x != y:
			hammingnum += 1
	return hammingnum

strings = rna.FASTAreader("rosalind_subo.txt")
d = strings[0]
f = strings[1]

print(str(func(d, f)) + " " + str(func(f, d)))