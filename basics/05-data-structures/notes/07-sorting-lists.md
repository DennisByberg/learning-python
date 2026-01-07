# Sorting Lists

## What is Sorting Lists?

Sorting arranges list items in a specific order - **ascending** (smallest to largest) or **descending** (largest to smallest).

## sort() Method

The **`sort()`** method sorts the list **in-place** (modifies the original list).

```python
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)  # [2, 3, 6, 8, 51]
```

### Descending Order

```python
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)  # [51, 8, 6, 3, 2]
```

## sorted() Function

The **`sorted()`** function returns a **new sorted list** without modifying the original.

```python
numbers = [3, 51, 2, 8, 6]
sorted_numbers = sorted(numbers)

print(sorted_numbers)  # [2, 3, 6, 8, 51]
print(numbers)         # [3, 51, 2, 8, 6] (unchanged)
```

### Descending Order

```python
numbers = [3, 51, 2, 8, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [51, 8, 6, 3, 2]
```

## Sorting Strings

```python
letters = ["c", "a", "b"]
letters.sort()
print(letters)  # ["a", "b", "c"]

# Case-sensitive: uppercase comes before lowercase
words = ["banana", "Apple", "cherry"]
words.sort()
print(words)  # ["Apple", "banana", "cherry"]
```

## Custom Sorting with key

Use the **`key`** parameter to define custom sorting logic.

### Sorting by Length

```python
words = ["python", "is", "awesome"]
words.sort(key=len)
print(words)  # ["is", "python", "awesome"]
```

### Sorting Tuples

```python
items = [("Product1", 20), ("Product2", 11), ("Product3", 22)]

def sort_item(item):
    return item[1]  # Sort by price (second element)

items.sort(key=sort_item)
print(items)
# [("Product2", 11), ("Product1", 20), ("Product3", 22)]
```

### Using Lambda Functions

```python
items = [("Product1", 20), ("Product2", 11), ("Product3", 22)]
items.sort(key=lambda item: item[1])
print(items)
# [("Product2", 11), ("Product1", 20), ("Product3", 22)]
```

## Sorting Complex Objects

```python
# List of tuples (name, age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sort by age
people.sort(key=lambda person: person[1])
print(people)
# [("Bob", 25), ("Alice", 30), ("Charlie", 35)]

# Sort by name
people.sort(key=lambda person: person[0])
print(people)
# [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
```

## Reverse Order

### reverse() Method

```python
numbers = [3, 51, 2, 8, 6]
numbers.reverse()
print(numbers)  # [6, 8, 2, 51, 3] (just reverses order)
```

**Note:** `reverse()` doesn't sort - it just **reverses** the current order.

## Comparison: sort() vs sorted()

| Feature | `sort()` | `sorted()` |
|---------|----------|------------|
| Type | Method | Function |
| Modifies original | Yes | No |
| Returns | `None` | New list |
| Usage | `list.sort()` | `sorted(list)` |

```python
numbers = [3, 1, 2]

# sort() returns None
result = numbers.sort()
print(result)   # None
print(numbers)  # [1, 2, 3]

# sorted() returns new list
numbers = [3, 1, 2]
result = sorted(numbers)
print(result)   # [1, 2, 3]
print(numbers)  # [3, 1, 2] (unchanged)
```

## Key Points

- **`sort()`** - sorts list in-place (modifies original)
- **`sorted()`** - returns new sorted list (preserves original)
- **`reverse=True`** - sort in descending order
- **`key=function`** - custom sorting logic
- **`key=len`** - sort by length
- **`key=lambda`** - inline custom function
- **`reverse()`** - reverses list order (doesn't sort)
- Sorting is **case-sensitive** for strings
- `sort()` returns `None`, `sorted()` returns a list
