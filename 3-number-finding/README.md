# Task 3 — Find Missing Numbers

A Python function that finds missing number(s) from a sequential array.

## How to Run

```bash
python3 find_missing.py
```

## How It Works

1. Sort the input array
2. Build a complete sequential set from min to max value
3. Subtract actual values from complete set to find missing numbers
4. Returns a single number if one is missing, or a list if multiple are missing

## Function Usage

```python
from find_missing import find_missing_numbers

# Single missing number
find_missing_numbers([3, 0, 2, 4])              # Output: 1
find_missing_numbers([3106, 3102, 3104, 3105, 3107])  # Output: 3103

# Multiple missing numbers
find_missing_numbers([1, 2, 4, 6, 7, 10])       # Output: [3, 5, 8, 9]
```

## Constraints
- Array can start from any number (not necessarily zero)
- Handles single or multiple missing numbers
- Input array must have at least 2 elements
