def body():
    while True:
        print(f"\nWelcome to My Own Python Menu Program")
        print(f"Bachelor Of Science In Infomation Technology - 1C")
        print(f"\nPlease Select an Option:   ")
        print(f"\n1. Open Activity Folder")  
        print(f"2. Open Code Challenge Folder")
        print(f"3. Exit Program")

        menu = input(f"\nChoose what action you want to do:  ")
            
        if menu == "1":
        
            def act_folder1():
                print(f"\nWelcome to everyone this is my activities please enjoy!!")
                print(f"Bachelor Of Science In Infomation Technology - 1C")
                print(f"Activity 1")
                print(f"Activity 2")
                print(f"Activity 3")
                print(f"Activity 4")
                print(f"Activity 5")
                print(f"Activity 6")
                print(f"Activity 7")
                print(f"Activity 8")
                print(f"Activity 9")
                print(f"Activity 10")
                print(f"Activity 12")
                print(f"Activity 13")
                print(f"Activity 13")
                print(f"Activity 14")
                print(f"Activity 15")
                print(f"Activity 16")
                print(f"Activity 17")
                print(f"Activity 18")
                print(f"Activity 19")
                print(f"Activity 20")
                print(f"Activity 21")
                print(f"Activity 22")
                print(f"Activity 23")
                print(f"Activity 24")
                print(f"Activity 25")
                print(f"Type 'exit' to back to menu")
                tuloy = True
                while tuloy == True:
                    piliact = input(f"Choose the number of activity you wish to open--->  ")
                    if piliact =="1":
                        print("Hello World")
                        name = input("Please Enter your Name: ")
                        print("Hi " + name)
                    elif piliact =="2":
                        num1 = eval(input("Please enter the First Number: "))
                        num2 = eval(input("Please enter the Second Number: "))
                        result = num1 + num2
                        print(num1, "+", num2, "=", result)
                    elif piliact =="3":
                        num1 = eval(input("Please Enter the First Number: "))
                        num2 = eval(input("Please Enter the Second Number: "))
                        result = num1 + num2
                        print(result)
                    elif piliact =="4":
                        number1 = eval(input("Enter a number ----> "))
                        number2 = eval(input("Enter a number ----> "))
                        answer = number1 + number2
                        answer2 = number1 - number2
                        answer3 = number1 * number2
                        answer4 = number1 / number2
                        answer5 = number1 ** number2
                        answer6 = number1 // number2
                        answer7 = number1 % number2
                        print("The sum of " ,number1 , " and ",number2 ," is " , answer)
                        print("The difference of " ,number1 , " and ",number2 ," is " , answer2)
                        print("The product of " ,number1 , " and ",number2 ," is " , answer3)
                        print("The quotient of " ,number1 , " and ",number2 ," is " , answer4)
                        print("The exponent of " ,number1 , " and ",number2 ," is " , answer5)
                        print("The floor division of " ,number1 , " and ",number2 ," is " , answer6)
                        print("The reminder of " ,number1 , " and ",number2 ," is " , answer7)
                    elif piliact =="5":
                        print("FAHRENTHEIT to CELCIUS CONVERTER")
                        temp = eval(input("Enter temperature in Fahreinheit: "))
                        celcius = (temp - 32) * 5 / 9
                        print(f"The Convertion of {temp} degree Fahrenheit is {round(celcius, 2)} degree Celcius")
                    elif piliact =="6":
                        #Assignment Operators
                        x = 10
                        print(x)
                        a = x + 10
                        print(a)
                        c = 100
                        c += 100
                        print(c)
                        d =  100
                        d -= 100
                        print(d)
                        e = 100
                        e *= 100
                        print(e)
                        f = 100
                        f /= 100
                        print(f)
                        g = 100
                        g //= 100
                        print(f)
                        h = 100
                        h **= 1
                        print(h)
                        i = 100
                        i %= 100
                        print(i)
                    elif piliact =="7":
                        #Conditional Statement
                        gold = 0 
                        miner = input("Hi, please Enter your Name: ")
                        HasMine = input("Did you mine something today?: ")
                        if HasMine.lower() == "yes":
                            gold += 1_000_000_000
                            print(f"Hi {miner}, today you have a total of {gold} gold")
                        elif HasMine.lower() == "no":
                            print(f"Hi {miner}, Please mine a Gold!:)")
                        elif HasMine.lower() != "yes" and "no":
                            print("Please write the right Input")
                        else:
                            print(f"Hi {miner}, today you have a total of {gold} gold")
                    elif piliact =="8":
                        Password = input("Please Enter your Password: ")

                        if Password.lower() == "secret":
                            print("Access Granted")
                            print("Welcome to the System")
                            print("Enjoy using the System")
                        else:
                            print("Access Denied!")
                            print("Thank your for using the System!")
                    elif piliact =="9":
                        Age = eval(input("Enter your Age: ") )
                        if Age >= 0 and Age <= 7:
                            print("You are a Toddler")
                        elif Age > 7 and Age <= 13:
                            print("You are a Pre-Teen")
                        elif Age > 13 and Age <= 18:
                            print("You are a Teenager")
                        elif Age > 18 and Age <= 31:
                            print("You are an Early Adult ")
                        elif Age > 31 and Age <= 45:
                            print("You are a Mid Adult ")
                        elif Age > 45 and Age <=59: 
                            print("You are a Past Adult")
                        elif Age > 59 and Age <=120:
                            print("You are a Senior")
                        else: 
                            print("Please Input a Valid Number")
                    elif piliact =="10":
                        print("DLL Free BSIT Scholarship Form\n")
                        isDLL = input("Are you a current student of DLL ( yes / no ) : ")
                        isIT = input("Are you interested in taking the course of Bachelor Science in Information Technology ( yes / no ): ")

                        if isIT.lower() == "yes":
                            print("Welcome Future IT Student!")
    
                            if isDLL.lower() == "yes":
                                print("Welcome to the DLL BSIT Scholarship!")
        
                                isGG = input("Are you from Brgy. Gulang - Gulang ( yes / no ): ")

                                if isGG.lower() == "yes":
                                    print("Please Fill up the Second Form ")
            
                                    isLevel = input("What is your curent year level right now in DLL: \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior \nPlease input your answer: ")
            
                                    if isLevel.lower() == "f":
                                        print("Hi, Freshmen!")
                                    elif isLevel.lower() == "f":
                                        print("Hi, Sophomore!")
                                    elif isLevel.lower() == "j":
                                        print("Hi, Junior!")
                                    elif isLevel.lower() == "r":
                                        print("Hi, Senior!")
                                    else:
                                        print("Invalid Choice")

                                    isNeeded = input("Do you need this Scholarship ( yes / no): ")

                                    if isNeeded.lower() == "yes":
                                        print("Scholarship Granted!")
                                    else:
                                        print("Thank you for stopping by!")
                                else:
                                    print("Sorry, this Scholarship are only given from the Residents of Gulang - Gulang")
                            else:
                                print("Thank you for stopping by!")
                        else:
                            print("Sorry, this Form is only for those who want to take the Course of BSIT in DLL\nThank you for stopping by! ")

                        print("Thank you for stopping by!")
                    elif piliact =="11":
                        for x in range(1, 11):
                            print(x, "Hello World")
                            print("Happy Foundation Day")
                            name = input("Hi, what is your name: ")
                            print(f"Hi {name}!") 
                    elif piliact =="12":
                        for cycle in range(10, 0, -1):
                            print(cycle)
                    elif piliact =="13":
                        num1 = eval(input("Enter any number: "))
                        factorial = 1
                        for i in range(num1, 0 , -1):
                            factorial *= i
                        print(f" the factorial of {sum} is {factorial} ")
                    elif piliact =="14":
                        for x in range(0, 11):
                            print(x, end = "")
                            for y in range(x, 11):
                                print("*", end = " ")
                            print()
                    elif piliact =="15":
                        for x in range(0, 21):
                            print(x, end= " ")
                            for y in range(0, x):
                                print("*", end= " ")
                            print()
                    elif piliact =="16":
                        for a in range(1, 6):
                            for b in range(6, a,  -1):
                                print(" ", end = " ")
                            for c in range(1, a + 1):
                                print("*", end = " ")
                            for c in range(1, a + 1):
                                print("*", end = " ")
                            print()
                    elif piliact =="17":
                        col = eval(input("Enter number of column: "))
                        for x in range(1, 11):
                            for y in range(1,col +1):
                                print(f"{x} x {y} = {x*y}", end =  "\t")
                            print()
                    elif piliact =="18":
                        no = eval(input("Enter number of Triangle: "))
                        for x in range(1, 5):
                            for r in range(1,no + 1):
                                for y in range(1,x + 1):
                                    print("*", end= " ")
                                for z in range(5, x, -1):
                                    print(" ",end= " ")
                            print()
                    elif piliact =="19":
                        tuloy = True
                        while tuloy == True:
                            name = input('Please enter a name: ')
                            if name.lower() == "stop":
                                print("Program Terminated")
                                break
                                tuloy = False
                            else:
                                continue
                    elif piliact =="20":
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
                    elif piliact =="21":
                        #BASIC REQUIREMENT OF CREATING YOUR OWN PYTHON FUNCTION

                        def pang_hello():
                         print("Hello IT1C")

                        pang_hello()

                        #FUNCTION WITH A PARAMETER
                        def pang_hello_v2(name):
                            print(f"Hello {name}")
                        def activity3():
                            num1 = eval(input("Please Enter the First Number: "))
                            num2 = eval(input("Please Enter the Second Number: "))

                            result = num1 + num2
                            print(result)

                        tuloy = True
                        while tuloy == True:
                            ask = input("Please provide a name: ")

                            if ask.lower() != "stop":
                                pang_hello_v2(ask)
                            elif ask.lower() == "3":
                                activity3()
                                continue
                            else:
                                break
                    elif piliact =="22":
                        #name listing and then count names 
                        lup = True
                        names = []

                        while lup == True:
                            askName = input("What name would you like to add?> ")
                            if askName.lower() == "stop":
                                print(names)
                                print(f"You have entered {len(names)} names! ")
                                break
                            else:
                                names.append(askName)
                    elif piliact =="23":
                        def factorial(number):
                            """ This Function again is for calculating Factorial Numbers, just provide a value, and it would automatincally compute the factorial"""
                            fact = 1
                            for x in range(number, 0, -1):
                                fact *= 1
                            return fact
                        help(factorial)
                        help(help)
                    elif piliact =="24":
                        #MODULES
                        from Activity24 import factorial
                        print(f"The factorial of 4 is {factorial(4)}")
                    elif piliact =="25":
                        #LIST

                        #fruit1 = "apples"
                        #fruit2 = "banana"
                        #fruit3 = "oranges"
                        #furuit4 = "star apple"
                        #fruit5 = "guyabano"
                        #PYTHON LIST
                        fruits = ["apples", "banana", "orange", "star apple", "guyabano"]
                        print(fruits)
                        #INDEXING / INDEX - Address / Location of an item inside a list
                        #            0          1        2          3           4   
                        #fruit = ["apples", "banana", "orange", "star apple", "guyabano"]
                        print(f"My favorite childhood fruit is{fruits[3]}")
                        print(f"THe last item on the list is {fruits[-1]}")
                        #Adding another Item on the list
                        fruits.append("longgan")
                        print(fruits)
                        fruits.append("chico")
                        print(fruits)
                        #Inserting Item on specific index
                        fruits.insert(3, "papaya")
                        print(fruits)
                        #Removing an Item on a list
                        fruits.remove("longgan")
                        print(fruits)
                        while True:
                            fruit = input("Do youwish to add more fruits(Yes/No):")
                            if fruit.lower() == "no":
                                print(fruits)
                                break
                            else:
                                print("Fruit added to list!")
                                continue
                    elif piliact.lower() =="back":
                        return menu
                    else:
                        print("Invalid Choice, Please try again.")    
                        continue                  
            act_folder1()
            
        elif menu == "2":
            
            def cc_folder2():
                print(f"\nWelcome to My Code_Challenge Enjoy!! ")
                print(f"Bachelor Of Science In Infomation Technology - 1C")
                print(f"Code Challenge 1")
                print(f"Code Challenge 2")
                print(f"Code Challenge 3")
                print(f"Code Challenge 4")
                print(f"Code Challenge 5")
                print(f"Code Challenge 6")
                print(f"Code Challenge 7")
                print(f"Code Challenge 8")
                print(f"Code Challenge 9")
                print(f"Code Challenge 10")
                print(f"Code Challenge 11")
                print(f"Code Challenge 12")
                print(f"Code Challenge 13")
                print(f"Code Challenge 14")
                print(f"Code Challenge 15")
                print(f"Code Challenge 16")
                print(f"Type 'exit' to back to menu")  
                tuloy = True
                while tuloy == True:
                    pilicc = input(f"Choose the number of activity you wish to open--->  ")
                    if pilicc =="1":
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t    *")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ***")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *****")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t *******")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t *******")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *****")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ***")
                        (f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t    *")
                    elif pilicc =="2":
                        name = input('Please Enter your name---> ')
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t    *")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ***")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *****")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t *******")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t Hi" + name + '')
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t *******")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t  *****")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ***")
                        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t    *")
                    elif pilicc =="3":
                        name = input('Please input your name here> ')
                        age = input('Please input your age> ')
                        birthdate = input('Please input your birthdate here> ')
                        birthmonth = input('Please input your birthmonth here> ')
                        birthyear = input('Please input your birthyear here> ')
                        adress = input('Please input your adress here> ')
                        mobile = input('Please input your mobile here> ')
                        email = input('Please input your email here> ')
                        print("\n\n\n\nHello, Myname is " , name , "\b.\nI'm " , age , "\b.\nMy Birthday is in" , birthmonth , birthdate , birthyear, "\b.\nl live in" , adress , "\b.\nMy mobile number is" , mobile , "\b.\nYou may also contact me through my email as" , email , "\b.\n\n\n")
                    elif pilicc =="4":
                        number1 = eval(input("Enter first number ---> "))
                        number2 = eval(input("Enter second number ---> "))
                        answer1 = number1 + number2
                        answer2 = number1 - number2
                        answer3 = number1 * number2
                        answer4 = number1 / number2
                        answer5 = number1 ** number2
                        answer6 = number1 % number2
                        answer7 = number1 // number2
                        print("The sum of", number1, "and", number2, "is", answer1)
                        print("The difference of", number1, "and", number2, "is", answer2)
                        print("The product of", number1, "and", number2, "is", answer3)
                        print("The quotient of", number1, "and", number2, "is", answer4)
                        print(number1 , 'exponent by ' , number2 , 'is ' ,answer5 )
                        print('The reminder of' , number1, 'and' , number2, 'is ' , answer6)
                        print('The floor division of' , number1, 'and' , number2, 'is ' , answer7)
                    elif pilicc =="5":
                        pera = eval(input('Enter amount to deposit ---> '))
                        print(" -------------------------------------")
                        print('  - 1,000 ')
                        print('  -   500 ')
                        print('  -   200 ')
                        print('  -   100 ')
                        print('  -    50 ')
                        print('  -    20 ')
                        print('  -    10 ')
                        print('  -     5 ')
                        print('  -     1 ')
                    elif pilicc =="6":
                        # Compute the final grade
                        prelim = eval(input('Please Input Your Prelim Grade --> '))
                        midterm = eval(input('Midterm Grade --> '))
                        sfinals = eval(input('Semi-Finals Grade --> '))
                        finals = eval(input('Finals Grade --> '))
                        quiz = eval(input('Your Quiz Grade --> '))
                        project = eval(input('Input Your Project Grade --> '))
                        # Check if all grades are valid
                        if (65 <= prelim <= 100) and (65 <= midterm <= 100) and (65 <= sfinals <= 100) and \
                            (65 <= finals <= 100) and (65 <= quiz <= 100) and (65 <= project <= 100):
                            FG = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + \
                                (finals * 0.15) + (quiz * 0.15) + (project * 0.15)
    
                            if FG >= 65:
                                print('Congrats, you pass the course/subject')
                            else:
                                print('Sorry, you failed')
                        else:
                            print('Invalid Grade')
                    elif pilicc =="7":
                        def calculate_bill():
                            """Calculates the total bill, including tax and discounts."""

                            grocery = input("Did you buy a grocery (yes/no): ").lower()
                            item = input("Name of the Item: ")
                            price = float(input("Price of the Item: "))
                            amount_paid = float(input("Amount Paid: "))
                            age = int(input("What is your Age: "))

                            tax_rate = 0.123  # 12.3% tax rate
                            discount_rate = 0.052  # 5.2% discount rate for seniors

                            total_price_with_tax = price * (1 + tax_rate)
                            tax_amount = total_price_with_tax - price
                            discount_amount = total_price_with_tax * discount_rate if age >= 60 else 0
                            final_price = total_price_with_tax - discount_amount
                            change = amount_paid - final_price

                            print(f"Hi Customer, you purchased a {item} with a price of {price:.2f} plus {tax_rate:.2%} Tax which is {tax_amount:.2f} Pesos, the total price is {total_price_with_tax:.2f} Pesos")

                            if age >= 60:
                                print(f"Additionally, you will get a discount of {discount_rate:.2%} or {discount_amount:.2f} pesos.")
                                print(f"The total price will be reduced by {discount_amount:.2f} pesos to {final_price:.2f} Pesos.")

                            print(f"The total change will be {change:.2f} Pesos")
                            print("Thank you Customer! Come Again :)")
                        if __name__ == "__main__":
                            calculate_bill()
                    elif pilicc =="8":
                        odd = 0
                        even = 0
                        total_sum = 0

                        for x in range(1, 11):
                            num = int(input(f"Enter {x}: "))
                            total_sum += num
                            if num % 2 == 0:
                                even += num
                            else:
                                odd += num 

                        print(f"The sum of all numbers given is {total_sum}")
                        print(f"The sum of all odd numbers given is {odd}")
                        print(f"The sum of all even numbers given is {even}")
                    elif pilicc =="9":
                        for x in range(0, 11):
                                for y in range(1, x + 1):
                                    print(" " , end  = " ")
                                for y in range(11, x, -1):
                                    print("*" , end = " ")
                                print()
                    elif pilicc =="10":
                        for x in range(6, 0, -1):
                            for y in range(1, x + 1):
                                print(" ", end=" ")
                            for z in range(6, x, -1):
                                print("*", end=" ")
                            for a in range(6, x, -1):
                                print("*", end=" ")
                            print()

                            for x in range(1, 5):
                                for y in range(1, x + 2):
                                    print(" ", end=" ")
                                for z in range(5, x, -1):
                                    print("*", end=" ")
                                for a in range(5, x, -1):
                                    print("*", end=" ")
                                print()
                    elif pilicc =="11":
                        for a in range(0, 4):
                            for b in range(4, a, -1):
                                print(" ", end=" ")
                            for c in range(0, a, + 1):
                                print("b", end=" ")
                            for c in range(1, a, + 1):
                                print("v", end=" ")
                            print()


                        for e in range(0, 3):
                            for f in range(0, e):
                                print(" ", end=" ")
                        for g in range(3, e, -1):
                                print("y", end=" ")
                        for g in range(2, e, -1):
                                print("l", end=" ")
                        print()
                    elif pilicc =="12":
                        for x in range(7, 0, -1):
                            for y in range(1, x + 1):
                                print(" ", end=" ")
                            for z in range(6, x, -1):
                                print("*", end=" ")
                            for a in range(5, x, -1):
                                print("*", end=" ")
                            print()
                        for x in range(0, 4):
                            for y in range(4, 0, -1):
                                print(" ", end= " ")
                            for z in range(1,1):
                                print("*", end= " ")
                            for a in range(3, 0, -1):
                                print("*", end= " ")
                            print()
                    elif pilicc =="13":
                        for x in range(1,7):
                            for y in range(6, x, -1):
                                print(" ", end= " ")
                            for z in range(x, 1, -1):
                                print(z, end= " ")
                            for a in range(1, x + 1):
                                print(a, end= " ")
                            print()
                        for x in range(5, 0, -1):
                            for y in range(5 - x + 1):
                                print(" ", end=" ")
                            for z in range(x, 0, -1):
                                print(z, end=" ")
                            for a in range(2, x + 1):
                                print(a, end=" ")
                            print()
                    elif pilicc =="14":
                        Go = True
                        a = 0
                        while Go == True:
                            number = eval(input("Enter a number: "))
                            if number == 0:
                                print("Program Terminated")
                                print(f"The total of the number you enter is {a}")
                                break
                            else:
                                a += number
                                continue
                    elif pilicc =="15":
                        import os

                        isContinue = True
                        no = 0
                        while isContinue == True:
                            ask = input("Would you like to add another triangle (yes / no )--> ")

                            if ask.lower() == "no":
                                print("PROGRAM TERMINATED")
                                break
                                isContinue = False
                            elif ask.lower() == "yes":
                                os.system('cls')
                                no += 1
                                for x in range (1, 6):
                                    for r in range (1 , no + 1):
                                        for y in range (1 , x + 1):
                                            print("*", end=" ")
                                        for z in range (6, x, -1):
                                            print(" ",end=" ")
                                    print()
                            else:
                                print("INVALID ANSWER it's only (yes/no)")
                                continue
                    elif pilicc =="16":
                        def breakdown_denomination(amount):
                            ("Denomination Breakdown:")
                            denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
                            for denom in denominations:
                                if amount >= denom:
                                    count = amount // denom
                                    print("PHP", denom, ":", count)
                                    amount = amount % denom


                        def create_account():
                            account_name = input("Enter your name: ")
                            initial_deposit = eval(input("Enter initial deposit: "))
                            if initial_deposit >= 0:
                                print("Account created for", account_name, "with balance PHP", initial_deposit)
                                return account_name, initial_deposit
                            else:
                                print("Initial deposit must be 0 or more.")
                                return None, 0


                        def deposit(account_name, account_balance):
                                if account_name == None:  
                                    print("No account found. Please create an account first.")
                                else:
                                    amount = eval(input("Enter amount to deposit: "))
                                    if amount > 0:
                                        account_balance += amount
                                        print("Deposited PHP", amount, ". Current balance: PHP", account_balance)
                                        breakdown_denomination(amount)
                                    else:
                                        print("Deposit amount must be greater than 0.")
                                return account_balance


                        def withdraw(account_name, account_balance):
                            if account_name == None:
                                print("No account found. Please create an account first.")
                            else:
                                amount = eval(input("Enter amount to withdraw: "))
                                if amount > account_balance:
                                    print("Insufficient balance!")
                                elif amount > 0:
                                    account_balance -= amount
                                    print("Withdrew PHP", amount, ". Current balance: PHP", account_balance)
                                else:
                                    print("Withdrawal amount must be greater than 0.")
                            return account_balance


                        def check_balance(account_name, account_balance):
                            if account_name == None:
                                print("No account found. Please create an account first.")
                            else:
                                print("Your current balance is PHP", account_balance)


                        def main():
                            account_name = None
                            account_balance = 0

                            while True:
                                print("\n=== Welcome to astino-Bank ===")
                                print("1. Create Account")
                                print("2. Deposit")
                                print("3. Withdraw")
                                print("4. Check Balance")
                                print("5. Exit")
                                choice = input("Choose an option (1-5): ")

                                if choice == "1":
                                    account_name, account_balance = create_account()
                                elif choice == "2":
                                    account_balance = deposit(account_name, account_balance)
                                elif choice == "3":
                                    account_balance = withdraw(account_name, account_balance)
                                elif choice == "4":
                                    check_balance(account_name, account_balance)
                                elif choice == "5":
                                    print("Thank you for using the banking system!")
                                    break
                                else:
                                    print("Invalid option. Please try again.")

                        main()
                    elif pilicc.lower() =="back":
                        return menu
                    else:
                        print("Invalid Choice, Please try again.")    
                        continue 


            cc_folder2()
                    
     

        elif menu == "3":
            
            def exit3():
                print(f"\nProgram terminated, Thank you this is my python menu program!!.\n")
            exit3()
            break
        else:
            print("Invalid Choice, Please try again.")    
            continue
body()   