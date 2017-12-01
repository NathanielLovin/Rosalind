from Bio import Entrez
from Bio import SeqIO
Entrez.email = "lovinn@carleton.edu"
handle = Entrez.efetch(db="nucleotide", id=["JX317624, JQ342169, BT149870, JQ712977, JX914595, JX462670, JF927163, JX475048"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
min = len(records[0].seq)
minloc = 0
for i in range(len(records)):
	if len(records[i].seq) < min:
		min = len(records[i].seq)
		minloc = i

print(records[minloc].format("fasta"))