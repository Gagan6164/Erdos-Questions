s = 0
s1=0
s2=0
for i in range(1,1001):
    if (i%2==0 or i%3==0 and i%6!=0):
        s=s+1
print(s)
