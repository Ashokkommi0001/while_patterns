def c():
    row=0
    while row<7:
        col=0
        while col<5:
            if (col==0 and (row!=0 and row!=6))  or ((row==0 or row==6) and (col>0)):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
