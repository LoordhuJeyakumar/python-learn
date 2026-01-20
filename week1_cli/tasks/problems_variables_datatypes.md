# TOPIC 1: VARIABLES & DATA TYPES
## Questions & Problem Statements

### Problem 1.1: Personal Information Variables
**Question:** Create variables to store your personal information and display them using f-strings.

**Requirements:**
- Create variables: name (string), age (integer), height (float), is_student (boolean), favorite_color (could be None)
- Use f-strings to display: "Hi, I'm [name], [age] years old, [height]m tall, and I [am/am not] a student"
- Test with different values to ensure the output changes correctly

**Test Cases:**
- [ ] Name displays correctly
- [ ] Age shows as number
- [ ] Height shows with proper decimal places
- [ ] Boolean displays as "am" or "am not"
- [ ] None value handled appropriately

---

### Problem 1.2: Type Conversion Calculator
**Question:** Create a program that demonstrates different type conversions.

**Requirements:**
- Convert string "42" to integer and add 10 to it
- Convert float 3.99 to integer (observe what happens to decimal part)
- Convert integer 1 and 0 to boolean values
- Convert boolean True to string and concatenate with another string
- Show the difference between string concatenation and numeric addition

**Expected Results:**
- [ ] String "42" + 10 = 52 (integer addition)
- [ ] Float 3.99 to int = 3 (truncation, not rounding)
- [ ] int(1) = True, int(0) = False
- [ ] str(True) + " is correct" = "True is correct"
- [ ] "10" + "20" = "1020" vs 10 + 20 = 30

---

### Problem 1.3: Type Checking Function
**Question:** Write a function that analyzes the type and truthiness of any value.

**Requirements:**
- Create function `analyze_value(value)` that returns information about the input
- Return: type name, whether it's truthy/falsy, and the actual value
- Test with these values: 0, 1, "", "hello", [], [1,2], {}, {"key": "value"}, None, True, False

**Test Results Expected:**
- [ ] 0: type='int', truthy=False, value=0
- [ ] "": type='str', truthy=False, value=''
- [ ] []: type='list', truthy=False, value=[]
- [ ] None: type='NoneType', truthy=False, value=None
- [ ] "hello": type='str', truthy=True, value='hello'

---

### Problem 1.4: Temperature Converter
**Question:** Create a temperature conversion program using variables and type conversion.

**Requirements:**
- Input temperature in Celsius (float)
- Convert to Fahrenheit using: F = (C × 9/5) + 32
- Display both temperatures with proper formatting
- Handle type conversion between input string and numeric calculations
- Show 2 decimal places for temperatures

**Example Output:**
```
Temperature: 25°C
In Fahrenheit: 77.00°F
```

**Test Cases:**
- [ ] 0°C = 32.00°F
- [ ] 100°C = 212.00°F
- [ ] 25°C = 77.00°F
- [ ] Input validation (numeric only)

---

### Problem 1.5: Personal Profile Generator
**Question:** Create a program that generates a formatted personal profile using all data types.

**Requirements:**
- Use variables of different types: str, int, float, bool, None
- Create a multi-line profile using f-strings
- Include conditional text based on boolean values
- Handle None values gracefully
- Format numbers appropriately (age, height, etc.)

**Sample Profile Structure:**
```
PERSONAL PROFILE
================
Name: John Doe
Age: 25 years old
Height: 1.75 meters
Occupation: Student (if is_student=True)
Favorite Color: Not specified (if None)
BMI Category: Normal (calculated if height and weight provided)
```

**Acceptance Criteria:**
- [ ] All variable types used
- [ ] Conditional formatting works
- [ ] None values handled without errors
- [ ] Numbers formatted properly
- [ ] Output is readable and well-structured

---

### Problem 1.6: Type Conversion Errors
**Question:** Demonstrate common type conversion errors and how to handle them.

**Requirements:**
- Show what happens when converting invalid strings to numbers
- Demonstrate ValueError when converting non-numeric strings
- Show how to safely convert with error handling
- Create a safe conversion function that returns None on error

**Error Scenarios to Handle:**
- [ ] int("hello") - should raise ValueError
- [ ] float("not_a_number") - should raise ValueError
- [ ] Safe conversion function that catches errors
- [ ] Test with valid and invalid inputs

---

### Problem 1.7: Data Type Quiz
**Question:** Create an interactive quiz that tests knowledge of Python data types.

**Requirements:**
- Ask user for different types of input
- Validate that the input matches expected type
- Give feedback on correct/incorrect types
- Use type() and isinstance() for validation
- Handle user input gracefully

**Quiz Questions:**
1. Enter your age (should be int)
2. Enter your name (should be str)
3. Enter your height (should be float)
4. Are you a student? (should be bool-like)

**Acceptance Criteria:**
- [ ] Input validation works for each type
- [ ] Clear feedback messages
- [ ] Program handles invalid inputs
- [ ] Uses appropriate type checking functions