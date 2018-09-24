a = '6'
b = '0'
for i in range(10000000,100000000):
    c = str(i)
    e = '0'*(9-len(c))+c
    f = a + e[0]+ a + e[1]+ a + e[2]+ b + e[3] + b + e[4] + a + e[5]+ a + e[6]+ a + e[7]+ b + e[8] + b
    g = int(f)
    if ((g**(0.5))%1==0):
        print(g)
    
