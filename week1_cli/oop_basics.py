#!/usr/bin/env python3
"""
OBJECT-ORIENTED PROGRAMMING BASICS - Complete Guide
===================================================

OOP is a programming paradigm that organizes code around objects and data.
Like a restaurant kitchen where each station (object) has its own tools and responsibilities.

ANALOGY: Restaurant Kitchen Stations
- Class = Station blueprint (grill station, prep station)
- Instance = Actual station (grill station #1, prep station #2)
- Methods = Station tools/actions (chop, grill, mix)
- Attributes = Station equipment/data (knives, oven temperature)
- Inheritance = Station specialization (sushi station inherits from prep station)

WHY OOP MATTERS:
- Code organization (related data and functions together)
- Reusability (create similar objects easily)
- Maintainability (changes isolated to specific objects)
- Real-world modeling (objects represent real things)
"""

# ==========================================
# 1. CLASSES AND INSTANCES
# ==========================================

print("🏗️ CLASSES AND INSTANCES - Station Blueprints")
print("=" * 50)


# Class is a blueprint for creating objects.
# Instance is a specific object created from a class.
# Methods are functions that are defined inside a class.
# Attributes are variables that are defined inside a class.
# Inheritance is a way to inherit attributes and methods from a parent class.

# Example of a class
class KitchenStation:
    """
    A kitchen station in a restaurant.

    ANALOGY: Blueprint for any kitchen station
    Defines what every station should have and do.
    """

    def __init__(self, name: str, station_type: str):
        """
        Constructor - Initialize a new station.

        ANALOGY: Setting up a new station with equipment
        Called automatically when creating a station instance.

        Args:
            name: Name of the station (e.g., "Grill Station #1")
            station_type: Type of station (e.g., "grill", "prep")
        """
        self.name = name                    # Station name
        self.station_type = station_type    # Type of station
        self.is_operational = True          # Is station working?
        self.tools = []                     # Tools available
        print(f"🏗️ Built {self.name} ({self.station_type} station)")
    
    def add_tool(self, tool: str):
        """
        Add a tool to the station.

        ANALOGY: Adding a tool to a station
        Returns a list of tools available.
        """
        self.tools.append(tool)
        print(f"🔧 Added {tool} to {self.name}")
        return self.tools
    
    def get_status(self) -> str:
        """
        Get the current status of the station.

        ANALOGY: Checking if station is ready to operate
        """
        status = "✅ Operational" if self.is_operational else "❌ Out of order"
        return f"{self.name}: {status}"
    

# Creating instances (actual stations)
print("🏪 Creating kitchen stations:")

# Creating instances of the class (actual stations in the kitchen)

# Instance 1: Grill Station #1
grill_station = KitchenStation(name="Grill Station #1", station_type="grill")
grill_station.add_tool("Grill")
grill_station.add_tool("thermometer")
grill_station.add_tool("tongs")


#instance 2: Prep Station #1
prep_station = KitchenStation(name="Prep Station #1", station_type="prep")
prep_station.add_tool("Knife")
prep_station.add_tool("cutting board")
prep_station.add_tool("bowl")


print(f"\nGrill station tools: {grill_station.tools}")
print(f"Prep station tools: {prep_station.tools}")
print(f"Grill station status: {grill_station.get_status()}")
print()



# ==========================================
# 2. INSTANCE VARIABLES VS CLASS VARIABLES
# ==========================================

print("📊 INSTANCE VS CLASS VARIABLES - Personal vs Shared Equipment")
print("=" * 50)

