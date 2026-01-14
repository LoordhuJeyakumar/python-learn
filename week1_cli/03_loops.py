#!/usr/bin/env python3
"""
LOOPS IN PYTHON - Complete Guide
=================================

Loops allow us to repeat code execution. Like a restaurant kitchen where
you repeat the same cooking process for multiple orders.

ANALOGY: Restaurant Kitchen
- for loop = Following a recipe step by step
- while loop = Cooking until timer goes off
- break = Emergency stop (fire alarm!)
- continue = Skip a bad ingredient
- pass = Placeholder while thinking
- else = What to do after finishing

TYPES OF LOOPS:
1. for loops - Iterate over sequences
2. while loops - Continue while condition is true
3. Nested loops - Loops inside loops
4. Loop control statements (break, continue, pass)
5. Loop else clauses
"""

# ==========================================
# 1. FOR LOOPS - Like following a recipe
# ==========================================

print("🍳 FOR LOOPS - Following a Recipe")
print("=" * 40)

# Basic for loop with range
print("📋 Basic range() - Count from 0 to 9:")
for i in range(10):  # range(10) = [0,1,2,3,4,5,6,7,8,9]
    print(f"Step {i}: Mix ingredients")
print()

# Range with start and stop
print("📋 Range with start and stop - Count from 5 to 14:")
for i in range(5, 15):  # Start at 5, stop before 15
    print(f"Cooking timer: {i} minutes")
print()

# Range with start, stop, and step
print("📋 Range with step - Every other number:")
for i in range(1, 11, 2):  # Start 1, stop before 11, step by 2
    print(f"Odd number: {i}")
print()

# For loop with enumerate - Like numbering recipe steps
print("📋 Enumerate - Numbering recipe steps:")
ingredients = ["flour", "eggs", "milk", "sugar", "butter"]
for step_number, ingredient in enumerate(ingredients, 1):
    print(f"Step {step_number}: Add {ingredient}")
print()

