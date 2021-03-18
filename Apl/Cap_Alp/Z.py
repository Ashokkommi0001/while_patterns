def Z():
    i=0
    while i<7:
        j=0
        while j<7:
            if i==0 or i==6 or i+j==6 :
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
