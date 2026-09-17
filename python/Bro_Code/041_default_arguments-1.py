# default arguments = A default value for certain parameters
#                     default arguments are used when arguments are omitted
#                     makes the functions more flexible and reduces # of arguments
#                     1. positional 2. default 3. keyword 4. arbitrary

def new_price(price, discount=0, tax=0.1):
    tax_amount = price * tax
    discount_amount = price * discount
    return price + tax_amount - discount_amount

print(new_price(100))
# default arguments will be overridden by given arguments
print(new_price(100, 0.1))
print(new_price(100, 0.2, 0.1))