class RestaurantEmployee:
    """
    A restaurant employee.

    Shows difference between instance variables (personal)
    and class variables (shared by all employees).
    """

    #Class variable (shared by all employees)
    restaurant_name = "Pythonic Restaurant" # same for all instances
    minimum_wage = 12.50 # same for all instances
    employee_count = 0 # same for all instances

 
    def __init__(self, name: str, role: str, hourly_rate: float):
        # Instance variables (unique to each employee)
        self.name = name                # Personal name
        self.role = role                # Personal role
        self.hourly_rate = hourly_rate  # Personal rate
        self.hours_worked = 0           # Personal hours

        # Update class variable
        RestaurantEmployee.employee_count += 1
        print(f"👤 Hired {self.name} as {self.role}")

    def work_shift(self, hours: float):
        """Work a shift and track hours."""
        self.hours_worked += hours
        print(f"⏰ {self.name} worked {hours} hours (total: {self.hours_worked})")

    def calculate_paycheck(self) -> float:
        """Calculate weekly paycheck."""
        return self.hours_worked * self.hourly_rate

# Creating employees
print("🏪 Hiring restaurant employees:")
chef1 = RestaurantEmployee(name="Alice", role="Chef", hourly_rate=15.0)
chef2 = RestaurantEmployee(name="Bob", role="Chef", hourly_rate=15.0)
waiter1 = RestaurantEmployee(name="Charlie", role="Waiter", hourly_rate=10.0)
waiter2 = RestaurantEmployee(name="Diana", role="Waiter", hourly_rate=10.0)

print(f"\nTotal employees: {RestaurantEmployee.employee_count}")
print(f"Restaurant name: {RestaurantEmployee.restaurant_name}")
print(f"Minimum wage: ${RestaurantEmployee.minimum_wage:.2f}")
print()


print(f"\n👤 Instance variables (personal):")
print(f"Alice's role: {chef1.role}")
print(f"Bob's hourly rate: ${chef2.hourly_rate:.2f}")
print(f"Charlie's hours worked: {waiter1.hours_worked}")
print(f"Diana's total pay: ${waiter2.calculate_paycheck():.2f}")
print()


print(f"\n👥 Class variables (shared):")
print(f"Total employees: {RestaurantEmployee.employee_count}")
print(f"Restaurant name: {RestaurantEmployee.restaurant_name}")
print(f"Minimum wage: ${RestaurantEmployee.minimum_wage:.2f}")
print()



# ==========================================
# 3. METHODS - INSTANCE VS STATIC VS CLASS
# ==========================================

print("🔧 METHODS - Station Tools & Actions")
print("=" * 50)


class MenuItem:
    """
    A menu item with different types of methods.
    """

    #Class variable
    tax_rate = 0.0875 # 8.75 % tax

    def __init__(self, name:str, base_price:float):
        self.name = name
        self.base_price = base_price
        
    # Instance method (works on specific item)
    def calculate_price(self) -> float:
        """Calculate final price with tax."""
        return self.base_price * (1 + MenuItem.tax_rate)

    def describe(self) -> str:
        """Describe this menu item."""
        return f"{self.name}: ${self.calculate_price():.2f}"

    
    @classmethod
    def update_tax_rate(cls, new_rate:float):
        """Update the tax rate for all menu items."""
        cls.tax_rate = new_rate
        print(f"💰 Tax rate updated to {new_rate*100}%")


    # Static method (utility function, no self or cls) => used for utility functions that don't depend on the instance or class
    @staticmethod
    def format_price(price:float) -> str:
        """Format a price as a string with two decimal places."""
        return f"${price:.2f}"


# Using different method types
print("🍽️ Menu item methods:")

pizza = MenuItem("Margherita Pizza", 15.99)
pasta = MenuItem("Spaghetti Carbonara", 12.50)

print(f"Instance method: {pizza.describe()}")
print(f"Instance method: {pasta.describe()}")

print(f"\nStatic method: {MenuItem.format_price(19.99)}")
print(f"Static method: {MenuItem.format_price(pizza.calculate_price())}")

MenuItem.update_tax_rate(0.10)  # Class method
print(f"After tax change: {pizza.describe()}")
print()


# ==========================================
# 4. INHERITANCE - Station Specialization
# ==========================================

print("👪 INHERITANCE - Station Specialization")
print("=" * 50)

