import os
import json

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index}. {task['title']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    title = input("Enter the task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!\n")
    else:
        print("Task title cannot be empty.\n")

# Mark task as done or undone
def mark_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to toggle status: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = not tasks[choice - 1]["completed"]
            print("Task status updated.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Task '{removed_task['title']}' removed successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Display menu
def display_menu():
    print("==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done/Undone")
    print("4. Remove Task")
    print("5. Exit")
    print("=========================")

# Main program
def main():
    print("Welcome to the To-Do List Application!\n")
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nThank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
