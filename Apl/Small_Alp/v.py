def v():
    row=0
    while row<8:
        col=0
        while col<16:
            if (row-col==0 or row+col==14):
                print("*",end="")
            else:
                print(end=" ")
            col+=1
        row+=1
        print()
