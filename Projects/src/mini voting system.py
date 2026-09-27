candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

for i in range(5):

    print("\nCandidates: A, B, C")

    vote = input("Enter your vote: ").upper()

    if vote in candidates:
        candidates[vote] += 1
        print("Vote recorded")
    else:
        print("Invalid vote")

print("\nVoting Results")

for candidate, votes in candidates.items():
    print(candidate, ":", votes)