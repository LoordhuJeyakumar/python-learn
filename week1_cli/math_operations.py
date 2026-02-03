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