for i in range(7,10000000):
    c = i
    while(i>0):
        if ((i%7)==0 or (i%13)==0): 
            break
        else:
            
            i = i - 13
            if (i<0):
                print(c)
        
