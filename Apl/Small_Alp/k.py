def k():
    row=0
    while row<7:
        col=0
        while col<5:
            if (col==0) or (row>1 and (row+col==5  or row-col==3)):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
