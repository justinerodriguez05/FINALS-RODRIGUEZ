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