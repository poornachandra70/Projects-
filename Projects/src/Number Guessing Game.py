# Computer randomly selects a number
# User tries to guess it
# Shows whether the guess is too high or too low
# Counts the number of attempts
# Simple beginner-level Python

import random


def guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations! You guessed the number.")
            print("Number of attempts:", attempts)
            break


guessing_game()