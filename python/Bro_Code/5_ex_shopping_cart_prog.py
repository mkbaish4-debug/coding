item = input("Which item have you purchased?: ")
price = float(input("What's the price of the item purchased?: "))
quantity = int(input("What's the quantity of the item purchased?: "))
total = price*quantity 
print(f"You've bought {quantity} {item}/s.")
print(f"Your total price is: ${total}.")
print("Thanks for visiting!")