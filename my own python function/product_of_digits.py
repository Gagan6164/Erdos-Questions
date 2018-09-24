def product(i):
    tot=1
    while(i>0):
        s=i%10
        tot=tot*s
        i=i//10
    return tot;
