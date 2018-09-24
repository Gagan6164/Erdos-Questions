n = 0
for i in range(1234567,12345670):
   while(i>0):
        s=i%10
        if (s == 1):
            n = n+1
        i=i//10 
print(n)
#10765431
#12365432
