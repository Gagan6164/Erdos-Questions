x = 0
for i in range(5555555555555555555,7777777777777777777):
    s = str(i)+'5'
    lst = list(s)
    j = int(s)
    n=0
    for k in range(20):
            if (lst[k]=='5' or lst[k]=='7'):
                n = n+1
            if (n ==20):
                print(j)
                if (j%7==0 and j%5==0):
                    x=x+1
print(x)
