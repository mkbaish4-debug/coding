# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year 
# (and therefore be out of date the next year). 

#Extras:

# Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

name = input("What is your name?: ")
age = int(input("What is your age?: "))
year = 2026 + (100-age)
print(f"Hello {name}, You will be 100 years old in the year {year}!")
num = int(input("What is your favorite number?: "))
while num > 0:
    print(f"Hello {name}, You will be 100 years old in the year {year}!")
    num -= 1