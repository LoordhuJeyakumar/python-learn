# TOPIC 2: CONTROL FLOW
## Questions & Problem Statements

### Problem 2.1: Age Category Classifier
**Question:** Write a program that categorizes people based on their age using if/elif/else statements.

**Requirements:**
- Input: age (integer)
- Categories:
  - Child: age < 13
  - Teenager: 13 ≤ age < 20
  - Adult: 20 ≤ age < 65
  - Senior: age ≥ 65
- Handle invalid ages (negative numbers or non-integers)

**Test Cases:**
- [ ] Age 5 → "Child"
- [ ] Age 15 → "Teenager"
- [ ] Age 25 → "Adult"
- [ ] Age 70 → "Senior"
- [ ] Age -5 → "Invalid age"
- [ ] Non-numeric input handled

---

### Problem 2.2: Grade Calculator
**Question:** Create a program that converts numeric scores to letter grades.

**Requirements:**
- Input: score (0-100)
- Grade scale:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: 0-59
- Handle scores outside valid range
- Test edge cases (exactly 90, 80, etc.)

**Test Cases:**
- [ ] Score 95 → "A"
- [ ] Score 85 → "B"
- [ ] Score 75 → "C"
- [ ] Score 65 → "D"
- [ ] Score 45 → "F"
- [ ] Score 105 → "Invalid score"
- [ ] Score -5 → "Invalid score"

---

### Problem 2.3: Weather Advisor
**Question:** Create a program that gives clothing recommendations based on weather conditions.

**Requirements:**
- Inputs: temperature (float), is_raining (boolean)
- Logic:
  - If raining: recommend raincoat and umbrella
  - If temperature < 10°C: recommend warm coat
  - If temperature > 25°C: recommend light clothing
  - Combine conditions appropriately
- Use logical operators (and, or)

**Test Cases:**
- [ ] 5°C, raining → "Wear a warm coat and bring an umbrella"
- [ ] 15°C, not raining → "Wear a light jacket"
- [ ] 30°C, raining → "Wear light clothing and bring an umbrella"
- [ ] 20°C, not raining → "Wear comfortable clothing"

---

### Problem 2.4: Login Authentication System
**Question:** Implement a basic login validation system using multiple conditions.

**Requirements:**
- Inputs: username, password, is_admin_attempt (boolean)
- Validation rules:
  - Username must exist (check against predefined users)
  - Password must match
  - Account must be active
  - Admin access requires admin role
- Use nested if statements and logical operators

**Test Scenarios:**
- [ ] Valid user login → "Login successful"
- [ ] Wrong password → "Invalid password"
- [ ] Inactive account → "Account deactivated"
- [ ] Non-admin trying admin access → "Insufficient privileges"
- [ ] Non-existent user → "User not found"

---

### Problem 2.5: Number Comparison Tool
**Question:** Create a program that compares two numbers and provides detailed feedback.

**Requirements:**
- Input: two numbers (num1, num2)
- Compare using all comparison operators: ==, !=, <, >, <=, >=
- Display results of each comparison
- Show which number is larger/smaller
- Handle equal numbers case

**Sample Output:**
```
Comparing 10 and 5:
10 > 5: True
10 >= 5: True
10 < 5: False
10 <= 5: False
10 == 5: False
10 != 5: True
10 is larger than 5
```

**Test Cases:**
- [ ] 10 vs 5 (first larger)
- [ ] 3 vs 8 (first smaller)
- [ ] 7 vs 7 (equal)
- [ ] Negative numbers: -5 vs 2

---

### Problem 2.6: BMI Calculator with Categories
**Question:** Create a BMI calculator that categorizes health status using conditionals.

**Requirements:**
- Inputs: weight (kg), height (meters)
- Calculate BMI: weight / (height²)
- Categories:
  - Underweight: BMI < 18.5
  - Normal: 18.5 ≤ BMI < 25
  - Overweight: 25 ≤ BMI < 30
  - Obese: BMI ≥ 30
- Handle invalid inputs (negative values, zero height)

**Test Cases:**
- [ ] Weight: 70kg, Height: 1.75m → BMI ≈ 22.9 → "Normal"
- [ ] Weight: 50kg, Height: 1.70m → BMI ≈ 17.3 → "Underweight"
- [ ] Weight: 90kg, Height: 1.80m → BMI ≈ 27.8 → "Overweight"
- [ ] Invalid height (0 or negative) → "Invalid height"

---

### Problem 2.7: Traffic Light Controller
**Question:** Simulate a traffic light system using conditional logic.

**Requirements:**
- Input: current light color ("red", "yellow", "green")
- Determine what action to take:
  - Red: "Stop"
  - Yellow: "Prepare to stop" or "Prepare to go" (depending on context)
  - Green: "Go"
- Handle invalid colors
- Add pedestrian crossing logic

**Test Cases:**
- [ ] "red" → "Stop"
- [ ] "yellow" → "Caution: Prepare to stop"
- [ ] "green" → "Go"
- [ ] "blue" → "Invalid light color"
- [ ] Add pedestrian crossing: "green" with pedestrian → "Stop for pedestrian"

---

### Problem 2.8: Discount Calculator
**Question:** Create a discount system for an online store using complex conditions.

**Requirements:**
- Inputs: purchase_amount, customer_type ("regular", "premium", "vip"), first_time (boolean)
- Discount rules:
  - First-time customers: 10% off
  - Premium customers: 15% off
  - VIP customers: 20% off
  - Orders > $100: additional 5% off
  - Orders > $500: additional 10% off
- Calculate final price after all applicable discounts

**Test Cases:**
- [ ] $50, regular, first-time → 10% off → $45
- [ ] $150, premium, returning → 15% + 5% = 20% off → $120
- [ ] $600, vip, first-time → 20% + 10% + 10% = 40% off → $360
- [ ] $25, regular, returning → No discount → $25

---

### Problem 2.9: Truthiness Evaluator
**Question:** Create a program that demonstrates Python's concept of truthiness.

**Requirements:**
- Test various values for truthiness: 0, 1, "", "hello", [], [1,2], {}, {"a":1}, None, True, False
- For each value, show:
  - The value itself
  - Its type
  - Whether it's truthy or falsy
  - Why it's truthy/falsy
- Use if statements to test truthiness

**Expected Results:**
- [ ] Falsy values: 0, "", [], {}, None, False
- [ ] Truthy values: non-zero numbers, non-empty strings/lists/dicts, True
- [ ] Clear explanation of why each value is truthy/falsy

---

### Problem 2.10: Simple Game Score Evaluator
**Question:** Create a program that evaluates game scores using multiple conditions.

**Requirements:**
- Input: player_score, level, time_bonus (boolean)
- Scoring rules:
  - Base score: player_score
  - Level multiplier: level 1=x1, 2=x1.5, 3=x2, 4+=x2.5
  - Time bonus: +20% if completed quickly
  - Grade: S (90%+), A (80-89%), B (70-79%), C (60-69%), D (below 60%)
- Calculate final score and grade

**Test Cases:**
- [ ] Score: 100, Level: 1, No bonus → Final: 100, Grade: S
- [ ] Score: 80, Level: 2, With bonus → Final: 120, Grade: S
- [ ] Score: 60, Level: 3, No bonus → Final: 120, Grade: A
- [ ] Score: 40, Level: 1, With bonus → Final: 48, Grade: D