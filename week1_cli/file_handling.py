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
# 8. PICKLE SERIALIZATION - Python Objects
# ==========================================

print("🥒 PICKLE SERIALIZATION - Preserving Python Objects")
print("=" * 55)

# Sample Python object
python_object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Save to pickle file
print("💾 Saving Python object to pickle:")
pickle_file = "python_object.pkl"
with open(pickle_file, 'wb') as file:
    pickle.dump(python_object, file)
print(f"✅ Saved Python object to {pickle_file}")
print(f"✅ Pickled {len(python_object)} python objects to {pickle_file}")
print()

# Load from pickle file
print("📖 Loading Python object from pickle:")
with open(pickle_file, 'rb') as file:
    loaded_python_object = pickle.load(file)
print(f"Loaded Python object: {loaded_python_object}")
print()




# ==========================================
# 9. ERROR HANDLING FOR FILES
# ==========================================

print("🚨 ERROR HANDLING - Safe File Operations")
print("=" * 55)

def safe_file_read(filename: str) -> Optional[str]:
    """
    Safely read a file with comprehensive error handling.

    ANALOGY: Carefully opening a storage container
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
    except PermissionError:
        print(f"❌ Permission denied: {filename}")
    except UnicodeDecodeError:
        print(f"❌ Encoding error (try binary mode): {filename}")
    except Exception as error:
        print(f"❌ Unexpected error reading {filename}: {error}")
    return None

def safe_file_write(filename: str, content: str) -> bool:
    """
    Safely write to a file with error handling.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"❌ Permission denied: {filename}")
    except Exception as error:
        print(f"❌ Error writing to {filename}: {error}")
    return False

print("🛡️ Testing safe file operations:")
# Test reading non-existent file
result = safe_file_read("nonexistent_file.txt")
print(f"Read result: {result}")
print()

# Test writing to file
success = safe_file_write("safe_write_test.txt", "This is safe content!")
print(f"Write success: {success}")
print()


# ==========================================
# 10. TEMPORARY FILES & DIRECTORIES
# ==========================================

print("🕒 TEMPORARY FILES - Short-term Storage")
print("=" * 55)

# Temporary file
print("📄 Temporary file:")
with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
    temp_file.write("This is temporary data!\n")
    temp_file.write("It will be cleaned up automatically.\n")
    temp_filename = temp_file.name

    # Read it back
    temp_file.seek(0)
    content = temp_file.read()
    print(f"Temporary file created: {temp_filename}")
    print(f"Content: {repr(content)}")

# Clean up
os.unlink(temp_filename)
print("🧹 Temporary file cleaned up")
print()



# Temporary directory
print("📁 Temporary directory:")
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created temp directory: {temp_dir}")

    # Create files in temp directory
    temp_files = []
    for i in range(3):
        file_path = os.path.join(temp_dir, f"temp_file_{i}.txt")
        with open(file_path, 'w') as file:
            file.write(f"Content of file {i}\n")
        temp_files.append(file_path)

    print(f"Created {len(temp_files)} files in temp directory")

    # List contents
    contents = os.listdir(temp_dir)
    print(f"Directory contents: {contents}")

print("🧹 Temporary directory and files cleaned up automatically")
print()




# ==========================================
# 11. FILE PATH OPERATIONS
# ==========================================

print("🛤️ FILE PATH OPERATIONS - Navigation System")
print("=" * 55)

#Absolute path vs relative path
print("🔍 Absolute path vs relative path:")
print(f"Absolute path: {os.path.abspath('demo_directory/recipe1.txt')}")
print(f"Relative path: {os.path.relpath('demo_directory/recipe1.txt')}")
print()


# Using pathlib (modern approach)
print("🚀 Modern pathlib approach:")
demo_path = Path("demo_directory/recipe1.txt")

print(f"Path: {demo_path}")
print(f"Exists: {demo_path.exists()}")
print(f"Is file: {demo_path.is_file()}")
print(f"Name: {demo_path.name}")
print(f"Stem: {demo_path.stem}")  # Name without extension
print(f"Suffix: {demo_path.suffix}")  # Extension
print(f"Parent: {demo_path.parent}")
print()

# Path operations
print("🔧 Path operations:")
new_path = Path("demo_directory") / "new_recipe.txt"
print(f"Path joining: {new_path}")

# Create nested directories
nested_path = Path("demo_directory/nested/deep/structure")
nested_path.parent.mkdir(parents=True, exist_ok=True)
(nested_path.parent / "test.txt").write_text("Nested file content")
print("✅ Created nested directory structure")
print()

# Find files recursively
print("🔍 Finding files recursively:")
txt_files = list(Path("demo_directory").rglob("*.txt"))
print(f"Found {len(txt_files)} .txt files:")
for file_path in txt_files[:5]:  # Show first 5
    print(f"  • {file_path}")
