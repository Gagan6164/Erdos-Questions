for i in range(0,32):
    a = str(bin(i))[2:]
    j = len(a)
    c = ('0'*(5-j)+a)
    b = c[::-1]
    k='1'+(c+b) + '1'
    l = (int(k, 2))
    m = oct(int(k, 2))[2:]
    n = hex(int(k, 2))[2:]
    x = m[::-1]
    y = n[::-1]
    if (x==m and y==n):
        print(k,m,n,l)


for i in range(0,2048):
    a = str(bin(i))[2:]
    j = len(a)
    c = ('0'*(11-j)+a)
    b = c[::-1]
    k='1'+(c+b) + '1'
    l = (int(k, 2))
    m = oct(int(k, 2))[2:]
    n = hex(int(k, 2))[2:]
    x = m[::-1]
    y = n[::-1]
    if (x==m and y==n):
        print(k,m,n,l)
        
    
    

