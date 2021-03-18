def S():
    i=0
    while i<7:
        j=0
        while j<5:
            if (i==0 or i==3 or i==6) and (j>0 and j<4) or (j==0 and (i>0 and i<3)) or (j==4 and (i>3 and i<6)):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
