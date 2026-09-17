age = int(input("What is your age?: "))
if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up! ")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")

# order of if statements are imp
# first one will always be executed first if true
# exclude the conditions you don't want to happen first
# use "==" for comparision
