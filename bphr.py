from Bio import SeqIO
q = 22
record = SeqIO.parse("rosalind_bphr.txt", "fastq")

low = 0
a = []
count = 0
for s in record:
	count += 1
	if a == []:
		a = [0] * len(s.letter_annotations["phred_quality"])
	print(len(s.letter_annotations["phred_quality"]))
	for i in range(len(s.letter_annotations["phred_quality"])):
		a[i] += s.letter_annotations["phred_quality"][i]

mean = [0] * len(a)
for i in range(len(a)):
	mean[i] = a[i]/count

print(mean)
count = 0
for i in mean:
	if i < q:
		count += 1

print(count)