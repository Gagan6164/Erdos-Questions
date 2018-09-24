n = 0
for i in range(1,10001):
    j = int(str(2**i)[:1])
    if (j==1):
        n = n+1
#print(((n-1)/i)*(10**6))
print('no of iteration', i)
print(n)
