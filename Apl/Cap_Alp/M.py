def M():
    i=0
    while i<6:
        j=0
        while j<5:
            if (j==0 or j==4) or (i<3 and (i-j==0 or i+j==4)):
                print("*",end="  ")
            else:
                print(end="   ")
            j+=1
        i+=1
        print()
