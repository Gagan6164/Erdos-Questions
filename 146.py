import math
def primeFactors(n):
    a = 0
    e = 0
    d = 0
    s = n
    c = 0
    while n % 2 == 0:
        a = a + 1
        n = n / 2
        if (a>2):
                e = 1000
    for i in range(3,int(math.sqrt(n))+1,2):
        c = 0
        while n % i== 0:
            c = c + 1
            n = n / i
            if (c>2):
                d = 1000
    if (d == 0 and e == 0):
        return s
    else:
        return 0

sum1 = 0
sum2 = 0
for i in range(2,1234567):
    sum1 = sum1 + primeFactors(i)
    #sum2 = sum2 + i
    #print(primeFactors(i))
print(sum1+1)
#print(sum2 + 1)
#print(sum2-sum1)
