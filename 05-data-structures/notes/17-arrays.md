# Arrays

## What is an Array?

An array is like a list, but **type-constrained** - all items must be the **same type**.

Arrays use **less memory** than lists but are **less flexible**.

## Why Use Arrays?

- **Memory efficient** - stores data more compactly
- **Performance** - faster for large datasets
- **Type safety** - ensures all items are same type

**Note:** Most Python programs use **lists** instead. Arrays are for specialized cases.

## Creating Arrays

```python
from array import array

# Syntax: array(typecode, [values])
numbers = array("i", [1, 2, 3])  # Integer array
```

## Type Codes

| Code  | Type  | Description            |
| ----- | ----- | ---------------------- |
| `'i'` | int   | Signed integer         |
| `'I'` | int   | Unsigned integer       |
| `'f'` | float | Floating point         |
| `'d'` | float | Double precision float |
| `'b'` | int   | Signed byte            |
| `'B'` | int   | Unsigned byte          |

```python
from array import array

integers = array("i", [1, 2, 3])
floats = array("f", [1.5, 2.5, 3.5])
bytes_arr = array("b", [10, 20, 30])
```

## Basic Operations

```python
from array import array

numbers = array("i", [1, 2, 3])

# Append
numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])

# Insert at index
numbers.insert(0, 7)
print(numbers)  # array('i', [7, 1, 2, 3, 4])

# Access
print(numbers[0])  # 7

# Remove
numbers.remove(7)
print(numbers)  # array('i', [1, 2, 3, 4])
```

## Type Enforcement

```python
from array import array

numbers = array("i", [1, 2, 3])

# This works
numbers.append(4)

# This causes TypeError
numbers.append(1.5)  # TypeError: integer argument expected, got float
```

## Converting Between Array and List

```python
from array import array

# List to array
my_list = [1, 2, 3]
my_array = array("i", my_list)

# Array to list
my_array = array("i", [1, 2, 3])
my_list = list(my_array)
print(my_list)  # [1, 2, 3]
```

## Array vs List

| Feature     | Array                           | List            |
| ----------- | ------------------------------- | --------------- |
| Type        | Single type only                | Mixed types     |
| Memory      | Less memory                     | More memory     |
| Performance | Faster for large datasets       | Slower          |
| Flexibility | Limited                         | Flexible        |
| Import      | Needs `from array import array` | Built-in        |
| Use case    | Large numeric data              | General purpose |

## When to Use Arrays

✅ **Use arrays when:**

- Working with **large numeric datasets**
- **Memory** is a concern
- Need **type safety**

❌ **Use lists when:**

- Need **mixed types**
- Need **flexibility**
- Working with **small datasets**

## Key Points

- **`from array import array`** - must import
- **Type-constrained** - all items same type
- **Type code** required: `"i"` (int), `"f"` (float), etc.
- **More memory efficient** than lists
- **Less flexible** than lists
- Same methods as lists: `append()`, `insert()`, `remove()`
- **Lists are preferred** for most cases
