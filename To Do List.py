import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file or initialize empty list
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {status}")

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (low, medium, high): ").lower()
    tasks.append({"description": description, "due_date": due_date, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    task_num = int(input("Enter task number to mark as complete: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number!")

# Edit a task
def edit_task(tasks):
    task_num = int(input("Enter task number to edit: "))
    if 0 < task_num <= len(tasks):
        task = tasks[task_num - 1]
        task["description"] = input(f"Enter new description (current: {task['description']}): ") or task["description"]
        task["due_date"] = input(f"Enter new due date (current: {task['due_date']}): ") or task["due_date"]
        task["priority"] = input(f"Enter new priority (current: {task['priority']}): ").lower() or task["priority"]
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

# Main menu for the To-Do list
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
