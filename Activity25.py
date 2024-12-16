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
#fruits = ["apples", "banana", "orange", "star apple", "guyabano"]

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