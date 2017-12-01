n = 82
k=10
nfac = 1
nkfac = 1
for i in range(1,n+1):
	nfac = nfac * i
	if i == (n-k):
		nkfac = nfac
top = nfac
bottom = nkfac
solution = top / bottom % 1000000
print(solution)