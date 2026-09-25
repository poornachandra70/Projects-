correct_pin = "1234"

attempts = 3

while attempts > 0:

    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        break

    else:
        attempts -= 1
        print("Wrong PIN")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Account temporarily locked.")