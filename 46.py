a = [0,1,1,2,3]
b = 1
c = 2
d = 3
for i in range(1,514):
    b = c
    c = d
    d = c + b
    a.append(d)


m = [2]
for i in range(1,514):
    if (i%2==0):
        m.append(5*a[i-1]-m[i-2])
    else:
        m.append(0)

#print(m)
#print(a)

prod = 1
for i in range(1,10):
    prod = prod*m[2**i]


print(prod%1000000007)

