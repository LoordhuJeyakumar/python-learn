#!/usr/bin/env python3
"""
STRING OPERATIONS IN PYTHON - Complete Guide
=============================================

Strings are sequences of characters. Like words in a cookbook -
you can combine, modify, search, and format them.

ANALOGY: Cooking with Text
- Concatenation = Combining ingredients
- Slicing = Cutting ingredients
- Methods = Kitchen tools (chop, grill, mix)
- Formatting = Plating and presentation

WHY STRINGS MATTER:
- User interfaces (displaying messages)
- Data processing (parsing input)
- File handling (reading/writing text)
- Web development (HTML, JSON, APIs)
"""

# ==========================================
# 1. BASIC STRING CREATION & OPERATIONS
# ==========================================

print("📝 BASIC STRING OPERATIONS - Text Ingredients")
print("=" * 50)

# String creation
print("🏷️ String creation methods:")
single_quotes = 'Hello World'
double_quotes = "Hello World"
triple_quotes = """Hello
World"""  # Multi-line

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes: {triple_quotes}")
print()

# String concatenation (combining)
print("🔗 String concatenation:")
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Repetition
print("🔄 String repetition:")
laugh = "ha" * 3
print(f"Laugh: {laugh}")

stars = "⭐" * 5
print(f"Stars: {stars}")
print()

# ==========================================
# 2. STRING INDEXING & SLICING
# ==========================================

print("✂️ STRING INDEXING & SLICING - Text Cutting")
print("=" * 50)

text = "Python Programming"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")
print()

# Indexing (single characters)
print("📍 Indexing (positions start at 0):")
print(f"text[0] = '{text[0]}'")      # First character
print(f"text[6] = '{text[6]}'")      # 7th character (space)
print(f"text[-1] = '{text[-1]}'")    # Last character
print(f"text[-2] = '{text[-2]}'")    # Second to last
print()

# Slicing (substrings)
print("🔪 Slicing [start:end:step]:")
print(f"text[0:6] = '{text[0:6]}'")    # First 6 characters
print(f"text[7:] = '{text[7:]}'")      # From position 7 to end
print(f"text[:6] = '{text[:6]}'")      # From start to position 6
print(f"text[::2] = '{text[::2]}'")    # Every other character
print(f"text[::-1] = '{text[::-1]}'")  # Reverse string
print()

# Practical slicing examples
filename = "document.pdf"
print("📄 Practical slicing examples:")
print(f"Filename: '{filename}'")
print(f"Name: '{filename[:-4]}'")      # Remove extension
print(f"Extension: '{filename[-4:]}'") # Get extension
print()

# ==========================================
# 3. STRING METHODS - TEXT PROCESSING TOOLS
# ==========================================

print("🛠️ STRING METHODS - Kitchen Tools")
print("=" * 50)

sample_text = "  Hello, World! Welcome to Python.  "
print(f"Sample text: '{sample_text}'")
print()

# Case conversion
print("🔤 Case conversion:")
print(f"Upper: '{sample_text.upper()}'")
print(f"Lower: '{sample_text.lower()}'")
print(f"Title: '{sample_text.title()}'")
print(f"Capitalize: '{sample_text.capitalize()}'")
print()

# Whitespace handling
print("🧽 Whitespace handling:")
print(f"Strip: '{sample_text.strip()}'")      # Remove all whitespace
print(f"Lstrip: '{sample_text.lstrip()}'")    # Left strip
print(f"Rstrip: '{sample_text.rstrip()}'")    # Right strip
print()

# Search and replace
print("🔍 Search and replace:")
text = "I like Python. Python is great!"
print(f"Original: '{text}'")
print(f"Find 'Python': {text.find('Python')}")           # First occurrence
print(f"Replace: '{text.replace('Python', 'JavaScript')}'")
print(f"Count 'Python': {text.count('Python')}")
print()

# Splitting and joining
print("✂️ Splitting and joining:")
sentence = "Python is fun and powerful"
words = sentence.split()  # Split into list
print(f"Split: {words}")

# Join back together
rejoined = " ".join(words)
print(f"Join: '{rejoined}'")

# Split by specific character
csv_data = "Alice,30,Engineer"
fields = csv_data.split(",")
print(f"CSV split: {fields}")
print()

# ==========================================
# 4. STRING FORMATTING - TEXT PRESENTATION
# ==========================================

print("🎨 STRING FORMATTING - Plating & Presentation")
print("=" * 50)

# Old-style formatting (% operator)
print("📜 Old-style formatting:")
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
print()

# New-style formatting (.format())
print("🆕 New-style formatting:")
print("My name is {} and I am {} years old.".format(name, age))
print("Hello {name}, you are {age} years old.".format(name="Bob", age=25))
print()

# f-strings (most modern and readable)
print("⚡ f-strings (recommended):")
print(f"My name is {name} and I am {age} years old.")

# f-strings with expressions
price = 19.99
tax = 0.08
total = price * (1 + tax)
print(f"Price: ${price:.2f}, Tax: {tax*100:.0f}%, Total: ${total:.2f}")

