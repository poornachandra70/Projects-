class Bank:

    def __init__(self, balance):
        # Private variable
        self.__balance = balance

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


bank = Bank(10000)

bank.deposit(5000)

print("Balance:", bank.get_balance())