from Bio import Entrez
Entrez.email = "lovinn@carleton.edu"
handle = Entrez.esearch(db="nucleotide", term="Micropsitta[Organism]", datetype = 'pdat', mindate = "2007/03/17", maxdate = "2009/03/19")
record = Entrez.read(handle)
print(record['Count'])