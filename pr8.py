a=2
for i in range(3,10**9,2):
    c=0
    for j in range(3,i):
        if(i%j == 0):
            c=5
            break
    if(c!=5):
        for l in str(i):
            a = a+int(i)
    
print(a)
