def sum1(i):
    tot=0
    while(i>0):
        s=i%10
        tot=tot+s
        i=i//10
    return tot;
