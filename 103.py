sum1 = 0
for i in range(333333,777777):
    s = str(i)+'3'
    lst = list(s)
    j = int(s)
    n=0
    for k in range(7):
            if (lst[k]=='3' or lst[k]=='7'):
                n = n+1
            if (n ==7):
                print(j)
                if (j%7==0 and j%10==3):
                    sum1 = sum1 + j
print(sum1)
