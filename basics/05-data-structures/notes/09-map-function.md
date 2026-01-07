# Map Function

## What is Map?

`map()` applies a function to every item in an iterable (like a list) and returns a map object (which you can convert to a list).

## Syntax

```python
map(function, iterable)
```

## Basic Examples

```python
# Double all numbers
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]

# Convert to strings
numbers = [1, 2, 3]
strings = list(map(str, numbers))
print(strings)  # ['1', '2', '3']

# Extract prices from tuples
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
prices = list(map(lambda item: item[1], items))
print(prices)  # [10, 9, 12]
```

## Map vs List Comprehension

```python
# Using map
doubled = list(map(lambda x: x * 2, numbers))

# Using list comprehension (often more readable)
doubled = [x * 2 for x in numbers]
```

## Key Points

- `map()` returns a map object, not a list (use `list()` to convert)
- First argument is the function to apply
- Second argument is the iterable to process
- More functional programming style
- List comprehensions are often more Pythonic and readable
- Useful when you already have a function defined

## When to Use Map

- When you have an existing function to apply
- When working in a functional programming style
- When chaining multiple operations

## When to Use List Comprehension Instead

- When you need filtering (`if` conditions)
- When the transformation is simple
- When readability is preferred (most cases in Python)
