"""
Fibonacci Sequence Demo

Demonstrates multiple approaches to computing Fibonacci numbers:
  1. Recursive (naive)
  2. Memoized (top-down dynamic programming)
  3. Iterative (bottom-up)
  4. Generator (lazy evaluation)
"""

from functools import lru_cache


# ---------------------------------------------------------------------------
# 1. Recursive (naive)
# ---------------------------------------------------------------------------
def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number using plain recursion.

    Warning: This has exponential time complexity O(2^n) and is only
    practical for small values of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ---------------------------------------------------------------------------
# 2. Memoized (top-down dynamic programming)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Return the nth Fibonacci number using memoization.

    Time complexity:  O(n)
    Space complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


# ---------------------------------------------------------------------------
# 3. Iterative (bottom-up)
# ---------------------------------------------------------------------------
def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number using iteration.

    Time complexity:  O(n)
    Space complexity: O(1)
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ---------------------------------------------------------------------------
# 4. Generator (lazy evaluation)
# ---------------------------------------------------------------------------
def fibonacci_generator(count: int):
    """Yield the first `count` Fibonacci numbers.

    This is useful when you want to iterate over a sequence without
    storing all values in memory at once.
    """
    if count <= 0:
        return
    a, b = 0, 1
    yield a
    for _ in range(1, count):
        yield b
        a, b = b, a + b


# ---------------------------------------------------------------------------
# Interactive demo
# ---------------------------------------------------------------------------
def print_sequence(n: int) -> None:
    """Pretty-print the first n Fibonacci numbers."""
    print(f"\nFirst {n} Fibonacci numbers:")
    print("-" * 40)
    for i, num in enumerate(fibonacci_generator(n)):
        print(f"  F({i}) = {num}")


def compare_methods(n: int) -> None:
    """Compute F(n) with each method and display the results."""
    print(f"\nComputing F({n}) using different methods:")
    print("-" * 40)

    result_iter = fibonacci_iterative(n)
    print(f"  Iterative:  {result_iter}")

    result_memo = fibonacci_memoized(n)
    print(f"  Memoized:   {result_memo}")

    if n <= 30:
        result_rec = fibonacci_recursive(n)
        print(f"  Recursive:  {result_rec}")
    else:
        print(f"  Recursive:  (skipped — too slow for n > 30)")


def main() -> None:
    print("=" * 40)
    print("   Fibonacci Sequence Demo")
    print("=" * 40)

    # Show the first 15 numbers
    print_sequence(15)

    # Compare methods for a moderate value
    compare_methods(20)

    # Show a larger value computed iteratively
    big_n = 100
    print(f"\nF({big_n}) = {fibonacci_iterative(big_n)}")


if __name__ == "__main__":
    main()
