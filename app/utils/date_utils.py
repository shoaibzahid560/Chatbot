from datetime import datetime

# Format date to readable string
def format_date(date_string):
    """Convert a date string to a formatted date"""
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y")

# Calculate days between two dates
def days_between(start_date, end_date):
    """Calculate the number of days between two date strings"""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return (end - start).days

# Calculate days from today to a target date
def days_until(target_date):
    """Calculate days from today until a target date"""
    today = datetime.now()
    target = datetime.strptime(target_date, "%Y-%m-%d")
    return (target - today).days

# Check if a date is in the past
def is_past_due(date_string):
    """Check if a date is in the past"""
    target = datetime.strptime(date_string, "%Y-%m-%d")
    return target < datetime.now()

# Get current date as string
def get_today_string():
    """Get today's date as a formatted string"""
    return datetime.now().strftime("%Y-%m-%d")