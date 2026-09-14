food = input("Enter food: ")

if food == "pizza":
    size = input("Enter size (small/large): ")

    if size == "large":
        print("Large pizza ordered - ₹300")
    else:
        print("Small pizza ordered - ₹200")
else:
    print("Food is not available.")