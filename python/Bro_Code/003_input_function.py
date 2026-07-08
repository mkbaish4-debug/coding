#input = It is a function that prompts the user to enter data 
#        and returns the entered data as a string 
name = input("What is your name?: ")
print(f"Hello {name}!")
age = input("How old are you?: ")
age = int(age)
#or we can directly do the following:
#age = int(input("How old are you?: ")) it is more convenient
# age = age + 1
# print(f"HAPPY BIRTHDAY!, You are {age} years old now!")
print(f"HAPPY BIRTHDAY!, You are {age + 1} years old now!")