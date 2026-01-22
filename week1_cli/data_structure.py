#!/usr/bin/env python3
"""
DATA STRUCTURES IN PYTHON - Complete Guide
===========================================

Data structures are containers that hold and organize data.
Like different types of storage containers in a kitchen.

ANALOGY: Kitchen Storage
- Lists = Shopping bags (ordered, can add/remove items)
- Dictionaries = Recipe boxes (key-value pairs, like labeled drawers)
- Tuples = Frozen meal trays (immutable, fixed portions)
- Sets = Ingredient checklists (unique items, no duplicates)

WHY DATA STRUCTURES MATTER:
- Organize data efficiently
- Access data quickly
- Perform operations on collections
- Memory management
"""

# ==========================================
# 1. LISTS - Ordered, Mutable Collections
# ==========================================
from hmac import new
from typing import Any


print("🛒 LISTS - Ordered, Mutable Collections for example Shopping Bags (Ordered & Mutable)")
print("=" * 40)

#create a list
print("📋 Creating a list:")
empty_list = [] # empty list
print(empty_list)

#create a list with items - values are separated by commas and enclosed in square brackets and 0 based index
shopping_list = ["bread", "milk", "eggs"]  # Filled shopping bag
mixed_list = [1, "apple", True, 3.14]  # Different item types

print(shopping_list)
print(mixed_list)

# List operations
print("🔧 List operations:")

#add an item to the list - appened value to the end of the list
print("📋 Adding an item to the list:")
shopping_list.append("butter")
print(shopping_list)

#insert an item at a specific index
print("📋 Inserting an item at a specific index:")
shopping_list.insert(1, "butter")
print(shopping_list)

#remove an item from the list - remove the first occurrence of the item
print("📋 Removing an item from the list:")
shopping_list.remove("milk")
print(shopping_list)

#remove an item from the list at a specific index
print("📋 Removing an item from the list at a specific index:")
shopping_list.pop(1) # remove the item at index 1 - 'butter'
print(shopping_list)

shopping_list.pop() # remove the last item from the list
print(shopping_list) # ['bread', 'eggs']


#Accessing items in a list
print("=" * 40)
print("📋 Accessing items in a list:")
print(shopping_list[0]) # access the first item in the list
print(shopping_list[1]) # access the second item in the list
print(shopping_list[-1]) # access the last item in the list
print(shopping_list[-2]) # access the second last item in the list

#Slicing a list
print("📋 Slicing a list:")

# slicing a list - get a sublist from the list
print("📋 Slicing a list:")
print(shopping_list[0:2]) # slice the list from index 0 to 2 - ['bread', 'eggs'] - 0 is inclusive and 2 is exclusive
print(shopping_list[:2]) # slice the list from the beginning to index 2 - ['bread', 'eggs'] - 0 is inclusive and 2 is exclusive
print(shopping_list[2:]) # slice the list from index 2 to the end - ['eggs'] - 2 is inclusive and the end is exclusive
print(shopping_list[-2:]) # slice the list from the second last item to the end - ['eggs'] - -2 is inclusive and the end is exclusive
print(shopping_list[-2:]) # slice the list from the second last item to the end - ['eggs'] - -2 is inclusive and the end is exclusive

# step in slicing a list
print("📋 Step in slicing a list:")
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange", "Pear", "Pineapple", "Plum", "Pomegranate", "Raspberry", "Strawberry", "Tangerine", "Watermelon"]

print(fruits[0:10:2]) # slice the list from index 0 to 10 with a step of 2 - ['Apple', 'Cherry', 'Orange', 'Pineapple', 'Raspberry', 'Tangerine']

print(fruits[::-1]) # slice the list from the end to the beginning with a step of 1 - ['Watermelon', 'Tangerine', 'Strawberry', 'Raspberry', 'Pomegranate', 'Plum', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple']

print(fruits[::2]) # slice the list from the beginning to the end with a step of 2 - ['Apple', 'Cherry', 'Orange', 'Pineapple', 'Raspberry', 'Tangerine', 'Watermelon']

print(fruits[10:0:-1]) # slice the list from index 10 to 0 with a step of -1 - ['Raspberry', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple']


#list methods
print("📋 List methods:")
print("=" * 40)


