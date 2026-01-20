# Week 1: Complete Task Breakdown - CLI Task Manager

## 📋 Overview
This document provides **complete, detailed tasks** for Week 1 covering all Python fundamentals. Each task includes acceptance criteria, learning objectives, and code examples.

---

## **DAY 1: Setup & Variables**

### Task 1.1: Environment Setup ✅
**Objective:** Create a professional Python development environment

**Steps:**
1. Create a project directory: `mkdir week1_cli && cd week1_cli`
2. Initialize Python virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Create `requirements.txt` with `pytest==8.0.0`
5. Install: `pip install -r requirements.txt`

**Acceptance Criteria:**
- [ ] Virtual environment created and activated
- [ ] `which python` shows path inside venv
- [ ] Can run `python --version`
- [ ] requirements.txt exists

**Concepts Covered:**
- Virtual environments (dependency isolation)
- pip package management
- Project structure

---

### Task 1.2: Variables & Data Types ✅
**Objective:** Master Python's primitive data types

**File:** `variable.py`

**Write code that:**
1. Creates variables of each type:
   - `name = "Python"` (string)
   - `age = 5` (integer)
   - `version = 3.11` (float)
   - `is_fun = True` (boolean)
   - `nothing = None` (null)

2. Uses f-strings to format output:
   ```python
   print(f"Python is {age} years old")
   print(f"Version: {version}")
   ```

3. Demonstrates type conversion:
   ```python
   str_number = "42"
   int_number = int(str_number)
   float_number = float(int_number)
   ```

4. Shows type checking:
   ```python
   print(type(name))
   print(isinstance(age, int))
   ```

**Acceptance Criteria:**
- [ ] All 5 data types created and printed
- [ ] F-string formatting used correctly
- [ ] Type conversions work without error
- [ ] `type()` and `isinstance()` demonstrated
- [ ] No hardcoded strings in calculations

**Concepts Covered:**
- int, float, str, bool, None types
- Type conversion & casting
- F-strings
- `type()` and `isinstance()` functions

---

### Task 1.3: Basic Task Manager Skeleton ✅
**Objective:** Create the foundation for the entire project

**File:** `task_manager.py`

**Write code that:**
1. Initializes an empty tasks list:
   ```python
   tasks = []
   ```

2. Creates an `add_task()` function with docstring:
   ```python
   def add_task(title, priority="medium"):
       """
       Add a new task to the tasks list.
       
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
   ```

3. Create a `list_tasks()` function:
   ```python
   def list_tasks():
       """Display all tasks"""
       if not tasks:
           print("No tasks yet!")
           return
       
       for task in tasks:
           status = "✓" if task["completed"] else "○"
           print(f"{status} [{task['id']}] {task['title']} ({task['priority']})")
   ```

4. Add a simple test:
   ```python
   if __name__ == "__main__":
       add_task("Learn Python", "high")
       add_task("Build a project", "medium")
       list_tasks()
   ```

**Acceptance Criteria:**
- [ ] Task structure includes: id, title, priority, completed
- [ ] `add_task()` has docstring
- [ ] `list_tasks()` displays tasks with formatting
- [ ] Running script prints tasks
- [ ] No errors when executed

**Concepts Covered:**
- Dictionaries (data structures)
- Lists (collections)
- Function definition with parameters & defaults
- Docstrings
- Main guard pattern

---

## **DAY 2: Control Flow**

### Task 2.1: If/Elif/Else Conditionals ✅
**Objective:** Master decision-making in code

**File:** `control_flow.py`

**Write code that:**
1. Creates a priority validator:
   ```python
   def validate_priority(priority):
       """Validate and normalize priority"""
       priority = priority.lower()
       if priority in ["high", "medium", "low"]:
           return priority
       elif priority == "urgent":
           return "high"
       else:
           return "medium"
   ```

2. Creates a task status checker:
   ```python
   def get_task_status(task):
       """Return readable status"""
       if task["completed"]:
           return "✓ Completed"
       elif task["priority"] == "high":
           return "⚠ High Priority"
       else:
           return "○ Pending"
   ```