# Base class
class KitchenStation:
    """Base kitchen station."""

    def __init__(self, name: str):
        self.name = name
        self.temperature = 70  # Room temperature
        self.is_clean = True

    def heat_up(self, target_temp: int):
        """Heat the station."""
        self.temperature = target_temp
        print(f"🔥 {self.name} heated to {self.temperature}°F")

    def clean(self):
        """Clean the station."""
        self.is_clean = True
        print(f"🧽 {self.name} cleaned")

# Child class (inherits from KitchenStation)
class GrillStation(KitchenStation):
    """Specialized grill station."""

    def __init__(self, name: str, grill_type: str = "gas"):
        # Call parent constructor
        super().__init__(name)
        self.grill_type = grill_type
        self.is_on = False

    def turn_on(self):
        """Turn on the grill."""
        self.is_on = True
        self.heat_up(400)  # Grills need high heat
        print(f"🔥 {self.name} ({self.grill_type} grill) is now ON")

    def grill_item(self, item: str):
        """Grill a menu item."""
        if not self.is_on:
            print(f"❌ {self.name} is not turned on!")
            return

        print(f"🍖 Grilling {item} on {self.name}")


# Another child class
class PrepStation(KitchenStation):
    """Specialized prep station."""

    def __init__(self, name: str):
        super().__init__(name)
        self.tools = ["knife", "cutting_board", "peeler"]

    def chop_vegetable(self, vegetable: str):
        """Chop a vegetable."""
        if not self.is_clean:
            print(f"❌ {self.name} needs cleaning first!")
            return

        print(f"🥕 Chopping {vegetable} at {self.name}")
        self.is_clean = False  # Gets messy when chopping

print("👨‍🍳 Station inheritance:")


# Create specialized stations
grill = GrillStation("Main Grill", "charcoal")
prep = PrepStation("Vegetable Prep")



# Use inherited methods
grill.clean()
prep.heat_up(72)  # Cooler temperature for prep

# Use specialized methods
grill.turn_on()
grill.grill_item("steak")

prep.chop_vegetable("onions")
prep.chop_vegetable("tomatoes")  # Will be messy now
print()




# ==========================================
# 5. ENCAPSULATION - Private Data
# ==========================================

print("🔒 ENCAPSULATION - Private Kitchen Secrets")
print("=" * 50)

class Recipe:
    """
    A recipe with secret ingredients and methods.

    ANALOGY: A chef's secret recipe that outsiders can't modify directly.
    """

    def __init__(self, name: str, secret_ingredient: str):
        self.name = name
        self._secret_ingredient = secret_ingredient  # "Private" (convention)
        self.__cooking_time = 30  # "Very private" (name mangling)

    def get_secret(self):
        """Public method to access secret (controlled access)."""
        return f"The secret ingredient is... {self._secret_ingredient}!"

    def _internal_method(self):
        """Internal method (conventionally private)."""
        return f"Internal: {self.__cooking_time} minutes"

    def cook(self):
        """Public cooking method."""
        secret = self.get_secret()
        time = self._internal_method()
        return f"🍳 Cooking {self.name}: {secret} ({time})"

# Using encapsulation
print("👨‍🍳 Recipe encapsulation:")

carbonara = Recipe("Spaghetti Carbonara", "pecorino cheese")



print(f"Public access: {carbonara.name}")
print(f"Controlled access: {carbonara.get_secret()}")
print(f"Cooking: {carbonara.cook()}")

# Conventionally private (but accessible)
print(f"Conventionally private: {carbonara._secret_ingredient}")

# Name mangling makes it harder to access
# print(carbonara.__cooking_time)  # Would fail
print(f"Name mangled: {carbonara._Recipe__cooking_time}")  # Still accessible
print()




# ==========================================
# 6. POLYMORPHISM - Same Interface, Different Behavior
# ==========================================

print("🎭 POLYMORPHISM - Same Tools, Different Results")
print("=" * 50)

class KitchenTool:
    """Base kitchen tool."""

    def __init__(self, name: str):
        self.name = name

    def use(self) -> str:
        """Use the tool (to be overridden by subclasses)."""
        return f"Using {self.name}"

