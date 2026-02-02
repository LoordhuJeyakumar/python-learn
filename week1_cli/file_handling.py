#!/usr/bin/env python3
"""
FILE HANDLING IN PYTHON - Complete Guide
=========================================

File handling is essential for backend applications. Like a restaurant's storage system:
- Files = Long-term storage (fridge, pantry)
- Directories = Organization system (shelves, cabinets)
- File operations = Storing/retrieving ingredients
- Serialization = Preserving food for later use

ANALOGY: Restaurant Storage System
- Text files = Recipe cards (human readable)
- Binary files = Frozen meals (machine readable)
- JSON = Standardized containers (everyone can read)
- CSV = Inventory spreadsheets
- Pickle = Chef's special preserved dishes

WHY FILE HANDLING MATTERS:
- Configuration files (settings, credentials)
- Logging (error logs, access logs)
- Data persistence (databases, caches)
- User uploads (images, documents)
- Temporary storage (session data, cache)
"""

import os # operating system
import json # JavaScript Object Notation
import csv # Comma Separated Values

import pickle # Python Object Serialization
import tempfile # Temporary File Management
import shutil # File Operations
from pathlib import Path # Pathlib is a library for handling file paths



# ==========================================
# 1. Basic File Operations
# ==========================================

print("📁 BASIC FILE OPERATIONS - Opening the Storage")
print("=" * 55)

# File opening modes
print("🔑 File Opening Modes:")
print("  'r'  = Read (default) - Open for reading")
print("  'w'  = Write - Create/truncate file for writing")
print("  'a'  = Append - Add to end of file")
print("  'x'  = Exclusive - Create file, fail if exists")
print("  'b'  = Binary - Binary mode")
print("  't'  = Text (default) - Text mode")
print("  '+'  = Read+Write - Update mode")
print()


demo_file = "demo_file.txt"

