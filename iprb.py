from __future__ import division

f = open('/Users/Nat/Downloads/rosalind_iprb (1).txt', 'r')
data = f.readline().strip().split()
k = int(data[0])
m = int(data[1])
n = int(data[2])

pop = k + m + n

dom = k/pop
heterohetro = m/pop * 3/4 * (m-1)/(pop-1) + m/pop * 1/2 * n/(pop-1) + m/pop * k/(pop-1)
heterorec = n/pop * 1/2 * m/(pop-1) + n/pop * k/(pop-1)

print dom + heterohetro + heterorec