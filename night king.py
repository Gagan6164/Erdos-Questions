k=0
c=0
for i in range(123456,1,-1):
    b=123456789%i
    if (b==0):
        k = k+1
        print(k)
        while(c>0):
            c=123456789-k
            print(k)
