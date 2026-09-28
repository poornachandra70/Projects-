class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:

    print("\n===== BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":

        account.show_balance()

    elif choice == "4":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")