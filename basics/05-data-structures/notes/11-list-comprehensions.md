# List Comprehensions

## What are List Comprehensions?

A concise way to create lists based on existing iterables. They're more Pythonic and readable than using `map()` and `filter()`.

## Basic Syntax

```python
[expression for item in iterable]
```

## Basic Examples

```python
# Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Extract prices from tuples
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
prices = [item[1] for item in items]
print(prices)  # [10, 9, 12]

# Convert to uppercase
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD']
```

## With Conditions (Filtering)

```python
# Get even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6]

# Filter items by price
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
items_over_ten = [item for item in items if item[1] >= 10]
print(items_over_ten)  # [('Product1', 10), ('Product3', 12)]

# Get positive numbers
numbers = [-2, -1, 0, 1, 2]
positives = [x for x in numbers if x > 0]
print(positives)  # [1, 2]
```

## With If-Else

```python
# Replace negatives with 0
numbers = [-2, -1, 0, 1, 2]
result = [x if x > 0 else 0 for x in numbers]
print(result)  # [0, 0, 0, 1, 2]

# Label numbers as even/odd
numbers = [1, 2, 3, 4]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even']
```

## List Comprehension vs Traditional Loops

```python
# Traditional loop
squares = []
for x in numbers:
    squares.append(x ** 2)

# List comprehension (more Pythonic)
squares = [x ** 2 for x in numbers]
```

## List Comprehension vs Map/Filter

```python
# Using map
prices = list(map(lambda item: item[1], items))

# Using list comprehension (more readable)
prices = [item[1] for item in items]

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (more readable)
evens = [x for x in numbers if x % 2 == 0]
```

## Key Points

- More concise and readable than loops
- More Pythonic than `map()` and `filter()`
- Can include conditions with `if`
- Can include if-else expressions
- Returns a list directly (no need for `list()` conversion)
- Best for simple transformations and filtering

## When to Use List Comprehensions

- Creating new lists from existing iterables
- Simple transformations
- Simple filtering
- When readability is important

## When NOT to Use

- Complex logic (use regular loops instead)
- When you need side effects (use regular loops)
- When it becomes too long or hard to read
