for i in range(100000,1000000):
    x = str(i)
    #a,b,c,d,e,f=x.split("")
    j=list(x)
    y = j[0]+j[1]+j[2]
    z = j[3]+j[4]+j[5]
    g=y+z
    h=z+y
    u = int(g)
    v = int(h)
    if (u*6==v):
        print(u)
    
