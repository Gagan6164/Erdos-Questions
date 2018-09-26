a = 65
for i in range(1,66):
    c = i
    b = a-c
    a1 = b-c
    b1 = a + c
    b2 = a1 + c
    b3 = a1 - c
    c1 = b - a1
    c2 = a1 + b
    c3 = a + b
    print(a,b,c)
    print("  for a-->  ",a,a1,"  for b--> ",b,b2,b1,b3,"  for c-->  ",c,c1,c2,c3)
