# Adding or Removing Items

## What is Adding or Removing Items?

Lists are **mutable**, meaning you can add, remove, or modify items after creation.

## Adding Items

### append() - Add to End

```python
letters = ["a", "b", "c"]
letters.append("d")
print(letters)  # ["a", "b", "c", "d"]
```

### insert() - Add at Specific Position

```python
letters = ["a", "b", "c"]
letters.insert(0, "z")  # Insert at index 0
print(letters)  # ["z", "a", "b", "c"]

letters.insert(2, "x")  # Insert at index 2
print(letters)  # ["z", "a", "x", "b", "c"]
```

### extend() - Add Multiple Items

```python
letters = ["a", "b", "c"]
letters.extend(["d", "e", "f"])
print(letters)  # ["a", "b", "c", "d", "e", "f"]
```

## Removing Items

### pop() - Remove and Return Last Item

```python
letters = ["a", "b", "c"]
last = letters.pop()
print(last)     # "c"
print(letters)  # ["a", "b"]
```

### pop(index) - Remove at Specific Index

```python
letters = ["a", "b", "c", "d"]
first = letters.pop(0)
print(first)    # "a"
print(letters)  # ["b", "c", "d"]
```

### remove() - Remove by Value

```python
letters = ["a", "b", "c", "b"]
letters.remove("b")  # Removes first occurrence
print(letters)  # ["a", "c", "b"]
```

**Note:** `remove()` only removes the **first** matching item.

### del - Delete by Index or Slice

```python
letters = ["a", "b", "c", "d", "e"]

# Delete single item
del letters[0]
print(letters)  # ["b", "c", "d", "e"]

# Delete slice
letters = ["a", "b", "c", "d", "e"]
del letters[0:3]
print(letters)  # ["d", "e"]

# Delete entire list
del letters
# print(letters)  # NameError: name 'letters' is not defined
```

### clear() - Remove All Items

```python
letters = ["a", "b", "c"]
letters.clear()
print(letters)  # []
```

## Comparison Table

| Method | Action | Returns Value | Example |
|--------|--------|---------------|---------|
| `append(x)` | Add to end | No | `list.append("d")` |
| `insert(i, x)` | Add at index | No | `list.insert(0, "z")` |
| `extend(list)` | Add multiple | No | `list.extend(["d", "e"])` |
| `pop()` | Remove last | Yes | `item = list.pop()` |
| `pop(i)` | Remove at index | Yes | `item = list.pop(0)` |
| `remove(x)` | Remove by value | No | `list.remove("b")` |
| `del list[i]` | Delete by index | No | `del list[0]` |
| `del list[i:j]` | Delete slice | No | `del list[0:3]` |
| `clear()` | Remove all | No | `list.clear()` |

## Error Handling

```python
letters = ["a", "b", "c"]

# ValueError: item not in list
letters.remove("z")  # "z" doesn't exist

# IndexError: pop index out of range
letters.pop(10)  # Index 10 doesn't exist
```

## Key Points

- **`append(x)`** - add item to end
- **`insert(i, x)`** - add item at specific index
- **`extend(list)`** - add multiple items
- **`pop()`** - remove and return last item
- **`pop(i)`** - remove and return item at index
- **`remove(x)`** - remove first occurrence of value
- **`del list[i]`** - delete item at index
- **`del list[i:j]`** - delete slice
- **`clear()`** - remove all items
- `pop()` **returns** the removed item
- `remove()` and `del` do **not** return values
