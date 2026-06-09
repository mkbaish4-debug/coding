# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.

x = int(input("Enter an integer: "))
if x%2 == 0:
  print("The number is even!")
  if x%4 == 0:
   print("Infact! the number is a multiple of 4.")
else:
  print("The number is odd!")

num, check = float(input("Enter the first number: ")), float(input("Enter a second number to divide by: "))
while check == 0:
  print("Can't divide by zero!")
  check = float(input("Enter a second number to divide by: "))

if num%check == 0:
  result = num/check
  print(f"Second number divides first one evenly! and is equal to: {result:.2f}")
else:
  print("Second number does not divide the first number evenly! ")
