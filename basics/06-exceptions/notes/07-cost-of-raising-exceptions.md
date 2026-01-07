# Cost of Raising Exceptions

## Performance Impact

Raising and catching exceptions is **slower** than normal control flow (like if-statements).

## Performance Comparison

```python
from timeit import timeit

# Using exceptions
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError:
    pass
"""

# Using return value
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Exceptions:", timeit(code1, number=10_000))  # Slower
print("Return None:", timeit(code2, number=10_000))  # Faster
```

**Typical result:** Exceptions are **~3-5x slower** than checking return values.

## When to Use Exceptions

Despite the cost, **use exceptions** when:

1. **Exceptional conditions** - truly unexpected errors
2. **Errors that shouldn't be ignored** - force caller to handle
3. **Clarity** - makes error handling explicit

```python
# Good - exceptional condition
def open_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} not found")
    return open(path)
```

## When NOT to Use Exceptions

**Avoid exceptions** for:

1. **Expected flow control** - normal program logic
2. **Performance-critical code** - inner loops

```python
# Bad - using exception for normal flow
try:
    index = 0
    while True:
        print(items[index])
        index += 1
except IndexError:
    pass  # Expected end of list

# Good - use normal control flow
for item in items:
    print(item)
```

## Key Points

- Exceptions are **slower** than normal control flow
- **Use for exceptional conditions**, not regular logic
- **Don't use in tight loops** or performance-critical code
- Clarity and correctness > micro-optimization
- **EAFP** (Easier to Ask Forgiveness than Permission) vs **LBYL** (Look Before You Leap) - Python prefers EAFP, but be aware of cost
