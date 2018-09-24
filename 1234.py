y = 0
for i in range(1,100000):
    
    x = (i**6 + 8*(i**4)-6*(i**2)+8)
    y = x**(1/6)
    print(y)
    if (y%1==0):
        print(i,y)
        break
print("chomu")
