def X():
    i=0
    while i<7:
        j=0
        while j<7:
            if (i-j==0 or i+j==6):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
