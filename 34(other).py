import time
import math
def countConsecutive(N): 

    count = 0
    L = 1
    while( L * (L + 1) < 2 * N): 
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1) 
        if (a - int(a) == 0.0): 
            count += 1
        L += 1
    return count 
tic = time.time()
for i in range(17,18):
    N = math.factorial(i)
    print(countConsecutive(N))
    
toc = time.time()
print((toc-tic),"s")

  
