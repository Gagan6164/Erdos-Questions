a = 1
b = 2
c = 3
e = '6343'
g = []
for i in range(181000):
    a = b
    b = c
    c = a + b
    d = str(c)
    if (len(d)>= 4):
        if (d[-4:]==e):
            print(i+6,'index')
            g.append(i+6)
for i in range(len(g)):
    print(g[i+1]-g[i])
    
        
