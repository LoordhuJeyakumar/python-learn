#!/usr/bin/env python3
"""
LIST COMPREHENSIONS & GENERATORS - Complete Guide
==================================================

List comprehensions are a concise way to create lists from existing iterables.
Like a fast-food assembly line for creating collections.

ANALOGY: Fast Food Assembly Line
- Traditional loop = Hand-making each burger one by one
- List comprehension = Assembly line producing burgers quickly
- Generator = Just-in-time burger production (save ingredients)

WHY THEY MATTER:
- More readable than traditional loops
- Often faster execution
- Less code to write and maintain
- Functional programming style
"""

# ==========================================
# 1. BASIC LIST COMPREHENSIONS
# ==========================================

print("🏭 BASIC LIST COMPREHENSIONS - Assembly Line Basics")
print("=" * 55)

# Traditional approach (slow assembly line)
print("🐌 Traditional loop approach:")
numbers = [1, 2, 3, 4, 5]
squares_traditional = []
for num in numbers:
    squares_traditional.append(num ** 2)
print(f"Squares: {squares_traditional}")
print()

# List comprehension (fast assembly line)
print("⚡ List comprehension approach:")
squares_comprehension = [num ** 2 for num in numbers]
print(f"Squares: {squares_comprehension}")
print()

# Anatomy of list comprehension
print("🔍 List comprehension anatomy:")
print("   [expression for item in iterable]")
print("   [   num**2  for   num  in  numbers ]")
print()

# ==========================================
# 2. CONDITIONAL COMPREHENSIONS
# ==========================================

print("🎯 CONDITIONAL COMPREHENSIONS - Quality Control")
print("=" * 55)

# Filter with condition
print("🔍 Filter even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(f"Evens: {evens}")
print()

# Filter and transform
print("🔄 Filter and transform:")
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word.upper() for word in words if len(word) > 5]
print(f"Long words (uppercase): {long_words}")
print()

# Multiple conditions
print("🎭 Multiple conditions:")
grades = [85, 92, 78, 95, 88, 73, 99]
honors = [grade for grade in grades if grade >= 90 and grade % 10 == 5]
print(f"A+ grades: {honors}")
print()

# ==========================================
# 3. NESTED COMPREHENSIONS
# ==========================================

print("🔄 NESTED COMPREHENSIONS - Multi-Level Assembly")
print("=" * 55)

# Matrix creation
print("📊 Create multiplication table:")
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in table:
    print(row)
print()

# Flatten nested lists
print("🗂️ Flatten nested lists:")
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [num for sublist in nested for num in sublist]
print(f"Flattened: {flattened}")
print()

# Matrix transpose
print("🔀 Matrix transpose:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed:")
for row in transposed:
    print(row)
print()

# ==========================================
# 4. DICTIONARY COMPREHENSIONS
# ==========================================

print("📚 DICTIONARY COMPREHENSIONS - Recipe Book Assembly")
print("=" * 55)

# Basic dictionary comprehension
print("🔤 Create word-length dictionary:")
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")
print()

# Dictionary from two lists
print("🔗 Dictionary from two lists:")
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(f"Person dict: {person}")
print()

# Conditional dictionary comprehension
print("🎯 Conditional dictionary:")
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
passing_scores = {name: score for name, score in scores.items() if score >= 80}
print(f"Passing scores: {passing_scores}")
print()

# Swap keys and values
print("🔄 Swap keys and values:")
swapped = {score: name for name, score in scores.items()}
print(f"Score to name: {swapped}")
print()

# ==========================================
# 5. SET COMPREHENSIONS
# ==========================================

print("✅ SET COMPREHENSIONS - Unique Item Assembly")
print("=" * 55)

# Basic set comprehension
print("🔤 Extract unique vowels:")
text = "hello world, this is a test message"
vowels = {char.lower() for char in text if char.lower() in 'aeiou'}
print(f"Unique vowels: {vowels}")
print()

# Set from list with duplicates
print("🧹 Remove duplicates from list:")
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = {num for num in numbers_with_dupes}
print(f"Unique numbers: {unique_numbers}")
print()

