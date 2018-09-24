
n = 0
def sum1(i):
    tot=0
    while(i>0):
        s=i%10
        tot=tot+s
        i=i//10
    return tot;
for i in range(59999,99996):
    j = sum1(i)
    if (j==41 and i%11==0):
        n = n+1
print(n)
       
