#Control Flow in python

# if, elif, else

# example
age = 18
if age >= 18:
    print("You are eligible to vote")
elif age < 18:
    print("You are not eligible to vote")
else:
    print("You are not eligible to vote")   


# for loop
# range(start, stop, step) => start is inclusive, stop is exclusive and step is optional 
print("Range with stop")
for i in range(10):
    print(i)
print("\n")
print("Range with start and stop")
for i in range(1, 10):
    print(i)
print("\n")
print("Range with start, stop and step")
for i in range(1, 10, 2):
    print(i)
print("\n")

#another for loop example with enumerate
# enumerate() => returns a tuple containing the index and value of each item in the list
print("Range with enumerate")
for index, value in enumerate(range(10)):
    print(index, value)
print("\n")

# without range

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)
print("\n")



# while loop
# while condition:
#     code block
# break and continue

i = 0

while i < 10:
    print(i)
    i += 1
print("\n")

# break and continue

# break => breaks out of the loop
print("Break")
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
print("\n")
    
# continue => skips the current iteration and moves to the next iteration
print("Continue")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
print("\n")


# pass => does nothing and it is used as a placeholder
print("Pass")
i = 0
while i < 10:
    if i == 5:
        pass
    print(i)
    i += 1
print("\n")


# else
print("Else")
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 10")
print("\n")


# nested loop
print("Nested Loop")
for i in range(10):
    for j in range(10):
        print(i, j)
print("\n")


# infinite loop
print("Infinite Loop")
i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break
print("\n")
