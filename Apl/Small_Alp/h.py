def h():
    row=0
    while row<7:
        col=0
        while col<6:
            if (col==0 ) or ((row==3) and col<5) or (col==5 and (row>3)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
            col+=1
        row+=1
        print()
