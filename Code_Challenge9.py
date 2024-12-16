for x in range(0, 11):
        for y in range(1, x + 1):
            print(" " , end  = " ")
        for y in range(11, x, -1):
            print("*" , end = " ")
        print()
