from Bio import SeqIO
q = 24
record = SeqIO.parse("rosalind_phre.txt", "fastq")

low = 0
for s in record:
	sum = 0
	count = 0
	for i in s.letter_annotations["phred_quality"]:
		sum += i
		count += 1
	if sum / count < q:
		low += 1

print(low)