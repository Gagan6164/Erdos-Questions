a = 0
b = 1
c = 2
sum1 = 0
for i in range(1,274000):
    a = b
    b = c
    c = a + b + i + 1
    sum1 = sum1 + c
print (sum1%1000000007)

