for i in range(100000,999999):
    a = str(i)
    b = a[:3]
    c = a[3:]
    d = int(c+b)
    if (i*6 == d):
        break
print(i)
