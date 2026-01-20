# TOPIC 3: LOOPS & ITERATION
## Questions & Problem Statements

### Problem 3.1: Number Sequence Generator
**Question:** Create a program that generates different number sequences using for loops.

**Requirements:**
- Generate first 10 even numbers (2, 4, 6, ...)
- Generate first 10 odd numbers (1, 3, 5, ...)
- Generate squares of numbers 1-10 (1, 4, 9, ...)
- Generate countdown from 20 to 1
- Use range() function appropriately
- Display results clearly

**Test Output:**
- [ ] Evens: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
- [ ] Odds: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
- [ ] Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
- [ ] Countdown: 20, 19, 18, ..., 1

---

### Problem 3.2: Shopping List Processor
**Question:** Process a shopping list using for loops and enumerate.

**Requirements:**
- Shopping list: ["bread", "milk", "eggs", "chicken", "rice", "apples"]
- Display items with numbers starting from 1
- Add priority levels: items 1-2 "HIGH", 3-4 "MEDIUM", others "LOW"
- Calculate total items and count by priority
- Use enumerate() for numbering

**Expected Output:**
```
Shopping List:
1. HIGH - bread
2. HIGH - milk
3. MEDIUM - eggs
4. MEDIUM - chicken
5. LOW - rice
6. LOW - apples

Total items: 6
High priority: 2, Medium priority: 2, Low priority: 2
```

---

### Problem 3.3: While Loop Counter
**Question:** Create a program that demonstrates while loops with different conditions.

**Requirements:**
- Count from 1 to 10 using while loop
- Count down from 10 to 1
- Sum numbers from 1 to 100
- Generate Fibonacci sequence until a number exceeds 100
- Use appropriate loop conditions

**Test Results:**
- [ ] Count up: 1, 2, 3, ..., 10
- [ ] Count down: 10, 9, 8, ..., 1
- [ ] Sum 1-100 = 5050
- [ ] Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

---

### Problem 3.4: Password Validator with Loop
**Question:** Create a password validation system that keeps asking until valid.

**Requirements:**
- Password requirements:
  - At least 8 characters
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
- Keep prompting until all requirements met
- Show specific error messages for each failed requirement
- Count number of attempts

**Test Cases:**
- [ ] "password" → "Password must contain uppercase letter"
- [ ] "Password" → "Password must contain a digit"
- [ ] "Pass123" → "Password must be at least 8 characters"
- [ ] "Password123" → "Valid password! Attempts: 4"

---

### Problem 3.5: Multiplication Table Generator
**Question:** Generate a formatted multiplication table using nested loops.

**Requirements:**
- Create 10x10 multiplication table (1-10)
- Format as a grid with proper alignment
- Include row and column headers
- Use nested for loops
- Right-align numbers for readability

**Sample Output:**
```
   |  1  2  3  4  5  6  7  8  9 10
---+-------------------------------
 1 |  1  2  3  4  5  6  7  8  9 10
 2 |  2  4  6  8 10 12 14 16 18 20
...
10 | 10 20 30 40 50 60 70 80 90 100
```

---

### Problem 3.6: Break and Continue Demonstration
**Question:** Create programs that demonstrate break and continue statements.

**Requirements:**
- Find first number divisible by 7 between 1-100 (use break)
- Print numbers 1-20, but skip multiples of 3 (use continue)
- Search for a specific item in a list and break when found
- Process a list but skip invalid items (continue)
- Show the difference between break and continue

**Test Cases:**
- [ ] First multiple of 7: 7 (stops at first match)
- [ ] Numbers 1-20 skipping 3's: 1,2,4,5,7,8,10,11,13,14,16,17,19,20
- [ ] Search "apple" in ["banana", "orange", "apple", "grape"] → Found at index 2

---

### Problem 3.7: Prime Number Finder
**Question:** Write a program to find prime numbers with optimized loop control.

**Requirements:**
- Find all prime numbers between 1 and 100
- Use break in inner loop for optimization
- Use continue to skip even numbers > 2
- Display primes in a formatted grid
- Count total primes found

**Optimization Rules:**
- [ ] Skip even numbers greater than 2
- [ ] Break inner loop when divisor found
- [ ] Only check divisors up to square root of number
- [ ] 2 is prime, 1 is not prime

**Expected Output:**
```
Prime numbers between 1 and 100:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97

Total primes: 25
```

---

### Problem 3.8: Student Grade Processor
**Question:** Process student grades using loops and conditional logic.

**Requirements:**
- Grades list: [85, 92, 78, 96, 88, 73, 91, 84, 79, 87]
- Calculate: average, highest, lowest, number of passing grades (≥80)
- Create grade distribution (A:90+, B:80-89, C:70-79, D:60-69, F:<60)
- Use loops to process all calculations
- Display results clearly

**Expected Calculations:**
- [ ] Average: sum/count = 87.3
- [ ] Highest: 96, Lowest: 73
- [ ] Passing: 7 out of 10
- [ ] Distribution: A:3, B:4, C:3, D:0, F:0

---

### Problem 3.9: Pattern Generator
**Question:** Create different patterns using nested loops.

**Requirements:**
- Generate triangle pattern:
  ```
  *
  **
  ***
  ****
  *****
  ```
- Generate inverted triangle
- Generate number pyramid:
  ```
     1
    123
   12345
  1234567
  ```
- Generate checkerboard pattern (5x5 with alternating symbols)

**Test Patterns:**
- [ ] Triangle: 5 rows, increasing asterisks
- [ ] Inverted: 5 rows, decreasing asterisks
- [ ] Number pyramid: centered, odd rows
- [ ] Checkerboard: alternating ▫️ and ▪️

---

### Problem 3.10: Interactive Menu System
**Question:** Create an interactive menu using while loops.

**Requirements:**
- Display menu options: Add item, View items, Remove item, Exit
- Keep showing menu until user chooses Exit
- Handle invalid menu choices
- Store items in a list
- Use while loop for menu repetition
- Use for loops for displaying items

**Menu Flow:**
```
=== MENU ===
1. Add item
2. View items
3. Remove item
4. Exit

Choice: 1
Enter item: apple
Item added!

Choice: 2
Items: 1. apple

Choice: 4
Goodbye!
```

**Acceptance Criteria:**
- [ ] Menu displays repeatedly until exit
- [ ] Invalid choices handled gracefully
- [ ] Items can be added, viewed, and removed
- [ ] Clear user feedback for each action