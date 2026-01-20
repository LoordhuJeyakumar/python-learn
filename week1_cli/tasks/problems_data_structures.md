# TOPIC 4: DATA STRUCTURES
## Questions & Problem Statements

### Problem 4.1: List Operations Master
**Question:** Create a program that demonstrates comprehensive list operations.

**Requirements:**
- Start with empty list and perform operations:
  - Add items using append(), extend(), insert()
  - Remove items using remove(), pop(), clear()
  - Sort and reverse the list
  - Find index of items, count occurrences
  - Slice the list (first 3, last 2, every other item)
- Test with numbers: [3, 1, 4, 1, 5, 9, 2, 6]

**Operations to Implement:**
- [ ] append(8) → [3, 1, 4, 1, 5, 9, 2, 6, 8]
- [ ] insert(0, 0) → [0, 3, 1, 4, 1, 5, 9, 2, 6, 8]
- [ ] remove(1) → [0, 3, 4, 1, 5, 9, 2, 6, 8] (removes first 1)
- [ ] pop() → [0, 3, 4, 1, 5, 9, 2, 6] (removes last item)
- [ ] sort() → [0, 1, 2, 3, 4, 5, 6, 9]
- [ ] slice [2:5] → [2, 3, 4]

---

### Problem 4.2: Student Grade Book (Lists)
**Question:** Create a student grade book using lists to store and analyze data.

**Requirements:**
- Store student names and their grades in parallel lists
- Calculate: average, highest, lowest grade
- Find students with grades above average
- Sort students by grade (highest to lowest)
- Create grade distribution (A:90+, B:80-89, etc.)

**Test Data:**
```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
grades = [85, 92, 78, 96, 88]
```

**Required Calculations:**
- [ ] Average grade: 87.8
- [ ] Highest: Diana (96), Lowest: Charlie (78)
- [ ] Above average: Alice, Bob, Diana, Eve
- [ ] Sorted: Diana(96), Bob(92), Eve(88), Alice(85), Charlie(78)

---

### Problem 4.3: Dictionary Contact Book
**Question:** Create a contact book application using dictionaries.

**Requirements:**
- Store contacts as dictionaries: {"name", "phone", "email", "city"}
- Add at least 5 contacts
- Search contacts by name (case-insensitive)
- Update contact information
- Display all contacts in formatted table
- Remove contacts by name

**Contact Data Structure:**
```python
contact = {
    "name": "John Doe",
    "phone": "555-0123",
    "email": "john@example.com",
    "city": "New York"
}
```

**Operations:**
- [ ] Add new contact
- [ ] Search "john" → finds "John Doe"
- [ ] Update phone number
- [ ] Display formatted table
- [ ] Remove contact

---

### Problem 4.4: Word Frequency Counter (Dict)
**Question:** Count word frequencies in text using dictionaries.

**Requirements:**
- Input text: "the quick brown fox jumps over the lazy dog the fox is quick"
- Count frequency of each word (case-insensitive)
- Display words sorted by frequency (highest first)
- Find most and least common words
- Show unique words count

**Expected Results:**
- [ ] "the": 3, "quick": 2, "brown": 1, etc.
- [ ] Most common: "the" (3)
- [ ] Least common: words with count 1
- [ ] Unique words: 8 out of 12 total words
- [ ] Sorted: the(3), quick(2), fox(2), over(1), ...

---

### Problem 4.5: Tuple Coordinate System
**Question:** Create a coordinate system using tuples for immutable points.

**Requirements:**
- Represent points as (x, y) tuples
- Calculate distance between two points: sqrt((x2-x1)² + (y2-y1)²)
- Find points within radius of origin
- Sort points by distance from origin
- Group points by quadrant (I, II, III, IV)

**Test Points:**
```python
points = [(1, 2), (-3, 4), (2, -1), (-1, -2), (0, 3)]
```

**Calculations:**
- [ ] Distance (0,0) to (3,4) = 5.0
- [ ] Points within radius 3 of origin
- [ ] Sorted by distance: closest to farthest
- [ ] Quadrant I: (+,+), II: (-,+), III: (-,-), IV: (+,-)

---

### Problem 4.6: Set Operations Survey
**Question:** Analyze survey responses using set operations.

