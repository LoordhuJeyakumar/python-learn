# TOPIC 5: LIST COMPREHENSIONS & GENERATORS
## Questions & Problem Statements

### Problem 5.1: Basic List Comprehensions
**Question:** Create various list comprehensions for different transformations.

**Requirements:**
- Generate squares of numbers 1-10
- Filter even numbers from 1-20
- Convert list of strings to uppercase
- Create list of lengths for each word in a sentence
- Generate all combinations of two lists (Cartesian product)

**Test Cases:**
- [ ] Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
- [ ] Evens: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
- [ ] Uppercase: ["HELLO", "WORLD", "PYTHON"]
- [ ] Word lengths: [5, 5, 6] for ["Hello", "world", "Python"]
- [ ] Cartesian: [(1,'a'), (1,'b'), (2,'a'), (2,'b')] for [1,2] × ['a','b']

---

### Problem 5.2: Conditional List Comprehensions
**Question:** Use conditions in list comprehensions for filtering.

**Requirements:**
- Numbers divisible by 3 AND 5 from 1-100
- Words longer than 4 characters from a sentence
- Positive numbers from a mixed list
- Students with grades above 80
- Even-length strings from a list

**Test Data:**
```python
numbers = [3, 15, 7, 30, 45, 2, 90, 8]
words = ["the", "quick", "brown", "fox", "jumps", "over"]
grades = [85, 92, 78, 96, 73, 88]
strings = ["hi", "hello", "hey", "greetings", "sup"]
```

**Expected Results:**
- [ ] Multiples of 15: [15, 30, 45, 90]
- [ ] Long words: ["quick", "brown", "jumps", "over"]
- [ ] Passing grades: [85, 92, 96, 88]
- [ ] Even length: ["hi", "hey", "sup"]

---

### Problem 5.3: Nested List Comprehensions
**Question:** Create nested comprehensions for matrix operations.

**Requirements:**
- Generate 3x3 multiplication table
- Create identity matrix (1s on diagonal, 0s elsewhere)
- Flatten a 2D list into 1D
- Transpose a matrix
- Create checkerboard pattern matrix

**Examples:**
- [ ] Table: [[1,2,3], [2,4,6], [3,6,9]]
- [ ] Identity: [[1,0,0], [0,1,0], [0,0,1]]
- [ ] Flatten: [1,2,3,4,5,6] from [[1,2,3],[4,5,6]]
- [ ] Transpose: [[1,4],[2,5],[3,6]] from [[1,2,3],[4,5,6]]

---

### Problem 5.4: Dictionary Comprehensions
**Question:** Create dictionaries using comprehensions.

**Requirements:**
- Create dict of squares: {1:1, 2:4, 3:9, ...}
- Convert list of tuples to dict: [("a",1), ("b",2)] → {"a":1, "b":2}
- Swap keys and values in existing dict
- Create dict of word frequencies from text
- Filter dict to keep only certain entries

**Test Cases:**
- [ ] Squares dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
- [ ] From tuples: {"apple": 3, "banana": 2, "cherry": 5}
- [ ] Swapped: {3: "apple", 2: "banana", 5: "cherry"}
- [ ] Frequencies: {"the": 3, "quick": 2, "brown": 1}

---

### Problem 5.5: Set Comprehensions
**Question:** Create sets using comprehensions.

**Requirements:**
- Get unique vowels from a string
- Create set of squares for numbers 1-10
- Find unique file extensions from filenames
- Get unique first letters from list of words
- Create set of lengths from list of strings

**Test Data:**
```python
text = "comprehensions are powerful"
numbers = [1, 2, 2, 3, 4, 4, 5]
files = ["doc.txt", "image.jpg", "doc.pdf", "music.mp3", "doc.txt"]
words = ["python", "programming", "powerful", "language"]
```

**Expected Results:**
- [ ] Vowels: {'o', 'e', 'i', 'a', 'u'}
- [ ] Unique squares: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
- [ ] Extensions: {'.txt', '.jpg', '.pdf', '.mp3'}
- [ ] First letters: {'p', 'l'}
- [ ] String lengths: {6, 11, 8, 8}

---

### Problem 5.6: Generator Expressions
**Question:** Use generator expressions for memory-efficient processing.

**Requirements:**
- Sum squares of numbers 1-1,000,000 (without creating list)
- Find first 10 even numbers using generator
- Process large file line by line (simulate)
- Calculate running average of numbers
- Find prime numbers using generator

