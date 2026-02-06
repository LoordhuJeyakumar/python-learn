#-------------------------------
# Task 3.1: For Loop & iteration
#-------------------------------

# 1. Iterating with a for loop

tasks = ["Learn Python", "Build API", "Deploy"]

print("Simple iteration:")
for task in tasks:
    print(f"- {task}")

print("\nIteration with index (enumerate):")
for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")
    
print("\nIteration with range:")
for i in range(1, 6):
    print(f"Task {i}")
    
#-------------------------------
# 2. Nested Loops
#-------------------------------

priorites = ["high", "medium", "low"]
days = ["Monday", "Tuesday", "Wednesday"]

print("\nNested loops Output:")
for day in days:
    for priority in priorites:
        print(f"{day} task on {priority}")
        
#-------------------------------
# 3. List Methods Demo
#-------------------------------

tasks_list = []

print("\nList methods demo:")

tasks_list.append("Task 1")
tasks_list.extend(["Task 2", "Task 3"])
tasks_list.insert(0, "Priority Task")

print("After add:", tasks_list)

tasks_list.remove("Task 1")
tasks_list.pop()

print("After remove:", tasks_list)

tasks_list.sort()
print("After sort:", tasks_list)

tasks_list.clear()
print("After clear:", tasks_list)

#-------------------------------
# 4. Task deletion using for loops + list comprehension
#-------------------------------

tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Build API"},
    {"id": 3, "title": "Deploy"}
]

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    
print("\nBefore delete:", tasks)
delete_task(2)
print("After delete:", tasks)