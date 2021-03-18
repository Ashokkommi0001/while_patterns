def T():
    i=0
    while i<6:
        j=0
        while j<5:
            if (i==0 or j==2):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
