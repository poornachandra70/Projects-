time = int(input("Enter hour: "))

if time < 12 or time >= 18:
    print("Morning or evening")
else:
    print("Afternoon")