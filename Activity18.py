no = eval(input("Enter number of Triangle: "))

for x in range(1, 5):
    for r in range(1,no + 1):
        for y in range(1,x + 1):
            print("*", end= " ")
    
        for z in range(5, x, -1):
            print(" ",end= " ")
    print()