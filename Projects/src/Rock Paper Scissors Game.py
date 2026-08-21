# What you learn:

# random
# input()
# if / elif / else
# while loop
# Functions
# Basic error handling


import random


def play_game():
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    print("🎮 ROCK PAPER SCISSORS GAME")
    print("----------------------------")

    while True:
        user = input("\nEnter rock, paper, scissors or quit: ").lower()

        if user == "quit":
            break

        if user not in choices:
            print("❌ Invalid choice! Try again.")
            continue

        computer = random.choice(choices)

        print("You chose:", user)
        print("Computer chose:", computer)

        if user == computer:
            print("🤝 It's a draw!")

        elif (
            (user == "rock" and computer == "scissors")
            or (user == "paper" and computer == "rock")
            or (user == "scissors" and computer == "paper")
        ):
            print("🎉 You win!")
            user_score += 1

        else:
            print("💻 Computer wins!")
            computer_score += 1

        print("Your Score:", user_score)
        print("Computer Score:", computer_score)

    print("\n🏆 FINAL SCORE")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("Thanks for playing!")


play_game()
  
