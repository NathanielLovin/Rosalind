from Bio import SeqIO
q = 25
p = 85/100
record = SeqIO.parse("rosalind_filt.txt", "fastq")

high = 0
for s in record:
	sum = 0
	count = 0
	for i in s.letter_annotations["phred_quality"]:
		count += 1
		if i >= q:
			sum += 1
	if sum / count >= p:
		high += 1

print(high)