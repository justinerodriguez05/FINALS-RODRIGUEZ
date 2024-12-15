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
