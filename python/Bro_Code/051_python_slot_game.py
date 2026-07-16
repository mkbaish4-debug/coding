# python slot game
import random

def spin():
    symbols = ["🍒", "🍋", "🍉", "⭐", "🔔"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*" * 30)
    print(" | ".join(row))

def result(row, bet):
    if row[0] == row[1] == row[2]:
        print("*" * 30)
        print("You won!")
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "⭐":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
    else:
        print("*" * 30)
        print("You lost!")
        return bet * 0


def main():
    balance = 100
    print("*" * 30)
    print("Welcome to slot mathine!")
    print("Symbols: 🍒 🍋 🍉 ⭐ 🔔")

    while True:
        print("*" * 30)
        print(f"Your balance is: ${balance:.2f}")
        print("*" * 30)
        bet = input("How much would you like to bet: ")
        if not bet.isdigit():
            print("Enter a valid unit!")
        else:
            bet = int(bet)
            if bet <= 0:
                print("Bet must be greater than zero!")
            else:
                if bet <= balance:
                    balance -= bet
                    row = spin()
                    print_row(row)
                    payout = result(row, bet)
                    balance += payout
                    if balance == 0:
                        print("*" * 30)
                        print("you ran out of balance! Game over.")
                        break
                else:
                    print("You don't have enough money!")

if __name__ == "__main__":
    main()
