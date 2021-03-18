def w():
    row=0
    while row<6:
        col=0
        while col<7:
            if (col%3==0 and row<5) or (row==5 and col%3!=0):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
