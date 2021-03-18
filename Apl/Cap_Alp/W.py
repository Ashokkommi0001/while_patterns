def W():
    i=0
    while i<6:
        j=0
        while j<5:
            if (j==0 or j==4) or (i>2 and (i+j==5 or i-j==1)):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
