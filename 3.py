import math
for i in range(50000,60000):
    y = 1
    c = 0
    b = []
    while(c!=4):
        if (math.sqrt(i*y**2+1)%1==0):
            c=4
            x = math.sqrt(i*y**2+1)
            print(i,y,x)
            b.append([x,i])
        else:
            y = y + 1
    
print(b)