# list length
print("📋 List length:")
print(len(fruits)) # print the length of the list - 13

# list index
print("📋 List index:")
print(fruits.index("Apple")) # print the index of the item "Apple" - 0

# list count
print("📋 List count:")
print(fruits.count("Apple")) # print the count of the item "Apple" - 1

# add an item to the list
print("📋 Adding an item to the list:")
fruits.append("Grape")
print(fruits)

# insert an item at a specific index
print("📋 Inserting an item at a specific index:")
fruits.insert(1, "Grape")
print(fruits)

# remove an item from the list
print("📋 Removing an item from the list:")
fruits.remove("Grape")
print(fruits)

# remove an item from the list at a specific index
print("📋 Removing an item from the list at a specific index:")
fruits.pop(1)
print(fruits)

# remove the last item from the list
print("📋 Removing the last item from the list:")
fruits.pop()


# clear the list
print("📋 Clearing the list:")
fruits.clear() # clear the list - remove all items from the list and the list will be empty
print(fruits)

# sort the list
print("📋 Sorting the list:")
fruits.sort() # sort the list in ascending order - ['Apple', 'Banana', 'Cherry', 'Mango', 'Orange', 'Pear', 'Pineapple', 'Plum', 'Pomegranate', 'Raspberry', 'Strawberry', 'Tangerine', 'Watermelon']

# reverse the list
fruits.sort(reverse=True) # sort the list in descending order - ['Watermelon', 'Tangerine', 'Strawberry', 'Raspberry', 'Pomegranate', 'Plum', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple']

print(fruits)


# copy the list
print("📋 Copying the list:")
fruits_copy = fruits.copy() # copy the list - ['Watermelon', 'Tangerine', 'Strawberry', 'Raspberry', 'Pomegranate', 'Plum', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple']
print(fruits_copy)

# concatenate two lists
print("📋 Concatenating two lists:")
fruits_copy.extend(fruits) # concatenate the list - ['Watermelon', 'Tangerine', 'Strawberry', 'Raspberry', 'Pomegranate', 'Plum', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple', 'Watermelon', 'Tangerine', 'Strawberry', 'Raspberry', 'Pomegranate', 'Plum', 'Pineapple', 'Orange', 'Mango', 'Cherry', 'Banana', 'Apple']
print(fruits_copy)

# remove all items from the list
print("📋 Removing all items from the list:")
fruits_copy.clear() # remove all items from the list and the list will be empty
print(fruits_copy)


# comparing two lists
print("📋 Comparing two lists:")
print(fruits == fruits_copy) # compare the two lists - True
print(fruits != fruits_copy) # compare the two lists - False
print(fruits < fruits_copy) # compare the two lists - False
print(fruits > fruits_copy) # compare the two lists - False
print(fruits <= fruits_copy) # compare the two lists - True
print(fruits >= fruits_copy) # compare the two lists - True 


# nested list
print("📋 Nested list:")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

# access the nested list
print("📋 Accessing the nested list:")
print(nested_list[0]) # access the first list - [1, 2, 3]
print(nested_list[0][0]) # access the first item in the first list - 1



# Tuple => Tuple (Collection of Items in an ordered sequence ) and it is immutable (Cannot be changed) 
print("🧁 TUPLES - Immutable Collections for example Frozen Meal Trays (Immutable)")
print("=" * 40)

#create a tuple
print("📋 Creating a tuple:")
empty_tuple = () # empty tuple
print(empty_tuple)

#create a tuple with items - values are separated by commas and enclosed in parentheses and 0 based index
fruits_tuple = ("apple", "banana", "cherry") # filled tuple
print(fruits_tuple)

#mixed tuple
print("📋 Mixed tuple:")
mixed_tuple = (1, "apple", True, 3.14) # mixed tuple
print(mixed_tuple)

#nested tuple
print("📋 Nested tuple:")
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9)) # nested tuple
print(nested_tuple)

#access the nested tuple
print("📋 Accessing the nested tuple:")
print(nested_tuple[0]) # access the first tuple - (1, 2, 3)
print(nested_tuple[0][0]) # access the first item in the first tuple - 1

#tuple length
print("📋 Tuple length:")
print(len(nested_tuple)) # print the length of the tuple - 3

