#!/usr/bin/env python3
"""
ERROR HANDLING IN PYTHON - Complete Guide
==========================================

Errors happen in programming. Learning to handle them gracefully
is like being a professional chef who knows how to fix mistakes.

ANALOGY: Restaurant Kitchen Accidents
- Errors = Kitchen accidents (burnt food, dropped plates)
- Try/Except = Safety protocols (fire extinguishers, backup plans)
- Finally = Cleanup procedures (washing dishes, closing kitchen)
- Raise = Calling for help when something goes wrong

WHY ERROR HANDLING MATTERS:
- Programs crash less often
- Better user experience
- Easier debugging
- Professional code quality
"""

# ==========================================
# 1. UNDERSTANDING ERRORS
# ==========================================

print("💥 UNDERSTANDING ERRORS - Kitchen Accidents")
print("=" * 50)

print("🔍 Common Python errors:")
print("1. ZeroDivisionError - Dividing by zero")
print("2. ValueError - Wrong value type")
print("3. KeyError - Missing dictionary key")
print("4. IndexError - List index out of range")
print("5. TypeError - Wrong data type operation")
print("6. FileNotFoundError - File doesn't exist")
print()


# Examples of errors (commented out to avoid crashes)
print("🚨 Examples of errors that would crash:")

# ZeroDivisionError
# result = 10 / 0  # Division by zero

# ValueError
# number = int("not_a_number")  # Can't convert text to number

# KeyError
# person = {"name": "Alice"}
# age = person["age"]  # Key doesn't exist

# IndexError
# fruits = ["apple", "banana"]
# fruit = fruits[5]  # Index 5 doesn't exist (only 0,1)

print("These would crash the program... unless we handle them!")
print()

# ==========================================
# 2. BASIC TRY/EXCEPT
# ==========================================

print("🛡️ BASIC TRY/EXCEPT - Safety Nets")
print("=" * 50)

print("🔧 Basic error handling structure:")
print("""
try:
    # Code that might cause an error
    risky_code()
except ErrorType:
    # What to do if error occurs
    handle_error()
""")


# Example 1: Division with error handling
print("📐 Example 1: Safe division")
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"✅ {numerator} ÷ {denominator} = {result}")
        return result
    except ZeroDivisionError:
        print(f"❌ Cannot divide {numerator} by zero!")
        return None

safe_divide(10, 2)  # Works fine
safe_divide(10, 0)  # Handles error gracefully
print()

#Example 2: Safe number conversion
print("🔢 Example 2: Safe number conversion")
def safe_convert_to_int(text):
    try:
        number = int(text)
        print(f"✅ '{text}' converted to {number}")
        return number
    except ValueError:
        print(f"❌ '{text}' is not a valid number!")
        return None

safe_convert_to_int("42")      # Works
safe_convert_to_int("hello")   # Error handled
safe_convert_to_int("")        # Error handled
print()



# ==========================================
# 3. MULTIPLE EXCEPT BLOCKS
# ==========================================

print("🎯 MULTIPLE EXCEPT BLOCKS - Different Safety Measures")
print("=" * 50)

def process_user_data(user_input):
    """
    Process user data with different error handling for each type.

    ANALOGY: Different kitchen stations handle different types of accidents
    - Division errors = Math station
    - Value errors = Input validation station
    - General errors = Emergency response team
    """
    try:
        # Step 1: Convert to number
        number = int(user_input)

        # Step 2: Use in calculation
        result = 100 / number

        # Step 3: Convert back to string
        message = f"Result: {result}"

        print(f"✅ Processing successful: {message}")
        return message

    except ValueError:
        print("❌ ValueError: Please enter a valid number!")
        return None

    except ZeroDivisionError:
        print("❌ ZeroDivisionError: Cannot divide by zero!")
        return None

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

print("🧪 Testing different error types:")
process_user_data("10")     # Success
process_user_data("0")      # Zero division
process_user_data("hello")  # Value error
process_user_data("")       # Value error
print()



