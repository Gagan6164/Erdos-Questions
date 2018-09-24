c=0
for k in range(1500,2000):
    for m in range(k):
        for n in range(m):
            if (m+n>k):
                
                if (((3**k)%(10**4))==((3**m)%(10**4))==((3**n)%(10**4))):
                    print(k,m,n,k+m+n)
                    c=5
                    break
    if(c==5):
        break
        
