import urllib2
import re
import collections

f = open('rosalind_mprt.txt', 'r')
label = ''
d = {}
rx = '(?=(N[^P][ST][^P]))'
for line in f:
	label = line.strip()
	url = 'http://www.uniprot.org/uniprot/' + label + '.fasta'
	html = urllib2.urlopen(url)
	string = ''
	for line in html:
		if line[0:1] is not '>':
			string += line.strip()
	found = ''
	for m in re.finditer(rx, string):
		found += str(m.start()+1) + ' '
	if found is not '':
		print label
		print found[:-1]
f.close()