# ==========================================
# 4. ELSE AND FINALLY BLOCKS
# ==========================================

print("🎉 ELSE AND FINALLY - Success & Cleanup")
print("=" * 50)

def process_order(order_data):
    """
    Process a restaurant order with complete error handling.

    ANALOGY: Restaurant order processing
    - Try = Attempt to prepare order
    - Except = Handle preparation problems
    - Else = Order completed successfully
    - Finally = Clean up regardless of outcome
    """
    order_complete = False

    try:
        print(f"👨‍🍳 Starting order: {order_data}")

        # Simulate processing steps
        customer_name = order_data["customer"]
        items = order_data["items"]

        # This could fail if keys missing
        total = sum(order_data["prices"])

        print(f"✅ Order for {customer_name}: {items}")
        print(f"💰 Total: ${total:.2f}")

        order_complete = True

    except KeyError as e:
        print(f"❌ Missing order information: {e}")

    except TypeError as e:
        print(f"❌ Wrong data type: {e}")

    else:
        # Only runs if no exception occurred
        print("🎉 Order processed successfully!")

    finally:
        # Always runs, regardless of success/failure
        print("🧹 Cleaning up order processing...")
        if order_complete:
            print("📧 Sending confirmation email...")
        else:
            print("📞 Calling customer about order issue...")
        print("🏁 Order processing complete.\n")

# Test successful order
print("✅ Testing successful order:")
process_order({
    "customer": "Alice",
    "items": ["pizza", "salad"],
    "prices": [15.99, 8.50]
})

# Test failed order (missing key)
print("❌ Testing failed order:")
process_order({
    "customer": "Bob",
    "items": ["pasta"]
    # Missing "prices" key
})



# ==========================================
# 5. RAISING EXCEPTIONS
# ==========================================

print("🚨 RAISING EXCEPTIONS - Calling for Help")
print("=" * 50)

def validate_age(age):
    """
    Validate age with custom error messages.

    ANALOGY: Bouncer at a club - checking if someone meets requirements
    If they don't qualify, "raise" them out (politely)
    """
    if not isinstance(age, int):
        raise TypeError("Age must be a number!")

    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age < 18:
        raise ValueError("Must be 18 or older!")

    return f"✅ Age {age} is valid!"

def register_user(name, age_input):
    """
    Register a user with age validation.

    ANALOGY: Customer registration process
    - Try to validate age
    - Handle validation failures
    - Proceed if validation passes
    """
    try:
        age = int(age_input)  # Convert string to int
        result = validate_age(age)
        print(f"✅ {name} registered successfully!")
        return True

    except ValueError as e:
        print(f"❌ Registration failed: {e}")
        return False

    except TypeError as e:
        print(f"❌ Registration failed: {e}")
        return False

print("📝 Testing user registration:")
register_user("Alice", "25")     # Success
register_user("Bob", "17")       # Too young
register_user("Charlie", "-5")   # Negative age
register_user("David", "not_number")  # Invalid input
print()



# ==========================================
# 6. CUSTOM EXCEPTIONS
# ==========================================

print("🎨 CUSTOM EXCEPTIONS - Specialized Error Handling")
print("=" * 50)

class KitchenError(Exception):
    """Base class for kitchen-related errors."""
    pass

class OutOfIngredientsError(KitchenError):
    """Raised when ingredients are not available."""
    def __init__(self, ingredient, needed, available):
        self.ingredient = ingredient
        self.needed = needed
        self.available = available
        super().__init__(f"Out of {ingredient}! Needed: {needed}, Available: {available}")

class BurntFoodError(KitchenError):
    """Raised when food is overcooked."""
    pass

