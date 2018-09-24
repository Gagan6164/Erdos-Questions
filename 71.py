def product(i):
    tot=1
    while(i>0):
        s=i%10
        tot=tot*s
        i=i//10
    return tot;
c = 0
for i in range(9999,99999):
    j = product(i)
    if (j%10==0 and j!=0):
        c = c+1
print(c)
        

