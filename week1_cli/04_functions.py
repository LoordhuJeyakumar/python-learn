#!/usr/bin/env python3
"""
FUNCTIONS IN PYTHON - Complete Guide
====================================

Functions are reusable blocks of code that perform specific tasks.
Like recipes in cooking - you can call them whenever you need them.

ANALOGY: Restaurant Kitchen
- Function definition = Writing a recipe
- Function call = Using the recipe to cook
- Parameters = Ingredients you provide
- Return value = Finished dish
- Docstrings = Recipe instructions

WHY FUNCTIONS MATTER:
- Code reuse (don't repeat yourself)
- Organization (break complex tasks into smaller ones)
- Testing (test each function separately)
- Readability (self-documenting code)
"""


# ==========================================
# 1. BASIC FUNCTION DEFINITION & CALLING
# ==========================================

print("🍳 BASIC FUNCTIONS - Simple Recipes")
print("=" * 40)

# Function definition (for example its like a writing a recipe)

def greet_customer():
    """
    Greet a customer - like a standard restaurant greeting.

    ANALOGY: A simple greeting script that staff memorize.
    No ingredients needed, just performs an action.
    """
    print("Welcome to Python Kitchen! 🏪")
    print("How can I help you today?")

# Function call (like using the recipe to cook)
greet_customer()


# ==========================================
# 2. FUNCTIONS WITH PARAMETERS
# ==========================================

print("🍳 FUNCTIONS WITH PARAMETERS - Custom Recipes")
print("=" * 40)

# Function definition with parameters (like a recipe that takes ingredients)

def greet_customer_name(name):
    """
    Greet a customer by name.

    ANALOGY: Personalized greeting with customer's name.
    Like adding a name tag to the standard greeting.

    Args:
        name (str): The customer's name
    """
    print(f"Welcome to Python Kitchen, {name}! 🏪")
    print("How can I help you today?")

print("👨‍🍳 Calling greet_customer_name('Alice'):")
greet_customer_name("Alice")
print()


# Function with multiple parameters (optional quantity)

def prepare_order(customer_name, dish_name, quantity=1):
    """
    Prepare a customer order.

    ANALOGY: Taking an order with customer details.
    Like a waiter writing down what the customer wants.

    Args:
        customer_name (str): Name of the customer
        dish_name (str): Name of the dish ordered
        quantity (int): How many servings (default 1)
    """
    print(f"📝 Order received for {customer_name}:")
    print(f"   🍽️ {quantity}x {dish_name}")
    print("   ⏳ Preparing your order...")

print("👨‍🍳 Calling prepare_order('Alice', 'Pizza', 2):")
prepare_order("Alice", "Pizza", 2)
print()


# ==========================================
# 3. FUNCTIONS WITH RETURN VALUES
# ==========================================

print("🍽️ FUNCTIONS WITH RETURN VALUES - Recipes That Produce Food")
print("=" * 40)

def calculate_bill(price_per_item, quantity, tax_rate=0.08):
    """
    Calculate the total bill including tax.

    ANALOGY: Cashier calculating the final amount.
    Takes inputs, performs calculation, returns result.

    Args:
        price_per_item (float): Price of one item
        quantity (int): Number of items
        tax_rate (float): Tax rate as decimal (default 8%)

    Returns:
        float: Total amount including tax
    """
    subtotal = price_per_item * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    return total  # Give result back to caller


# Using the return value
print("🧾 Calculating bills:")
bill1 = calculate_bill(1585.99, 2)  # Pizza
bill2 = calculate_bill(850.50, 1, 0.10)  # With 10% tax

print(f"🧾 Total for 2 pizzas: ${bill1:,.2f}") # Format the bill with 2 decimal places and a comma separator
print(f"🧾 Total for 1 coffee with 10% tax: ${bill2:,.2f}") # Format the bill with 2 decimal places and a comma separator
print()


# ==========================================
# 5. FUNCTION SCOPE (Local vs Global)
# ==========================================

print("🍳 FUNCTION SCOPE (Local vs Global) - Recipes That Produce Food")
print("=" * 40)

# global variable (it's like available in the entire program and it can be accessed by all the functions)

kitchen_open = True
total_orders_today = 0

