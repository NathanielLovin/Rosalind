from scipy.stats import binom
from numpy import log10

n=42
a = []
for k in range(1,2*n+1):
	y = 0
	for i in range(k, 2*n+1):
		y += binom.pmf(i,2*n,.5)
	print y
	a.append(log(y,10))
p = ""
print(len(a))
for x in a:
	p += "%.3f" %x  + " "
print p

'''R worked better "%.4f", pbinom(0:(2*42-1), 2*42, 0.5, FALSE, TRUE)/log(10)), but who knows'''