# What is a leap year?
# A leap year has:

# 366 days instead of 365.
# An extra day, February 29.
# It happens roughly every 4 years, but there are exceptions:
# A year is a leap year if:
# It is divisible by 4.
# BUT not divisible by 100, unless...
# It is divisible by 400.


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year"
            else:
                return f"{year} is not a leap year"
        else:
            return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"


is_leap_year(2000)
# 2000 > Leap
# 2100 > Not Leap


# OR
def is_leap_year(year):
    # Simplified logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"


# Explanation:
"""
Leap Year Rules:
----------------
A year is a leap year if:
	1.	Condition 1: It is divisible by 4 AND not divisible by 100.
	•	This identifies most leap years.
	•	Example:
	•	Year 2024 → Divisible by 4 (✅), not divisible by 100 (✅) → Leap Year.
	2.	Condition 2: It is divisible by 400.
	•	This makes exceptions for years divisible by 100 but still leap years.
	•	Example:
	•	Year 2000 → Divisible by 4 (✅), divisible by 100 (✅), divisible by 400 (✅) → Leap Year.
	•	Year 2100 → Divisible by 4 (✅), divisible by 100 (✅), not divisible by 400 (❌) → Not a Leap Year.
"""
