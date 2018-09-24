n = 0
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            for l in range(1,101):
                if(i+l == j+k):
                    n = n + 1
                    #print(i , j,'/n', k, l)
print(n)
