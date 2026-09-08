num = 1

while num != 0:
    num = int(input("Enter a number (0 to stop): "))

    if num > 0:
        if num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")

    elif num < 0:
        if num % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")

    else:
        print("Program ended")