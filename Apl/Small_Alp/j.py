def j():
    row=0
    while row<7:
        col=0
        while col<5:
            if (col==3 and row!=1 and row!=6) or (row==6 and col>0 and col<3) or (col==0 and row==5) or (row==col==2):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
