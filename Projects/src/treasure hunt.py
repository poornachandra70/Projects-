box = input("Choose a box (red/blue): ")

if box == "red":
    key = input("Do you have the key? (yes/no): ")

    if key == "yes":
        print("Congratulations! You found the treasure!")
    else:
        print("You need a key.")

else:
    print("This box is empty.")