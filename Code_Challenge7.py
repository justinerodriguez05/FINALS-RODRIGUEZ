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
