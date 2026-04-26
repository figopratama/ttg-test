from itertools import permutations


def calculate(a, op, b):
    """Apply operator between two numbers."""
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b


def evaluate(nums, ops):
    """
    Evaluate all possible expressions with different groupings.
    Returns list of (result, expression_string) tuples.
    """
    results = []
    n = len(nums)

    if n == 2:
        val = calculate(nums[0], ops[0], nums[1])
        expr = f"{nums[0]} {ops[0]} {nums[1]}"
        results.append((val, expr))

    elif n == 3:
        # Pattern 1: (a OP b) OP c
        v1 = calculate(nums[0], ops[0], nums[1])
        v2 = calculate(v1, ops[1], nums[2])
        e2 = f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}"
        results.append((v2, e2))

        # Pattern 2: a OP (b OP c)
        v3 = calculate(nums[1], ops[1], nums[2])
        v4 = calculate(nums[0], ops[0], v3)
        e4 = f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})"
        results.append((v4, e4))

    elif n == 4:
        a, b, c, d = nums
        o1, o2, o3 = ops

        patterns = [
            # ((a OP b) OP c) OP d
            lambda: (calculate(calculate(calculate(a,o1,b),o2,c),o3,d),
                     f"(({a} {o1} {b}) {o2} {c}) {o3} {d}"),
            # (a OP (b OP c)) OP d
            lambda: (calculate(calculate(a,o1,calculate(b,o2,c)),o3,d),
                     f"({a} {o1} ({b} {o2} {c})) {o3} {d}"),
            # (a OP b) OP (c OP d)
            lambda: (calculate(calculate(a,o1,b),o2,calculate(c,o3,d)),
                     f"({a} {o1} {b}) {o2} ({c} {o3} {d})"),
            # a OP ((b OP c) OP d)
            lambda: (calculate(a,o1,calculate(calculate(b,o2,c),o3,d)),
                     f"{a} {o1} (({b} {o2} {c}) {o3} {d})"),
            # a OP (b OP (c OP d))
            lambda: (calculate(a,o1,calculate(b,o2,calculate(c,o3,d))),
                     f"{a} {o1} ({b} {o2} ({c} {o3} {d}))"),
        ]

        for pattern in patterns:
            try:
                val, expr = pattern()
                results.append((val, expr))
            except Exception:
                pass

    return results


def find_expressions(numbers, target):
    """
    Find all expressions using given numbers that equal the target.
    - All numbers must be used exactly once
    - Operators: +, -. *
    - Returns all valid combinations
    """
    operators = ["+", "-", "*"]
    found = []
    seen_expressions = set()

    # Try all permutations of numbers
    for perm in permutations(numbers):
        n = len(perm)
        # Try all combinations of operators
        op_count = n - 1

        def generate_ops(depth, current_ops):
            if depth == op_count:
                results = evaluate(list(perm), current_ops)
                for val, expr in results:
                    if val == target and expr not in seen_expressions:
                        seen_expressions.add(expr)
                        found.append(expr)
                return
            for op in operators:
                generate_ops(depth + 1, current_ops + [op])

        generate_ops(0, [])

    return found


# ── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        {"numbers": [1, 4, 5, 6], "target": 16},
        {"numbers": [1, 4, 5, 6], "target": 18},
        {"numbers": [1, 4, 5, 6], "target": 50},
        {"numbers": [2, 3, 5, 10], "target": 25},
        {"numbers": [1, 2, 3],    "target": 9},
    ]

    print("=" * 60)
    print("  Task 4 — Calculation Formula Finder")
    print("=" * 60)

    for tc in test_cases:
        nums   = tc["numbers"]
        target = tc["target"]
        exprs  = find_expressions(nums, target)

        print(f"\nInput:  {nums}")
        print(f"Target: {target}")
        if exprs:
            print(f"Found {len(exprs)} solution(s):")
            for e in exprs:
                print(f"  → {e}")
        else:
            print("  No solution found.")

    print("\n" + "=" * 60)