# ==========================================
# 6. GENERATOR EXPRESSIONS
# ==========================================

print("⚡ GENERATOR EXPRESSIONS - Just-in-Time Production")
print("=" * 55)

# List comprehension (makes whole list at once)
print("📦 List comprehension - Make everything at once:")
large_squares_list = [x**2 for x in range(10)]
print(f"List: {large_squares_list}")
print(f"Memory usage: {len(large_squares_list)} items stored")
print()

# Generator expression (makes items one at a time)
print("🚀 Generator expression - Make on demand:")
large_squares_gen = (x**2 for x in range(10))
print(f"Generator: {large_squares_gen}")
print("Memory usage: 1 item at a time (lazy evaluation)")
print()

# Using generator
print("🔄 Using generator:")
for square in large_squares_gen:
    print(f"Generated: {square}")
print()

# Memory comparison
print("🧠 Memory efficiency comparison:")
import sys

# Large dataset
big_list = [x**2 for x in range(1000)]
big_gen = (x**2 for x in range(1000))

print(f"List memory: {sys.getsizeof(big_list)} bytes")
print(f"Generator memory: {sys.getsizeof(big_gen)} bytes")
print(f"Memory savings: {((sys.getsizeof(big_list) - sys.getsizeof(big_gen)) / sys.getsizeof(big_list) * 100):.1f}%")
print()

# ==========================================
# 7. GENERATOR FUNCTIONS
# ==========================================

print("🏭 GENERATOR FUNCTIONS - Custom Production Lines")
print("=" * 55)

def fibonacci_generator(n):
    """
    Generate Fibonacci sequence up to n terms.

    ANALOGY: A machine that produces Fibonacci numbers on demand
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a  # Pause here, return value, resume on next call
        a, b = b, a + b
        count += 1

print("🔢 Fibonacci generator:")
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")
print("\n")

def prime_generator():
    """
    Generate prime numbers indefinitely.

    ANALOGY: A prime number factory that never stops
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("🔢 Prime number generator (first 10):")
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen), end=" ")
print("\n")

# ==========================================
# 8. PRACTICAL EXAMPLES
# ==========================================

print("🏪 PRACTICAL EXAMPLES - Real Restaurant Scenarios")
print("=" * 55)

# Example 1: Menu filtering
print("🍽️ Example 1: Menu filtering")
menu_items = [
    {"name": "Margherita Pizza", "price": 15.99, "category": "main", "vegetarian": True},
    {"name": "Caesar Salad", "price": 8.99, "category": "starter", "vegetarian": True},
    {"name": "Grilled Salmon", "price": 22.99, "category": "main", "vegetarian": False},
    {"name": "Chocolate Cake", "price": 6.99, "category": "dessert", "vegetarian": True},
    {"name": "Steak", "price": 28.99, "category": "main", "vegetarian": False}
]

# Get all vegetarian items
vegetarian_items = [item for item in menu_items if item["vegetarian"]]
print("🥬 Vegetarian items:")
for item in vegetarian_items:
    print(f"  • {item['name']} - ${item['price']}")
print()

# Get main courses under $20
affordable_mains = [
    item for item in menu_items
    if item["category"] == "main" and item["price"] < 20
]
print("💰 Affordable main courses:")
for item in affordable_mains:
    print(f"  • {item['name']} - ${item['price']}")
print()

# Example 2: Data processing
print("📊 Example 2: Customer data processing")
customers = [
    {"name": "Alice", "orders": 5, "total_spent": 127.50},
    {"name": "Bob", "orders": 3, "total_spent": 89.25},
    {"name": "Charlie", "orders": 8, "total_spent": 203.75},
    {"name": "Diana", "orders": 2, "total_spent": 45.00}
]

# Calculate average order value
avg_order_values = {
    customer["name"]: customer["total_spent"] / customer["orders"]
    for customer in customers
}
print("📈 Average order values:")
for name, avg in avg_order_values.items():
    print(".2f")
print()

# Example 3: Inventory management
print("📦 Example 3: Inventory alerts")
inventory = {
    "pasta": 45,
    "tomatoes": 12,
    "cheese": 8,
    "flour": 23,
    "olive_oil": 5
}

