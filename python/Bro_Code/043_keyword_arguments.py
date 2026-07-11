# keyword = An argument preceded by an identifier
#           they are useful for readability
#           order of arguments doesn't matter if they are keyword arguments
#           all the positional arguments follows keyword arguments

def hello(greetings, title, first, last):
    print(f"{greetings} {title}{first} {last}")


hello("Namaste", last="Kiran", first="Raj", title="Prof.")
