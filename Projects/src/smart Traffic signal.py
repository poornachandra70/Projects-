signal = input("Enter signal color: ")

if signal == "green":
    vehicle = input("Is a vehicle present? (yes/no): ")

    if vehicle == "yes":
        print("You can move carefully.")
    else:
        print("Road is clear.")
else:
    print("Stop the vehicle.")