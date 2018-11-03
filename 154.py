def farm(y):
    if (y<=6):
        r = ((16 + y*y)**(0.5)-4)
        area = 3.14159265359*(4 + (r**2)/4 )
    else:
        area = 25.1327412287
    return area
sum1 = 0
for i in range(4,1001):
    sum1 = sum1 + farm(i)

print(sum1)