3. Implements comparison operators:
   ```python
   age = 25
   if age >= 18:
       print("Adult")
   
   score = 75
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   elif score >= 70:
       print("C")
   else:
       print("F")
   ```

**Acceptance Criteria:**
- [ ] Uses if/elif/else structure
- [ ] Comparison operators: ==, !=, <, >, <=, >=
- [ ] Logical operators: and, or, not
- [ ] Nested if statements
- [ ] No syntax errors

**Concepts Covered:**
- if/elif/else statements
- Comparison operators
- Logical operators
- Nested conditions

---

### Task 2.2: While Loops & Menu System ✅
**Objective:** Create interactive menu that repeats until exit

**File:** `environment_cli.py` (or add to task_manager.py)

**Write code that:**
1. Creates a persistent menu:
   ```python
   def show_menu():
       print("\n=== Task Manager ===")
       print("1. Add Task")
       print("2. List Tasks")
       print("3. Complete Task")
       print("4. Exit")
       return input("Choose option: ")
   
   def run_app():
       while True:
           choice = show_menu()
           
           if choice == "1":
               title = input("Task title: ")
               add_task(title)
               print("✓ Task added!")
           
           elif choice == "2":
               list_tasks()
           
           elif choice == "3":
               task_id = int(input("Task ID: "))
               complete_task(task_id)
           
           elif choice == "4":
               print("Goodbye!")
               break
           
           else:
               print("Invalid option")
   ```

2. Implements input validation:
   ```python
   def get_valid_choice(options):
       while True:
           choice = input(f"Choose {options}: ")
           if choice in options:
               return choice
           print("Invalid choice!")
   ```

3. Demonstrates break/continue:
   ```python
   count = 0
   while count < 5:
       if count == 2:
           count += 1
           continue
       print(count)
       count += 1
   ```

**Acceptance Criteria:**
- [ ] Menu displays after each action
- [ ] While loop exits cleanly
- [ ] Input validation works
- [ ] break and continue are used
- [ ] No infinite loops

**Concepts Covered:**
- while loops
- break and continue statements
- Input validation
- Menu-driven applications

---

## **DAY 3: Lists & Loops**

### Task 3.1: For Loops & Iteration ✅
**Objective:** Master iteration patterns

**File:** `loops.py`

**Write code that:**
1. Iterates with for loops:
   ```python
   tasks = ["Learn Python", "Build API", "Deploy"]
   
   # Simple iteration
   for task in tasks:
       print(f"- {task}")
   
   # With index using enumerate()
   for index, task in enumerate(tasks, 1):
       print(f"{index}. {task}")
   
   # Range iteration
   for i in range(1, 6):
       print(f"Task {i}")
   ```

2. Demonstrates nested loops:
   ```python
   priorities = ["high", "medium", "low"]
   days = ["Mon", "Tue", "Wed"]
   
   for day in days:
       for priority in priorities:
           print(f"{day}: {priority}")
   ```

3. Uses list methods:
   ```python
   tasks = []
   tasks.append("Task 1")  # Add
   tasks.extend(["Task 2", "Task 3"])  # Add multiple
   tasks.insert(0, "Priority Task")  # Insert at index
   tasks.remove("Task 1")  # Remove by value
   tasks.pop()  # Remove last
   tasks.sort()  # Sort
   tasks.clear()  # Clear all
   ```

4. Implements task deletion:
   ```python
   def delete_task(task_id):
       global tasks
       tasks = [t for t in tasks if t["id"] != task_id]
   ```

**Acceptance Criteria:**
- [ ] for loops iterate correctly
- [ ] enumerate() used with index
- [ ] range() used for numeric loops
- [ ] Nested loops work
- [ ] List methods: append, extend, insert, remove, pop, sort, clear
- [ ] No index errors

**Concepts Covered:**
- for loops
- enumerate() function
- range() function
- List methods
- Nested loops
- List iteration patterns

---

### Task 3.2: List Operations & Complete Task ✅
**Objective:** Implement task completion functionality

**File:** `data_structure.py`

**Write code that:**
1. Creates a complete_task function:
   ```python
   def complete_task(task_id):
       """Mark task as complete"""
       for task in tasks:
           if task["id"] == task_id:
               task["completed"] = True
               return True
       return False
   ```

