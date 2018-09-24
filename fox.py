a = 1
b = 2
c = 4
for i in range(1,31):
    d = a + b + c + 1
    a = b
    b = c
    c = d
    print(i+3,'-->',d)


"""a = [1,2,4]

for i in range(1,9):
    b = []
    for j in range(len(a)):
        for k in range(j):
            for l in range(k):
                b.append(a[j]+a[k]+a[l]+1)
                b.sort()
                print('this is b',b)
                
                
                g = 0
                for m in b:
                    h = 0
                    if (m==b[h]):
                        g = g + 1
                    else:
                        h = h + 1
                                   
    a.append(max(b))
print("this is a",a)
        
        
            
    






while(h==0):
                    if (z != len(b)):
                        if (b[z]!=b[z+1]):
                            h=2
                            minb = b[z]
                    else:
                        minb = b[z]
                        h =3
                    if (h==0):
                        z = z + 1
                       

"""

