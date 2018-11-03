import math
def primeFactors(n):
    a = n
    num = list(str(a))
    num.sort()
    fac = []
    for i in range(3,int(math.sqrt(n))+1,2):
	    while (n%i==0):
		    fac.append(i)
		    n = n / i
		    
    if n > 2:
        fac.append(int(n))
    b = []   
    if (len(fac)==2):
        s1 = str(fac[0])
        s2 = str(fac[1])
        if (len(s1)==len(s2)):
            b = (list(s1)) + (list(s2))
                
        b.sort()
        if (b==num):
            return print(a,fac)

for i in range(10349527,99999999,2):
    primeFactors(i)
