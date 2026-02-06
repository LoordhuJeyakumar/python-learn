#-------------------------------
# Task 3.2: List Operations & Complete Task 
#-------------------------------

# Task Storage

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False, "priority": "high"},
    {"id": 2, "title": "Build API", "completed": False, "priority": "medium"},
    {"id": 3, "title": "Deploy APP", "completed": False, "priority": "high"},
    {"id": 4, "title": "Write Docs", "completed": True, "priority": "low"}
]

#-------------------------------
# 1. Complete Task Function
#-------------------------------

def complete_task(task_id):
    """Mark task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
        return False

#-------------------------------
# 2. Filter Function
#-------------------------------

def incomplete_tasks():
    """Filter incomplete tasks."""
    return [t for t in tasks if not t["completed"]]

def get_high_priority_tasks():
    """Filter high priority tasks."""
    return [t for t in tasks if t["priority"] == "high"]

#-------------------------------
# 3. List Slicing demo
#-------------------------------

first_three_tasks = tasks[:3]
last_two_tasks = tasks[-2:]
reversed_tasks = tasks[::-1]

#-------------------------------
# 4. Demo Outputs
#-------------------------------

if __name__ == "__main__":
    print("Before completion:")
    print(tasks)

    print("\nCompleting Task with ID = 2")
    complete_task(2)

    print("After completion:")
    print(tasks)
    
    print("\nIncomplete Tasks:")
    print(incomplete_tasks())

    print("\nHigh Priority Tasks:")
    print(get_high_priority_tasks())

    print("\nSlicing examples:")
    print("First three tasks:", first_three_tasks)
    print("Last two tasks:", last_two_tasks)
    print("Reversed tasks:", reversed_tasks)