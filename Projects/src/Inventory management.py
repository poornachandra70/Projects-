inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10
}

product = input("Enter product: ")
quantity = int(input("Enter quantity sold: "))

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("Sale successful")
        print("Remaining:", inventory[product])
    else:
        print("Not enough stock")
else:
    print("Product not found")