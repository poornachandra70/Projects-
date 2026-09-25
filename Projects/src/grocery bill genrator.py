items = {
    "Rice": 60,
    "Milk": 30,
    "Bread": 40,
    "Eggs": 70
}

total = 0

print("----- Grocery Items -----")

for item, price in items.items():
    print(item, "₹", price)
    total = total + price

print("-------------------------")
print("Total Bill: ₹", total)