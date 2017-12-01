from __future__ import division

f = open('/Users/Nat/Downloads/rosalind_gc (2).txt', 'r')
label = f.readline().strip()[1:]
strings = []
count = 0
length = 0
for line in f:
	x = line.strip()
	if x[0:1] == '>':
		content = count/length * 100.00
		strings.append([label[:], content])
		count = 0
		length = 0
		label = x[1:]
	else:
		for y in x:
			if y == 'G' or y == 'C':
				count += 1
		length += len(x)

maxlabel = strings[0][0]
maxcontent = strings[0][1]
for x in strings[1:]:
	if x[1] > maxcontent:
		maxlabel = x[0]
		maxcontent = x[1]
print maxlabel
print maxcontent
print strings