
for i in range(1,10000):
    m = i//13
    for j in range(1,m):
        a = i
        while(a>0):
            a = a - j*13
            if (a%7==0):
                k = i
print(k)
            
