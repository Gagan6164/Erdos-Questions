sum1 = 0
for i in range(0,1000000001):
    a = bin(i)[2:]
    m = oct(i)[2:]
    n = hex(i)[2:]
    b = a[::-1]
    x = m[::-1]
    y = n[::-1]
    if (x==m and y==n and a==b):
        print(a,m,n,i)
        sum1 = sum1 + i
print(sum1)
