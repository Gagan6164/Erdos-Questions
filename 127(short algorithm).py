import math
sum1 = 0
a = 4444444444
for i in range(0,20):
    b = 4**i
    c = b*2
    d = (a - b)/(c)
    sum1 = sum1 + (math.floor(d)+1)
    
print(d)
print(sum1)
    
