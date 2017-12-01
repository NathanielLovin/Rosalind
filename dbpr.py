from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('A2S9K2')
record = SwissProt.read(handle) 
for x in record.cross_references:
	if x[0] == 'GO':
		if x[2][0:2] == 'P:':
			print(x[2][2:])