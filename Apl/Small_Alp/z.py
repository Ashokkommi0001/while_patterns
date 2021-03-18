def z():
    row=0
    while row<5:
        col=0
        while col<5:
            if row==0 or row==4 or row+col==4 :
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