# f-strings with formatting
large_number = 1234567890
print(f"Large number: {large_number:,}")  # Add commas
print(f"Binary: {42:b}, Hex: {42:x}, Octal: {42:o}")
print()

# Alignment and width
print("📐 Alignment and width:")
names = ["Alice", "Bob", "Catherine"]
for name in names:
    print(f"{name:<10} | {len(name):>3} chars")  # Left align, right align
print()

# ==========================================
# 5. STRING VALIDATION & CHECKING
# ==========================================

print("✅ STRING VALIDATION - Quality Control")
print("=" * 50)

test_strings = [
    "hello",
    "Hello123",
    "12345",
    "Hello World",
    "",
    "   ",
    "HELLO",
    "hello world"
]

print("🧪 String validation tests:")
for s in test_strings:
    print(f"String: '{s}'")
    print(f"  isalpha(): {s.isalpha()}    isdigit(): {s.isdigit()}")
    print(f"  isalnum(): {s.isalnum()}    isspace(): {s.isspace()}")
    print(f"  isupper(): {s.isupper()}    islower(): {s.islower()}")
    print(f"  startswith('H'): {s.startswith('H')}    endswith('d'): {s.endswith('d')}")
    print()

# Custom validation functions
def is_valid_email(email):
    """Check if string looks like a valid email."""
    return "@" in email and "." in email and len(email) > 5

def is_strong_password(password):
    """Check if password meets strength criteria."""
    return (len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password))

print("🔒 Custom validation:")
emails = ["user@example.com", "invalid-email", "test@.com", ""]
for email in emails:
    print(f"Email '{email}' valid: {is_valid_email(email)}")

passwords = ["weak", "Strong123", "12345678", "Strong"]
for pwd in passwords:
    print(f"Password '{pwd}' strong: {is_strong_password(pwd)}")
print()

# ==========================================
# 6. ADVANCED STRING OPERATIONS
# ==========================================

print("🚀 ADVANCED STRING OPERATIONS - Chef Techniques")
print("=" * 50)

# String encoding/decoding
print("🔄 Encoding/decoding:")
text = "Hello, 世界!"
print(f"Original: {text}")

# UTF-8 encoding
encoded = text.encode('utf-8')
print(f"Encoded: {encoded}")

# Decode back
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")
print()

# Regular expressions (basic examples)
import re

print("🔍 Basic regular expressions:")
phone_numbers = [
    "123-456-7890",
    "(555) 123-4567",
    "555.123.4567",
    "invalid-phone"
]

phone_pattern = r'[\(\)\.\-\s]*\d{3}[\(\)\.\-\s]*\d{3}[\(\)\.\-\s]*\d{4}'
for phone in phone_numbers:
    is_valid = bool(re.match(phone_pattern, phone))
    print(f"Phone '{phone}' valid: {is_valid}")
print()

# String templates
from string import Template

print("📋 String templates:")
template = Template("Hello $name, welcome to $place!")
result = template.substitute(name="Alice", place="Python World")
print(result)

# Safe substitution (won't crash on missing variables)
safe_template = Template("Hello $name, welcome to ${place}!")
safe_result = safe_template.safe_substitute(name="Bob")  # place is missing
print(safe_result)
print()

# ==========================================
# 7. PRACTICAL EXAMPLES - REAL APPLICATIONS
# ==========================================

print("🏪 PRACTICAL EXAMPLES - Real Restaurant Scenarios")
print("=" * 50)

# Example 1: Menu item formatting
print("🍽️ Example 1: Menu formatting")
menu_items = [
    ("Margherita Pizza", 15.99),
    ("Caesar Salad", 8.50),
    ("Grilled Salmon", 22.99),
    ("Chocolate Cake", 6.99)
]

print("RESTAURANT MENU")
print("=" * 30)
for name, price in menu_items:
    print(f"{name:<20} ${price:>6.2f}")
print()

# Example 2: Customer name processing
print("👥 Example 2: Name processing")
customer_names = [
    "alice johnson",
    "BOB SMITH",
    "charlie brown",
    "DIANA PRINCE"
]

print("Customer name formatting:")
for name in customer_names:
    formatted = name.title()  # Capitalize each word
    print(f"'{name}' → '{formatted}'")
print()

# Example 3: Order parsing
print("📝 Example 3: Order parsing")
order_text = "2 pizzas, 1 salad, 3 waters"
print(f"Original order: {order_text}")

# Extract numbers and items
import re
numbers = re.findall(r'\d+', order_text)
items = re.findall(r'\d+\s+([a-zA-Z]+)', order_text)

print("Parsed order:")
for num, item in zip(numbers, items):
    print(f"  {num} x {item}")
print()

