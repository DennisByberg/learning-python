# Dictionaries

## What is a Dictionary?

A dictionary is a collection of **key-value pairs** - unordered, mutable, and indexed by keys.

## Creating Dictionaries

```python
# Using curly braces
point = {"x": 1, "y": 2}

# Using dict() constructor
footballers = dict(zlatan=10, neymar=11)

# Empty dictionary
empty = {}
```

## Accessing Values

```python
point = {"x": 1, "y": 2}

# Using key
print(point["x"])  # 1

# Using get() - safer, returns None if not found
print(point.get("z"))  # None
print(point.get("z", 0))  # 0 (default value)
```

## Adding/Updating Items

```python
footballers = {"zlatan": 10, "neymar": 11}

# Add/update single item
footballers["ronaldo"] = 7

# Update multiple items
footballers.update(ronaldo=7, messi=10)
footballers.update({"mbappe": 7, "haaland": 9})
```

## Removing Items

```python
point = {"x": 1, "y": 2, "z": 3}

# Remove specific key
del point["z"]

# Pop - remove and return value
value = point.pop("y")  # 2

# Clear all
point.clear()
```

## Checking Keys

```python
point = {"x": 1, "y": 2}

if "x" in point:
    print("x exists")

if "z" not in point:
    print("z doesn't exist")
```

## Looping Through Dictionaries

```python
footballers = {"zlatan": 10, "neymar": 11, "ronaldo": 7}

# Loop through keys
for key in footballers:
    print(key)

# Loop through values
for value in footballers.values():
    print(value)

# Loop through key-value pairs
for footballer, number in footballers.items():
    print(f"{footballer} has number {number}")
```

## Dictionary Methods

```python
point = {"x": 1, "y": 2}

# Get all keys
keys = point.keys()  # dict_keys(['x', 'y'])

# Get all values
values = point.values()  # dict_values([1, 2])

# Get all key-value pairs
items = point.items()  # dict_items([('x', 1), ('y', 2)])
```

## Dictionary Comprehension

```python
# Create dictionary from range
numbers = {x: x * 2 for x in range(5)}
print(numbers)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```

## Common Use Cases

```python
# Store user data
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@email.com"
}

# Count occurrences
text = "hello"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Group data
students = {
    "Alice": "Math",
    "Bob": "Science",
    "Charlie": "Math"
}
```

## Key Points

- **Key-value pairs** - access by key, not index
- **Unordered** (Python 3.7+ preserves insertion order)
- **Keys must be unique** and immutable (strings, numbers, tuples)
- **Values can be any type**
- Use **`get()`** for safe access
- **Methods**: `keys()`, `values()`, `items()`, `update()`, `pop()`
- Loop with **`items()`** to get both key and value
- Empty dict: **`{}`** (unlike sets which need `set()`)
