for row in range(1,7):
    for col in range(5,row-1,-1):
        print(end=" ")
    for col2 in range(1,row+1):
        print("*",end=" ")
    print()