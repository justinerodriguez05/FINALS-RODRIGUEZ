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