2. Finds tasks by filtering:
   ```python
   def get_incomplete_tasks():
       """Filter incomplete tasks"""
       return [t for t in tasks if not t["completed"]]
   
   def get_high_priority_tasks():
       """Filter high priority tasks"""
       return [t for t in tasks if t["priority"] == "high"]
   ```

3. Demonstrates slicing:
   ```python
   first_three = tasks[:3]
   last_two = tasks[-2:]
   reversed_tasks = tasks[::-1]
   ```

**Acceptance Criteria:**
- [ ] complete_task() marks task as done
- [ ] Filter functions return correct subset
- [ ] Slicing operations work correctly
- [ ] No IndexError when empty
- [ ] Task IDs remain unique

**Concepts Covered:**
- List searching
- List filtering
- List slicing
- Modifying list items

---

## **DAY 4: Dictionaries & Data Structures**

### Task 4.1: Dictionary Operations ✅
**Objective:** Master complex data structures

**File:** `data_structure.py`

**Write code that:**
1. Creates nested data structures:
   ```python
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
   ```

2. Accesses and modifies:
   ```python
   print(task["title"])
   print(task.get("category", "uncategorized"))
   
   task["priority"] = "medium"
   task["status"] = "in_progress"
   
   for key, value in task.items():
       print(f"{key}: {value}")
   
   keys = task.keys()
   values = task.values()
   ```

3. Implements task filtering by category:
   ```python
   def filter_by_category(category):
       return [t for t in tasks if t.get("category") == category]
   
   def count_by_priority():
       counts = {"high": 0, "medium": 0, "low": 0}
       for task in tasks:
           counts[task["priority"]] += 1
       return counts
   ```

**Acceptance Criteria:**
- [ ] Nested dictionaries created
- [ ] `.get()` used with defaults
- [ ] `.items()`, `.keys()`, `.values()` demonstrated
- [ ] Dictionary iteration works
- [ ] Filtering by category/priority works
- [ ] Count aggregation works

**Concepts Covered:**
- Dictionary creation & access
- Nested data structures
- Dictionary methods: keys(), values(), items(), get()
- Dictionary iteration
- Aggregation patterns

---

### Task 4.2: List & Dict Comprehensions ✅
**Objective:** Write concise data transformations

**File:** `list_comprehensions.py`

**Write code that:**
1. Creates list comprehensions:
   ```python
   # Simple list comprehension
   squares = [x**2 for x in range(1, 6)]
   # [1, 4, 9, 16, 25]
   
   # With condition
   evens = [x for x in range(10) if x % 2 == 0]
   # [0, 2, 4, 6, 8]
   
   # With transformation
   titles = [t["title"].upper() for t in tasks]
   ```

2. Creates dict comprehensions:
   ```python
   # Convert to ID-indexed dictionary
   tasks_by_id = {t["id"]: t for t in tasks}
   
   # Create summary
   priority_counts = {
       p: len([t for t in tasks if t["priority"] == p])
       for p in ["high", "medium", "low"]
   }
   ```

3. Uses set comprehensions:
   ```python
   # Get unique categories
   categories = {t["category"] for t in tasks}
   ```

4. Demonstrates generator expressions:
   ```python
   # Memory-efficient iteration
   high_priority = (t for t in tasks if t["priority"] == "high")
   for task in high_priority:
       print(task["title"])
   ```

**Acceptance Criteria:**
- [ ] List comprehensions with and without conditions
- [ ] Dict comprehensions working correctly
- [ ] Set comprehensions for unique values
- [ ] Generator expressions created
- [ ] All produce correct results

**Concepts Covered:**
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions
- Conditional filtering in comprehensions

---

## **DAY 5: Functions & Code Organization**

### Task 5.1: Function Definition & Scope ✅
**Objective:** Write reusable, well-documented functions

**File:** `functions.py`

**Write code that:**
1. Creates functions with parameters & defaults:
   ```python
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
   ```

