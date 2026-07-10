# concession stand program
menu = {"popcorn": 6.00, "pretzel": 5.00, "soda": 4.00, "fries": 7.00}

cart = []
total = 0

print("Welcome to the concession stand!")
print("-" * 10 + "Our Menu" + "-" * 10)

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-" * 10 + "-" * 10)
print()

order = input("What would you like to enjoy(q to quit): ")
if order.lower() == "q":
    print("Thank you for your order!")
    print("-" * 10 + "-" * 10)
else:
    if menu.get(order) != None:
        cart.append(order)
        total += menu.get(order)
    else:
        print("We don't serve this. Sorry!")

    while True:
        order = input("Anything else?: ")
        if order.lower() == "q":
            print("Thank you for your order!")
            print("-" * 10 + "-" * 10)
            break
        elif menu.get(order) != None:
            cart.append(order)
            total += menu.get(order)
        else:
            print("We don't serve this. Sorry!")

print()
print("----------Your order----------")
for i in range(len(cart)):
    print(f"{cart[i]}")

print()
print(f"Your total is: ${total:.2f}")
