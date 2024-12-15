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
