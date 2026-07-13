# if __name__ == '__main__': (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)
#
#                Ex. library = import library for functionality
#                    When running library directly, display a help page

print("This is bound to run")
def add(x, y):
    result = x + y
    print(result)

if __name__ == "__main__":
    add(5, 6)