# function definition (it's like a recipe that takes an order and updates the global counter)
def take_order(dish_name, price, quantity=1):
    """
    Take a customer order and update global counter.

    ANALOGY: Each station updates the shared order counter.
    Shows how functions can access and modify global variables.
    """
    global total_orders_today  # Declare we want to modify global
    
    # local variable (it's like a ingredient that is only available in the function)
    total_price = price * quantity
    print(f"📝 Order: {dish_name} - ${total_price}")
    total_orders_today += 1
    print(f"📊 Total orders today: {total_orders_today}")
    return total_price

# function call (it's like using the recipe to cook)
take_order("Pizza", 1585.99)
print()

# function call (it's like using the recipe to cook)
take_order("Coffee", 850.50)
print()


def close_kitchen():
    """
    Close the kitchen and print the total orders.
    """
    global kitchen_open
    kitchen_open = False
    print("🔒 Kitchen is closed. Thank you for your visit!")
    print(f"📊 Total orders today: {total_orders_today}")
    return total_orders_today

# function call (it's like using the recipe to cook)
close_kitchen()
print()


# ==========================================
# 6. FUNCTIONS RETURNING MULTIPLE VALUES
# ==========================================


print("📦 FUNCTIONS RETURNING MULTIPLE VALUES - Complete Meal Prep")
print("=" * 40)

def prepare_meal(main_dish, side_dish, drink="Water"):
    """
    Prepare a complete meal.

   ANALOGY: A function that prepares multiple dishes at once.
    Like a meal prep service that returns a complete plate.

    Args:
        main_dish (str): The main dish (required)
        side_dish (str): The side dish (required)
        drink (str): The drink (default Water)

    returns:
        tuple: (main_dish, side_dish, drink)
        - The main dish is the main dish of the meal
        - The side dish is the side dish of the meal
        - The drink is the drink of the meal
    """

    # Simulate preparation times
    prep_times = {"pizza": 20, "pasta": 15, "salad": 5} # Dictionary of preparation times for different dishes
    main_time = prep_times.get(main_dish, 10) # Get the preparation time for the main dish, if not found, use 10 minutes
    side_time = 5  # Sides are quick
    total_time = main_time + side_time

    print(f"👨‍🍳 Preparing: {main_dish} + {side_dish} + {drink}")
    print(f"⏰ Total prep time: {total_time} minutes")

    return main_dish,side_dish,drink,total_time

# function call (it's like using the recipe to cook)
result = prepare_meal("Pizza", "Salad", "Water")

main_dish, side_dish, drink, total_time = result
print(f"🍽️ Meal ready: {main_dish} + {side_dish} + {drink}")
print(f"⏰ Total prep time: {total_time} minutes")
print()

# function call (it's like using the recipe to cook)
result = prepare_meal("Pasta", "Salad", "Water")

main_dish, side_dish, drink, total_time = result
print(f"🍽️ Meal ready: {main_dish} + {side_dish} + {drink}")
print(f"⏰ Total prep time: {total_time} minutes")
print()


# ==========================================
# 7. FUNCTION DOCUMENTATION (Docstrings)
# ==========================================



print("📚 FUNCTION DOCUMENTATION - Recipe Instructions")
print("=" * 40)

def complex_recipe(name, ingredients, cooking_method, temperature=350, time_minutes=30):
    """
    Prepare a complex recipe with detailed instructions.

    This function demonstrates comprehensive documentation.
    Like a professional recipe book with all details.

    Args:
        name (str): Name of the dish to prepare
        ingredients (list): List of ingredients needed
        cooking_method (str): How to cook (bake, fry, boil, etc.)
        temperature (int): Cooking temperature in Fahrenheit (default 350)
        time_minutes (int): Cooking time in minutes (default 30)

    Returns:
        dict: Recipe summary with all details

    Raises:
        ValueError: If cooking method is invalid

    Example:
        >>> result = complex_recipe("chocolate cake",
        ...                        ["flour", "sugar", "eggs"],
        ...                        "bake", 350, 45)
        >>> print(result["status"])
        "Successfully prepared chocolate cake"
    """
    # Validate inputs
    valid_methods = ["bake", "fry", "boil", "steam", "grill"]
    if cooking_method not in valid_methods:
        raise ValueError(f"Invalid cooking method. Must be one of: {valid_methods}")

    # Simulate cooking
    print(f"👨‍🍳 Preparing {name} using {cooking_method} method")
    print(f"🌡️ Temperature: {temperature}°F")
    print(f"⏰ Time: {time_minutes} minutes")
    print("🥕 Ingredients used:")
    for ingredient in ingredients:
        print(f"   • {ingredient}")

    # Return summary
    return {
        "dish_name": name,
        "method": cooking_method,
        "temperature": temperature,
        "cooking_time": time_minutes,
        "ingredients_used": len(ingredients),
        "status": f"Successfully prepared {name}"
    }

