def q():
    row=0
    while row<7:
        col=0
        while col<6:
            if col==4 or (col==0 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)) or (row==5 and col==5):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
                
        print()
