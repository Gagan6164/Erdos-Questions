def facto(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return (fact)

sum1 = 0   
for i in range(1,1001):
    sum1 = sum1 + (i**2 + i + 1)*(facto(i))
print(sum1%(3**20))
