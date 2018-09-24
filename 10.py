a = 1
sum3 = 0

sum2 = 0
sum1 = 0
n = int(input('enter the no.-->'))
for i in range(0,n):
    a = a + i*2

    sum1 = sum1 + a



for i in range(0,int((n-1)/2.0)):
    sum2 = sum2 + 2
    sum3= sum3 + sum2

print(2*sum1+(2*sum3-1))

    
    
