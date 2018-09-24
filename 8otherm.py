n=0
def isPrime(num):
    s=0
    for j in range (1, num):
        if(num%j==0):
            s=s+1
            if(s>1):
                break
    return(s)                
for i in range(1, 10000):
        if(isPrime(i)==1 and isPrime(sum(int(x) for x in str(i)))==1):
            n=n+1
            print( i, sum(int(x) for x in str(i)))
print(n)