# Example 4: Receipt generation
print("🧾 Example 4: Receipt generation")
def generate_receipt(items, customer_name):
    """Generate a formatted receipt."""
    total = sum(price for _, price in items)

    receipt = f"""
RECEIPT FOR {customer_name.upper()}
{'='*40}

ITEMS ORDERED:
"""

    for name, price in items:
        receipt += f"{name:<20} ${price:>7.2f}\n"

    receipt += f"""
{'='*40}
TOTAL: ${total:>29.2f}
{'='*40}

Thank you for dining with us!
"""

    return receipt

customer_order = [
    ("Margherita Pizza", 15.99),
    ("Caesar Salad", 8.50),
    ("Soda", 2.99)
]

receipt = generate_receipt(customer_order, "Alice Johnson")
print(receipt)

# ==========================================
# 8. STRING PERFORMANCE & BEST PRACTICES
# ==========================================

print("⚡ STRING PERFORMANCE & BEST PRACTICES")
print("=" * 50)

# String concatenation performance
print("🐌 Inefficient string concatenation (slow):")
result = ""
for i in range(5):
    result += str(i)  # Creates new string each time
print(f"Result: '{result}'")
print()

print("⚡ Efficient string concatenation:")
result_list = [str(i) for i in range(5)]
result = "".join(result_list)  # Single operation
print(f"Result: '{result}'")
print()

# String interning
print("🔍 String interning:")
a = "hello"
b = "hello"
print(f"a is b: {a is b}")  # Same object in memory

c = "hello world"
d = "hello world"
print(f"c is d: {c is d}")  # May be different objects
print()

# Best practices
print("💡 String handling best practices:")
print("• Use f-strings for formatting (fastest)")
print("• Use .join() for concatenation (efficient)")
print("• Use .strip() to clean user input")
print("• Use .lower() for case-insensitive comparison")
print("• Validate input before processing")
print("• Use raw strings (r'') for regex patterns")
print()

# ==========================================
# 9. COMMON STRING PATTERNS
# ==========================================

print("🎯 COMMON STRING PATTERNS - Recipe Collection")
print("=" * 50)

# Pattern 1: Cleaning user input
def clean_input(text):
    """Clean and normalize user input."""
    return text.strip().lower()

user_inputs = ["  HELLO WORLD  ", "Python Programming", "  test  "]
print("🧹 Input cleaning:")
for inp in user_inputs:
    cleaned = clean_input(inp)
    print(f"'{inp}' → '{cleaned}'")
print()

# Pattern 2: Extracting information
def extract_domain(email):
    """Extract domain from email address."""
    return email.split('@')[-1]

emails = ["user@example.com", "test@gmail.com", "admin@company.org"]
print("📧 Domain extraction:")
for email in emails:
    domain = extract_domain(email)
    print(f"{email} → {domain}")
print()

# Pattern 3: Text formatting
def format_phone_number(phone):
    """Format phone number consistently."""
    # Remove all non-digit characters
    digits = ''.join(c for c in phone if c.isdigit())

    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone  # Return original if can't format

phones = ["1234567890", "(555) 123-4567", "555.123.4567"]
print("📞 Phone formatting:")
for phone in phones:
    formatted = format_phone_number(phone)
    print(f"'{phone}' → '{formatted}'")
print()

# Pattern 4: Text truncation
def truncate_text(text, max_length=50, suffix="..."):
    """Truncate text to max length with suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

long_texts = [
    "This is a very long sentence that needs to be truncated.",
    "Short text",
    "Another long text that should be cut off at some point"
]

print("✂️ Text truncation:")
for text in long_texts:
    truncated = truncate_text(text, 30)
    print(f"'{text}' → '{truncated}'")
print()

# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON STRING OPERATIONS SUMMARY")
print("=" * 50)
print("✅ String Creation:")
print("   • Single quotes: 'text'")
print("   • Double quotes: \"text\"")
print("   • Triple quotes: \"\"\"multi-line\"\"\"")
print()
print("✅ String Operations:")
print("   • Concatenation: 'hello' + ' ' + 'world'")
print("   • Repetition: 'ha' * 3")
print("   • Indexing: text[0], text[-1]")
print("   • Slicing: text[0:5], text[::2]")
print()
print("✅ Common Methods:")
print("   • .upper(), .lower(), .title() - Case conversion")
print("   • .strip(), .lstrip(), .rstrip() - Whitespace")
print("   • .split(), .join() - Breaking/combining")
print("   • .find(), .replace(), .count() - Search/modify")
print("   • .startswith(), .endswith() - Checking")
print()
print("✅ Validation Methods:")
print("   • .isalpha(), .isdigit(), .isalnum() - Content checks")
print("   • .isupper(), .islower(), .isspace() - Case/space checks")
print()
print("✅ Formatting Options:")
print("   • f-strings: f\"Hello {name}!\"")
print("   • .format(): \"Hello {}!\".format(name)")
print("   • % operator: \"Hello %s!\" % name")
print()
print("💡 Pro Tips:")
print("• Use f-strings (fastest and most readable)")
print("• Clean user input with .strip().lower()")
print("• Use .join() for efficient concatenation")
print("• Validate before processing")
print("• Consider encoding for international text")