import math

def p(n,r):
    sum1 =0
    k = r
    m = 2 
    while (n//r>0):
        sum1 = sum1 + (n//r)
        r = k**m
        m = m + 1
    return sum1

def nCr(a,b,c):
    return (p(a,c)-(p(b,c)+ p((a-b),c)))

print(nCr(66,24,3))
print(nCr(73,27,2))
print(nCr(3280,1367,3))
print(nCr(3712,2005,2))
print(nCr(14348,7519,2))
    



