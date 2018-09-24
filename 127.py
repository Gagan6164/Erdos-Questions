n = list(range(1, 45))


    
for l in n:
    for k in n[:l]:
     if (2*k == l):
        n.remove(l)
        break


print(n)
print(len(n))