def cook_dish(dish_name, ingredients_needed, cook_time):
    """
    Cook a dish with custom error handling.

    ANALOGY: Professional kitchen with specific error types
    - OutOfIngredientsError = Inventory problem
    - BurntFoodError = Cooking mistake
    """
    # Check inventory
    inventory = {
        "pasta": 10,
        "tomatoes": 5,
        "cheese": 8,
        "flour": 0  # Out of flour!
    }

    for ingredient, needed in ingredients_needed.items():
        available = inventory.get(ingredient, 0)
        if available < needed:
            raise OutOfIngredientsError(ingredient, needed, available)

    # Simulate cooking
    if cook_time > 20:
        raise BurntFoodError(f"{dish_name} is burnt! Cook time too long.")

    return f"✅ {dish_name} cooked perfectly!"

def handle_kitchen_order(dish_name, ingredients, cook_time):
    """Handle kitchen order with proper error handling."""
    try:
        result = cook_dish(dish_name, ingredients, cook_time)
        print(result)

    except OutOfIngredientsError as e:
        print(f"🍽️ Inventory Issue: {e}")
        print("   Please restock ingredients!")

    except BurntFoodError as e:
        print(f"🔥 Cooking Error: {e}")
        print("   Try shorter cooking time!")

    except Exception as e:
        print(f"❌ Unexpected kitchen error: {e}")

print("👨‍🍳 Testing kitchen orders:")
# Success case
handle_kitchen_order("pasta", {"pasta": 2, "tomatoes": 1}, 15)

# Out of ingredients
handle_kitchen_order("pizza", {"flour": 3, "cheese": 1}, 20)

# Burnt food
handle_kitchen_order("steak", {"pasta": 1}, 30)
print()




# ==========================================
# 7. PRACTICAL ERROR HANDLING PATTERNS
# ==========================================

print("🏪 PRACTICAL PATTERNS - Real-World Error Handling")
print("=" * 50)

# Pattern 1: Safe file operations
def safe_read_file(filename):
    """Safely read a file with proper error handling."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ No permission to read '{filename}'!")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

# Pattern 2: Safe API-like operations
def safe_api_call(url, retries=3):
    """
    Simulate safe API call with retries.

    ANALOGY: Restaurant calling supplier with backup plans
    """
    import time  # Simulate network delay

    for attempt in range(retries):
        try:
            # Simulate API call
            time.sleep(0.1)
            if attempt == 1:  # Simulate failure on second attempt
                raise ConnectionError("Network timeout")

            return f"✅ API call to {url} successful!"

        except ConnectionError as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                print("🔄 Retrying...")
                time.sleep(0.5)
            else:
                print("💥 All retries failed!")
                return None

# Pattern 3: Resource cleanup
def process_with_cleanup(data):
    """Process data with guaranteed cleanup."""
    resource = None

    try:
        # Acquire resource
        resource = f"Resource for {data}"
        print(f"📎 Acquired: {resource}")

        # Process data (simulate)
        if data == "error":
            raise ValueError("Processing failed!")

        result = f"✅ Processed: {data}"
        print(result)
        return result

    except Exception as e:
        print(f"❌ Processing error: {e}")
        return None

    finally:
        # Always cleanup (like closing kitchen)
        if resource:
            print(f"🧹 Cleaned up: {resource}")
        print("🏁 Process complete\n")

print("🧪 Testing practical patterns:")

# File operations
safe_read_file("existing_file.txt")
safe_read_file("nonexistent_file.txt")

# API calls
safe_api_call("api.example.com")

# Resource cleanup
process_with_cleanup("good_data")
process_with_cleanup("error")



# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON ERROR HANDLING SUMMARY")
print("=" * 50)
print("✅ try/except: Basic error catching")
print("   try: risky code")
print("   except ErrorType: handle error")
print()
print("✅ Multiple except: Different handlers for different errors")
print("   except ValueError: handle value errors")
print("   except ZeroDivisionError: handle math errors")
print()
print("✅ else: Code that runs only if no errors")
print("✅ finally: Code that always runs (cleanup)")
print()
print("✅ raise: Throw your own errors")
print("   raise ValueError('Custom message')")
print()
print("✅ Custom exceptions: Create specific error types")
print("   class MyError(Exception): pass")
print()
print("💡 Error handling makes your programs robust and user-friendly!")
print("   Users see helpful messages instead of crashes.")

































