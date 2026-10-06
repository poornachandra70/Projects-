from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1000)