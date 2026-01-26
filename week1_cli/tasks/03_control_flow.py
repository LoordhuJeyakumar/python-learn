#1.Priority validator

def validate_priority(priority):
    """Validate and normalize priority"""
    priority = priority.lower()

    if priority in ["high", "medium", "low"]:
        return priority
    elif priority == "urgent":
        return "high"
    else:
        return "medium"
    
#2. Task status checker

def get_task_status(task):
    """Return readable status"""

    if task["completed"] and task["priority"] == "high":
        return "Completed (High Priority)"
    elif task["completed"]:
        return "Completed"
    elif task["priority"] == "high":
        return "High Priority"
    else:
        return "Pending"
    
#3. Comparison operator

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
    
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
    
# Nested if 

task = {
    "completed": False,
    "priority": "high",
    "due_days": 1
}

if not task["completed"]:
    if task["completed"] == "high" and task["due_days"] <= 1:
        print("Urgent task")
    else:
        print("Task is Pending") 