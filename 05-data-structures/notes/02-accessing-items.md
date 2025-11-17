# Accessing Items

## What is Accessing Items?

Accessing items means **retrieving specific elements** from a list using their index position.

## Index Basics

```python
letters = ["a", "b", "c", "d", "e"]

print(letters[0])   # "a" - first item
print(letters[1])   # "b" - second item
print(letters[4])   # "e" - fifth item
```

**Remember:** Index starts at **0**, not 1!

## Negative Indices

Use negative numbers to count from the **end** of the list.

```python
letters = ["a", "b", "c", "d", "e"]

print(letters[-1])  # "e" - last item
print(letters[-2])  # "d" - second to last
print(letters[-5])  # "a" - first item (same as [0])
```

## Index Out of Range

Accessing an index that doesn't exist causes an **IndexError**.

```python
letters = ["a", "b", "c"]

print(letters[3])   # IndexError: list index out of range
print(letters[10])  # IndexError: list index out of range
```

## Modifying Items

You can **change** items by assigning a new value to an index.

```python
letters = ["a", "b", "c"]
letters[0] = "A"
print(letters)  # ["A", "b", "c"]

letters[-1] = "Z"
print(letters)  # ["A", "b", "Z"]
```

## Accessing Nested Lists

For nested lists (lists inside lists), use **multiple indices**.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])      # [1, 2, 3] - first row
print(matrix[0][0])   # 1 - first row, first column
print(matrix[1][2])   # 6 - second row, third column
print(matrix[-1][-1]) # 9 - last row, last column
```

## Key Points

- **Index starts at 0** - first item is `[0]`
- **Negative indices** count from the end - `[-1]` is last item
- **IndexError** occurs when index is out of range
- Lists are **mutable** - you can change items after creation
- Use `[row][column]` to access nested lists
- Always check list length with `len()` before accessing
