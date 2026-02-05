import json
import os

# Global task list
tasks = []

# Load tasks (safe)
def load_tasks(filename="tasks.json"):
    global tasks

    if not os.path.exists(filename):
        print(f"No {filename} found, starting fresh")
        tasks = []
        return

    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print(f"✓ {len(tasks)} tasks loaded from {filename}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON file")
        tasks = []


# Save tasks
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)
    print(f"✓ {len(tasks)} tasks saved to {filename}")


# Helper function
def find_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# Add task
def add_task(title, priority="medium"):
    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks()   # Save after change
    return task


# Complete task
def complete_task(task_id):
    task = find_task_by_id(task_id)
    if task:
        task["completed"] = True
        save_tasks()   # Save after change
        print(f"Task {task_id} completed")
    else:
        print("Task not found")


# Show tasks
def list_tasks():
    if not tasks:
        print("No tasks available")
        return

    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f'{task["id"]}. {task["title"]} [{task["priority"]}] {status}')


# Program start
load_tasks()

# Sample usage
add_task("Learn Python", "high")
add_task("Practice File I/O")
list_tasks()
complete_task(1)
list_tasks()
