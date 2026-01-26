#!/usr/bin/env python3
"""
DATETIME OPERATIONS - Complete Guide
====================================

Date and time handling is crucial for backend applications.
Like a master clock that keeps everything synchronized and tracked.

ANALOGY: Restaurant Time Management
- datetime.now() = Current time check
- Timestamps = Order timestamps
- Time zones = Different restaurant locations
- Scheduling = Reservation system
- Formatting = Receipt timestamps

WHY DATETIME MATTERS:
- Logging (when events happened)
- Data tracking (creation/update times)
- Scheduling (future events)
- Time zones (global applications)
- Performance monitoring (elapsed time)
"""

import datetime
import time
from dateutil import relativedelta
import calendar

# ==========================================
# 1. BASIC DATETIME CREATION
# ==========================================

print("🕒 Basic datetime creation:")

#Current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

#Current date
current_date = datetime.date.today() 
print(f"Current date: {current_date}")

#Current time
current_time = datetime.time(current_datetime.hour, current_datetime.minute, current_datetime.second)
print(f"Current time: {datetime.datetime.time(current_datetime)}")

print(f"Current time: {current_time}")

print(f"Timezone: { current_datetime.tzinfo}") # Usually None in local timezone 


# ==========================================

# Creating specific dates and times
specific_date = datetime.date(2024,12, 25)
print(f"Specific date: {specific_date}")

specific_time = datetime.time(12, 30, 45)
print(f"Specific time: {specific_time}")

specific_datetime = datetime.datetime(2024, 12, 25, 12, 0, 0)
print(f"Specific datetime: {specific_datetime}")


# ==========================================
# 2. DATETIME COMPONENTS - Breaking Down Time
# ==========================================

print("🔍 DATETIME COMPONENTS - Dissecting Time")
print("=" * 50)

now = datetime.datetime.now()


print(f"Current datetime: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"Weekday: {now.weekday()}")  # 0=Monday, 6=Sunday
print(f"Day of year: {now.timetuple().tm_yday}") # 1-366    
print(f"Day of week: {now.strftime('%A')}") # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
print(f"Day of week: {now.strftime('%w')}") # 0-6, 0=Sunday
print(f"Day of week: {now.strftime('%d')}") # 01-31
print(f"Day of week: {now.strftime('%m')}") # 01-12
print(f"Day of week: {now.strftime('%y')}") # 24
print(f"Day of week: {now.strftime('%Y')}") # 2024
print(f"Day of week: {now.strftime('%H')}") # 00-23 
print(f"Day of week: {now.strftime('%M')}") # 00-59
print(f"Day of week: {now.strftime('%S')}") # 00-59


# Date components
today = datetime.date.today()
print(f"Today's date: {today}")
print(f"ISO format: {today.isoformat()}")
print(f"Weekday name: {today.strftime('%A')}")
print(f"Month name: {today.strftime('%B')}")
print()



# ==========================================
# 3. FORMATTING DATES - Time Display
# ==========================================

print("🎨 FORMATTING DATES - Time Display Styles")
print("=" * 50)

now = datetime.datetime.now()

print("📋 Common date formats:")
formats = [
    ("%Y-%m-%d", "ISO date"),
    ("%d/%m/%Y", "European date"),
    ("%m/%d/%Y", "US date"),
    ("%B %d, %Y", "Long date"),
    ("%A, %B %d", "Weekday date"),
    ("%Y-%m-%d %H:%M:%S", "ISO datetime"),
    ("%I:%M %p", "12-hour time"),
    ("%H:%M:%S", "24-hour time")
]

for fmt, description in formats:
    print(f"   {description}: {now.strftime(fmt)}")
print()

# Parsing dates from strings
print("🔄 Parsing dates from strings:")
date_strings = [
    "2024-12-25",
    "12/25/2024",
    "December 25, 2024",
    "2024-12-25 14:30:45"
]

formats_to_try = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%B %d, %Y",
    "%Y-%m-%d %H:%M:%S"
]

for date_str in date_strings:
    for fmt in formats_to_try:
        try:
            parsed = datetime.datetime.strptime(date_str, fmt)
            print(f"   '{date_str}' → {parsed} (format: {fmt})")
            break
        except ValueError:
            continue
    else:
        print(f"   '{date_str}' → Could not parse")
print()


# ==========================================
# 4. DATE ARITHMETIC - Time Calculations
# ==========================================

print("🧮 DATE ARITHMETIC - Time Calculations")
print("=" * 50)

# Creating time differences
print("📅 Time differences (timedelta):")
one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)
two_hours = datetime.timedelta(hours=2)


