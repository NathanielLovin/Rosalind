def merge(a, b):
    c = []
    x = 0
    y = 0
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            c.append(a[x])
            x+=1
        else:
            c.append(b[y])
            y+=1
    if x == len(a):
        for i in b[y:]:
            c.append(i)
        else:
            for i in a[x:]:
                c.append(i)
return c

def sort(a):
    if len(a) == 1:
        return a
        else:
            return merge(sort(a[:len(a)/2]), sort(a[len(a)/2:]))

a = []
inv = 0
for x in range(len(a)):
    if x % 1000 == 0:
        print(x)
    for y in range(x+1, len(a)):
        if a[x] > a[y]:
            inv += 1

print(inv)
