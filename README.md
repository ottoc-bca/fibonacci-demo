# Fibonacci Sequence Demo

A Python demo showcasing multiple approaches to computing the Fibonacci sequence.

## Implementations

- **Recursive** — Classic recursive approach
- **Memoized** — Top-down dynamic programming with caching
- **Iterative** — Bottom-up iterative approach
- **Generator** — Python generator for lazy evaluation

## Usage

```bash
python fibonacci.py
```

You can also import and use the functions directly:

```python
from fibonacci import fibonacci_iterative, fibonacci_generator

# Get the 10th Fibonacci number
print(fibonacci_iterative(10))  # 55

# Generate the first 10 Fibonacci numbers
for num in fibonacci_generator(10):
    print(num)
```

## Running Tests

```bash
python -m pytest test_fibonacci.py -v
```
