numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
    if number % 2 != 0:
        continue

    print(number, "is Even")