import json

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):

    title = input("Enter task: ")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("✅ Task added successfully!")


# Display all tasks
def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✅ Completed"
        else:
            status = "⏳ Pending"

        print(f"{index}. {task['title']} - {status}")


# Mark task as completed
def complete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            save_tasks(tasks)

            print("✅ Task marked as completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


# Delete a task
def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):

            removed_task = tasks.pop(number - 1)

            save_tasks(tasks)

            print("🗑️ Deleted:", removed_task["title"])

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a number.")


# Main program
def main():

    tasks = load_tasks()

    while True:

        print("\n======================")
        print("       TO-DO APP")
        print("======================")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using To-Do App! 👋")
            break

        else:
            print("❌ Invalid choice.")


# Start application
main()