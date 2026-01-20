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
