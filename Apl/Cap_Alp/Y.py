def Y():
    i=0
    while i<7:
        j=0
        while j<7:
            if (i-j==0 and i<3) or (i+j==6 and i<3) or (i>2 and j==3):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
