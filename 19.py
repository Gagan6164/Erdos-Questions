a = 201413
b = 2**21
for i in range(1,100):
    if (((a**i)%b)==1):
        print(i)