#tuple index
print("📋 Tuple index:")
print(nested_tuple.index()) # print the index of the item (1, 2, 3) - 0


# tuple methods
print("📋 Tuple methods:")
print("=" * 40)

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(new_tuple)

print(new_tuple.count(1)) # print the count of the item 1 - 1


print(new_tuple.index(1)) # print the index of the item 1 - 0

print(len(new_tuple)) # print the length of the tuple - 9

print(new_tuple[0]) # print the first item in the tuple - 1

#slicing a tuple
print("📋 Slicing a tuple:")
print(new_tuple[0:3]) # print the first 3 items in the tuple - (1, 2, 3)
print(new_tuple[:3]) # print the first 3 items in the tuple - (1, 2, 3)
print(new_tuple[3:]) # print the last 6 items in the tuple - (4, 5, 6, 7, 8, 9)
print(new_tuple[-3:]) # print the last 3 items in the tuple - (7, 8, 9)
print(new_tuple[-3:]) # print the last 3 items in the tuple - (7, 8, 9)

# step in slicing a tuple
print("📋 Step in slicing a tuple:")
print(new_tuple[0:10:2]) # print the first 10 items in the tuple with a step of 2 - (1, 3, 5, 7, 9)
print(new_tuple[::-1]) # print the tuple from the end to the beginning with a step of 1 - (9, 8, 7, 6, 5, 4, 3, 2, 1)


# Tuple packing and unpacking
print("📋 Tuple packing and unpacking:")
print(new_tuple) # print the tuple - (1, 2, 3, 4, 5, 6, 7, 8, 9)

a, b, c, d, e, f, g, h, i = new_tuple # unpack the tuple - a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8, i = 9

print(a) # print the value of a - 1
print(b) # print the value of b - 2
print(c) # print the value of c - 3
print(d) # print the value of d - 4
print(e) # print the value of e - 5
print(f) # print the value of f - 6


# Tuple packing
print("📋 Tuple packing:")
new_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9 # pack the tuple - (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(new_tuple) # print the tuple - (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Tuple unpacking
print("📋 Tuple unpacking:")
a, b, c, d, e, f, g, h, i = new_tuple # unpack the tuple - a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8, i = 9
print(a) # print the value of a - 1
print(b) # print the value of b - 2
print(c) # print the value of c - 3
print(d) # print the value of d - 4
print(e) # print the value of e - 5
print(f) # print the value of f - 6

# tuple multiple assignment
print("📋 Tuple multiple assignment:")
a, b, c = 10, 20, 30 # multiple assignment - a = 10, b = 20, c = 30
print(a) # print the value of a - 10
print(b) # print the value of b - 20
print(c) # print the value of c - 30


# When to use tuples vs lists
print("When to use tuples")
print("✅ Use tuples for:")
print("🔹 Fixed data that won't change for example coordinates, RGB values, security tokens, etc.")
print("🔹 Funtions that return multiple values")
print("🔹 Dictionary keys and values")
print("🔹 When you need to ensure data integrity and security")
print("🔹 Protecting data from modification or accidental modification")

print("❌ Avoid using tuples for:")
print("🔹 Dynamic data that needs to be modified for example a shopping list, a to-do list, etc.")
print("🔹 When you need to add or remove items from the list")
print("🔹 When you need to sort the list")
print("🔹 When you need to reverse the list")
print("🔹 When you need to search the list")
print("🔹 When you need to iterate over the list")
print("🔹 When you need to perform operations on the list")


print("✅ Use lists for:")
print("🔹 Dynamic data that needs to be modified for example a shopping list, a to-do list, etc.")
print("🔹 When you need to add or remove items from the list")
print("🔹 When you need to sort the list")
print("🔹 When you need to reverse the list")
print("🔹 When you need to search the list")
print("🔹 When you need to iterate over the list")
print("🔹 When you need to perform operations on the list")

print("❌ Avoid using lists for:")
print("🔹 Fixed data that won't change for example coordinates, RGB values, security tokens, etc.")
print("🔹 Funtions that return multiple values")
print("🔹 Dictionary keys and values")


# ==========================================
# 3. DICTIONARIES - Key-Value Pairs => 
# ==========================================

print("📚 DICTIONARIES - Recipe Boxes (Key-Value Storage)")
print("=" * 50)

