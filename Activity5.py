print("FAHRENTHEIT to CELCIUS CONVERTER")
temp = eval(input("Enter temperature in Fahreinheit: "))

celcius = (temp - 32) * 5 / 9


print(f"The Convertion of {temp} degree Fahrenheit is {round(celcius, 2)} degree Celcius")