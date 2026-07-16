balance = 100


def show_balance():
    print("*" * 30)
    print(f"Your balance is: ${balance:.2f}")


def withdraw():
    global balance  # A function can''t edit global variables without this
    print("*" * 30)
    while True:
        amount = input("Enter the amount you want to withdraw: ")
        if not amount.isdigit():
            print("Enter a valid amount!")
        else:
            amount = int(amount)
            if amount > balance:
                print("*" * 30)
                print("You don't have enough balance!")
            else:
                balance -= amount
                print("*" * 30)
                print(f"${amount:.2f} has been successfully withdrawn!")
                break


def deposit():
    global balance
    print("*" * 30)
    while True:
        amount = input("Enter the amount you want to deposit: ")
        if not amount.isdigit():
            print("Enter a valid amount!")
        else:
            amount = int(amount)
            balance += amount
            print("*" * 30)
            print(f"${amount:.2f} has been successfully deposited!")
            break
def main():
    print("*" * 30)
    print("Banking Program")

    isrunning = True

    while isrunning:
        print("*" * 30)
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        print("*" * 30)
        choice = input("Enter your choice: ")
        if choice in ("1", "2", "3", "4"):
            choice = int(choice)
            match choice:
                case 1:
                    show_balance()
                case 2:
                    withdraw()
                case 3:
                    deposit()
                case 4:
                    print("*" * 30)
                    print("Thank you and have a nice day!")
                    print("*" * 30)
                    isrunning = False
        else:
            print("*" * 30)
            print("Enter a valid input!")

if __name__ == "__main__":
    main()