**Efficiency Demonstrations:**
- [ ] Sum 1M squares using gen: fast, low memory
- [ ] Sum 1M squares using list: slow, high memory
- [ ] First 10 evens: (x for x in range(1000000) if x % 2 == 0)
- [ ] Running average: accumulate values without storing all

---

### Problem 5.7: Advanced Comprehensions
**Question:** Combine multiple concepts in complex comprehensions.

**Requirements:**
- Create dict where keys are numbers 1-10, values are lists of their multiples up to 100
- Filter dict comprehension to keep only even keys
- Create nested comprehension for matrix operations
- Use conditional expressions in comprehensions
- Chain multiple comprehensions together

**Complex Examples:**
- [ ] Multiples dict: {1: [1,2,3,...,100], 2: [2,4,6,...,100], ...}
- [ ] Even keys only: filter comprehension for even numbers
- [ ] Matrix multiplication simulation
- [ ] Conditional: ["even" if x%2==0 else "odd" for x in range(10)]

---

### Problem 5.8: File Processing with Comprehensions
**Question:** Process file-like data using comprehensions.

**Requirements:**
- Process list of "log lines" (simulated file)
- Extract IP addresses from log entries
- Count occurrences of each status code
- Find lines containing specific keywords
- Calculate statistics from numeric data

**Simulated Log Data:**
```python
logs = [
    "192.168.1.1 - GET /home - 200",
    "192.168.1.2 - POST /login - 401",
    "192.168.1.1 - GET /profile - 200",
    "10.0.0.1 - GET /admin - 403",
    "192.168.1.2 - GET /logout - 200"
]
```

**Processing Tasks:**
- [ ] Extract IPs: ["192.168.1.1", "192.168.1.2", ...]
- [ ] Status counts: {200: 3, 401: 1, 403: 1}
- [ ] Lines with "192.168": filter specific IPs
- [ ] Unique IPs: set comprehension

---

### Problem 5.9: Data Analysis with Comprehensions
**Question:** Perform data analysis using comprehensions.

**Requirements:**
- Process student grades data
- Calculate averages using comprehensions
- Find students above average
- Create grade distributions
- Group students by performance categories

**Student Data:**
```python
students = [
    {"name": "Alice", "grades": [85, 92, 88]},
    {"name": "Bob", "grades": [78, 85, 82]},
    {"name": "Charlie", "grades": [92, 95, 89]}
]
```

**Analysis Tasks:**
- [ ] Average per student: [88.33, 81.67, 92.0]
- [ ] Overall class average
- [ ] Students above class average
- [ ] Grade distributions (A/B/C count per student)
- [ ] Best performing students

---

### Problem 5.10: Performance Comparison
**Question:** Compare performance of comprehensions vs traditional loops.

**Requirements:**
- Time list comprehension vs for loop for large data
- Compare memory usage of list vs generator
- Demonstrate when to use each approach
- Show readability differences
- Profile different comprehension patterns

**Performance Tests:**
- [ ] Create list of 1M squares: time comprehension vs loop
- [ ] Sum 1M numbers: comprehension vs loop vs built-in sum()
- [ ] Filter 1M items: comprehension vs loop with if
- [ ] Memory usage: list comp vs generator expression
- [ ] Readability: which is more readable for each task?

---

### Problem 5.11: Real-world Application
**Question:** Build a complete application using comprehensions.

**Requirements:**
- Create a book catalog system
- Books with: title, author, genre, rating, pages
- Search books by author using comprehension
- Filter by genre and rating
- Calculate statistics (avg rating per genre, etc.)
- Generate reading recommendations

**Book Data Structure:**
```python
books = [
    {"title": "Python Basics", "author": "John Doe", "genre": "Programming", "rating": 4.5, "pages": 300},
    {"title": "Web Development", "author": "Jane Smith", "genre": "Programming", "rating": 4.2, "pages": 400},
    {"title": "Data Science", "author": "Bob Wilson", "genre": "Data", "rating": 4.8, "pages": 500}
]
```

**Features:**
- [ ] Books by author: comprehension filter
- [ ] High-rated books: rating >= 4.5
- [ ] Genre statistics: avg rating per genre
- [ ] Reading time estimates
- [ ] Recommendations based on preferences