2. Uses *args and **kwargs:
   ```python
   def log_action(*args, **kwargs):
       """Log any action with flexible arguments"""
       print(f"Action: {args}")
       print(f"Metadata: {kwargs}")
   
   log_action("task_added", "Learn Python", priority="high", user="john")
   ```

3. Implements function composition:
   ```python
   def find_task_by_id(task_id):
       """Find task by ID (helper function)"""
       for task in tasks:
           if task["id"] == task_id:
               return task
       return None
   
   def complete_task(task_id):
       """Use helper to find then complete"""
       task = find_task_by_id(task_id)
       if task:
           task["completed"] = True
           return True
       return False
   ```

4. Demonstrates function returns:
   ```python
   def validate_input(prompt, valid_options):
       """Keep asking until valid input"""
       while True:
           choice = input(prompt)
           if choice in valid_options:
               return choice
           print("Invalid choice!")
   ```

**Acceptance Criteria:**
- [ ] Functions have comprehensive docstrings
- [ ] Parameters include type hints in docstrings
- [ ] Default parameters work correctly
- [ ] *args and **kwargs used appropriately
- [ ] Functions are DRY (Don't Repeat Yourself)
- [ ] Proper return types

**Concepts Covered:**
- Function definition syntax
- Parameters & arguments
- Default parameters
- *args and **kwargs
- Return statements
- Docstrings
- Variable scope (local vs global)
- Function composition

---

### Task 5.2: Code Refactoring ✅
**Objective:** DRY principle - eliminate duplicate code

**File:** `task_manager.py` (refactor)

**Refactor to:**
1. Extract repeated logic into helpers:
   ```python
   def find_task_by_id(task_id):
       """Eliminate repeated find logic"""
       for task in tasks:
           if task["id"] == task_id:
               return task
       return None
   
   # Now use everywhere instead of repeating the loop
   def mark_complete(task_id):
       task = find_task_by_id(task_id)
       if task:
           task["completed"] = True
   ```

2. Create validation function:
   ```python
   def validate_task_title(title):
       """Centralized validation"""
       if not title or len(title) < 3:
           raise ValueError("Title must be at least 3 characters")
       return title.strip()
   ```

3. Create consistent formatting:
   ```python
   def format_task(task):
       """Consistent task display"""
       status = "✓" if task["completed"] else "○"
       return f"{status} [{task['id']:2}] {task['title']:<30} ({task['priority']})"
   ```

**Acceptance Criteria:**
- [ ] No repeated code blocks
- [ ] Helper functions created
- [ ] Validation centralized
- [ ] Formatting consistent
- [ ] All functions have clear purpose
- [ ] Code is more readable

**Concepts Covered:**
- DRY principle
- Code organization
- Helper functions
- Refactoring patterns

---

## **DAY 6-7: File I/O & Persistence**

### Task 6.1: File Handling Basics ✅
**Objective:** Learn to read and write files

**File:** `file_handling.py`

**Write code that:**
1. Creates basic file operations:
   ```python
   # Write to file
   with open("notes.txt", "w") as file:
       file.write("Task Manager Notes\n")
       file.write("==================\n")
   
   # Append to file
   with open("notes.txt", "a") as file:
       file.write("New note added\n")
   
   # Read from file
   with open("notes.txt", "r") as file:
       content = file.read()
       print(content)
   
   # Read line by line
   with open("notes.txt", "r") as file:
       for line in file:
           print(line.strip())
   ```

2. Demonstrates context managers:
   ```python
   # Why 'with' is better:
   # BAD:
   file = open("data.txt", "r")
   content = file.read()
   file.close()  # Might not run if error occurs
   
   # GOOD:
   with open("data.txt", "r") as file:
       content = file.read()  # Always closes, even if error
   ```

3. Implements file existence checking:
   ```python
   import os
   
   if os.path.exists("tasks.json"):
       print("File exists")
   else:
       print("File not found")
   
   file_size = os.path.getsize("tasks.json")
   ```

**Acceptance Criteria:**
- [ ] Read files successfully
- [ ] Write files successfully
- [ ] Append to files works
- [ ] Context manager (with) used
- [ ] File existence checked
- [ ] No file handle leaks

**Concepts Covered:**
- File modes: r, w, a, r+
- Reading: read(), readline(), readlines()
- Writing: write(), writelines()
- Context managers (with statement)
- File operations with os module

---

### Task 6.2: JSON Persistence ✅
**Objective:** Save and load tasks from JSON file

**File:** `task_manager.py` (add persistence)

**Write code that:**
1. Creates JSON save function:
   ```python
   import json
   
   def save_tasks(filename="tasks.json"):
       """Save tasks to JSON file"""
       with open(filename, "w") as file:
           json.dump(tasks, file, indent=2)
       print(f"✓ {len(tasks)} tasks saved to {filename}")
   
   def load_tasks(filename="tasks.json"):
       """Load tasks from JSON file"""
       global tasks
       
       if not os.path.exists(filename):
           print(f"No {filename} found, starting fresh")
           return
       
       with open(filename, "r") as file:
           tasks = json.load(file)
       print(f"✓ {len(tasks)} tasks loaded from {filename}")
   ```

2. Integrates save on every change:
   ```python
   def add_task(title, priority="medium"):
       task = {
           "id": max([t["id"] for t in tasks], default=0) + 1,
           "title": title,
           "priority": priority,
           "completed": False
       }
       tasks.append(task)
       save_tasks()  # Save after change
       return task
   
   def complete_task(task_id):
       task = find_task_by_id(task_id)
       if task:
           task["completed"] = True
           save_tasks()  # Save after change
   ```

3. Implements error handling:
   ```python
   def load_tasks_safe(filename="tasks.json"):
       """Safely load with error handling"""
       try:
           with open(filename, "r") as file:
               return json.load(file)
       except FileNotFoundError:
           return []
       except json.JSONDecodeError:
           print("Error: Invalid JSON file")
           return []
   ```

**Acceptance Criteria:**
- [ ] Tasks save to JSON file
- [ ] Tasks load from JSON on startup
- [ ] File formatted with indentation (readable)
- [ ] Changes persist between runs
- [ ] Error handling for missing/corrupted files
- [ ] IDs remain unique after save/load

**Concepts Covered:**
- json.dump() and json.load()
- File formatting (indent parameter)
- Error handling with try/except
- File existence checking
- Data persistence

---

### Task 6.3: Complete Task Manager Application ✅
**Objective:** Integrate all concepts into working application

**File:** `complete_task_manager.py`

**Implement:**
1. Full menu system with all operations
2. Persistence (save/load)
3. Data validation
4. Error handling
5. User-friendly display

**Sample Menu Flow:**
```
=== Task Manager ===
1. Add Task
2. List All Tasks
3. List High Priority
4. Complete Task
5. Delete Task
6. Export Stats
7. Exit

Choose option (1-7): 
```

**Acceptance Criteria:**
- [ ] Add task (with priority)
- [ ] List all tasks
- [ ] Filter by priority
- [ ] Mark task complete
- [ ] Delete task
- [ ] Display statistics (total, completed, by priority)
- [ ] Save on exit
- [ ] Load on startup
- [ ] Handle invalid input gracefully
- [ ] Clear, formatted output

**Concepts Covered:**
- Integration of all Week 1 concepts
- Full CLI application
- Data persistence
- Error handling
- User input validation

---

## **Summary: What Students Will Learn**

By completing all these tasks, students will be able to:

✅ Set up professional Python development environments
✅ Work with all basic data types (int, float, str, bool, None)
✅ Use control flow (if/elif/else, while, for)
✅ Manipulate lists and dictionaries
✅ Write and organize functions with docstrings
✅ Handle files and persist data with JSON
✅ Build a complete, interactive CLI application
✅ Think in terms of reusable, DRY code
✅ Handle errors gracefully

---

## **Testing Checklist**

Each task should be tested by:
- [ ] Running without errors
- [ ] Producing correct output
- [ ] Handling edge cases (empty input, invalid choices)
- [ ] Persisting data correctly
- [ ] Following PEP 8 style guidelines

---

## **Next Steps**

Once Week 1 is complete, students should feel confident enough to:
- Understand the Week 1 CLI Task Manager code
- Modify and extend it
- Build similar CLI applications
- Begin Week 2 (OOP refactoring)
