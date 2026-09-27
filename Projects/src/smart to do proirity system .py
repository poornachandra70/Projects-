tasks = []

while True:

    task = input("Enter task: ")

    if task.lower() == "done":
        break

    priority = input("Priority (high/medium/low): ")

    tasks.append((priority, task))

print("\nYour Tasks:")

order = {"high": 1, "medium": 2, "low": 3}

tasks.sort(key=lambda x: order[x[0]])

for priority, task in tasks:
    print(priority.upper(), "->", task)