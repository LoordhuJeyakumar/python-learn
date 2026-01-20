# Week 1: Python Fundamentals - Questions & Problem Statements

## 📋 Instructions
Solve each problem below using Python code. Write your solutions in separate Python files or in a Jupyter notebook. Test your code thoroughly and ensure it handles edge cases.

---

## **SECTION 1: VARIABLES & DATA TYPES**

### Problem 1.1: Variable Creation & Types
**Question:** Create variables to store information about a person and display them using f-strings.

**Requirements:**
- Create variables for: name (string), age (integer), height (float), is_student (boolean)
- Use f-strings to display: "John is 25 years old, 5.9 feet tall, and is a student"
- Change the values and ensure the output updates correctly

**Acceptance Criteria:**
- [ ] All required variables created with correct types
- [ ] F-string displays all information correctly
- [ ] Code runs without errors

---

### Problem 1.2: Type Conversion
**Question:** Write a program that demonstrates type conversion between different data types.

**Requirements:**
- Convert string "123" to integer and add 10
- Convert float 45.67 to integer (what happens to decimal part?)
- Convert boolean True to string and concatenate with " is true"
- Convert integer 0 to boolean (what is the result?)

**Acceptance Criteria:**
- [ ] All conversions work correctly
- [ ] Understand implicit vs explicit conversion
- [ ] Handle potential conversion errors

---

### Problem 1.3: Type Checking
**Question:** Create a function that analyzes the type of any input value.

**Requirements:**
- Function should accept any value as parameter
- Return the type name and whether it's "truthy" or "falsy"
- Test with: 0, "", None, [], {}, False, "hello", 42

**Acceptance Criteria:**
- [ ] Function works for all test cases
- [ ] Correctly identifies type names
- [ ] Properly determines truthiness

---

## **SECTION 2: CONTROL FLOW**

### Problem 2.1: Age Category Classifier
**Question:** Write a program that classifies people into age categories.

**Requirements:**
- Input: age (integer)
- Output categories:
  - Child: age < 13
  - Teenager: 13 ≤ age < 20
  - Adult: 20 ≤ age < 65
  - Senior: age ≥ 65
- Handle invalid ages (negative numbers)

**Acceptance Criteria:**
- [ ] All age ranges work correctly
- [ ] Invalid input handled gracefully
- [ ] Clear, readable output

---

### Problem 2.2: Grade Calculator
**Question:** Create a program that converts numeric scores to letter grades.

**Requirements:**
- Input: score (0-100)
- Output grades:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: 0-59
- Handle scores outside 0-100 range

**Acceptance Criteria:**
- [ ] All grade ranges correct
- [ ] Invalid scores handled
- [ ] Edge cases (exactly 90, 80, etc.) work

---

### Problem 2.3: Login System Logic
**Question:** Implement login validation logic using boolean operators.

**Requirements:**
- Check if username exists AND password is correct
- Account must be active AND not locked
- User must have valid email OR phone verification
- Display appropriate messages for each failure case

**Acceptance Criteria:**
- [ ] All logical conditions work correctly
- [ ] Clear error messages for each failure
- [ ] Success case properly handled

---

### Problem 2.4: Weather Decision Maker
**Question:** Create a program that gives clothing recommendations based on weather.

**Requirements:**
- Inputs: temperature (float), is_raining (boolean), wind_speed (float)
- Logic:
  - If raining: recommend raincoat and umbrella
  - If temperature < 10°C: recommend warm coat
  - If temperature > 25°C: recommend light clothing
  - If wind_speed > 30 km/h: recommend windbreaker
- Combine multiple conditions appropriately

**Acceptance Criteria:**
- [ ] All weather combinations covered
- [ ] Logical conditions are correct
- [ ] Clear recommendations given

---

## **SECTION 3: LOOPS & ITERATION**

### Problem 3.1: Number Sequence Generator
**Question:** Write a program that generates different number sequences using loops.

**Requirements:**
- Generate first 10 even numbers
- Generate first 10 odd numbers
- Generate squares of numbers 1-10
- Generate countdown from 20 to 1
- Use both for loops and while loops

**Acceptance Criteria:**
- [ ] All sequences generate correct numbers
- [ ] Both loop types demonstrated
- [ ] Code is efficient and readable