print(f"One day: {one_day}")
print(f"One week: {one_week}")
print(f"Two hours: {two_hours}")

now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"In one day: {now + one_day}")
print(f"One week ago: {now - one_week}")
print(f"In 2 hours: {now + two_hours}")
print()


#Date Difference
new_year = datetime.datetime(2026, 1, 1)
today = datetime.date.today()


if new_year.date() > today:
   days_until_new_year = (new_year.date() - today).days
   print(f"New Year is in {days_until_new_year} days")
else:
    days_until_new_year = (today - new_year.date()).days
    print(f"New Year is in {days_until_new_year} days")
print()

def add_business_days(start_date, days):
    current_date = start_date
    while days > 0:
        current_date += datetime.timedelta(days=1)
        if current_date.weekday() < 5: # 0-4 = Monday-Friday
            days -= 1
    return current_date
print("💼 Business days calculation:")
start = datetime.date.today()
result = add_business_days(start, 5)
print(f"5 business days from {start} is {result}")
print()


# ==========================================
# 5. TIME ZONES - Global Time Handling
# ==========================================

print("🌍 TIME ZONES - Global Time Coordination")
print("=" * 50)



# Naive vs aware datetimes
print("📍 Naive vs Aware datetimes:")
naive_time = datetime.datetime.now()
print(f"Naive time (no timezone): {naive_time}")
print(f"Timezone info: {naive_time.tzinfo}")
print()


# Using UTC time
print("🌍 UTC time handling:")
utc_now = datetime.datetime.utcnow()
print(f"UTC time: {utc_now}")
print()

def to_timezone(dt, offset_hours):
    """Convert a datetime to a specific timezone"""
    return dt + datetime.timedelta(hours=offset_hours)


print("Time zone conversions (simplified):")
current_utc = datetime.datetime.utcnow()
print(f"UTC: {current_utc}")

ny_time = to_timezone(current_utc, -5)  # EST
london_time = to_timezone(current_utc, 0)  # GMT
tokyo_time = to_timezone(current_utc, 9)  # JST

print(f"New York (EST): {ny_time}")
print(f"London (GMT): {london_time}")
print(f"Tokyo (JST): {tokyo_time}")
print()



# ==========================================
# 6. PRACTICAL APPLICATIONS - Backend Scenarios
# ==========================================

print("🏪 PRACTICAL APPLICATIONS - Real Backend Scenarios")
print("=" * 50)

# Logging with timestamps
def log_event(event_type, message):
    """Log an event with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event_type}: {message}")

print("📝 Event logging:")
log_event("INFO", "Application started")
log_event("INFO", "Database connected")
log_event("WARNING", "Low disk space")
print()

# User session tracking
class UserSession:
    """Track user login sessions."""

    def __init__(self, user_id):
        self.user_id = user_id
        self.login_time = datetime.datetime.now()
        self.last_activity = self.login_time

    def update_activity(self):
        """Update last activity timestamp."""
        self.last_activity = datetime.datetime.now()

    def get_session_duration(self):
        """Get session duration in minutes."""
        duration = datetime.datetime.now() - self.login_time
        return duration.total_seconds() / 60

    def is_session_expired(self, max_minutes=30):
        """Check if session has expired."""
        return self.get_session_duration() > max_minutes

# Session demonstration
print("👤 User session tracking:")
session = UserSession("user123")
print(f"Login time: {session.login_time}")
print(f"Session duration: {session.get_session_duration():.1f} minutes")

# Simulate activity after 5 minutes
time.sleep(0.1)  # Simulate 5 minutes (actually 0.1 seconds)
session.update_activity()
print(f"After activity: {session.get_session_duration():.1f} minutes")
print(f"Session expired: {session.is_session_expired(30)}")
print()

# Data record timestamps
class DataRecord:
    """A data record with automatic timestamps."""

    def __init__(self, data):
        self.data = data
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update(self, new_data):
        """Update the record."""
        self.data = new_data
        self.updated_at = datetime.datetime.now()

    def get_age_days(self):
        """Get record age in days."""
        age = datetime.datetime.now() - self.created_at
        return age.days

print("📊 Data record timestamps:")
record = DataRecord({"name": "Alice", "email": "alice@example.com"})
print(f"Created: {record.created_at}")
print(f"Data: {record.data}")

# Simulate update
time.sleep(0.1)  # Simulate time passing
record.update({"name": "Alice Johnson", "email": "alice.johnson@example.com"})
print(f"Updated: {record.updated_at}")
print(f"Age: {record.get_age_days()} days")
print(f"Updated data: {record.data}")
print()