# For loop over list directly
print("📋 Loop over list directly:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"🍎 Washing {fruit}")
print()

# For loop over string
print("📋 Loop over string (characters):")
word = "Python"
for letter in word:
    print(f"📝 Letter: {letter}")
print()

# ==========================================
# 2. WHILE LOOPS - Like cooking until done
# ==========================================

print("⏰ WHILE LOOPS - Cooking Until Done")
print("=" * 40)

# Basic while loop
print("📋 Basic while loop - Count to 5:")
counter = 1
while counter <= 5:
    print(f"Attempt #{counter}: Trying recipe")
    counter += 1
print("✅ Recipe successful!")
print()

# While loop with user input
print("📋 While with input - Keep asking until correct:")
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("✅ Access granted!")
        break
    else:
        attempts += 1
        print(f"❌ Wrong password. {3-attempts} attempts left.")

if attempts >= 3:
    print("🚫 Account locked!")
print()

# ==========================================
# 3. LOOP CONTROL STATEMENTS
# ==========================================

print("🎛️ LOOP CONTROL - Kitchen Emergency Controls")
print("=" * 40)

# BREAK - Emergency stop (like fire alarm)
print("🚨 BREAK - Stop when we find what we need:")
shopping_list = ["bread", "milk", "eggs", "butter", "cheese"]
found_item = None

for item in shopping_list:
    print(f"🔍 Checking: {item}")
    if item == "eggs":
        found_item = item
        print(f"✅ Found {item}! Stopping search.")
        break  # Emergency stop!

print(f"🎯 Result: Found {found_item}")
print()

# CONTINUE - Skip bad ingredients
print("⏭️ CONTINUE - Skip spoiled ingredients:")
ingredients = ["fresh_tomato", "rotten_apple", "fresh_onion", "bad_carrot", "fresh_garlic"]

print("🧹 Sorting ingredients:")
for ingredient in ingredients:
    if "rotten" in ingredient or "bad" in ingredient:
        print(f"🗑️ Skipping {ingredient}")
        continue  # Skip this one, go to next

    print(f"✅ Using {ingredient}")
print()

# PASS - Placeholder while thinking
print("🤔 PASS - Placeholder for future code:")
tasks = ["plan_menu", "buy_ingredients", "cook_dinner", "clean_kitchen"]

for task in tasks:
    print(f"📝 Task: {task}")
    if task == "cook_dinner":
        pass  # TODO: Add cooking logic later
        print("   ⏳ Cooking logic coming soon...")
    else:
        print("   ✅ Task completed")
print()

# ==========================================
# 4. LOOP ELSE CLAUSES
# ==========================================

print("🎯 LOOP ELSE - What happens after the loop")
print("=" * 40)

# For loop with else - Like "what to do after cooking"
print("🍳 For-else - What to do after following recipe:")
recipe_steps = ["mix_ingredients", "heat_pan", "cook_pancake", "flip_pancake"]

for step in recipe_steps:
    print(f"👨‍🍳 {step}")
else:
    print("✅ Recipe completed! Time to eat!")
print()

# While-else
print("⏰ While-else - What to do when timer runs out:")
timer = 5
while timer > 0:
    print(f"⏲️ {timer} minutes remaining...")
    timer -= 1
else:
    print("⏰ Timer finished! Check the food!")
print()

# Break prevents else execution
print("🚨 Break prevents else - Emergency stop:")
numbers = [1, 2, 3, 4, 5, 99, 6, 7, 8]
for num in numbers:
    print(f"🔢 Checking: {num}")
    if num == 99:
        print("🚨 Found error! Stopping.")
        break
else:
    print("✅ All numbers checked - no errors found!")
print()

# ==========================================
# 5. NESTED LOOPS - Loops inside loops
# ==========================================

print("🔄 NESTED LOOPS - Complex Cooking")
print("=" * 40)

# Nested loops - Like cooking multiple dishes with multiple steps
print("👨‍🍳 Cooking multiple dishes:")
dishes = ["pasta", "salad", "dessert"]
steps = ["prep", "cook", "serve"]

for dish in dishes:
    print(f"\n🍽️ Preparing {dish}:")
    for step in steps:
        print(f"   {step.capitalize()}ing {dish}...")
print()

# Multiplication table - Like recipe scaling
print("📊 Multiplication table (nested loops):")
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        product = i * j
        print(f"{i}×{j}={product}", end="\t")
    print()  # New line after each row
print()

# Pattern printing - Like arranging ingredients
print("🎨 Pattern with nested loops:")
for i in range(5):
    for j in range(i + 1):
        print("⭐", end="")
    print()
print()

# ==========================================
# 6. INFINITE LOOPS & SAFETY
# ==========================================

print("⚠️ INFINITE LOOPS - Dangerous but Useful")
print("=" * 40)

# Controlled infinite loop (like a restaurant that's always open)
print("🏪 Restaurant that's always open (with exit condition):")
customers_served = 0

while True:  # Infinite loop
    customers_served += 1
    print(f"👥 Served customer #{customers_served}")

    # Safety exit condition
    if customers_served >= 5:
        print("🏁 Closing time!")
        break
print()

# Infinite loop with user control
print("🎮 User-controlled infinite loop:")
attempts = 0
while True:
    response = input("Continue? (y/n): ").lower()
    attempts += 1

    if response == 'n':
        print(f"👋 Goodbye after {attempts} attempts!")
        break
    elif response == 'y':
        print(f"🔄 Continuing... (attempt {attempts})")
    else:
        print("❓ Please enter 'y' or 'n'")
print()

# ==========================================
# 7. PRACTICAL EXAMPLES
# ==========================================

print("🍽️ PRACTICAL EXAMPLES - Real Cooking Scenarios")
print("=" * 40)

# Example 1: Restaurant menu iteration
print("📖 Restaurant Menu Processing:")
menu = {
    "appetizers": ["soup", "salad", "breadsticks"],
    "mains": ["pasta", "steak", "fish"],
    "desserts": ["cake", "ice_cream", "fruit"]
}

for course, dishes in menu.items():
    print(f"\n🍽️ {course.upper()}:")
    for dish in dishes:
        print(f"   • {dish.replace('_', ' ').title()}")
print()

# Example 2: Inventory checking with break
print("📦 Inventory Check (stop when out of stock):")
inventory = ["flour", "eggs", "milk", "sugar", "butter", "vanilla"]
needed_items = ["flour", "eggs", "vanilla"]

print("🔍 Checking for needed ingredients:")
for item in needed_items:
    if item not in inventory:
        print(f"❌ Out of stock: {item}")
        break
    else:
        print(f"✅ Found: {item}")
else:
    print("🎉 All ingredients available!")
print()

# Example 3: Quality control with continue
print("🔬 Quality Control (skip defective items):")
products = ["good_apple", "bad_apple", "good_banana", "rotten_orange", "good_grape"]
quality_products = []

for product in products:
    if "bad" in product or "rotten" in product:
        print(f"🗑️ Discarding {product}")
        continue
    quality_products.append(product)
    print(f"✅ Approved {product}")

print(f"\n📊 Quality products: {quality_products}")
print()

# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON LOOPS SUMMARY")
print("=" * 40)
print("✅ for loops: Iterate over sequences (like recipe steps)")
print("✅ while loops: Continue while condition is true (like cooking timer)")
print("✅ break: Emergency exit (like fire alarm)")
print("✅ continue: Skip current iteration (like bad ingredient)")
print("✅ pass: Placeholder for future code")
print("✅ else: Execute after loop completes normally")
print("✅ nested loops: Loops inside loops (complex recipes)")
print()
print("💡 Loops are like cooking instructions - they help you repeat")
print("   actions efficiently, just like a kitchen handles multiple orders!")