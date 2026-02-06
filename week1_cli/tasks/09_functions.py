# ----------------------------------
# Task 5.1: Function Definition & Scope
# ----------------------------------

# Global task list
tasks = []


# ----------------------------------
# 1. Function with parameters & defaults
# ----------------------------------
def add_task(title, priority="medium", category="general"):
    """
    Add a new task to the list.

    Args:
        title (str): Task title, required
        priority (str): Task priority (low/medium/high), default "medium"
        category (str): Task category, default "general"

    Returns:
        dict: The newly created task

    Raises:
        ValueError: If title is empty
    """
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "priority": priority,
        "category": category,
        "completed": False
    }

    tasks.append(task)
    return task


# ----------------------------------
# 2. *args and **kwargs
# --------------------------------
def log_action(*args, **kwargs):
    """
    Log any action with flexible arguments.

    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments
    """
    print(f"Action: {args}")
    print(f"Metadata: {kwargs}")


# ----------------------------------
# 3. Function composition (helper functions)
# ----------------------------------
def find_task_by_id(task_id):
    """
    Find a task by its ID.

    Args:
        task_id (int): Task identifier

    Returns:
        dict | None: Task if found, else None
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(task_id):
    """
    Mark a task as completed.

    Args:
        task_id (int): Task identifier

    Returns:
        bool: True if completed, False if not found
    """
    task = find_task_by_id(task_id)
    if task:
        task["completed"] = True
        return True
    return False


# ----------------------------------
# 4. Function with return value
# ----------------------------------
def validate_input(prompt, valid_options):
    """
    Keep asking user until a valid option is entered.

    Args:
        prompt (str): Input prompt
        valid_options (list): Allowed choices

    Returns:
        str: Valid user input
    """
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        print("Invalid choice!")


# ----------------------------------
# Demo / Testing
# ----------------------------------
if __name__ == "__main__":
    # Add tasks
    add_task("Learn Python", priority="high", category="learning")
    add_task("Build API")

    # Log action
    log_action("task_added", "Learn Python", priority="high", user="john")

    # Complete task
    complete_task(1)

    # Validate input demo
    # choice = validate_input("Choose (y/n): ", ["y", "n"])
    # print("You chose:", choice)

    print("\nFinal task list:")
    print(tasks)
