# Leap Year Checker

This Python script determines whether a given year is a leap year according to the Gregorian calendar rules.

## Features

*   Accurately checks for leap years based on divisibility by 4, 100, and 400.
*   Provides clear output indicating whether a year is a leap year or not.

## Leap Year Explained

A leap year is a year with one extra day, February 29th, resulting in a total of 366 days instead of the usual 365. Leap years occur roughly every four years, but there are some exceptions to this rule.

### Determining Leap Years

The following rules help determine if a year is a leap year:

1. **Divisible by 4:**  If a year is evenly divisible by 4, it's a leap year (with some exceptions).  For example, the year 2024 is divisible by 4, so it's a leap year.
2. **Exception: Not Divisible by 100:**  However, years divisible by 100 (century years) are not leap years unless...
3. **Exception: Divisible by 400:**  Years divisible by 100 **and** by 400 are considered leap years.  For example, the year 2000 is divisible by both 100 and 400, making it a leap year.  Year 2100, however, is only divisible by 100 and not by 400, so it's not a leap year.

These rules ensure the calendar remains synchronized with the Earth's revolution around the sun.

**Explanation:**

The provided code snippet outlines the leap year rules:

* **Condition 1:** A year is a leap year if it's divisible by 4 but not by 100. This covers most leap years.
* **Condition 2:** A year divisible by 400 is a leap year, even if it's also divisible by 100. This accounts for century years that are exceptions to the first rule.

These rules ensure accurate leap year calculation.


## How to Use

1.  Clone the repository:

    ```bash
    git clone [https://github.com/](https://github.com/)<your_username>/leap_year_checker.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd leap_year_checker
    ```

3.  Run the script, replacing `YEAR` with the year you want to check:

    ```bash
    python leap_year_checker.py <YEAR>
    ```

    For example:

    ```bash
    python leap_year_checker.py 2024
    ```

## Example Output:

**Example 1: Leap Year**

```bash
python leap_year_checker.py 2024

2024 is a leap year
