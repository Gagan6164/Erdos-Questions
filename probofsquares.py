for k in range(1,4):
    l = 10**k
    n = 0
    t = 0
    for i in range(l,1,-1):
        for j in range(i,0,-1):
            t = t + 1
            if (((i+j)**0.5)%1==0):
                n = n + 1
    print(n)
    print(t)
    print(n/t)
