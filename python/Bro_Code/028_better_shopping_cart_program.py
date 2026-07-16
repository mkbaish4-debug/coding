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
        while True:
           price = input(f"What is the price of {item} in $: ")
           if price.replace(".", "", 1).isdigit():
               prices.append(float(price))
               break
           else:
                print("Invalid price!")

print("----Shoping Cart----")
print("You've purchased the following items: ")

for item in items:
    print(f"{items.index(item) + 1}. {item}", end = "    ")
print()
for price in prices:
    total += price
print(f"Your total amount for the purchased items is ${total:,.2f}.")
