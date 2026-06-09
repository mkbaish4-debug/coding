# shopping cart program
items = []
prices = []
total = 0
while True:
    item = input("What would you like to purchase(q to quit): ")
    if item.lower() == "q":
        break
    else:
        items.append(item)
        price = input(f"What is the price of {item} in $: ")
        while not price.count(".") == 1 and not price.isdigit():
            print("Enter a valid price!")
            price = input(f"What is the price of {item} in $: ")
        price = float(price)
        prices.append(price)

       

print("----Shoping Cart----")
print("You've purchased the following items: ")

for item in items:
    print(f"৹{item}", end = "    ")
print()
for price in prices:
    total += price
print(f"Your total amount for the purchased items is ${total:,.2f}.")



