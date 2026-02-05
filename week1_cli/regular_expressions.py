#!/usr/bin/env python3
"""
REGULAR EXPRESSIONS - Complete Guide
====================================

Regular expressions (regex) are patterns for matching and manipulating text.
Like a master key that can unlock any text pattern you can imagine.

ANALOGY: Text Treasure Hunt
- Pattern = Treasure map with clues
- Text = The landscape to search
- Match = Finding the treasure
- Groups = Collecting different treasures
- Replace = Trading treasures

WHY REGEX MATTERS:
- Input validation (emails, phones, URLs)
- Data extraction (parsing logs, HTML, JSON)
- Text processing (find/replace, formatting)
- Search functionality (database queries, file search)
"""

import re


# ==========================================
# 1. BASIC PATTERN MATCHING
# ==========================================

print("🔍 BASIC PATTERN MATCHING - Finding Treasure")
print("=" * 50)

# Simple text matching
print("📝 Simple pattern matching:")

text = "Hello world! Welcome to Python programming."
pattern = r"Python"

# Search for pattern
match = re.search(pattern, text)
if match:
    print(f"✅ Found '{pattern}' at position {match.start()}-{match.end()}")
    print(f"   Match: '{match.group()}'")
else:
    print(f"❌ '{pattern}' not found")

# Find all occurrences
all_matches = re.findall(pattern, text)
print(f"All matches: {all_matches}")
print()



# ==========================================
# 2. METACHARACTERS - Special Symbols
# ==========================================

print("🔮 METACHARACTERS - Magic Symbols")
print("=" * 50)

# . (dot) - matches any character except newline
print("📍 Dot (.) - Any character:")
patterns = [r"p.t", r"c.t", r"d.g"]
test_words = ["pet", "cat", "dog", "cut", "dot"]

for pattern in patterns:
    for word in test_words:
        if re.search(pattern, word):
            print(f"   {pattern} matches '{word}'")
print()

# ^ (caret) - start of string
# $ (dollar) - end of string
print("📍 Anchors (^ and $) - String boundaries:")
text = "Python is great. Python is fun. Python is powerful."

# Start of string
start_matches = re.findall(r"^Python", text)
print(f"Lines starting with 'Python': {start_matches}")

# End of string (multiline)
end_matches = re.findall(r"powerful.$", text)
print(f"Lines ending with 'powerful.': {end_matches}")
print()

# * (asterisk) - zero or more
# + (plus) - one or more
# ? (question) - zero or one
print("📍 Quantifiers (*, +, ?) - How many times:")
test_strings = ["a", "aa", "aaa", "b", "ab", "aab", "aaab"]

patterns_quantifiers = [
    (r"a*", "zero or more 'a's"),
    (r"a+", "one or more 'a's"),
    (r"a?", "zero or one 'a'")
]

for pattern, description in patterns_quantifiers:
    print(f"{description}:")
    for s in test_strings:
        if re.search(pattern, s):
            print(f"   '{s}' matches {pattern}")
print()



# ==========================================
# 3. CHARACTER CLASSES - What to Match
# ==========================================

print("📚 CHARACTER CLASSES - What Characters to Accept")
print("=" * 50)

# [abc] - any of a, b, or c
print("📍 Character sets [abc]:")
text = "The cat sat on the mat."
matches = re.findall(r"[cm]at", text)  # cat or mat
print(f"Words ending with 'at': {matches}")

# [a-z] - range of characters
print("📍 Character ranges [a-z], [0-9]:")
text = "Order #123: 5 apples, 3 bananas, 2 oranges"

# Find all numbers
numbers = re.findall(r"[0-9]+", text)
print(f"Numbers found: {numbers}")

# Find all lowercase letters
letters = re.findall(r"[a-z]+", text)
print(f"Words found: {letters}")
print()

# \d - digit, \w - word char, \s - whitespace
print("📍 Shorthand classes (\\d, \\w, \\s):")
text = "Email: user123@example.com, Phone: (555) 123-4567"

# Extract different types
digits = re.findall(r"\d+", text)
words = re.findall(r"\w+", text)
whitespace = re.findall(r"\s+", text)

print(f"Digits: {digits}")
print(f"Words: {words}")
print(f"Whitespace lengths: {[len(w) for w in whitespace]}")
print()



# ==========================================
# 4. GROUPS AND CAPTURING - Collecting Treasures
# ==========================================

print("🎒 GROUPS AND CAPTURING - Collecting Different Treasures")
print("=" * 50)

# (pattern) - capturing group
print("📍 Capturing groups (parentheses):")
phone_text = "Call me at (555) 123-4567 or (800) 555-0199"

# Extract area code and number separately
phones = re.findall(r"\((\d{3})\)\s*(\d{3})-(\d{4})", phone_text)
print("Phone numbers with groups:")
for area, prefix, suffix in phones:
    print(f"   Area: {area}, Number: {prefix}-{suffix}")
print()

# Named groups (?P<name>pattern)
print("📍 Named groups (?P<name>):")
email_text = "Contact: john.doe@example.com or jane@example.org"

