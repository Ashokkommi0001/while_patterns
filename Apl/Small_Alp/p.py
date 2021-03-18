def p():
    row=0
    while row<7:
        col=0
        while col<5:
            if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
