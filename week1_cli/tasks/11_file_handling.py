# File handling

import os

# 1. Write to file
with open("notes.txt", "w") as file:
    file.write("Task Manager Notes\n")
    file.write("==================\n")

# 2. Append to file
with open("notes.txt", "a") as file:
    file.write("New note added\n")

# 3. Read full file
with open("notes.txt", "r") as file:
    content = file.read()
    print("FULL FILE CONTENT:")
    print(content)

# 4. Read line by line
print("READING LINE BY LINE:")
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# 5. File existence checking
if os.path.exists("notes.txt"):
    print("notes.txt exists")
    file_size = os.path.getsize("notes.txt")
    print("File size:", file_size, "bytes")
else:
    print("notes.txt not found")

# 6.Context manager example (GOOD practice)
with open("notes.txt", "r") as file:
    data = file.read()
