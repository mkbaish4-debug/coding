#validate user input exercise
# 1. username is no more than 12 characters 
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter the username: ")
if len(username) < 12 and username.isalpha == True and username.count(" ") == 0:
       print("Valid USERNAME!")
else:
       print("Invalid USERNAME!")
