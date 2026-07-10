import random
low_num = 1
high_num = 100
randnum = random.randint(low_num, high_num)
guess = 0
tries = 0

print("-"*10 + "Guessing game" + "-"*10)

while guess != randnum:
    guess = (input(f"Guess a number between {low_num}-{high_num}: "))
    if guess.isdigit():
        tries += 1
        guess = int(guess)
        if guess < randnum:
            print("Too low! Try again...")
        elif guess > randnum:
            print("Too high! Try again...")
        else:
            print("Correct! You guessed the number.")
            print(f"You took {tries} tries to guess the number.")
            print("-"*33)
    else:
        print("Invalid input!")

