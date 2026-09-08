a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    if a > 0:
        print("First number is smallest and positive")
    else:
        print("First number is smallest")
else:
    if b > 0:
        print("Second number is smallest and positive")
    else:
        print("Second number is smallest")