#creating and writing to a file
print(f"🔍 Creating and Writing to {demo_file}:")
with open(demo_file, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a demo file.\n")
    file.write("We will use this file to demonstrate file operations from python.\n")

print(f"✅ Created {demo_file}")
print()

## Reading from a file
print(f"🔍 Reading {demo_file} line by line:")
with open(demo_file, "r") as file:
   content = file.read()
   print("File content:")
   print(content)
print()

# Reading line by line
print(f"🔍 Reading {demo_file} line by line:")
with open(demo_file, "r") as file:
    for line_num, line in enumerate(file, 1): # enumerate is used to get the line number and the line content
        print(f"Line {line_num}: {line.strip()}")
print()



# ==========================================
# 2. FILE MODES IN DETAIL
# ==========================================

print("🔧 FILE MODES - Different Ways to Access Storage")
print("=" * 55)

# Write mode (Overwrite existing file )
print("✍️ Write mode ('w') - Creates/truncates:")
with open("write_demo.txt", "w") as file:
    file.write("This overwrites any existing content\n")
    file.write("Fresh start!\n")
    file.write("This is a write demo file.\n")


with open("write_demo.txt", 'r') as file:
    print("Write mode result:", repr(file.read()))
print()

# Append mode (adds to existing file)
print("📎 Append mode ('a') - Adds to end:")
with open("write_demo.txt", 'a') as file:
    file.write("This gets appended!\n")
    file.write("More content added.\n")


with open("write_demo.txt", 'r') as file:
    print("Append mode result:")
    print(file.read())
print()

# Exclusive mode (fails if file exists)
print("🚫 Exclusive mode ('x') - Create only if doesn't exist:")

try:
    with open("write_demo.txt", 'x') as file:
        file.write("This should fail!\n")
except FileExistsError:
    print("❌ File already exists - exclusive mode failed as expected")

try:
    with open("new_file.txt", 'x') as file:
        file.write("This succeeds - file didn't exist\n")
    print("✅ Exclusive mode succeeded for new file")
except FileExistsError:
    print("❌ Unexpected error")
print()


# ==========================================
# 3. TEXT VS BINARY FILES
# ==========================================

print("📄 TEXT VS BINARY FILES - Different Storage Types")
print("=" * 55)

# Text file (human readable)
print("📝 Text file handling:")
text_data = "Hello World!\nThis is text data.\nWith multiple lines."
with open("text_demo.txt", 'w', encoding='utf-8') as file:
    file.write(text_data)

with open("text_demo.txt", 'r', encoding='utf-8') as file:
    print("Text file content:")
    print(repr(file.read()))
print()

# Binary file (machine readable)
print("🔢 Binary file handling:")
binary_data = b"Hello World!\x00\x01\x02\xff"
with open("binary_demo.bin", 'wb') as file:
    file.write(binary_data)

with open("binary_demo.bin", 'rb') as file:
    read_binary = file.read()
    print("Binary file content:")
    print(repr(read_binary))
print()




# ==========================================
# 4. FILE POSITION AND NAVIGATION
# ==========================================

print("🧭 FILE POSITION - Navigating Storage")
print("=" * 55)

# File position operations
print("📍 File position operations:")
with open("position_demo.txt", 'w') as file:
    file.write("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")


with open("position_demo.txt", "r") as file:
    print(f"File size: {file.seek(0, os.SEEK_END)} bytes")
    file.seek(0) # move to the beginning of the file

    file.seek(5) # move to the 6th character
    print(f"Position 5: '{file.read(5)}'")  # Read 5 chars

    file.seek(10)  # Go to position 10
    print(f"Position 10: '{file.read(10)}'")  # Read 10 chars

    print(f"Current position: {file.tell()}")
print()


# ==========================================
# 5. WORKING WITH DIRECTORIES
# ==========================================

print("📂 WORKING WITH DIRECTORIES - Storage Organization")
print("=" * 55)
# Directory operations
demo_dir = "demo_directory"


# Create directory
print("🏗️ Creating directory:")
os.makedirs(demo_dir, exist_ok=True) # exist_ok=True means that if the directory already exists, it will not raise an error
print(f"✅ Created directory: {demo_dir}")
print()




# List directory contents
print("📋 Directory listing:")
files_in_dir = os.listdir(".") # list the files in the current directory
print(f"Files in current directory: {files_in_dir}")
print("Files in current directory:")
for file in sorted(files_in_dir)[:10]:  # Show first 10
    if file.startswith("demo") or file.startswith("write"):
        print(f"  • {file}")
print()



# Directory information
print("ℹ️ Directory information:")
if os.path.exists(demo_dir):
    print(f"Directory exists: {demo_dir}")
    print(f"Is directory: {os.path.isdir(demo_dir)}")
    print(f"Absolute path: {os.path.abspath(demo_dir)}")
print()



# Create files in directory
print("📝 Creating files in directory:")
file_paths = [
    os.path.join(demo_dir, "recipe1.txt"),
    os.path.join(demo_dir, "recipe2.txt"),
    os.path.join(demo_dir, "inventory.csv"),
    os.path.join(demo_dir, "recipe3.json"),

]

for file_path in file_paths:
    with open(file_path, 'w') as file:
        file.write(f"Content of {os.path.basename(file_path)}\n")

print(f"✅ Created {len(file_paths)} files in {demo_dir}")
print()


# Walk directory tree
print("🚶 Walking directory tree:")
for root, dirs, files in os.walk("."):
    if "demo" in root:
        print(f"Directory: {root}")
        if dirs:
            print(f"  Subdirs: {dirs}")
        if files:
            print(f"  Files: {files}")
        print()
        break  # Just show demo directory
print()



# ==========================================
# 6. JSON SERIALIZATION - Data Storage
# ==========================================

print("📦 JSON SERIALIZATION - Standardized Containers")
print("=" * 55)

# Sample data structure
restaurant_data = {
    "name": "Python Kitchen",
    "location": "Downtown",
    "rating": 4.8,
    "menu": {
        "appetizers": ["soup", "salad", "breadsticks"],
        "mains": ["pizza", "pasta", "grilled_fish"],
        "prices": {
            "pizza": 15.99,
            "pasta": 12.50,
            "salad": 8.99
        }
    },
    "staff": [
        {"name": "Chef Alice", "role": "Head Chef", "experience": 10},
        {"name": "Bob", "role": "Waiter", "experience": 3}
    ],
    "open_hours": {
        "monday": ["11:00", "22:00"],
        "tuesday": ["11:00", "22:00"],
        "wednesday": ["11:00", "22:00"]
    }
}

# Save to JSON file
print("💾 Saving data to JSON:")
json_file = "restaurant_data.json"

with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(restaurant_data, file, indent=2, ensure_ascii=False) # dump is used to save the data to the file and indent is used to format the file
print(f"✅ Saved data to {json_file}")




# Load from JSON file
print("📖 Loading data from JSON:")
with open(json_file, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file) # load is used to load the data from the file and it returns a dictionary

print(f"Restaurant: {loaded_data['name']}")
print(f"Rating: {loaded_data['rating']}")
print(f"Menu items: {len(loaded_data['menu']['mains'])} mains") # len is used to get the number of items in the list
print(f"Staff count: {len(loaded_data['staff'])}") # len is used to get the number of items in the list
print()




# ==========================================
# 7. CSV FILE HANDLING - Spreadsheet Data
# ==========================================

print("📊 CSV FILE HANDLING - Spreadsheet Storage")
print("=" * 55)

# Sample inventory data
inventory_data = [
    ["item_id", "name", "category", "quantity", "unit_price", "supplier"],
    [1, "Flour", "Baking", 50, 3.99, "Baker's Best"],
    [2, "Tomatoes", "Produce", 100, 1.99, "Farm Fresh"],
    [3, "Cheese", "Dairy", 25, 8.99, "Dairy Corp"],
    [4, "Olive Oil", "Pantry", 15, 12.99, "Mediterranean Imports"],
    [5, "Pasta", "Pantry", 75, 2.49, "Italian Foods"]
]

# Write CSV file
print("📝 Writing CSV file:")
csv_file = "inventory.csv"
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in inventory_data:
        writer.writerow(row)

print(f"✅ Created CSV file: {csv_file}")
print()

# Read CSV file
print("📖 Reading CSV file:")
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    print("Inventory data:")
    for i, row in enumerate(reader):
        if i == 0:  # Header
            print(f"Headers: {', '.join(row)}")
        else:
            print(f"  {row[1]}: {row[3]} units @ ${row[4]}")
        if i >= 3:  # Show first few rows
            print("  ...")
            break
print()

# CSV with dictionaries
print("📚 CSV with dictionary access:")
dict_csv_file = "inventory_dict.csv"
fieldnames = ["item_id", "name", "category", "quantity", "unit_price", "supplier"]

with open(dict_csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in inventory_data[1:]:  # Skip header
        writer.writerow(dict(zip(fieldnames, item)))

# Read as dictionaries
with open(dict_csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print("Reading as dictionaries:")
    total_value = 0
    for row in reader:
        value = int(row['quantity']) * float(row['unit_price'])
        total_value += value
        print(f"  {row['name']}: ${value:.2f} total value")

    print(f"\n💰 Total inventory value: ${total_value:.2f}")
print()




# ==========================================
# 7. CSV SERIALIZATION - Data Storage
# ==========================================

print("📊 CSV SERIALIZATION - Spreadsheet-like Containers")
