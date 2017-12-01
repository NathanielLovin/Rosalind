prev1 = 1
prev2 = 0
print("1 1")
for x in range(2,26):
	print(str(x) + " " + str(prev1 + prev2))
	new = prev1 + prev2
	prev2 = prev1
	prev1 = new