print("📖 Using well-documented function:")
try:
    recipe_result = complex_recipe(
        name="lasagna",
        ingredients=["pasta", "ground beef", "cheese", "tomato sauce"],
        cooking_method="bake",
        temperature=375,
        time_minutes=45
    )
    print(f"✅ {recipe_result['status']}")
except ValueError as e:
    print(f"❌ Error: {e}")
print()



# ==========================================
# 8. PRACTICAL FUNCTION EXAMPLES
# ==========================================

print("🏪 PRACTICAL EXAMPLES - Real Restaurant Functions")
print("=" * 40)

def validate_menu_item(item_name, menu):
    """
    Check if an item is on the menu.

    ANALOGY: Waiter checking if customer ordered something we serve.
    """
    return item_name.lower() in [item.lower() for item in menu]

def calculate_tip(bill_amount, tip_percentage=15):
    """
    Calculate tip amount.

    ANALOGY: Calculating gratuity for service.
    """
    return bill_amount * (tip_percentage / 100)

def format_receipt(customer_name, items, prices):
    """
    Format a restaurant receipt.

    ANALOGY: Cashier printing the final bill.
    """
    print(f"\n🧾 RECEIPT FOR {customer_name.upper()}")
    print("=" * 40)

    subtotal = 0
    for item, price in zip(items, prices):
        print(f"   🍽️ {item} - ${price:,.2f}")
        subtotal += price

    tip = calculate_tip(subtotal)
    total = subtotal + tip

    print(f"   💰 Subtotal: ${subtotal:,.2f}")
    print(f"   💰 Tip: ${tip:,.2f}")
    print(f"   💰 Total: ${total:,.2f}")
    print("=" * 40)

# Test the practical functions
menu = ["pizza", "pasta", "salad", "dessert"]
print("🔍 Menu validation:")
print(f"Is 'pizza' on menu? {validate_menu_item('pizza', menu)}")
print(f"Is 'burger' on menu? {validate_menu_item('burger', menu)}")
print()

print("🧾 Receipt formatting:")
format_receipt(
    "Alice Johnson",
    ["Margherita Pizza", "Caesar Salad", "Tiramisu"],
    [18.99, 8.50, 6.99]
)

# ==========================================
# 9. FUNCTION COMPOSITION => Building Complex Recipes From Simple Ones (like a master chef coordinating multiple kitchen stations)
# one function calls another function to build a more complex dish
# ==========================================

print("🔗 FUNCTION COMPOSITION - Building Complex Recipes")
print("=" * 40)

def chop_vegetables(vegetables):
    """Step 1: Chop vegetables."""
    chopped = [f"chopped_{veg}" for veg in vegetables]
    print(f"🥕 Chopped: {chopped}")
    return chopped

def cook_sauce(base, spices):
    """Step 2: Cook sauce."""
    sauce = f"{base}_sauce_with_{'_'.join(spices)}"
    print(f"🍅 Cooked: {sauce}")
    return sauce

def assemble_pasta(pasta_type, sauce, vegetables):
    """Step 3: Assemble the final dish."""
    dish = f"{pasta_type}_with_{sauce}_and_{'_'.join(vegetables)}"
    print(f"🍝 Assembled: {dish}")
    return dish

def make_pasta_dish(pasta_type, vegetables, base_sauce, spices):
    """
    Complete pasta preparation using function composition.

    ANALOGY: A master chef coordinating multiple kitchen stations.
    Each function does one job, then passes result to next function.
    """
    print(f"👨‍🍳 Making {pasta_type} dish...")

    # Step 1: Prep vegetables (function call)
    chopped_veggies = chop_vegetables(vegetables)

    # Step 2: Make sauce (function call)
    sauce = cook_sauce(base_sauce, spices)

    # Step 3: Assemble (function call)
    final_dish = assemble_pasta(pasta_type, sauce, chopped_veggies)

    return final_dish

print("🔗 Function composition example:")
result = make_pasta_dish(
    pasta_type="spaghetti",
    vegetables=["onions", "garlic", "mushrooms"],
    base_sauce="tomato",
    spices=["basil", "oregano"]
)
print(f"✅ Final dish: {result}")
print()
