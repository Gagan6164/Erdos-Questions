import math
sum1 = 0
c = 0
sum2 = 0
for i in range(1,161):
    sum1 = sum1 + ((math.log(10**22))**i)/(i*math.factorial(i))
    sum2 = sum2 + ((math.log(2))**i)/(i*math.factorial(i))
    b = math.log(math.log(10**22)) - math.log(math.log(2))

g = int(sum1 + b - sum2)
f = 201467286689315906290
print(g-f,i)