# Items running low (less than 10)
low_stock = {item: qty for item, qty in inventory.items() if qty < 10}
print("⚠️ Low stock alerts:")
for item, qty in low_stock.items():
    print(f"  • {item.replace('_', ' ').title()}: {qty} remaining")
print()

# ==========================================
# 9. PERFORMANCE COMPARISON
# ==========================================

print("⚡ PERFORMANCE COMPARISON - Speed vs Memory")
print("=" * 55)

import time

# Large dataset
data_size = 100000
data = list(range(data_size))

# Method 1: Traditional loop
print("🐌 Traditional loop:")
start = time.time()
traditional_result = []
for num in data:
    if num % 2 == 0:  # Even numbers only
        traditional_result.append(num * num)
traditional_time = time.time() - start
print(".4f")

# Method 2: List comprehension
print("⚡ List comprehension:")
start = time.time()
comprehension_result = [num * num for num in data if num % 2 == 0]
comprehension_time = time.time() - start
print(".4f")

# Method 3: Generator expression
print("🚀 Generator expression:")
start = time.time()
generator_result = (num * num for num in data if num % 2 == 0)
# Convert to list for fair comparison
generator_list = list(generator_result)
generator_time = time.time() - start
print(".4f")

print("\n💾 Memory usage:")
print(f"  Traditional: {len(traditional_result)} items")
print(f"  Comprehension: {len(comprehension_result)} items")
print(f"  Generator: {len(generator_list)} items (created on demand)")

speedup = traditional_time / comprehension_time
print(".2f")
print()

# ==========================================
# 10. COMMON PATTERNS & BEST PRACTICES
# ==========================================

print("🎯 COMMON PATTERNS & BEST PRACTICES")
print("=" * 55)

# Pattern 1: Filtering and transforming
print("🔍 Pattern 1: Filter and transform")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(f"Even squares: {even_squares}")

# Pattern 2: Nested comprehensions
print("\n🔄 Pattern 2: Nested comprehensions")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten and filter
flattened_odds = [num for row in matrix for num in row if num % 2 != 0]
print(f"Odd numbers from matrix: {flattened_odds}")

# Pattern 3: Dictionary comprehensions with conditions
print("\n📚 Pattern 3: Conditional dictionary comprehensions")
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88
}

# Grade mapping
grades = {
    name: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    for name, score in students.items()
}
print(f"Letter grades: {grades}")

# Pattern 4: Multiple generators
print("\n🔗 Pattern 4: Chaining generators")
# Generate, filter, transform
result = (
    num ** 2                    # Square it
    for num in range(20)        # Generate numbers
    if num % 3 == 0             # Keep multiples of 3
)
filtered_squares = list(result)
print(f"Squares of multiples of 3: {filtered_squares}")
print()

# ==========================================
# SUMMARY
# ==========================================

print("🎓 LIST COMPREHENSIONS & GENERATORS SUMMARY")
print("=" * 55)
print("✅ List Comprehensions: [expression for item in iterable if condition]")
print("   • Concise way to create lists")
print("   • Often faster than traditional loops")
print("   • Can include conditions and nested loops")
print()
print("✅ Dictionary Comprehensions: {key: value for item in iterable}")
print("   • Create dictionaries from iterables")
print("   • Can include conditions")
print("   • Great for data transformation")
print()
print("✅ Set Comprehensions: {expression for item in iterable}")
print("   • Create sets (unique values only)")
print("   • Automatic duplicate removal")
print()
print("✅ Generator Expressions: (expression for item in iterable)")
print("   • Memory efficient (lazy evaluation)")
print("   • Create items on demand")
print("   • Use next() or for loops to consume")
print()
print("✅ Generator Functions: Use 'yield' instead of 'return'")
print("   • Can pause and resume execution")
print("   • Great for large datasets")
print("   • Memory efficient")
print()
print("💡 When to use which:")
print("   • Small data + need all results → List comprehension")
print("   • Large data + process all → Generator expression")
print("   • Custom iteration logic → Generator function")
print("   • Key-value data → Dictionary comprehension")
print("   • Unique values → Set comprehension")