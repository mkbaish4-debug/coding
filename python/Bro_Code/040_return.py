# return = statement used to end a function
# and send a result back to caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def division(x, y):
    if y != 0:
        z = x / y
        return z
    else:
        return "Can't divide by zero!"


print(add(2, 3))

print(subtract(5, 6))

print(multiply(65786, 96))

print(division(3, 0))
