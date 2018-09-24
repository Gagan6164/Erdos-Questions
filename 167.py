b = ['3','5','7']
for m in range(20,35):
    for l in range(3):
        a = int(str(2**m)+'3'+b[l])
        c = 0
        for j in range(1,a+1):
            if (a%j==0):
                c = c + j
        if (c == 3*a):
            print(a)

    
