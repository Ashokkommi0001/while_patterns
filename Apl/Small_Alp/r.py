def r():
    row=0
    while row<7:
        col=0
        while col<6:
            if (col==2 and row>0) or (row<1 and col>2) or row==col==0:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