---

### Problem 3.2: Shopping List Processor
**Question:** Create a program that processes a shopping list with priorities.

**Requirements:**
- Shopping list: ["bread", "milk", "eggs", "chicken", "rice", "apples"]
- Priorities: items at index 0-1 are "HIGH", 2-3 are "MEDIUM", rest are "LOW"
- Display each item with its priority and index
- Calculate total items and items per priority level

**Acceptance Criteria:**
- [ ] All items displayed with correct priorities
- [ ] Proper indexing used
- [ ] Statistics calculated correctly

---

### Problem 3.3: Password Validator with Loop
**Question:** Create a password validation system that keeps asking until valid.

**Requirements:**
- Password requirements:
  - At least 8 characters
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
- Keep prompting until all requirements met
- Show specific error messages for each failed requirement

**Acceptance Criteria:**
- [ ] All validation rules work
- [ ] Loop continues until valid password
- [ ] Clear feedback for each requirement

---

### Problem 3.4: Multiplication Table Generator
**Question:** Generate a formatted multiplication table using nested loops.

**Requirements:**
- Create 10x10 multiplication table
- Format output in a grid
- Include row and column headers
- Align numbers properly (right-aligned)

**Acceptance Criteria:**
- [ ] Table is properly formatted
- [ ] All calculations correct
- [ ] Output is readable and aligned

---

### Problem 3.5: Prime Number Finder
**Question:** Write a program that finds prime numbers with loop control.

**Requirements:**
- Find all prime numbers between 1 and 100
- Use break to optimize inner loop
- Use continue to skip even numbers > 2
- Display primes in a formatted list

