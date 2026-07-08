# while loop = execute some code forever
#              while some condition remains true

# name = input("Enter your name: ")

# while name == "":
#    print("You did not enter your name!")
#    name = input("Enter your name: ")
# print("Hello " + name + "!")

# age = int(input("Enter your age: "))
# while age < 0:
#    print("Age can't be negative!")
#    age = int(input("Enter your age: "))
# print(f"You are {age} years old!")

# food = input("Enter the food you like (q to quit): ")
# while not food.lower() == "q":
#    print(f"You like {food}!")
#    food = input("Enter another food you like (q to quit): ")
# print("Bye!")

num = int(input("Enter a number you like(0-10): "))
while num < 0 or  num >10:
    print("Please choose a number between 1-10!")
    num = int(input("Enter a number you like(0-10): "))
print("You chose " + str(num))
