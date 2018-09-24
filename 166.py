def G(n):
    c = 0
    a = 2**(2**n)+1
    f = len(str(a))
    for i in range(f):
        j = int(str(a)[i])
        c = c + j
    return ((c)%9)
sum1  = 0
for k in range(1,10):
    sum1 += G(k)
    print(G(k))
