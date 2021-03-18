def G():
    i=0
    while i<7:
        j=0
        while j<5:
            if (j==0 and (i!=0 and i!=6))  or ((i==0 or i==6) and (j>0)) or (i==3 and j>1) or (i>3 and j==4):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
