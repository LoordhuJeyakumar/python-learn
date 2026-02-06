# ----------------------------------
# Task 4.1: Dictionary Operations
# ----------------------------------

# 1. Nested dictionary (single task)
task = {
    "id": 1,
    "title": "Learn Python",
    "priority": "high",
    "category": "learning",
    "tags": ["python", "basics"],
    "metadata": {
        "created_at": "2025-01-12",
        "updated_at": "2025-01-13",
        "duration_hours": 8
    }
}

# ----------------------------------
# 2. Accessing and modifying dictionary
# ----------------------------------
print("Title:", task["title"])
print("Category:", task.get("category", "uncategorized"))

# Modify values
task["priority"] = "medium"
task["status"] = "in_progress"

print("\nTask details (items):")
for key, value in task.items():
    print(f"{key}: {value}")

keys = task.keys()
values = task.values()

print("\nKeys:", keys)
print("Values:", values)


# ----------------------------------
# 3. Multiple tasks for filtering
# ----------------------------------
tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "priority": "high",
        "category": "learning"
    },
    {
        "id": 2,
        "title": "Build API",
        "priority": "medium",
        "category": "development"
    },
    {
        "id": 3,
        "title": "Write Docs",
        "priority": "low",
        "category": "documentation"
    },
    {
        "id": 4,
        "title": "Practice Python",
        "priority": "high",
        "category": "learning"
    }
]


# ----------------------------------
# Filter & aggregation functions
# ----------------------------------
def filter_by_category(category):
    return [t for t in tasks if t.get("category") == category]


def count_by_priority():
    counts = {"high": 0, "medium": 0, "low": 0}
    for task in tasks:
        counts[task["priority"]] += 1
    return counts


# ----------------------------------
# Demo Output
# ----------------------------------
if __name__ == "__main__":
    print("\nLearning category tasks:")
    print(filter_by_category("learning"))

    print("\nTask count by priority:")
    print(count_by_priority())
