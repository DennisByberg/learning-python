# Filter Function

## What is Filter?

`filter()` creates a new iterable containing only the items that pass a test (return `True`).

## Syntax

```python
filter(function, iterable)
```

## Basic Examples

```python
# Get even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# Get positive numbers
numbers = [-2, -1, 0, 1, 2]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # [1, 2]

# Filter items by price
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
items_over_ten = list(filter(lambda item: item[1] >= 10, items))
print(items_over_ten)  # [('Product1', 10), ('Product3', 12)]
```

## Filter vs List Comprehension

```python
# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (often more readable)
evens = [x for x in numbers if x % 2 == 0]
```

## Key Points

- `filter()` returns a filter object, not a list (use `list()` to convert)
- The function must return `True` or `False`
- Items that return `True` are kept, `False` are filtered out
- More functional programming style
- List comprehensions are often more Pythonic

## When to Use Filter

- When you have an existing predicate function
- When working in a functional programming style
- When chaining multiple operations with map/filter

## When to Use List Comprehension Instead

- When you also need to transform items (not just filter)
- When readability is preferred (most cases in Python)
- When the condition is simple

## Combining Map and Filter

```python
# Get squares of even numbers
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16]

# Same with list comprehension (more readable)
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)  # [4, 16]
```