print()


# ==========================================

# ==========================================
# 12. PRACTICAL BACKEND EXAMPLES
# ==========================================

print("🏪 PRACTICAL BACKEND EXAMPLES - Real Application Scenarios")
print("=" * 55)

# Configuration file handling
print("⚙️ Example 1: Configuration file")
config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "restaurant_db",
        "user": "admin"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

config_file = "app_config.json"
with open(config_file, 'w') as file:
    json.dump(config_data, file, indent=2)

print("✅ Configuration saved")
print()

# Log file handling
print("📝 Example 2: Log file")
import datetime

def write_log(message: str, level: str = "INFO"):
    """Write a log entry to file."""
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] {level}: {message}\n"

    with open("app.log", 'a', encoding='utf-8') as log_file:
        log_file.write(log_entry)

# Write some log entries
write_log("Application started")
write_log("Database connection established")
write_log("API server listening on port 8000")
write_log("User login successful", "INFO")
write_log("Invalid password attempt", "WARNING")

print("✅ Log entries written")
print()

# Cache file handling
print("💾 Example 3: Cache file")
import hashlib

def get_cache_filename(key: str) -> str:
    """Generate cache filename from key."""
    hash_obj = hashlib.md5(key.encode())
    return f"cache_{hash_obj.hexdigest()[:8]}.json"

def save_to_cache(key: str, data: Any) -> None:
    """Save data to cache file."""
    filename = get_cache_filename(key)
    with open(filename, 'w') as file:
        json.dump({
            "key": key,
            "data": data,
            "timestamp": datetime.datetime.now().isoformat()
        }, file, indent=2)

def load_from_cache(key: str) -> Optional[Any]:
    """Load data from cache file."""
    filename = get_cache_filename(key)
    if not os.path.exists(filename):
        return None

    try:
        with open(filename, 'r') as file:
            cache_data = json.load(file)
            return cache_data["data"]
    except:
        return None

# Test caching
test_key = "user_profile_123"
test_data = {"name": "Alice", "email": "alice@example.com", "role": "admin"}

save_to_cache(test_key, test_data)
cached_data = load_from_cache(test_key)

print(f"Original: {test_data}")
print(f"Cached: {cached_data}")
print(f"Cache hit: {test_data == cached_data}")
print()



# ==========================================
# CLEANUP DEMO FILES
# ==========================================

print("🧹 CLEANING UP DEMO FILES")
print("=" * 55)

demo_files = [
    "demo_file.txt", "write_demo.txt", "new_file.txt",
    "text_demo.txt", "binary_demo.bin", "position_demo.txt",
    "restaurant_data.json", "menu_items.json",
    "inventory.csv", "inventory_dict.csv",
    "chefs.pkl", "safe_write_test.txt",
    "app_config.json", "app.log"
]

demo_files.extend([f"cache_{hashlib.md5(f'key_{i}'.encode()).hexdigest()[:8]}.json" for i in range(3)])

for file in demo_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"🗑️ Removed {file}")

# Remove demo directory
if os.path.exists(demo_dir):
    shutil.rmtree(demo_dir)
    print(f"🗑️ Removed directory {demo_dir}")

print("\n✅ Cleanup complete!")
print()

# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON FILE HANDLING SUMMARY")
print("=" * 55)
print("✅ File Opening Modes:")
print("   • 'r' (read), 'w' (write), 'a' (append), 'x' (exclusive)")
print("   • 'b' (binary), 't' (text), '+' (read+write)")
print()
print("✅ Context Managers:")
print("   • with open() as file: - Automatic cleanup")
print("   • No need to manually close files")
print()
print("✅ File Operations:")
print("   • .read(), .write(), .seek(), .tell()")
print("   • Line-by-line reading with for loops")
print()
print("✅ Directory Operations:")
print("   • os.listdir(), os.makedirs(), os.path operations")
print("   • pathlib for modern path handling")
print()
print("✅ Data Serialization:")
print("   • JSON for human-readable data")
print("   • CSV for spreadsheet-like data")
print("   • Pickle for Python objects (use carefully!)")
print()
print("✅ Error Handling:")
print("   • FileNotFoundError, PermissionError")
print("   • UnicodeDecodeError, JSONDecodeError")
print("   • Always use try/except for file operations")
print()
print("✅ Best Practices:")
print("   • Always use 'with' statements")
print("   • Specify encoding='utf-8'")
print("   • Handle errors gracefully")
print("   • Use pathlib for path operations")
print("   • Consider security implications")
print()
print("💡 File handling is fundamental to backend development!")
print("   • Configuration files, logging, data storage, caching...")
print("   • Every serious application needs robust file operations.")