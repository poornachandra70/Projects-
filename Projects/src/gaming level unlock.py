level = int(input("Enter your level: "))
score = int(input("Enter your score: "))

if level >= 10:
    if score >= 500:
        print("New level unlocked!")
    else:
        print("You need more score.")
else:
    print("Reach level 10 first.")