def g():
    row=0
    while row<7:
        col=0
        while col<5:
            if (row%3==0) and (col>0 and col<4) or (col==0 and (row%3!=0 and row!=4)) or (col==4 and row<6):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
