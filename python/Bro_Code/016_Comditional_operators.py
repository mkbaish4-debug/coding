# conditional expressions = A one line shortcut for if-else statements (ternary operators)
# print or assign one of two values based on a condition
# x if condition else Y
x = 2
a = 11
b = 6
age = 35
password = "Admin@123"
# if x == 0:
  #print("zero")
#else :
#  print("positive" if x > 0 else "negative" )
#print("Even" if x%2 == 0 else "Odd")
# max_num = a if a > b else b
# print(max_num)
# status = "Adult" if age >= 18 else "Child"
# print(status)
access_level = "Full Access" if password == "Admin@123" else "Access Denied"
print(access_level)
