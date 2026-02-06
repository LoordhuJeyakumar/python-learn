# ----------------------------------
# Task 5.2: Code Refactoring (DRY)
# ----------------------------------

tasks = []


# ----------------------------------
# Helper functions
# ----------------------------------
def find_task_by_id(task_id):
    """Eliminate repeated find logic"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def validate_task_title(title):
    """Centralized validation"""
    if not title or len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters")
    return title.strip()


def format_task(task):
    """Consistent task display"""
    status = "✓" if task["completed"] else "○"
    return f"{status} [{task['id']:2}] {task['title']:<30} ({task['priority']})"


# ----------------------------------
# Core task operations
# ----------------------------------
def add_task(title, priority="medium"):
    title = validate_task_title(title)

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    return task


def mark_complete(task_id):
    task = find_task_by_id(task_id)
    if task:
        task["completed"] = True
        return True
    return False


def list_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(format_task(task))


# ----------------------------------
# Demo / Testing
# ----------------------------------
if __name__ == "__main__":
    add_task("Learn Python", "high")
    add_task("Build API")
    add_task("Write Docs", "low")

    print("\nAll Tasks:")
    list_tasks()

    print("\nCompleting task ID 2...\n")
    mark_complete(2)

    list_tasks()
