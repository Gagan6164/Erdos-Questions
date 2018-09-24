
import math
for a in range(2,100):
    b = math.factorial(a)
    c = (int((2*b)**0.5))
    n = 0
    for i in range(1,c):
        if ((b/i + (i+1)/2)%(1) == 0):
            n = n+1
    print(a,'-->',n)
            
