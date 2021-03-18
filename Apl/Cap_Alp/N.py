def N():
    i=0
    while i<7:
        j=0
        while j<7:
            if (j==0 or j==6) or i-j==0:
                print("*",end="  ")
            else:
                print(end="   ")
            j+=1
        i+=1        
        print()
