# Task 4 — Calculation Formula Finder

A Python function that finds all valid expressions using given numbers to reach a target value.

## How to Run

```bash
python3 calculator.py
```

## How It Works

1. Generate all permutations of the input numbers
2. Try all combinations of operators (+, -, *) between numbers
3. Try all possible groupings/parentheses patterns
4. Collect all expressions that equal the target
5. Returns all valid combinations

## Function Usage

```python
from calculator import find_expressions

# Single solution target
find_expressions([1, 4, 5, 6], 16)
# Output: ["((1 + 4) + 5) + 6", "1 + (4 + (5 + 6))", ...]

# Multiple solutions
find_expressions([2, 3, 5, 10], 25)
# Output: ["(2 + 3) * (10 - 5)", "5 * ((10 - 2) - 3)", ...]
```

## Constraints
- Operators used: +, -, *
- All input numbers must be used exactly once
- Returns ALL valid combinations that reach the target
- Handles all possible parentheses groupings