print(" Creating a dictionaries")

empty_dict = {}

person = {
    "name" : "John",
    "age" : 30,    
}

menu = {
    "pizza" : 200,
    "Salad": 100,
}



print(f"Empty Dict: {empty_dict}")
print(f"Person dict: {person}")
print(f"Menu dict: {menu}")

# Dictionary operations
print("Dictionary operations:")
print("=" * 40)

# Accessing values
print("📋 Accessing values:")
print(menu["pizza"]) # print the value of the key "pizza" - 200
print(menu["Salad"]) # print the value of the key "Salad" - 100
print(menu.get("pizza")) # print the value of the key "pizza" - 200
print(menu.get("drink")) # print the value of the key "drink" - None
print(menu.get("drink", "Not found")) # print the value of the key "drink" - Not found

# Accessing keys
print("📋 Accessing keys:")
print(menu.keys()) # print the keys of the dictionary - ['pizza', 'Salad'] dict_keys(['pizza', 'Salad'])

# Accessing values
print("📋 Accessing values:")
print(menu.values()) # print the values of the dictionary - [200, 100] dict_values([200, 100]) it will return a tuple of values

# Add a key-value pair to the dictionary
print("📋 Adding a key-value pair to the dictionary:")
menu["drink"] = 50
print(menu)

# Update a value
print("📋 Updating a value:")
menu["pizza"] = 250
print(menu)

# modify a key-value pair
print("📋 Modifying a key-value pair:")
menu["pizza"] = 300
print(menu)

# remove a key-value pair from the dictionary
print("📋 Removing a key-value pair from the dictionary:")
menu.pop("pizza")
print(menu)

# remove the last key-value pair from the dictionary
print("📋 Removing the last key-value pair from the dictionary:")
menu.popitem()
print(menu)

# clear the dictionary
print("📋 Clearing the dictionary:")
menu.clear()
print(menu)

# delete the dictionary
print("📋 Deleting the dictionary:")
#del menu
print(menu)

# copy the dictionary
print("📋 Copying the dictionary:")

new_menu_dict = {
    "drink": 50,
    "Salad": 100,
}

menu_copy = new_menu_dict.copy()
print(f"Menu copy: {menu_copy}")

# merge two dictionaries
print("📋 Merging two dictionaries:")
new_menu_dict.update(menu_copy)
print(f"New menu dict: {new_menu_dict}")

# iterate over a dictionary
print("📋 Iterating over a dictionary:")
for key, value in new_menu_dict.items():
    print(f"Key: {key}, Value: {value}")

# iterate over a dictionary keys
print("📋 Iterating over a dictionary keys:")
for key in new_menu_dict.keys():
    print(f"Key: {key}")

# iterate over a dictionary values
print("📋 Iterating over a dictionary values:")
for value in new_menu_dict.values():
    print(f"Value: {value}")


# nested dictionary
print("📋 Nested dictionary:")
nested_dict = {
    "menu": {
        "pizza": 200,
        "Salad": 100,
    },
    "contact": {
        "phone": "123-456-7890",
        "email": "info@example.com",
    }
}
print(nested_dict)

# access the nested dictionary
print("📋 Accessing the nested dictionary:")
print(nested_dict["menu"]["pizza"]) # print the value of the key "pizza" - 200
print(nested_dict["contact"]["phone"]) # print the value of the key "phone" - 123-456-7890
print(nested_dict["contact"]["email"]) # print the value of the key "email" - info@example.com

# iterate over a nested dictionary
print("📋 Iterating over a nested dictionary:")
for key, value in nested_dict.items():
    print(f"Key: {key}, Value: {value}")

# iterate over a nested dictionary keys
print("📋 Iterating over a nested dictionary keys:")
for key in nested_dict.keys():
    print(f"Key: {key}")

# iterate over a nested dictionary values
print("📋 Iterating over a nested dictionary values:")
for value in nested_dict.values():
    print(f"Value: {value}")



# ==========================================
# 4. SETS - Unordered, Unique Collections => Ingredient Checklists (Unique Items)
# ==========================================

print("📚 SETS - Ingredient Checklists (Unique Items)")
print("=" * 50)

print(" Creating a sets")

empty_set = set() # empty set
print(empty_set)

