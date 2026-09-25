questions = {
    "What is the capital of India?": "delhi",
    "Which language are we learning?": "python",
    "How many days are there in a week?": "7"
}

score = 0

for question, answer in questions.items():

    user_answer = input(question + " ").lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n----- Result -----")
print("Your score:", score, "/", len(questions))