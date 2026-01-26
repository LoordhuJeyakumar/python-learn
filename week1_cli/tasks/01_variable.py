#1.Create variables 

name = "Kathirvel" # String
age = 20 # Integer
time = 8.15 # Float
is_fun = True # Boolean
nothing = None # NoneType

print("Names:", name)
print("Age:", age)
print("Time:", time)
print("Is Fun:", is_fun)
print("Nothing:", nothing)

print("_" * 30)

#2.F strings for formatting

print(f"My name is {name}, I am {age} years old. The time is {time}. Is coding fun? {is_fun}. Nothing is {nothing}.")

print("_" * 30)

#3. Type conversion

string_number = 42
int_number = int(string_number)
float_number = float(string_number)

print("String Number:", string_number)
print("Integer Number:", int_number)
print("Float Number:", float_number)

print("_" * 30)

#4. Type checking

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of time:", type(time))