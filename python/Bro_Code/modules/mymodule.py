def square(x):
    return x*x

def cube(x):
    return x*x*x

def addall(*args):
    total = 0
    for arg in args:
        total += arg
    return total
