# 1. Initialize an empty task list

tasks = []


def add_task(title, priority="medium"):
    """
    Add a new task to the task list.

    Args:
        title (str): Task title
        priority (str): Task priority (low/medium/high)

    Returns:
        dict: The newly created task
    """
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    return task


def list_tasks():
    """Display all tasks"""
    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"{status} [{task['id']}] {task['title']} ({task['priority']})")


# 4. Simple test (main guard)

if __name__ == "__main__":
    add_task("Learn Python", "high")
    add_task("Build a project", "medium")
    list_tasks()