#create a set with items - values are separated by commas and enclosed in curly braces and 0 based index
fruits_set = {"apple", "banana", "cherry", "apple", "banana", "cherry"} # filled set - it will remove duplicates
print(fruits_set) # {'apple', 'banana', 'cherry'}

#mixed set
print("📋 Mixed set:")
mixed_set = {1, "apple", True, 3.14} # mixed set
print(mixed_set)

#nested set
print("📋 Nested set:")
nested_set = {(1, 2, 3), (4, 5, 6), (7, 8, 9)} # nested set
print(nested_set)

#set operations
print("📋 Set operations:")
print("=" * 40)

# add an item to the set
print("📋 Adding an item to the set:")
fruits_set.add("orange")
print(fruits_set)

# update a set
print("📋 Updating a set:")
fruits_set.update(["orange", "pineapple"])
print(fruits_set)

# remove an item from the set
print("📋 Removing an item from the set:")
fruits_set.remove("banana")
print(fruits_set)

# remove an item from the set at a specific index
print("📋 Removing an item from the set at a specific index:")
fruits_set.pop()
print(fruits_set)

# remove the last item from the set
print("📋 Removing the last item from the set:")
fruits_set.pop()
print(fruits_set)

# clear the set
print("📋 Clearing the set:")
fruits_set.clear()
print(fruits_set)

# delete the set
print("📋 Deleting the set:")
# del fruits_set
print(fruits_set)

# copy the set
print("📋 Copying the set:")
fruits_set_copy = fruits_set.copy()
print(fruits_set_copy)

# merge two sets
print("📋 Merging two sets:")
fruits_set.update(fruits_set_copy)
print(fruits_set)

# iterate over a set
print("📋 Iterating over a set:")
for fruit in fruits_set:
    print(f"Fruit: {fruit}")

# iterate over a set keys
print("📋 Iterating over a set keys:")
for key in fruits_set.keys():
    print(f"Key: {key}")

# iterate over a set values
print("📋 Iterating over a set values:")
for value in fruits_set.values():
    print(f"Value: {value}")


# nested set
print("📋 Nested set:")
nested_set = {(1, 2, 3), (4, 5, 6), (7, 8, 9)} # nested set
print(nested_set)

# access the nested set
print("📋 Accessing the nested set:")
print(nested_set[0]) # print the value of the key "0" - (1, 2, 3)
print(nested_set[0][0]) # print the value of the key "0" - 1
print(nested_set[0][1]) # print the value of the key "1" - 2
print(nested_set[0][2]) # print the value of the key "2" - 3

# iterate over a nested set
print("📋 Iterating over a nested set:")
for item in nested_set:
    print(f"Item: {item}")

# iterate over a nested set keys
print("📋 Iterating over a nested set keys:")
for key in nested_set.keys():
    print(f"Key: {key}")

# iterate over a nested set values
print("📋 Iterating over a nested set values:")
for value in nested_set.values():
    print(f"Value: {value}")


# Set Math Operations
print("📋 Set Math Operations:")
print("=" * 40)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {9, 10, 11, 12, 13}

# union of two sets
print("📋 Union of two sets:")
print(set_a.union(set_b))
print(set_a | set_b)
print(set_a.union(set_b, set_c))
print(set_a | set_b | set_c)

# intersection of two sets
print("📋 Intersection of two sets:")
print(set_a.intersection(set_b))
print(set_a & set_b)
print(set_a.intersection(set_b, set_c))
print(set_a & set_b & set_c)

# difference of two sets in A but not in B
print("📋 Difference of two sets:")
print(set_a.difference(set_b))
print(set_a - set_b)
print(set_a.difference(set_b, set_c))
print(set_a - set_b - set_c)

# difference of two sets in A but not in B and C
print("📋 Difference of two sets:")
print(set_a.difference(set_b, set_c))
print(set_a - set_b - set_c)

# symmetric difference of two sets
print("📋 Symmetric difference of two sets:")
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)



# Set membership testing (very fast!)
print("🚀 Set membership testing:")
large_set = set(range(100000))  # Set with 1000 numbers

import time
start = time.time()
result = 999 in large_set  # Very fast lookup
end = time.time()

print(f"Checking if 999 in large set: {result}")
print(".6f")
print(f"Time taken: {end - start} seconds")
