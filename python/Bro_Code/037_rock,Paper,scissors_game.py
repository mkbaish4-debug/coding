import random

options = ("rock", "paper", "scissors")
score = 0
isrunning = True

print("-" * 20 + "Guessing game" + "-" * 20)

while isrunning:
    your_choice = input("Choose between rock, paper, or scissors(q to quit): ").lower()
    computer_choice = random.choice(options)
    if your_choice in options:
        if your_choice == computer_choice:
            print("You tied! computer chose " + computer_choice)
        elif (
            (your_choice == "rock" and computer_choice == "scissors")
            or (your_choice == "paper" and computer_choice == "rock")
            or (your_choice == "scissors" and computer_choice == "paper")
        ):
            print("You won! computer chose " + computer_choice)
            score += 1
        else:
            print("You lost! computer chose " + computer_choice)
    elif your_choice == "q":
        print(f"Your final score is: {score}")
        isrunning = False
    else:
        print("Invalid input!")

print("-" * 40)
