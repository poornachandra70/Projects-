while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Sum =", a + b)

    choice = input("Continue? (y/n): ")

    if choice == "n":
        break