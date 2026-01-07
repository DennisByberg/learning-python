# Sets

## What is a Set?

A set is an **unordered collection** of **unique items** - no duplicates allowed.

## Creating Sets

```python
# Using curly braces
numbers = {1, 2, 3, 4}

# From a list (removes duplicates)
numbers = [1, 1, 2, 2, 3, 4]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4}

# Empty set
empty = set()  # NOT {}, that's a dictionary!
```

## Key Characteristics

- **Unordered** - no index
- **Unique** - duplicates automatically removed
- **Fast membership** testing - O(1)

## Basic Operations

```python
numbers = {1, 2, 3}

# Add
numbers.add(4)  # {1, 2, 3, 4}

# Remove
numbers.remove(2)  # {1, 3, 4}
numbers.discard(10)  # No error if not found

# Check membership
if 3 in numbers:
    print("Found!")
```

## Set Operations

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (combine)
set1 | set2  # {1, 2, 3, 4, 5}

# Intersection (common)
set1 & set2  # {3}

# Difference
set1 - set2  # {1, 2}

# Symmetric difference (either, not both)
set1 ^ set2  # {1, 2, 4, 5}
```

## Common Use Cases

```python
# Remove duplicates
items = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(items))  # [1, 2, 3, 4]

# Find common elements
common = set(list1) & set(list2)

# Fast lookup
if user_id in valid_ids:  # O(1) - very fast
    print("Valid")
```

## Key Points

- **Unordered** - no index access
- **Unique items** - duplicates removed
- **Fast membership** - O(1)
- Empty set: **`set()`**, not `{}`
- **Operators**: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference)
- **Methods**: `add()`, `remove()`, `discard()`
