

for j in range(1,40):
    n = 2**j
    sum1 = 1
    for i in range(2,n+1):
        sum1 = sum1^i
    print(n,sum1)
    
