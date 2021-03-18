def K():
    i=0
    while i<7:
        j=0
        while j<5:
            if (j==0) or (i+j==4 or i-j==2):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
