# Unpacking Operator

## What is the Unpacking Operator?

The **`*`** operator **unpacks** iterables (lists, tuples, sets) into individual elements.

## Basic Unpacking

```python
values = [1, 2, 3, 4, 5]

# Without unpacking
print(values)  # [1, 2, 3, 4, 5]

# With unpacking
print(*values)  # 1 2 3 4 5
```

## Function Arguments

```python
def add(x, y, z):
    return x + y + z

numbers = [1, 2, 3]

# Without unpacking (error)
# add(numbers)  # TypeError

# With unpacking
result = add(*numbers)
print(result)  # 6
```

## Combining Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Old way
combined = list1 + list2

# Using unpacking
combined = [*list1, *list2]
print(combined)  # [1, 2, 3, 4, 5, 6]

# With additional items
combined = [0, *list1, *list2, 7]
print(combined)  # [0, 1, 2, 3, 4, 5, 6, 7]
```

## Unpacking Multiple Iterables

```python
first = [1, 2]
second = [3, 4]
third = [5, 6]

combined = [*first, *second, *third]
print(combined)  # [1, 2, 3, 4, 5, 6]
```

## With range()

```python
values = list(range(1, 6))
print(*values)  # 1 2 3 4 5

# Useful for print formatting
print(*range(1, 11), sep=", ")  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

## Dictionary Unpacking (`**`)

```python
first = {"x": 1, "y": 2}
second = {"z": 3}

# Combine dictionaries
combined = {**first, **second}
print(combined)  # {'x': 1, 'y': 2, 'z': 3}

# Override values
combined = {**first, "y": 10, **second}
print(combined)  # {'x': 1, 'y': 10, 'z': 3}
```

## Function with \*\*kwargs

```python
def greet(**kwargs):
    print(kwargs)

user = {"name": "Alice", "age": 25}
greet(**user)  # {'name': 'Alice', 'age': 25}
```

## Unpacking in Assignments

```python
# Basic unpacking
a, b, c = [1, 2, 3]

# With * to capture rest
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# First and rest
first, *rest = [1, 2, 3, 4]
print(first)  # 1
print(rest)   # [2, 3, 4]
```

## Common Use Cases

```python
# Print list items separated
numbers = [1, 2, 3, 4, 5]
print(*numbers, sep=" - ")  # 1 - 2 - 3 - 4 - 5

# Merge lists
all_items = [*list1, *list2, *list3]

# Pass list to function expecting separate args
coords = [10, 20]
move_to(*coords)  # Same as move_to(10, 20)

# Merge dictionaries
settings = {**defaults, **user_settings}
```

## Key Points

- **`*`** unpacks lists, tuples, sets
- **`**`\*\* unpacks dictionaries
- **Syntax**: `*iterable` or `**dict`
- Use in **function calls** to pass elements as arguments
- Use in **lists/tuples** to combine iterables
- Use in **assignments** to capture multiple values
- **Print trick**: `print(*list)` for clean output
- Dictionary unpacking merges dicts (right overwrites left)