class Knife(KitchenTool):
    """A knife tool."""

    def use(self) -> str:
        return f"🗡️ Cutting with {self.name}"

class Spoon(KitchenTool):
    """A spoon tool."""

    def use(self) -> str:
        return f"🥄 Stirring with {self.name}"

class Oven(KitchenTool):
    """An oven tool."""

    def __init__(self, name: str, temperature: int = 350):
        super().__init__(name)
        self.temperature = temperature

    def use(self) -> str:
        return f"🔥 Baking in {self.name} at {self.temperature}°F"

# Polymorphism in action
def demonstrate_tool(tool: KitchenTool):
    """Demonstrate any kitchen tool (polymorphism)."""
    print(tool.use())

print("🛠️ Polymorphism demonstration:")

tools = [
    Knife("Chef's Knife"),
    Spoon("Wooden Spoon"),
    Oven("Convection Oven", 375)
]

for tool in tools:
    demonstrate_tool(tool)  # Same method, different behavior

print()


# ==========================================
# 7. PRACTICAL OOP EXAMPLE - Restaurant System
# ==========================================

print("🏪 PRACTICAL OOP - Complete Restaurant System")
print("=" * 50)


class MenuItem:
    """A menu item."""

    def __init__(self, name:str, price:float, category:str):
        self.name = name
        self.price = price
        self.category = category

    def get_description(self) -> str:
        return f"{self.name} - ${self.price:.2f} ({self.category})"


class Order:
    """A customer order."""

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []
        self.is_complete = False

    def add_item(self, item: MenuItem):
        """Add item to order."""
        self.items.append(item)
        print(f"✅ Added {item.name} to {self.customer_name}'s order")

    def calculate_total(self) -> float:
        """Calculate order total."""
        return sum(item.price for item in self.items)

    def complete_order(self):
        """Mark order as complete."""
        self.is_complete = True
        total = self.calculate_total()
        print(f"🍽️ Order complete for {self.customer_name}: ${total:.2f}")


# Using the restaurant system
print("🍽️ Restaurant ordering system:")

# Create menu items
pizza = MenuItem("Margherita Pizza", 15.99, "main")
salad = MenuItem("Caesar Salad", 8.99, "appetizer")
pasta = MenuItem("Spaghetti", 12.50, "main")


# Create orders
alice_order = Order("Alice")
bob_order = Order("Bob")


# Add items to orders
alice_order.add_item(pizza)
alice_order.add_item(salad)

bob_order.add_item(pasta)
bob_order.add_item(pizza)

# Complete orders
alice_order.complete_order()
bob_order.complete_order()
print()



# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON OOP BASICS SUMMARY")
print("=" * 50)
print("✅ Classes & Instances:")
print("   • class ClassName: - Define a class")
print("   • def __init__(self, params): - Constructor")
print("   • instance = ClassName(args) - Create instance")
print()
print("✅ Instance Variables:")
print("   • self.variable = value - Unique to each instance")
print("   • Accessed via self.variable")
print()
print("✅ Class Variables:")
print("   • ClassName.variable = value - Shared by all instances")
print("   • Accessed via ClassName.variable or self.variable")
print()
print("✅ Methods:")
print("   • def method(self): - Instance method")
print("   • @classmethod def method(cls): - Class method")
print("   • @staticmethod def method(): - Static method")
print()
print("✅ Inheritance:")
print("   • class Child(Parent): - Inherit from parent")
print("   • super().__init__(args) - Call parent constructor")
print("   • Override parent methods for specialization")
print()
print("✅ Encapsulation:")
print("   • _variable - Conventionally private")
print("   • __variable - Name mangling (harder to access)")
print("   • Provide public methods for controlled access")
print()
print("✅ Polymorphism:")
print("   • Same method name, different behavior")
print("   • Enables flexible, interchangeable objects")
print()
print("💡 OOP organizes code around real-world objects!")
print("   Each 'thing' in your program becomes a class with")
print("   its own data (attributes) and actions (methods).")