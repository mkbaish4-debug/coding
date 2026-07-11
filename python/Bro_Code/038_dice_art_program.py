# dice art program

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {1 : ("┌─────────┐",
                 "│         │",
                 "│    ●    │",
                 "│         │",
                 "└─────────┘"),
            2:  ("┌─────────┐",
                 "│  ●      │",
                 "│         │",
                 "│      ●  │",
                 "└─────────┘"),
            3 : ("┌─────────┐",
                 "│ ●       │",
                 "│    ●    │",
                 "│       ● │",
                 "└─────────┘"),
            4 : ("┌─────────┐",
                 "│ ●     ● │",
                 "│         │",
                 "│ ●     ● │",
                 "└─────────┘"),
            5 : ("┌─────────┐",
                 "│ ●     ● │",
                 "│    ●    │",
                 "│ ●     ● │",
                 "└─────────┘"),
            6 : ("┌─────────┐",
                 "│ ●     ● │",
                 "│ ●     ● │",
                 "│ ●     ● │",
                 "└─────────┘")}

import random
total = 0
dice = []
num_of_dice = input("How many dice?: ")
if num_of_dice.isdigit():
    num_of_dice = int(num_of_dice)
    for die in range(num_of_dice):
        rand_die = random.randint(1, 6)
        dice.append(rand_die)
        total += dice[die]
#         for line in range(len(dice_art.get(rand_die))):
#           print(dice_art.get(rand_die)[line])

    for line in range(5):
        for die in dice:
          print(dice_art.get(die)[line], end = "  ")
        print()
    print(total)
else:
    print("Invalid input!")





