emails = re.findall(r"(?P<username>[\w.]+)@(?P<domain>[\w.]+)", email_text)
print("Email components:")
for username, domain in emails:
    print(f"   Username: {username}, Domain: {domain}")
print()

# Non-capturing groups (?:pattern)
print("📍 Non-capturing groups (?:):")
text = "The colors are red, green, and blue."
colors = re.findall(r"\b(?:red|green|blue)\b", text)
print(f"Colors found: {colors}")
print()

# ==========================================
# 5. PRACTICAL REGEX PATTERNS - Real Applications
# ==========================================

print("🏪 PRACTICAL REGEX PATTERNS - Real Backend Scenarios")
print("=" * 50)

# Email validation
def validate_email(email):
    """Validate email address format."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print("📧 Email validation:")
emails = ["user@example.com", "test.email@domain.co.uk", "invalid-email", "@example.com", "user@"]
for email in emails:
    is_valid = validate_email(email)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"   {email}: {status}")
print()

# Phone number extraction
def extract_phone_numbers(text):
    """Extract phone numbers from text."""
    # Matches: (555) 123-4567, 555-123-4567, 555.123.4567, 5551234567
    pattern = r"\b(?:\(\d{3}\)\s*|\d{3}[.-]?)\d{3}[.-]?\d{4}\b"
    return re.findall(pattern, text)

print("📞 Phone number extraction:")
contact_text = """
Call us at (555) 123-4567 or 800-555-0199.
Emergency: 911
International: +1-555-123-4567
"""

phones = extract_phone_numbers(contact_text)
print("Phone numbers found:")
for phone in phones:
    print(f"   • {phone}")
print()

# URL extraction
def extract_urls(text):
    """Extract URLs from text."""
    pattern = r"https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w*))?)?"
    return re.findall(pattern, text)

print("🔗 URL extraction:")
web_text = """
Visit https://www.python.org for docs.
Check out https://github.com/user/repo for code.
Invalid: http://
"""

urls = extract_urls(web_text)
print("URLs found:")
for url in urls:
    print(f"   • {url}")
print()

# Log file parsing
def parse_log_entry(log_line):
    """Parse a log entry into components."""
    pattern = r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)"
    match = re.match(pattern, log_line)

    if match:
        date, time, level, message = match.groups()
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }
    return None

print("📝 Log file parsing:")
log_lines = [
    "2024-01-15 14:30:25 INFO User login successful",
    "2024-01-15 14:35:12 ERROR Database connection failed",
    "2024-01-15 14:40:01 WARNING Low disk space"
]

for log_line in log_lines:
    parsed = parse_log_entry(log_line)
    if parsed:
        print(f"   {parsed['level']}: {parsed['message']} (at {parsed['time']})")
print()

# ==========================================
# 6. SEARCH AND REPLACE - Text Editing
# ==========================================

print("🔄 SEARCH AND REPLACE - Text Editing")
print("=" * 50)

# Basic replace
print("📝 Basic string replacement:")
text = "I like Python. Python is great. Python is powerful."
new_text = re.sub(r"Python", "JavaScript", text)
print(f"Original: {text}")
print(f"Replaced: {new_text}")
print()

# Replace with function
def censor_word(match):
    """Censor a word by replacing with asterisks."""
    word = match.group()
    return "*" * len(word)

print("🔒 Censoring sensitive words:")
message = "The password is secret and confidential."
censored = re.sub(r"\b(?:password|secret|confidential)\b", censor_word, message, flags=re.IGNORECASE)
print(f"Original: {message}")
print(f"Censored: {censored}")
print()

# Replace with counter
print("🔢 Numbered replacement:")
text = "Item 1, Item 2, Item 3"
count = 0
def number_replacement(match):
    global count
    count += 1
    return f"Task {count}"

numbered = re.sub(r"Item \d+", number_replacement, text)
print(f"Original: {text}")
print(f"Numbered: {numbered}")
print()

# ==========================================
# 7. FLAGS AND OPTIONS - Advanced Matching
# ==========================================

print("🚩 FLAGS AND OPTIONS - Advanced Matching Modes")
print("=" * 50)

# Case insensitive matching
print("🔤 Case insensitive (re.IGNORECASE):")
text = "Python is GREAT. python is FUN. PyThOn Is PoWeRfUl."
matches = re.findall(r"python", text, re.IGNORECASE)
print(f"Text: {text}")
print(f"Case-insensitive 'python' matches: {matches}")
print()

# Multiline matching
print("📄 Multiline matching (re.MULTILINE):")
multiline_text = """Line 1: Start here
Line 2: Middle line
Line 3: End here"""

# Match lines starting with "Line"
line_matches = re.findall(r"^Line \d+", multiline_text, re.MULTILINE)
print("Multiline text:")
print(multiline_text)
print(f"Lines starting with 'Line': {line_matches}")
print()

# Dot matches newline
print("🔘 Dot matches all (re.DOTALL):")
html_text = """<div>
<span>Hello</span>
<span>World</span>
</div>"""

# Extract content between div tags
content = re.search(r"<div>(.*?)</div>", html_text, re.DOTALL)
if content:
    print(f"Content between div tags: '{content.group(1).strip()}'")
print()

# Verbose regex (re.VERBOSE)
print("📖 Verbose regex (re.VERBOSE) - Self-documenting patterns:")
# Complex email pattern with comments
email_pattern = r"""
    ^              # Start of string
    [\w\.-]+       # Username (word chars, dots, hyphens)
    @              # At symbol
    [\w\.-]+       # Domain name
    \.             # Dot
    \w+            # Top-level domain
    $              # End of string
