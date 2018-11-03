import math
def tor(n):
    sum1 = 0
    for k in range(1,n):
        if (math.gcd(n,k)==1):
            sum1 = sum1+1
    return sum1




for i in range(1000000,10000000):
    a = len(str(i))
    b = 10**(a-1)
    #print(i,tor(i),b)
    c = tor(i)
    if (c==b):
        print(i,c)



#100064101 is x
#no of digit in x! = 757083374
#function fo calculating no of digits in n!
"""
from math import log, floor, pi

def stirling(n):
    return floor( ((n+0.5)*log(n) - n + 0.5*log(2*pi))/log(10) ) + 1

"""