**Acceptance Criteria:**
- [ ] All primes between 1-100 found
- [ ] break and continue used appropriately
- [ ] Code is optimized (doesn't check unnecessary numbers)

---

## **SECTION 4: DATA STRUCTURES**

### Problem 4.1: Student Grade Analyzer
**Question:** Create a program that analyzes student grades using lists.

**Requirements:**
- Grades list: [85, 92, 78, 96, 88, 73, 91, 84, 79, 87]
- Calculate: average, highest, lowest, number of passing grades (≥80)
- Sort grades in ascending and descending order
- Find grades above average

**Acceptance Criteria:**
- [ ] All calculations correct
- [ ] List methods used appropriately
- [ ] Results clearly displayed

---

### Problem 4.2: Dictionary-Based Contact Book
**Question:** Create a simple contact book using dictionaries.

**Requirements:**
- Store contacts as dictionaries with: name, phone, email, city
- Add at least 5 contacts
- Search contacts by name
- Display all contacts in a formatted way
- Update a contact's information

**Acceptance Criteria:**
- [ ] Contacts stored in appropriate structure
- [ ] Search functionality works
- [ ] Display format is readable
- [ ] Update operations work correctly

---

### Problem 4.3: Word Frequency Counter
**Question:** Count word frequencies in a text using dictionaries.

**Requirements:**
- Input text: "the quick brown fox jumps over the lazy dog the fox is quick"
- Count frequency of each word
- Display words sorted by frequency (highest first)
- Find most common and least common words
- Handle case sensitivity (convert to lowercase)

**Acceptance Criteria:**
- [ ] All word frequencies correct
- [ ] Proper sorting implemented
- [ ] Case handled correctly

---

### Problem 4.4: Set Operations for Survey Analysis
**Question:** Analyze survey responses using set operations.

**Requirements:**
- Three groups of survey responses:
  - Python users: {"Alice", "Bob", "Charlie", "Diana"}
  - JavaScript users: {"Bob", "Diana", "Eve", "Frank"}
  - Managers: {"Alice", "Frank", "Grace"}
- Find: full-stack developers, all developers, technical managers
- Calculate percentages and statistics

**Acceptance Criteria:**
- [ ] All set operations correct
- [ ] Results properly interpreted
- [ ] Statistics calculated accurately

---

### Problem 4.5: List Comprehension Challenges
**Question:** Solve problems using list comprehensions.

**Requirements:**
- Create list of squares for numbers 1-20
- Filter even numbers from 1-50
- Create list of uppercase words from: ["hello", "WORLD", "python", "CODING"]
- Generate Pythagorean triples: (a,b,c) where a² + b² = c², a,b,c ≤ 20
- Flatten nested list: [[1,2,3], [4,5], [6,7,8,9]]

**Acceptance Criteria:**
- [ ] All comprehensions work correctly
- [ ] Code is concise and readable
- [ ] Results match expected output

---

### Problem 4.6: Tuple-Based Coordinate System
**Question:** Create a coordinate system using tuples.

**Requirements:**
- Represent points as (x, y) tuples
- Calculate distance between two points
- Find points within certain radius of origin
- Sort points by distance from origin
- Group points by quadrant

**Acceptance Criteria:**
- [ ] Distance calculations correct
- [ ] Points properly categorized
- [ ] Sorting works as expected

---

## **SECTION 5: COMPREHENSIVE APPLICATIONS**

### Problem 5.1: Simple Task Manager
**Question:** Create a basic task management system using all concepts learned.

**Requirements:**
- Tasks stored as dictionaries: {"id", "title", "priority", "completed"}
- Functions for: add_task, list_tasks, complete_task, delete_task
- Use loops for displaying tasks
- Use conditionals for priority filtering
- Persist data in memory (no file I/O yet)

**Acceptance Criteria:**
- [ ] All CRUD operations work
- [ ] Data properly structured
- [ ] Error handling for invalid operations

---

### Problem 5.2: Number Guessing Game
**Question:** Create an interactive number guessing game.

**Requirements:**
- Computer generates random number 1-100
- User has 7 attempts to guess
- Provide hints: "too high", "too low"
- Track number of attempts
- Allow replay without restarting program
- Show game statistics

**Acceptance Criteria:**
- [ ] Game logic works correctly
- [ ] Input validation implemented
- [ ] Statistics properly tracked

---

### Problem 5.3: Student Grade Book
**Question:** Create a comprehensive student grade book system.

**Requirements:**
- Students stored as dictionaries with courses and grades
- Calculate GPA for each student
- Find students with GPA above certain threshold
- Generate class statistics (average GPA, highest/lowest)
- Sort students by GPA
- Handle missing grades appropriately

**Acceptance Criteria:**
- [ ] All calculations correct
- [ ] Data properly structured
- [ ] Edge cases handled (missing grades, etc.)

---

## **SECTION 6: DEBUGGING CHALLENGES**

### Problem 6.1: Common Bug Fixes
**Question:** Identify and fix common programming bugs.

**Problems to fix:**
1. IndexError when accessing list element
2. KeyError when accessing dictionary
3. TypeError in string concatenation
4. Infinite loop in while condition
5. Logic error in conditional statements

**Acceptance Criteria:**
- [ ] All bugs identified
- [ ] Correct fixes implemented
- [ ] Understanding of why bugs occurred

---

### Problem 6.2: Edge Case Handling
**Question:** Write robust code that handles edge cases properly.

**Scenarios:**
1. Empty lists/dictionaries
2. Division by zero
3. Invalid user input types
4. File not found (when you learn file I/O)
5. Network errors (when you learn APIs)

**Acceptance Criteria:**
- [ ] All edge cases handled gracefully
- [ ] Appropriate error messages
- [ ] Program doesn't crash

---

## **GRADING RUBRIC**

### For Each Problem:
- **Correctness (40%)**: Does the code work as specified?
- **Efficiency (20%)**: Is the solution optimal?
- **Readability (20%)**: Is the code well-structured and commented?
- **Error Handling (20%)**: Does it handle edge cases properly?

### Overall Course Grade:
- **Section 1-2 (20%)**: Basic concepts mastery
- **Section 3-4 (40%)**: Data structures and loops
- **Section 5 (30%)**: Application of concepts
- **Section 6 (10%)**: Debugging and robustness

---

## **SUBMISSION GUIDELINES**

1. Create separate Python files for each major section
2. Include comments explaining your thought process
3. Test your code with multiple inputs
4. Handle errors gracefully
5. Follow PEP 8 style guidelines
6. Submit both code and sample outputs

**Remember:** Focus on understanding the concepts, not just getting the right output. Experiment, make mistakes, and learn from them!