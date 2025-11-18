# Generator Expressions

## What is a Generator Expression?

A **memory-efficient** way to create iterables that generate values **on-demand** instead of storing them all in memory.

## List Comprehension vs Generator Expression

```python
# List comprehension - creates entire list in memory
numbers_list = [x * 2 for x in range(10)]
print(numbers_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Generator expression - generates values on-demand
numbers_gen = (x * 2 for x in range(10))
print(numbers_gen)  # <generator object>
```

## Syntax

```python
# List comprehension uses []
list_comp = [x for x in range(5)]

# Generator expression uses ()
gen_expr = (x for x in range(5))
```

## Using Generator Expressions

```python
# Create generator
gen = (x * 2 for x in range(5))

# Consume with for loop
for num in gen:
    print(num)  # 0, 2, 4, 6, 8

# Or convert to list
gen = (x * 2 for x in range(5))
numbers = list(gen)
print(numbers)  # [0, 2, 4, 6, 8]
```

## Memory Efficiency

```python
import sys

# List comprehension - stores all values
list_comp = [x for x in range(10000)]
print(sys.getsizeof(list_comp))  # ~87,000 bytes

# Generator expression - minimal memory
gen_expr = (x for x in range(10000))
print(sys.getsizeof(gen_expr))  # ~128 bytes
```

## One-Time Use

```python
gen = (x * 2 for x in range(3))

# First iteration works
print(list(gen))  # [0, 2, 4]

# Second iteration is empty (generator exhausted)
print(list(gen))  # []
```

## With Functions

```python
# Generator expression with sum()
total = sum(x * 2 for x in range(100))
print(total)  # 9900

# With max()
maximum = max(x ** 2 for x in range(10))
print(maximum)  # 81

# With any()
has_even = any(x % 2 == 0 for x in range(5))
print(has_even)  # True
```

## Common Use Cases

```python
# Large file processing
lines = (line.strip() for line in open("file.txt"))

# Filter data
large_numbers = (x for x in range(1000000) if x > 999990)

# Transform data
uppercase = (name.upper() for name in ["alice", "bob", "charlie"])
```

## When to Use

✅ **Use generator expressions when:**

- Working with **large datasets**
- **Memory** is a concern
- You only need to **iterate once**
- Processing **streams** or **files**

❌ **Use list comprehensions when:**

- Need to **reuse** the result
- Need **indexing** or **slicing**
- Dataset is **small**

## Key Points

- **Syntax**: `(expression for item in iterable)`
- **Lazy evaluation** - values generated on-demand
- **Memory efficient** - doesn't store all values
- **One-time use** - exhausted after iteration
- Use **`()`** not `[]`
- Perfect for **large datasets** and **streams**
- Works with functions: `sum()`, `max()`, `min()`, `any()`, `all()`
