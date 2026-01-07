# Lists

## What are Lists?

Lists are **ordered, mutable collections** that can store multiple items.

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
```

## Creating Lists

```python
# Empty list
empty = []

# List with items
fruits = ["apple", "banana", "orange"]

# Using list() constructor
chars = list("Hello")  # ['H', 'e', 'l', 'l', 'o']
numbers = list(range(5))  # [0, 1, 2, 3, 4]

# Nested lists (matrix)
matrix = [[0, 1], [2, 3]]

# Repeating items
zeros = [0] * 5  # [0, 0, 0, 0, 0]
```

## Combining Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
```

## List Length

```python
letters = ["a", "b", "c"]
print(len(letters))  # 3
```

## Accessing Items

```python
letters = ["a", "b", "c"]

print(letters[0])   # "a" (first item)
print(letters[1])   # "b"
print(letters[-1])  # "c" (last item)
print(letters[-2])  # "b" (second to last)
```

## Modifying Items

```python
letters = ["a", "b", "c"]
letters[0] = "A"
print(letters)  # ["A", "b", "c"]
```

## Key Points

- Lists are **ordered** - items have a specific position
- Lists are **mutable** - can be changed after creation
- Use **square brackets** `[]` to create lists
- Access items with **index** starting at 0
- **Negative indices** count from the end (-1 is last item)
- Use **`len()`** to get the number of items
- Lists can contain **mixed data types**
- Use **`+`** to combine lists
