"""Tests for fibonacci.py"""

import pytest

from fibonacci import (
    fibonacci_generator,
    fibonacci_iterative,
    fibonacci_memoized,
    fibonacci_recursive,
)

KNOWN_VALUES = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
]


class TestFibonacciRecursive:
    @pytest.mark.parametrize("n, expected", KNOWN_VALUES)
    def test_known_values(self, n: int, expected: int) -> None:
        assert fibonacci_recursive(n) == expected

    def test_negative_input(self) -> None:
        with pytest.raises(ValueError):
            fibonacci_recursive(-1)


class TestFibonacciMemoized:
    @pytest.mark.parametrize("n, expected", KNOWN_VALUES)
    def test_known_values(self, n: int, expected: int) -> None:
        assert fibonacci_memoized(n) == expected

    def test_negative_input(self) -> None:
        with pytest.raises(ValueError):
            fibonacci_memoized(-1)


class TestFibonacciIterative:
    @pytest.mark.parametrize("n, expected", KNOWN_VALUES)
    def test_known_values(self, n: int, expected: int) -> None:
        assert fibonacci_iterative(n) == expected

    def test_negative_input(self) -> None:
        with pytest.raises(ValueError):
            fibonacci_iterative(-1)

    def test_large_value(self) -> None:
        assert fibonacci_iterative(100) == 354224848179261915075


class TestFibonacciGenerator:
    def test_first_ten(self) -> None:
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert list(fibonacci_generator(10)) == expected

    def test_zero_count(self) -> None:
        assert list(fibonacci_generator(0)) == []

    def test_one_element(self) -> None:
        assert list(fibonacci_generator(1)) == [0]

    def test_negative_count(self) -> None:
        assert list(fibonacci_generator(-5)) == []
