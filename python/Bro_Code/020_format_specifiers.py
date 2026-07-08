# Format specifiers = {value:flags} format a value based on
#                      what flags are inserted

# :.(number)f = round off to that many decimal places
# :(number)   = allocate that many spaces
# :0(number)  = allocate and zero pad that many spaces
# :>          = right justify
# :<          = left justify
# :^          = center align
# :+          = use a plus sign to indiacte positive numbers
# :=          = place sign to left most position
# :" "        = place a space before positive numbers
# :","        = comma separator

price_1 = 3.14159
price_2 = -11.14234
price_3 = 3.1

print(f"price 1 is {price_1: }")
print(f"price 2 is {price_2: }")
print(f"price 3 is {price_3: }")