**Requirements:**
- Three groups: Python devs, JavaScript devs, Managers
- Find: full-stack devs, all developers, technical managers
- Calculate percentages and statistics
- Demonstrate all set operations: union, intersection, difference

**Survey Data:**
```python
python_devs = {"Alice", "Bob", "Charlie", "Diana"}
js_devs = {"Bob", "Diana", "Eve", "Frank"}
managers = {"Alice", "Frank", "Grace"}
```

**Required Analysis:**
- [ ] Full-stack (both Python & JS): Bob, Diana
- [ ] All developers: Alice, Bob, Charlie, Diana, Eve, Frank
- [ ] Technical managers: Alice, Frank
- [ ] Python-only: Charlie
- [ ] JS-only: Eve
- [ ] Non-technical: Grace

---

### Problem 4.7: Inventory Management System
**Question:** Create an inventory system using multiple data structures.

**Requirements:**
- Use list of dictionaries for products
- Each product: {"id", "name", "price", "quantity", "category"}
- Implement: add product, update stock, search by category, calculate total value
- Use sets for unique categories
- Use tuples for immutable product IDs

**Product Structure:**
```python
products = [
    {"id": (1,), "name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics"},
    # ... more products
]
```

**Operations:**
- [ ] Add new product
- [ ] Update quantity (increase/decrease)
- [ ] Search products by category
- [ ] Calculate inventory value: sum(price × quantity)
- [ ] List unique categories

---

### Problem 4.8: Student Management System
**Question:** Create a comprehensive student management system.

**Requirements:**
- Students stored as dictionaries with: name, grades (list), major
- Courses stored as dictionary: {course_id: {"name", "credits"}}
- Calculate GPA using grade points (A=4, B=3, C=2, D=1, F=0)
- Find students by major
- Generate class statistics
- Sort students by GPA

**Data Structure:**
```python
students = [
    {
        "name": "Alice",
        "grades": ["A", "B", "A"],
        "major": "CS"
    }
]

courses = {
    "CS101": {"name": "Programming", "credits": 3},
    "MATH201": {"name": "Calculus", "credits": 4}
}
```

**Features:**
- [ ] GPA calculation: weighted average
- [ ] Students by major
- [ ] Class average GPA
- [ ] Top performers
- [ ] Grade distribution

---

### Problem 4.9: File System Simulator
**Question:** Simulate a file system using nested data structures.

**Requirements:**
- Use nested dictionaries for directory structure
- Files: {"name", "size", "type", "modified"}
- Directories can contain files and subdirectories
- Implement: create file/dir, delete, list contents, calculate sizes
- Find files by type or size

**Structure Example:**
```python
filesystem = {
    "root": {
        "type": "directory",
        "contents": {
            "documents": {
                "type": "directory",
                "contents": {
                    "resume.txt": {"type": "file", "size": 2048, "modified": "2024-01-15"}
                }
            },
            "photo.jpg": {"type": "file", "size": 15360, "modified": "2024-01-10"}
        }
    }
}
```

**Operations:**
- [ ] Create nested directory structure
- [ ] Add/remove files and directories
- [ ] Calculate total directory sizes
- [ ] Find all .txt files
- [ ] List directory contents recursively

---

### Problem 4.10: Game Character Inventory
**Question:** Create a game character's inventory using multiple data structures.

**Requirements:**
- Character: dictionary with name, level, health
- Inventory: list of item dictionaries
- Equipment: set of equipped items
- Skills: tuple of learned skills (immutable)
- Items: {"name", "type", "damage/defense", "rarity"}

**Data Structure:**
```python
character = {
    "name": "Hero",
    "level": 5,
    "health": 100,
    "inventory": [
        {"name": "Sword", "type": "weapon", "damage": 15, "rarity": "common"},
        {"name": "Shield", "type": "armor", "defense": 10, "rarity": "rare"}
    ],
    "equipment": {"Sword", "Shield"},  # set for uniqueness
    "skills": ("Fireball", "Heal", "Teleport")  # tuple, can't unlearn
}
```

**Features:**
- [ ] Add/remove items from inventory
- [ ] Equip/unequip items (limited slots)
- [ ] Calculate total stats from equipment
- [ ] Use potions (temporary effects)
- [ ] Level up character