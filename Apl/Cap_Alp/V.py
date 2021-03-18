def V():
    i=0
    while i<8:
        j=0
        while j<16:
            if (i-j==0 or i+j==14):
                print("*",end="")
            else:
                print(end=" ")
            j+=1
        i+=1
        print()
