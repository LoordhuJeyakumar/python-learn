import json
import os

FILENAME = "tasks.json"
tasks = []

# Load & Save
def load_tasks():
    global tasks
    if not os.path.exists(FILENAME):
        tasks = []
        return
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("Corrupted JSON file. Starting fresh.")
        tasks = []


def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=2)


# Helpers
def generate_id():
    return max([t["id"] for t in tasks], default=0) + 1


def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def input_priority():
    priority = input("Enter priority (low / medium / high): ").lower()
    if priority not in ["low", "medium", "high"]:
        print("Invalid priority. Defaulting to medium.")
        return "medium"
    return priority


# Operations
def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty")
        return

    task = {
        "id": generate_id(),
        "title": title,
        "priority": input_priority(),
        "completed": False
    }
    tasks.append(task)
    save_tasks()
    print("Task added")


def list_tasks(filter_priority=None):
    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        if filter_priority and task["priority"] != filter_priority:
            continue

        status = "true" if task["completed"] else "false"
        print(
            f'{task["id"]}. {task["title"]} '
            f'[{task["priority"]}] {status}'
        )


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid ID")
        return

    task = find_task(task_id)
    if not task:
        print("Task not found")
        return

    task["completed"] = True
    save_tasks()
    print("Task marked as completed")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return

    task = find_task(task_id)
    if not task:
        print("Task not found")
        return

    tasks.remove(task)
    save_tasks()
    print("Task deleted")


def export_stats():
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    high = len([t for t in tasks if t["priority"] == "high"])
    medium = len([t for t in tasks if t["priority"] == "medium"])
    low = len([t for t in tasks if t["priority"] == "low"])

    print("\n=== TASK STATS ===")
    print("Total tasks     :", total)
    print("Completed tasks :", completed)
    print("High priority   :", high)
    print("Medium priority :", medium)
    print("Low priority    :", low)


# Menu
def show_menu():
    print("""
=== Task Manager ===
1. Add Task
2. List All Tasks
3. List High Priority
4. Complete Task
5. Delete Task
6. Export Stats
7. Exit
""")


# Main Loop
def main():
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose option (1-7): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks("high")
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            export_stats()
        elif choice == "7":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