"""

test_emails = ["user@example.com", "test.email@domain.co.uk", "invalid@"]
for email in test_emails:
    is_valid = bool(re.match(email_pattern, email, re.VERBOSE))
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"   {email}: {status}")
print()

# ==========================================
# 8. PERFORMANCE AND BEST PRACTICES
# ==========================================

print("⚡ PERFORMANCE & BEST PRACTICES - Efficient Pattern Matching")
print("=" * 50)

import time

# Compile regex for reuse (faster)
print("🔧 Compiled regex (reuse pattern):")
email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

test_emails = ["user1@example.com", "user2@example.com", "invalid@", "user3@example.com"] * 100

# Method 1: Recompile each time (slow)
start = time.time()
for email in test_emails:
    re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)
slow_time = time.time() - start

# Method 2: Use compiled pattern (fast)
start = time.time()
for email in test_emails:
    email_pattern.match(email)
fast_time = time.time() - start

print(f"Slow method (recompile): {slow_time:.4f} seconds")
print(f"Fast method (compiled): {fast_time:.4f} seconds")
print(f"Speed improvement: {slow_time/fast_time:.1f}x faster")
print()

# Best practices
print("💡 Regex Best Practices:")
print("• Use raw strings (r'pattern') for patterns")
print("• Compile frequently used patterns with re.compile()")
print("• Use specific patterns instead of .* when possible")
print("• Test patterns with edge cases")
print("• Use re.VERBOSE for complex patterns")
print("• Consider alternatives (str methods) for simple tasks")
print("• Be careful with catastrophic backtracking")
print()

# ==========================================
# 9. COMMON REGEX PATTERNS - Backend Essentials
# ==========================================

print("🎯 COMMON REGEX PATTERNS - Backend Development Essentials")
print("=" * 50)

# Collection of useful patterns
patterns = {
    "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "phone_us": r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
    "zip_code": r"^\d{5}(-\d{4})?$",
    "credit_card": r"^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$",
    "ip_address": r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
    "url": r"^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w*))?)?"
}

test_data = {
    "email": ["user@example.com", "invalid-email", "test@domain.co.uk"],
    "phone_us": ["555-123-4567", "(800) 555-0199", "5551234567"],
    "zip_code": ["12345", "12345-6789", "123456"],
    "credit_card": ["1234 5678 9012 3456", "1234567890123456", "1234-5678-9012-3456"],
    "ip_address": ["192.168.1.1", "10.0.0.1", "256.1.1.1"],
    "url": ["https://example.com", "http://test.org/path", "invalid-url"]
}

print("🧪 Testing common patterns:")
for pattern_name, pattern in patterns.items():
    print(f"\n{pattern_name.upper()}:")
    compiled = re.compile(pattern)

    for test_value in test_data[pattern_name]:
        is_valid = bool(compiled.match(test_value))
        status = "✅" if is_valid else "❌"
        print(f"   {status} {test_value}")
print()

# ==========================================
# SUMMARY
# ==========================================

print("🎓 PYTHON REGULAR EXPRESSIONS SUMMARY")
print("=" * 50)
print("✅ Basic Functions:")
print("   • re.search() - Find first match anywhere")
print("   • re.match() - Match from start of string")
print("   • re.findall() - Find all matches")
print("   • re.sub() - Replace matches")
print()
print("✅ Metacharacters:")
print("   • . - Any character")
print("   • ^ - Start of string")
print("   • $ - End of string")
print("   • * - Zero or more")
print("   • + - One or more")
print("   • ? - Zero or one")
print()
print("✅ Character Classes:")
print("   • [abc] - Any of a, b, c")
print("   • [a-z] - Range of characters")
print("   • \\d - Digit, \\w - Word char, \\s - Whitespace")
print()
print("✅ Groups:")
print("   • (pattern) - Capturing group")
print("   • (?P<name>pattern) - Named group")
print("   • (?:pattern) - Non-capturing group")
print()
print("✅ Flags:")
print("   • re.IGNORECASE - Case insensitive")
print("   • re.MULTILINE - Multi-line matching")
print("   • re.DOTALL - Dot matches newlines")
print("   • re.VERBOSE - Self-documenting patterns")
print()
print("✅ Performance:")
print("   • Compile patterns: re.compile()")
print("   • Use specific patterns over .*")
print("   • Test with edge cases")
print()
print("💡 Regex is like a Swiss Army knife for text processing!")
print("   Master it and you'll handle any text manipulation task.")