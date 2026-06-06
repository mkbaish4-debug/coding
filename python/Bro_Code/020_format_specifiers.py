# Format specifiers = {value:flags} format a value based on
#                      what flags are inserted 

# :.(number)f = round off to that many decimal places
# :(number)   = allocate that many spaces 
# :0(number)  = allocate and zero pad that many spaces
# :>          = right justify
# :<          = left justify
# :^          = center align
# :+          = use a plus sign to indiacte positive numbers
# :=          = place 
# :" "        = space before positive numbers

price_1 = 30000.14159
price_2 = -123231.14234
price_3 = 3.1

print(f"price 1 is {price_1:^+020,}")
print(f"price 2 is {price_2:^+020,}")
print(f"price 3 is {price_3:^+020,}")