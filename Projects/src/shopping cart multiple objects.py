class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart")

    def total_price(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def display_cart(self):
        print("\nProducts in Cart:")

        for product in self.products:
            print(product.name, "-", product.price)

        print("Total:", self.total_price())


product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)
product3 = Product("Keyboard", 2000)

cart = ShoppingCart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.display_cart()