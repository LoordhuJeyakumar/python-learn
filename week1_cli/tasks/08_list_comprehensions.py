# ----------------------------------
# Task 4.2: List & Dict Comprehensions
# ----------------------------------

# Sample task data
tasks = [
    {"id": 1, "title": "Learn Python", "priority": "high", "category": "learning"},
    {"id": 2, "title": "Build API", "priority": "medium", "category": "development"},
    {"id": 3, "title": "Write Docs", "priority": "low", "category": "documentation"},
    {"id": 4, "title": "Practice Python", "priority": "high", "category": "learning"},
]


# ----------------------------------
# 1. List comprehensions
# ----------------------------------

# Simple list comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# With transformation
titles = [t["title"].upper() for t in tasks]
print("Titles:", titles)


# ----------------------------------
# 2. Dictionary comprehensions
# ----------------------------------

# ID-indexed dictionary
tasks_by_id = {t["id"]: t for t in tasks}
print("\nTasks by ID:", tasks_by_id)

# Priority summary
priority_counts = {
    p: len([t for t in tasks if t["priority"] == p])
    for p in ["high", "medium", "low"]
}
print("Priority counts:", priority_counts)


# ----------------------------------
# 3. Set comprehension
# ----------------------------------

# Unique categories
categories = {t["category"] for t in tasks}
print("\nCategories:", categories)


# ----------------------------------
# 4. Generator expression
# ----------------------------------

# Memory-efficient high priority tasks
high_priority = (t for t in tasks if t["priority"] == "high")

print("\nHigh priority tasks:")
for task in high_priority:
    print(task["title"])
