def find_missing_numbers(arr):
    """
    Find missing number(s) from a sequential array.
    - Array can start from any number (not necessarily 0)
    - Can handle single or multiple missing numbers
    """
    if not arr or len(arr) < 2:
        return []

    sorted_arr = sorted(arr)
    start = sorted_arr[0]
    end   = sorted_arr[-1]

    # Build complete sequential set from min to max
    complete_set = set(range(start, end + 1))
    actual_set   = set(sorted_arr)

    missing = sorted(list(complete_set - actual_set))

    if len(missing) == 1:
        return missing[0]
    return missing


# ── Test Cases ──────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        {"input": [3, 0, 2, 4],                        "expected": 1},
        {"input": [3106, 3102, 3104, 3105, 3107],      "expected": 3103},
        {"input": [1, 2, 4, 6, 7, 10],                 "expected": [3, 5, 8, 9]},
        {"input": [10, 12, 13, 15],                    "expected": [11, 14]},
        {"input": [100, 101, 103, 104, 105],            "expected": 102},
    ]

    print("=" * 50)
    print("  Task 3 — Find Missing Numbers")
    print("=" * 50)

    all_passed = True
    for i, tc in enumerate(test_cases):
        result  = find_missing_numbers(tc["input"])
        passed  = result == tc["expected"]
        status  = "✅ PASS" if passed else "❌ FAIL"
        if not passed:
            all_passed = False
        print(f"Test {i+1}: {status}")
        print(f"  Input:    {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got:      {result}")
        print()

    print("=" * 50)
    print(f"  Result: {'All tests passed! ✅' if all_passed else 'Some tests failed ❌'}")
    print("=" * 50)
