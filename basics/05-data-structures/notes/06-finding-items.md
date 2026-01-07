# Finding Items

## What is Finding Items?

Finding items means **searching for and locating** specific values in a list.

## Checking if Item Exists

Use the **`in`** operator to check if an item exists.

```python
letters = ["a", "b", "c"]

print("a" in letters)  # True
print("d" in letters)  # False
```

### not in Operator

```python
letters = ["a", "b", "c"]

print("d" not in letters)  # True
print("a" not in letters)  # False
```

## Finding Item Index

### index() - Find First Occurrence

```python
letters = ["a", "b", "c", "b"]

print(letters.index("b"))  # 1 (first occurrence)
```

### ValueError When Not Found

```python
letters = ["a", "b", "c"]

print(letters.index("z"))  # ValueError: 'z' is not in list
```

### Safe Way - Check Before Using index()

```python
letters = ["a", "b", "c"]

if "d" in letters:
    print(letters.index("d"))
else:
    print("Item not found")
```

## Counting Occurrences

Use **`count()`** to find how many times an item appears.

```python
letters = ["a", "b", "c", "b", "b"]

print(letters.count("b"))  # 3
print(letters.count("a"))  # 1
print(letters.count("z"))  # 0 (doesn't raise error)
```

## Finding All Indices

To find **all positions** of an item, use a loop.

```python
letters = ["a", "b", "c", "b", "a", "b"]

indices = []
for i, letter in enumerate(letters):
    if letter == "b":
        indices.append(i)

print(indices)  # [1, 3, 5]
```

### Using List Comprehension

```python
letters = ["a", "b", "c", "b", "a", "b"]

indices = [i for i, letter in enumerate(letters) if letter == "b"]
print(indices)  # [1, 3, 5]
```

## Finding Min and Max

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(min(numbers))  # 1
print(max(numbers))  # 9
```

### With Strings

```python
letters = ["c", "a", "b"]

print(min(letters))  # "a" (alphabetically first)
print(max(letters))  # "c" (alphabetically last)
```

## Comparison Table

| Method/Operator | Purpose             | Returns      | Raises Error?    |
| --------------- | ------------------- | ------------ | ---------------- |
| `x in list`     | Check existence     | `True/False` | No               |
| `x not in list` | Check non-existence | `True/False` | No               |
| `list.index(x)` | Find first index    | `int`        | Yes (ValueError) |
| `list.count(x)` | Count occurrences   | `int`        | No               |
| `min(list)`     | Find minimum        | value        | Yes (if empty)   |
| `max(list)`     | Find maximum        | value        | Yes (if empty)   |

## Key Points

- **`in`** - check if item exists (returns `True/False`)
- **`not in`** - check if item doesn't exist
- **`index(x)`** - find first occurrence index
- `index()` raises **ValueError** if item not found
- **Always check with `in`** before using `index()`
- **`count(x)`** - count occurrences (returns 0 if not found)
- `count()` **never raises** an error
- **`min()`** and **`max()`** work with numbers and strings
- Use **list comprehension** to find all indices
