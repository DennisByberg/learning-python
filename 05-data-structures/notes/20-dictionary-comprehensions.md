# Dictionary Comprehensions

## What is a Dictionary Comprehension?

A **concise way** to create dictionaries using a single line of code.

## Basic Syntax

```python
{key_expression: value_expression for item in iterable}
```

## Simple Examples

```python
# Create dictionary from range
numbers = {x: x * 2 for x in range(5)}
print(numbers)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Squares
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## With Condition

```python
# Only even numbers
evens = {x: x * 2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}
```

## From Lists

```python
# List to dictionary
items = ["apple", "banana", "cherry"]
lengths = {item: len(item) for item in items}
print(lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

## Transforming Dictionaries

```python
# Original dictionary
prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}

# Double all prices
doubled = {item: price * 2 for item, price in prices.items()}
print(doubled)  # {'apple': 3.0, 'banana': 1.0, 'cherry': 4.0}

print(footballers_number)
# Filter expensive items
expensive = {item: price for item, price in prices.items() if price > 1.0}
print(expensive)  # {'apple': 1.5, 'cherry': 2.0}
```

## Swapping Keys and Values

```python
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

## Using zip()

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]

person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

## Common Use Cases

```python
# Convert list to dictionary with index
items = ["apple", "banana", "cherry"]
indexed = {i: item for i, item in enumerate(items)}
print(indexed)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# Create lookup table
names = ["Alice", "Bob", "Charlie"]
ids = {name: i for i, name in enumerate(names, start=1)}
print(ids)  # {'Alice': 1, 'Bob': 2, 'Charlie': 3}

# Character counts
text = "hello"
counts = {char: text.count(char) for char in set(text)}
print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## Traditional vs Comprehension

```python
# Traditional way
squares = {}
for x in range(5):
    squares[x] = x ** 2

# Comprehension way (better!)
squares = {x: x ** 2 for x in range(5)}
```

## Key Points

- **Syntax**: `{key: value for item in iterable}`
- **More readable** than traditional loops
- **Single line** creation
- Can include **conditions** with `if`
- Use with **`items()`** to transform dictionaries
- Combine with **`zip()`** for parallel iteration
- Great for **transforming** and **filtering** data
