# validate user input exercise
# 1. username must not be more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter the username: ")
if len(username) > 12:
       print("Username must be less than or equal to 12 characters!")
elif username.find(" ") != -1:
       print("Username must not contain spaces!")
elif not username.isalpha():
       print("Username must not contain digits!")
else:
       print("Valid Username!")
