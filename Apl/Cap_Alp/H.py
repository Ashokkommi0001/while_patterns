def H():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or (j==4) or i==3:
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
