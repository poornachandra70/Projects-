# This is a simple console project where you can check balance, deposit money, withdraw money, and exit.

# Python concepts practiced:
# while loop
# if / elif / else
# break, Functions, User input, Variables

balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money deposited successfully!")
            print("New balance: ₹", balance)
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")