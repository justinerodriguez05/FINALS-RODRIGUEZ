import os

isContinue = True
no = 0
while isContinue == True:
    ask = input("Would you like to add another Triangle(Yes/No): ")

    if ask.lower() == "no":
        print('PROGRAM TERMINATED')
        break
        isContinue = False
    else:
        os.system('cls')
        no += 1
        for x in range (1, 5):
            for r in range(1,no + 1):
                for y in range(1,x, +1):
                    print("*", end = " ")
                
                for z in range(5, x, -1):
                    print(" ", end = " ")
            print()
        continue